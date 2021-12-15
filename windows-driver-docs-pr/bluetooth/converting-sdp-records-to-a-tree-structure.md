---
title: Converting SDP Records to a Tree Structure
description: Converting SDP Records to a Tree Structure
keywords:
- Bluetooth WDK , SDP server communication
- SDP WDK Bluetooth
- Service Discovery Protocol WDK Bluetooth
- browsing services WDK Bluetooth
- searching services WDK Bluetooth
- services browsing WDK Bluetooth
- converting SDP records
- tree structures from SDP records WDK Bluetooth
- SdpConvertStreamToTree
ms.date: 04/20/2017
---

# Converting SDP Records to a Tree Structure


Service Discovery Protocol (SDP) records are encoded in a complex binary stream. To enable profile drivers to parse SDP records more easily, the Bluetooth driver stack provides a number of functions that profile drivers can use to convert the SDP record stream into a hierarchical tree structure and back again.

Client profile drivers can use the [**SdpConvertStreamToTree**](/windows-hardware/drivers/ddi/bthsdpddi/nc-bthsdpddi-pconvertstreamtotree) function to convert an SDP record into a tree structure. The tree representation of the SDP record that results from calling the **SdpConvertStreamToTree** function consists of a root node that contains all information associated with the SDP record, defined by an [**SDP\_TREE\_ROOT\_NODE**](/windows-hardware/drivers/ddi/sdpnode/ns-sdpnode-_sdp_tree_root_node) structure. The root node contains a series of interconnected [**SDP\_NODE**](/windows-hardware/drivers/ddi/sdpnode/ns-sdpnode-_sdp_node) structures, each of which contains information about a single SDP attribute.

Each SDP\_NODE structure contains an [**SDP\_NODE\_HEADER**](/windows-hardware/drivers/ddi/sdpnode/ns-sdpnode-_sdp_node_header) structure and an
 [**SDP\_NODE\_DATA**](/windows-hardware/drivers/ddi/sdpnode/ns-sdpnode-_sdp_node_data) union.
  The header structure specifies the type of data that is contained in the node. Profile drivers use the [**LIST\_ENTRY**](/windows/win32/api/ntdef/ns-ntdef-list_entry) structure
   to access links to peer SDP\_NODE structures. By using the SDP\_NODE structure's **hdr.Link.Flink** and **hdr.Link.Blink** members, profile drivers can obtain the addresses of peer nodes in the tree.
    Keep in mind that LIST\_ENTRY pointers hold addresses to other LIST\_ENTRY structures, and that profile drivers must use the [**CONTAINING\_RECORD**](/windows/win32/api/ntdef/nf-ntdef-containing_record) macro to extract the address that contains the node record. For more information, see the [**SdpConvertStreamToTree**](/windows-hardware/drivers/ddi/bthsdpddi/nc-bthsdpddi-pconvertstreamtotree) topic.

After the SDP record stream is converted to a tree representation, a profile driver can call the [**SdpFindAttributeInTree**](/windows-hardware/drivers/ddi/sdplib/nf-sdplib-sdpfindattributeintree) function to obtain the address of a specified node in the tree.

Profile drivers can obtain a pointer to all of the functions discussed in this topic by querying for the [**BTHDDI\_SDP\_PARSE\_INTERFACE**](/windows-hardware/drivers/ddi/bthsdpddi/ns-bthsdpddi-_bthddi_sdp_parse_interface) and [**BTHDDI\_SDP\_NODE\_INTERFACE**](/windows-hardware/drivers/ddi/bthsdpddi/ns-bthsdpddi-_bthddi_sdp_node_interface) interfaces. For more information about how to query for these interfaces, see [Querying for Bluetooth Interfaces](querying-for-bluetooth-interfaces.md).

 

