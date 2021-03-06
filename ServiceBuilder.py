'''
Author: Rodrigo Moreira
Date: 06/09/2019
'''


#https://osm-download.etsi.org/ftp/osm-6.0-six/7th-hackfest/presentations/
# Each Service Builder in each Domain is able to receive NST to proced with Service Deployment

import logging, glob, os, pycos, socket, json

import yaml
import NANO
import MANO

logging.basicConfig(level=logging.DEBUG)


class ServiceBuilder:
    NSD = None
    VNFD = None
    NSTD = None

    message = ""

    """
    Receives a tar.gz NSD and returns a directory name of extracted files
    """
    def nsd_untar(self):
        dir = os.path.dirname("./cirros_2vnf_ns.tar.gz")  # get directory where file is stored
        dir_extract = os.path.dirname("./")
        filename = os.path.basename("./cirros_2vnf_ns.tar.gz")  # get filename
        file_tar, file_tar_ext = os.path.splitext("./cirros_2vnf_ns.tar.gz")  # split into file.tar and .gz
        file_untar, file_untar_ext = os.path.splitext(file_tar)  # split into file and .tar
        #os.chdir(dir)
        if file_tar_ext == ".gz" and file_untar_ext == ".tar":  # check if file had format .tar.gz
            import tarfile
            tar = tarfile.open(filename)
            tar.extractall(path=dir_extract)  # untar file into same directory
            tar.close()
            #os.chdir(file_untar)  # This fails if file.tar.gz has different name compared to the untarred folder e.g.. file1 instead of file

            logging.debug("Uncompressed NSD " + str(filename) + " on " + str(file_untar))

            # Dir name of extracted files
            return file_untar

    """
    Receives a tar.gz VNFD and returns a directory name of extracted files
    """
    def vnfd_untar(self):
        dir = os.path.dirname("./ns/cirros_vnf.tar.gz")  # get directory where file is stored
        dir_extract = os.path.dirname("./ns")
        filename = os.path.basename("./ns/cirros_vnf.tar.gz")  # get filename
        file_tar, file_tar_ext = os.path.splitext("./ns/cirros_vnf.tar.gz")  # split into file.tar and .gz
        file_untar, file_untar_ext = os.path.splitext(file_tar)  # split into file and .tar
        os.chdir(dir)
        if file_tar_ext == ".gz" and file_untar_ext == ".tar":  # check if file had format .tar.gz
            import tarfile
            tar = tarfile.open(filename)
            tar.extractall(path=dir_extract)  # untar file into same directory
            tar.close()
            #os.chdir(file_untar)  # This fails if file.tar.gz has different name compared to the untarred folder e.g.. file1 instead of file

            logging.debug("Uncompressed VNFD " + str(filename) + " on " + str(file_untar))

            # Dir name of extracted files
            return file_untar

    """
    Search for yaml in extracted directory
    """
    def search_ns_yaml(self, nsd_dir_name):
        os.chdir(nsd_dir_name)
        nsd_file_name = ""
        for nsd in glob.glob("*.yaml"):
            nsd_file_name = str(nsd)

        nsd_full_path = nsd_dir_name + str("\\") + nsd_file_name

        with open(nsd_full_path, 'r') as stream:
            NSD = yaml.safe_load(stream)
            self.NSD = NSD

            with open('ns_result.yaml', 'w') as yaml_file:
                yaml.dump(self.NSD, yaml_file, default_flow_style=False)

        #print(self.NSD)

    def search_vnf_yaml(self, vnf_dir_name):
        os.chdir(vnf_dir_name)
        vnf_file_name = ""
        for nsd in glob.glob("*.yaml"):
            vnf_file_name = str(nsd)

        vnf_absolute_path = os.path.abspath(vnf_file_name)

        with open(vnf_absolute_path, 'r') as stream:
            VNFD = yaml.safe_load(stream)
            self.VNFD = VNFD

            with open('vnf_result.yaml', 'w') as yaml_file:
                yaml.dump(self.VNFD, yaml_file, default_flow_style=False)

        #print(self.VNFD)



    def read_vnfd(self, VNF_DIR_NAME):
        with open(VNF_DIR_NAME, 'r') as stream:
            VNFD = yaml.safe_load(stream)

        self.VNFD = VNFD['vnfd:vnfd-catalog']

    def read_nstd(self):
        with open("./ns/cirros_nstd.yaml", 'r') as stream:
            NSTD = yaml.safe_load(stream)

        self.NSTD = NSTD['nst']


    def read_nsd(self):
        with open("./ns/cirros_2vnf_ns/cirros_2vnf_nsd.yaml", 'r') as stream:
            NSD = yaml.safe_load(stream)

        self.VNFD = NSD['nsd:nsd-catalog']

    #___________________________________________________________________________________________________________________
    def network_slice_template(self):
        #nano = NANO.NANO(1,self.NSTD,26599)
        #nano.eDomain_slice_builder()
        self.nano_exchange("CREATE_SLICE", self.NSTD,"192.168.0.105",8015)

    def speaker_proc(host, port, n, task=None):
        # Create a TCP Socket over port 8010 - we may change it further - with pycos we can create more than one socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = pycos.AsyncSocket(sock)
        yield sock.connect((host, port))
        msg = str(message) + '/'
        msg = msg.encode()
        yield sock.sendall(msg)
        sock.close()

    def nano_exchange(SOURCE, METHOD, NSTD, NANO_TARGET_HSOT, NANO_TARGET_PORT):

        global message
        message = NSTD

        print("YAML: "+str(message))

        #'end2end_next_hop': '2607:f0d0:2001:b::15', 'source': 7675}
        next_hop = "NOTHING"
        source = "NOTHING"


        json_message = json.dumps(message)
        json_message = """{%smethod%s: %s"""+str(METHOD)+"""%s, %sdetails%s: """+json_message+""", %send2end_next_hop%s: %s"""+next_hop+"""%s, %ssource%s: %s"""+source+"""%s}"""
        json_message = str(json_message % ("\"", "\"", "\"", "\"", "\"","\"", "\"","\"","\"","\"","\"","\"","\"","\""))

        message = json_message

        for n in range(1, 2):
            response = pycos.Task(ServiceBuilder.speaker_proc, NANO_TARGET_HSOT, NANO_TARGET_PORT, n)


    # ___________________________________________________________________________________________________________________




    def virtual_network_function_description(self, VNF_NAME):
        mano = MANO.MANO("", self.VNFD)
        mano.vnfd_yaml_interpreter(VNF_NAME)


if __name__ == '__main__':
    logging.debug('Running by IDE - ServiceBuilder')
    sb = ServiceBuilder()

    '''VNF Onboarding'''
    #vnfd_dir_name = sb.vnfd_untar()
    #sb.search_vnf_yaml("./cirros_vnf")
    #sb.virtual_network_function_description("Docker")


    '''Slice Template Onboarding'''
    sb.read_nstd()
    sb.network_slice_template()


    '''NS Onboarding'''
    #ns_dir_name = sb.nsd_untar()
    #sb.read_nsd()



else:
    logging.debug('Imported in somewhere place - ServiceBuilder')
    sb = ServiceBuilder()
    #sb.read_nsd()
    #sb.read_nstd()
    #sb.network_slice_template()
    #sb.read_vnfd()
    #sb.virtual_network_function_description()
    #sb.vnfd_untar()
    #sb.nsd_untar()
