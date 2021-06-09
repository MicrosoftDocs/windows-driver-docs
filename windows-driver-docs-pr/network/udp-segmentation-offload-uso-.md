---
title: UDP Segmentation Offload (USO)
description: UDP Segmentation Offload (USO)
keywords:
- network drivers WDK , UDP Segmentation Offload (USO)
- UDP Segmentation Offload (USO) WDK networking
- UDP Segmentation Offload (USO) WDK networking , about UDP Segmentation Offload (USO)
- about UDP Segmentation Offload (USO)
ms.date: 02/27/2020
ms.localizationpriority: medium
---

# UDP Segmentation Offload (USO)

UDP Segmentation Offload (USO), supported in Windows 10, version 2004 and later, is a feature that enables network interface cards (NICs) to offload the segmentation of UDP datagrams that are larger than the maximum transmission unit (MTU) of the network medium. By doing so, Windows reduces CPU utilization associated with per-packet TCP/IP processing. Requirements for USO are similar to [LSOv2](offloading-the-segmentation-of-large-tcp-packets.md), which is for the TCP transport protocol.

## Requirements for USO

This section refers primarily to NDIS protocol and miniport drivers. NDIS lightweight filter drivers (LWFs) must follow protocol driver requirements when modifying or sending packets, and can also assume that any packets provided to its [*FilterSendNetBufferLists*](/windows-hardware/drivers/ddi/content/ndis/nc-ndis-filter_send_net_buffer_lists) handler meet the protocol driver requirements.

Miniport drivers can offload the segmentation of large UDP packets that are larger than the MTU of the network medium. A NIC that supports the segmentation of large UDP packets must also be able to do the following:

- Calculate IP checksums for sent packets that contain IPv4 options
- Calculate UDP checksums for sent packets

A miniport driver that supports USO must determine the offload type from the [**NET_BUFFER_LIST**](/windows-hardware/drivers/ddi/content/nbl/ns-nbl-net_buffer_list) structure's out of band (OOB) information. If the value of the [**NDIS_UDP_SEGMENTATION_OFFLOAD_NET_BUFFER_LIST_INFO**](/windows-hardware/drivers/ddi/content/nbluso/ns-nbluso-ndis_udp_segmentation_offload_net_buffer_list_info) structure is non-zero, then the miniport driver must perform USO. Any **NET_BUFFER_LIST** that contains USO OOB data also contains a single [**NET_BUFFER**](/windows-hardware/drivers/ddi/content/nbl/ns-nbl-net_buffer) structure. However, in the case where the miniport driver has received [OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md) to turn off USO, after the miniport driver has completed the OID successfully it should reject and return any **NET_BUFFER_LIST** that has the USO OOB field set.

The TCP/IP transport offloads only those UDP packets that meet the following criteria:

- The packet is a UDP packet.
- The packet length must be greater than maximum segment size **(MSS) \* (MinSegmentCount - 1)**.
- If the miniport driver does not set the **SubMssFinalSegmentSupported** capability, then each large UDP packet offloaded by the transport must have **Length % MSS == 0**. That is, the large packet is divisible into **N** packets with each packet segment containing exactly **MSS** user bytes. If the miniport driver sets the **SubMssFinalSegmentSupported** capability, then this packet length divisibility condition on the transport does not apply. In other words, the final segment can be less than **MSS**.
- The packet is not a loopback packet.
- The **MF** bit in the IP header of the large UDP packet that the TCP/IP transport offloaded will not be set, and the **Fragment Offset** in the IP header will be zero.
- The application has specified UDP_SEND_MSG_SIZE/[WSASetUdpSendMessageSize](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsasetudpsendmessagesize).

Before offloading a large UDP packet for segmentation, the TCP/IP transport does the following:

- Updates the large packet segmentation information that is associated with the [**NET_BUFFER_LIST**](/windows-hardware/drivers/ddi/content/nbl/ns-nbl-net_buffer_list) structure. This information is an [**NDIS_UDP_SEGMENTATION_OFFLOAD_NET_BUFFER_LIST_INFO**](/windows-hardware/drivers/ddi/content/nbluso/ns-nbluso-ndis_udp_segmentation_offload_net_buffer_list_info) structure that is part of the **NET_BUFFER_LIST** structure's OOB information. The TCP/IP transport sets the MSS value to the desired MSS.
- Calculates a one's complement sum for the UDP pseudoheader and writes this sum to the **Checksum** field of the UDP header. The TCP/IP transport calculates the one's complements sum over the following fields in the pseudoheader: Source IP Address, Destination IP Address, and Protocol.  

