/* SPDX-License-Identifier: GPL-2.0 */
#include <stddef.h>
#include <linux/bpf.h>
#include <linux/in.h>
#include <linux/if_ether.h>
#include <linux/if_packet.h>
#include <linux/ipv6.h>
#include <linux/ip.h>
#include <linux/icmpv6.h>
#include <linux/seg6.h>
#include <linux/in6.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_endian.h>
/* Defines xdp_stats_map from packet04 */
#include "../common/xdp_stats_kern_user.h"
#include "../common/xdp_stats_kern.h"

#define ETH_P_IPV4 0x0800

/* Header cursor to keep track of current parsing position */
struct hdr_cursor {
	void *pos;
};

// Nicer way to call bpf_trace_printk()
#define bpf_custom_printk(fmt, ...)                     \
        ({                                              \
            char ____fmt[] = fmt;                       \
            bpf_trace_printk(____fmt, sizeof(____fmt),  \
                    ##__VA_ARGS__);                     \
        })

/* Packet parsing helpers.
 *
 * Each helper parses a packet header, including doing bounds checking, and
 * returns the type of its contents if successful, and -1 otherwise.
 *
 * For Ethernet and IP headers, the content type is the type of the payload
 * (h_proto for Ethernet, nexthdr for IPv6), for ICMP it is the ICMP type field.
 * All return values are in host byte order.
 */
/*static __always_inline int parse_ethhdr(struct hdr_cursor *nh,
					void *data_end,
					struct ethhdr **ethhdr)

{
	struct ethhdr *eth = nh->pos;
	int hdrsize = sizeof(*eth);

//	__u32 eth_proto;
	__u32 nh_off;

	nh_off = sizeof(struct ethhdr);

	// Byte-count bounds check; check if current pointer + size of header
	// is after data_end.
	
	if (nh->pos + nh_off > data_end)
		return -1;


	nh->pos += hdrsize;
	*ethhdr = eth;

	return eth->h_proto; // network-byte-order
}*/

/* Assignment 2: Implement and use this */
/*static __always_inline int parse_ip6hdr(struct hdr_cursor *nh,
					void *data_end,
					struct ipv6hdr **ip6hdr)
{
	struct ethhdr *eth = nh->pos;
	struct ipv6hdr *ip6h = nh->pos;
	int hdrsize = sizeof(*ip6h);

        __u32 nh_off;
        nh_off = hdrsize;


	if (ip6h + 1 > data_end)
		return -1;

	nh->pos += hdrsize;
        *ip6hdr = ip6h;

        return eth->h_proto; // network-byte-order

}*/

/* Assignment 3: Implement and use this */
/*static __always_inline int parse_icmp6hdr(struct hdr_cursor *nh,
					  void *data_end,
					  struct icmp6hdr **icmp6hdr)
{
}*/

SEC("xdp_packet_parser")
int  xdp_parser_func(struct xdp_md *ctx)
{
	void *data_end = (void *)(long)ctx->data_end;
	void *data = (void *)(long)ctx->data;
//	struct ethhdr *eth;
	struct ipv6hdr *ip6h;//Para IPv6

	/* Default action XDP_PASS, imply everything we couldn't parse, or that
	 * we don't want to deal with, we just pass up the stack and let the
	 * kernel deal with it.
	 */
	__u32 action = XDP_PASS; /* Default action */

        /* These keep track of the next header type and iterator pointer */
	struct hdr_cursor nh;
//	int nh_type;

	/* Start next header cursor position at data start */
	nh.pos = data;

	int index = ctx->ingress_ifindex;


	/* Packet parsing in steps: Get each header one at a time, aborting if
	 * parsing fails. Each helper function does sanity checking (is the
	 * header type in the packet correct?), and bounds checking.
	 */
	//nh_type = parse_ethhdr(&nh, data_end, &eth);

	//struct icmp6hdr *icmp6h;
	struct ipv6_sr_hdr *srhv6;

	//int *ifindex = 0;
	int a = 1;
	//char fmt6[] = "ingress forward to ifindex:%d daddr6:%x::%x\n";

	//char *text;
	long long *value = 0;

	struct ethhdr *eth = data;
	struct in6_addr *ipv6_list;
	if ((void*)eth + sizeof(*eth) <= data_end){
		bpf_custom_printk("Tipo de pacote eth %u\n",eth->h_proto);
		if(eth->h_proto == bpf_htons(ETH_P_IPV4)){
			bpf_custom_printk("Pacote nao eh IPv6\n");
                        goto out;
		}
		ip6h = data + sizeof(*eth);
		
//		bpf_custom_printk("Pacote eh IPv6 verificando dentro dele se ha SRH: %d\n", bpf_htons(ip6h->nexthdr));

		srhv6 = data + sizeof(*eth) + sizeof(*ip6h);
		//ipv6_list = srhv6->segments+3;
		ipv6_list = srhv6->segments;
		if ((void*)ipv6_list + sizeof(*ipv6_list) <= data_end) {
			//bpf_custom_printk("Pacote eh SRH Registrando no MAP. Segments_Left %d e IP: %x\n", srhv6->segments_left ,bpf_htons(ipv6_list->s6_addr16[0]));
			
			//bpf_map_update_elem(&xdp_stats_map, &srhv6->segments_left, &ipv6_list->s6_addr16[0],a=0);
                        bpf_custom_printk("Sements_left without HTONS %x\n", srhv6->segments_left);
			if(bpf_map_lookup_elem(&xdp_stats_map, &srhv6->segments_left)){
				bpf_custom_printk("Encontrou elemento no MAPA.. redirecionando para o indice: %d\n", index);
				const int ret_val =  bpf_redirect_map(&tx_port_map, a, 0);
	                        bpf_printk("RET-VAL: %d\n", ret_val);
                        return ret_val;
			}
			else{
				bpf_custom_printk("NAO Encontrou elemento no MAPA - Buscando no Mapa das Dev\n");
			        value = bpf_map_lookup_elem(&tx_port_map, &a);
				if (!value){
					bpf_custom_printk("Nao possui o indice: %x\n",*value);
					return bpf_redirect_map(&tx_port_map, a, 0);
				}
				else{
					bpf_custom_printk("Possui o indice - redirecionando");
					return bpf_redirect_map(&tx_port_map, a, 0);
				}
			}
		}
		else{
			bpf_custom_printk("Pacote nao eh ICMPv6\n");
			goto out;
		}

	}



//	nh_type = parse_ip6hdr(&nh, data_end, &ip6h);
//	bpf_custom_printk("Valor de nh_type = %d e valor de bpf_htons(ETH_P_IPV6) = %d\n",nh_type, bpf_htons(ETH_P_IPV4)); // <-- Adicionar essa linha
//	if (nh_type != bpf_htons(ETH_P_IPV4))
//		goto out;

	/* Assignment additions go below here */

//	action = XDP_DROP;
out:
	return xdp_stats_record_action(ctx, action); /* read via xdp_stats */
}
char _license[] SEC("license") = "GPL";