The one's complement sum for the pseudoheader provided by the TCP/IP transport gives the NIC an early start in calculating the real UDP checksum for each packet that the NIC derives from the large UDP packet, without having to examine the IP header. 

Note that [RFC 768](https://tools.ietf.org/html/rfc768) and [RFC 2460](https://tools.ietf.org/html/rfc2460) stipulate that the pseudoheader is calculated over the Source IP Address, the Destination IP Address, Protocol, and UDP Length (the length of the UDP header plus the length of the UDP payload, not including the length of the pseudoheader). However, because the underlying miniport driver and NIC generate UDP datagrams from the large packet that is passed down by the TCP/IP transport, the transport does not know the size of the UDP payload for each UDP datagram and thus cannot include the UDP Length in the pseudoheader calculation. Instead, as described in the following section, the NIC extends the pseudoheader checksum that was supplied by the TCP/IP transport to cover the UDP Length of each generated UDP datagram.

> [!IMPORTANT]
> If the UDP header checksum field provided by the TCP/IP transport is zero, the NIC should not perform UDP checksum calculation.

## Sending packets with USO

After the miniport driver obtains the [**NET_BUFFER_LIST**](/windows-hardware/drivers/ddi/content/nbl/ns-nbl-net_buffer_list) in its [*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/content/nbl/ns-nbl-net_buffer_list) callback function, it can call the [**NET_BUFFER_LIST_INFO**](/windows-hardware/drivers/ddi/content/nblaccessors/nf-nblaccessors-net_buffer_list_info) macro with an **_Id** of **UdpSegmentationOffloadInfo** to obtain the MSS value and IP protocol.

The miniport driver obtains the total length of the large packet from the length of the first [**NET_BUFFER**](/windows-hardware/drivers/ddi/content/nbl/ns-nbl-net_buffer) structure and uses the **MSS** value to divide the large UDP packet into smaller UDP packets. Each of the smaller packets contains **MSS** or fewer user data bytes. Note that only the last packet that was created from the segmented large packet should contain less than **MSS** user data bytes. All other packets that were created from the segmented packet must contain **MSS** user data bytes. If a miniport driver does not adhere to this rule, the UDP datagrams will be incorrectly delivered. If the miniport driver does not set the **SubMssFinalSegmentSupported** capability, then the packet length divides by **MSS** and each of the segmented packets contains **MSS** user bytes.

The miniport driver affixes MAC, IP, and UDP headers to each segment that is derived from the large packet. The miniport driver must calculate the IP and UDP checksums for these derived packets. To calculate the UDP checksum for each packet that was derived from the large UDP packet, the NIC calculates the variable part of the UDP checksum (for the UDP header and UDP payload), adds this checksum to the one's complement sum for the pseudoheader that was calculated by the TCP/IP transport, then calculates the 16-bit one's complement for the checksum. For more information about calculating such checksums, see [RFC 768](https://tools.ietf.org/html/rfc768) and [RFC 2460](https://tools.ietf.org/html/rfc2460). 

The length of the UDP user data in the large UDP packet must be less than or equal to the value that the miniport driver assigns to the **MaxOffLoadSize** value.

After a driver issues a status indication to indicate a change to the **MaxOffLoadSize** value, the driver must not cause a bug check if it receives an LSO send request that uses the previous **MaxOffLoadSize** value. Instead, the driver must fail the send request. Drivers **must** fail any send request they can't perform, for any reason (including size, minimum segment count, IP options, etc.). Drivers must send a status indication as soon as possible if their capabilities change.

An intermediate driver that independently issues status indications that report a change in the **MaxOffLoadSize** value must ensure that the underlying miniport adapter that has not issued a status indication does not get any packets that are larger than the **MaxOffLoadSize** value that the miniport adapter reported.

A miniport-intermediate driver that responds to [OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md) to turn off USO services must be prepared for a small window of time where USO requests could still reach the miniport driver.

The number of segmentation packets that were dervied from the large UDP packet must be equal to or greater than the **MinSegmentCount** value that is specified by the miniport driver.

When processing a large UDP packet, the miniport driver is responsible only for segmenting the packet and affixing MAC, IP, and UDP headers to the packets that are derived from the large UDP packet. If the miniport fails to send at least one segmented packet, the NBL must eventually be completed with a failure status. The miniport can continue sending subsequent packets but is not required to do so. The NBL cannot be completed back to NDIS until all segmented packets have transmitted or failed.

USO-capable miniport drivers must also do the following:

- Support both IPv4 and IPv6.
- Support replication of IPv4 options from the large packet in each segmented packet that the NIC generates.
- Use the IP and UDP header in the [**NET_BUFFER_LIST**](/windows-hardware/drivers/ddi/content/nbl/ns-nbl-net_buffer_list) structure as a template to generate UDP and IP headers for each segmented packet.
- Use IP identification (IP ID) values in the range from **0x0000** to **0xFFFF**. For example, if the template IP header starts with an Identification field value of **0xFFFE**, the first UDP datagram packet must have a value of **0xFFFE**, followed by **0xFFFF**, **0x0000**, **0x0001**, and so on.
- If the large UDP packet contains IP options, the miniport driver copies these options, unaltered, to each packet that is derived from the large UDP packet.
- Use the byte offset in the **UdpHeaderOffset** member of [**NDIS_UDP_SEGMENTATION_OFFLOAD_NET_BUFFER_LIST_INFO**](/windows-hardware/drivers/ddi/content/nbluso/ns-nbluso-ndis_udp_segmentation_offload_net_buffer_list_info) to determine the location of the UDP header, starting from the first byte of the packet.
- Increment transmit statistics based on the segmented packets. For example, include the count of Ethernet, IP, and UDP header bytes for each packet segment, and the packet count is the number of **MSS**-sized segments, not **1**.
- Set the UDP total length and IP length fields based on each segmented datagram size.

## NDIS interface changes

This section describes the changes in NDIS 6.83 that enable the host TCP/IP driver stack to harness the USO capabilities exposed by miniport drivers.

NDIS and the miniport driver perform the following:

- Advertise that the NIC supports USO capability
- Enable or disable USO
- Get the current USO functionality state

### Advertising USO capability

Miniport drivers advertise USO capability by filling in the **UdpSegmentation** field of the [**NDIS_OFFLOAD**](/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_offload) structure, which is passed in the parameters of [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismsetminiportattributes). The **Header.Revision** field in the **NDIS_OFFLOAD** structure must be set to **NDIS_OFFLOAD_REVISION_6** and the **Header.Size** field must be set to **NDIS_SIZEOF_NDIS_OFFLOAD_REVISION_6**.

### Querying USO state

The current USO state can be queried with [OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md). NDIS handles this OID and does not pass it down to the miniport driver.

### Changing USO state

USO can be enabled or disabled using [OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md). After the miniport driver processes the OID, it must send an [NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG](ndis-status-task-offload-current-config.md) status indication with the updated offload state.

## USO keywords

The USO enumeration keywords are as follows:

- **\*UsoIPv4**
- **\*UsoIPv6**

These values describe whether USO is enabled or disabled for that particular IP protocol. The USO settings are not dependent on the [**NDIS_TCP_IP_CHECKSUM_OFFLOAD**](/windows-hardware/drivers/ddi/content/ntddndis/ns-ntddndis-_ndis_tcp_ip_checksum_offload) configuration. For example, disabling **\*UDPChecksumOffloadIPv4** does not implicitly disable **\*UsoIPv4**.

| Subkey name | Parameter description | Value | Enum description |
| --- | --- | --- | --- |
| **\*UsoIPv4** | UDP Segmentation Offload (IPv4) | 0 | Disabled |
|   |   | 1 | Enabled |
| **\*UsoIPv6** | UDP Segmentation Offload (IPV6) | 0 | Disabled |
|   |   | 1 | Enabled |
