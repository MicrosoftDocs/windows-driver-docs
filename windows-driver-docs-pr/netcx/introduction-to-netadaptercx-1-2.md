---
title: Introduction to NetAdapterCx 1.2
description: Introduction to NetAdapterCx 1.2
ms.assetid: E8931BD4-4F66-4A18-8DF1-3F8ACB4D213E
keywords:
- WDF Network Adapter Class Extension version 1.2, NetAdapterCx 1.2, NetCx 1.2
ms.author: windowsdriverdev
ms.date: 02/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to NetAdapterCx 1.2

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

This topic introduces version 1.2 of the WDF Network Adapter Class Extension (NetAdapterCx). NetAdapterCx 1.2 is included in Windows 10, version 1803.

## Buffer management

Buffer management is a new feature in NetAdapterCx 1.2 that enables Network Interface Card (NIC) client drivers and the operating system to work together when allocating packet data buffers from system memory for the transmit (Tx) and receive (Rx) data paths. This can result in faster performance for the NIC, easier memory lifetime management for the NIC's client driver, and more control for the system over the memory.

For more info about buffer management, see [Network data buffer management](network-data-buffer-management.md).

### New DDIs and data structures for buffer management

- *[EVT_NET_ADAPTER_RETURN_RX_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_return_rx_buffer)*
- [NET_ADAPTER_DMA_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_dma_capabilities)
- [NET_ADAPTER_DMA_CAPABILITIES_INIT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_dma_capabilities_init)
- [NET_ADAPTER_RX_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_rx_capabilities)
- [NET_ADAPTER_RX_CAPABILITIES_INIT_DRIVER_MANAGED](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_rx_capabilities_init_driver_managed)
- [NET_ADAPTER_RX_CAPABILITIES_INIT_SYSTEM_MANAGED](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_rx_capabilities_init_system_managed)
- [NET_ADAPTER_RX_CAPABILITIES_INIT_SYSTEM_MANAGED_DMA](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_rx_capabilities_init_system_managed_dma)
- [NET_MEMORY_MAPPING_REQUIREMENT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ne-netadapter-_net_memory_mapping_requirement)
- [NET_RX_FRAGMENT_BUFFER_ALLOCATION_MODE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ne-netadapter-_net_rx_fragment_buffer_allocation_mode)
- [NET_RX_FRAGMENT_BUFFER_ATTACHMENT_MODE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ne-netadapter-_net_rx_fragment_buffer_attachment_mode)
- [NET_ADAPTER_TX_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_tx_capabilities)
- [NET_ADAPTER_TX_CAPABILITIES_INIT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_tx_capabilities_init)
- [NET_ADAPTER_TX_CAPABILITIES_INIT_FOR_DMA](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_tx_capabilities_init_for_dma)

### Updated DDIs and data structures for buffer management

- [NetAdapterSetDataPathCapabilities](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptersetdatapathcapabilities)
- [NET_RXQUEUE_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/ns-netrxqueue-_net_rxqueue_config)
- [NET_TXQUEUE_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/ns-nettxqueue-_net_txqueue_config)
- [NET_ADAPTER_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_config)

## Multi-level ring buffers and datapath descriptors

NetAdapterCx 1.2 brings multi-level ring buffers to each datapath queue, one for the queue's [NET_PACKET](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet)s and one for its [NET_PACKET_FRAGMENT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet_fragment)s. Where before each queue had only one ring buffer for its packets and fragment organization was opaque to drivers, now fragments are grouped "down a level" in a second, separate ring buffer from packets. 

Each packet in the packet ring buffer references the start of its fragments in the fragment ring buffer. Client drivers only work with the packet buffer directly, but this new arrangement of fragments means that they can now easily query a packet for how many fragments it has, retrieve a single fragment, or loop over all fragments in a packet. To do this, NetAdapterCx 1.2 provides several convenient macros and methods: [NetPacketGetFragmentCount](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-netpacketgetfragmentcount) and [NET_PACKET_GET_FRAGMENT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_packet_get_fragment).

To work with its packet ring buffer and fragments within a packet, each queue now has a new [NET_DATAPATH_DESCRIPTOR](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/ns-netdatapathdescriptor-_net_datapath_descriptor) structure that describes all of its ring buffers. This descriptor is how client drivers retrieve packet ring buffers, as well as perform asynchronous I/O on them with the methods defined in [Netadapterpacket.h](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/).

The following DDIs and data structures are new in NetAdapterCx 1.2 for multi-level ring buffers and datapath descriptors.

- [NET_DATAPATH_DESCRIPTOR_GET_PACKET_RING_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_datapath_descriptor_get_packet_ring_buffer)
- [NET_DATAPATH_DESCRIPTOR_GET_FRAGMENT_RING_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_datapath_descriptor_get_fragment_ring_buffer)
- [NET_PACKET_GET_FRAGMENT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_packet_get_fragment)
- [NetPacketGetFragmentCount](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-netpacketgetfragmentcount)
- [NET_DATAPATH_DESCRIPTOR](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/ns-netdatapathdescriptor-_net_datapath_descriptor)
- [NET_DATAPATH_RING_BUFFER_INDEX](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/ne-netdatapathdescriptor-_net_datapath_ring_buffer_index)
- [NetRxQueueGetDatapathDescriptor](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueuegetdatapathdescriptor)
- [NetTxQueueGetDatapathDescriptor](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-nettxqueuegetdatapathdescriptor)
- [NetRingBufferReturnAllPackets](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbufferreturnallpackets)

The following DDIs and data structures were updated to use a [NET_DATAPATH_DESCRIPTOR](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/ns-netdatapathdescriptor-_net_datapath_descriptor) as a parameter.

- [NetRingBufferGetPacketAtIndex](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbuffergetpacketatindex)
- [NetRingBufferGetNextPacket](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbuffergetnextpacket)
- [NetRingBufferAdvanceNextPacket](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbufferadvancenextpacket)
- [NetRingBufferReturnCompletedPacketsThroughIndex](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbufferreturncompletedpacketsthroughindex)
- [NetRingBufferReturnCompletedPackets](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netringbufferreturncompletedpackets)
- [NetPacketGetContextFromToken](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netpacketgetcontextfromtoken)
- [NetPacketGetTypedContext](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netpacketgettypedcontext)

## Packet extensions and advanced offloads

In addition to datapath descriptors for queues, NetAdapterCx also introduces packet descriptors and packet extensions for each **NET_PACKET**. Packet descriptors hold OS-specific information, while packet extensions provide space for NIC client drivers to store per-packet metadata. Attached to each packet's core descriptor, extensions are used by client drivers to share information with the upper layers. They can also hold advanced offload information like checksum, LSO, and RSS hash, or they can hold application-specific details.

For more information about packet descriptors and extensions, see [Packet descriptors and extensions](packet-descriptors-and-extensions.md).

### New DDIs and data structures for packet extensions and advanced offloads

- [NET_PACKET_EXTENSION](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/ns-netadapterpacket-_net_packet_extension)
- NET_PACKET_EXTENSION_INIT
- NET_PACKET_EXTENSION_QUERY
- NET_PACKET_EXTENSION_QUERY_INIT
- NetPacketGetExtension
- NetRxQueueGetPacketExtensionOffset
- NetTxQueueGetPacketExtensionOffset
- NET_PACKET_ADVANCED_OFFLOAD
- NET_PACKET_LARGE_SEND_SEGMENTATION
- NET_PACKET_RECEIVE_SEGMENT_COALESCENCE
- NetPacketGetPacketChecksum
- NetPacketGetPacketLargeSendSegmentation
- NetPacketGetPacketReceiveSetmentCoalescence

## Multiple NetAdapter objects per device

In version 1.2 of NetAdapterCx, NIC client drivers can now create, start, and stop multiple NETADAPTER objects per device object.

- NetAdapterStart
- NetAdapterStop

## NetAdapter RSS

- EVT_NET_ADAPTER_CREATE_RSSQUEUE_GROUP
- NetAdapterGetReceiveScalingHashSecretKey
- NetAdapterGetReceiveScalingHashType
- NetAdapterGetReceiveScalingProtocolTypes
- NetAdapterSetReceiveScalingCapabilities
- NETRSSQUEUEGROUP_INIT
- EVT_NET_ADAPTER_RECEIVE_SCALING_ENABLE
- EVT_NET_ADAPTER_RECEIVE_SCALING_DISABLE
- EVT_NET_ADAPTER_RECEIVE_SCALING_SET_HASH_SECRET_KEY
- EVT_NET_ADAPTER_RECEIVE_SCALING_SET_INDIRECTION_ENTRIES
- NET_ADAPTER_RECEIVE_SCALING_CAPABILITIES
- NET_ADAPTER_RECEIVE_SCALING_CAPABILITIES_INIT
- NET_ADAPTER_RECEIVE_SCALING_ENCAPSULATION_TYPE
- NET_ADAPTER_RECEIVE_SCALING_HASH_SECRET_KEY
- NET_ADAPTER_RECEIVE_SCALING_HASH_TYPE
- NET_ADAPTER_RECEIVE_SCALING_INDIRECTION_ENTRIES
- NET_ADAPTER_RECEIVE_SCALING_INDIRECTION_ENTRY
- NET_ADAPTER_RECEIVE_SCALING_PROTOCOL_TYPE
- NET_ADAPTER_RECEIVE_SCALING_UNHASHED_TARGET_TYPE

## Other new DDIs and data structures

- SIZE_T
- NetRequestGetAdapter
- NETADAPTER
- NetPacketIsIpv4
- NetPacketIsIpv6

## Other updated DDIs and data structures

The following DDIs and data structures were updated in NetAdapterCx 1.2. They are used by multiple new features and do not correspond to any one of them specifically.

- [NET_PACKET](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet)
- [NET_PACKET_FRAGMENT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet_fragment)

## Removed DDIs and data structures

The following DDIs and data structures were removed in NetAdapterCx 1.2. Their reference topics are no longer available. Instructions for which new or updated DDIs or data structures to use instead are provided.

| Removed DDI or data structure | Description |
| --- | --- |
| <ul><li>NET_ADAPTER_DATAPATH_CAPABILITIES</li><li>NET_ADAPTER_DATAPATH_CAPABILITIES_INIT</li></ul> | This combined datapath capabilities structure and its init method have been replaced by separate Rx and Tx capabilities structures/init methods. For more info, see [NET_ADAPTER_RX_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_rx_capabilities) and [NET_ADAPTER_TX_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_tx_capabilities). |
| <ul><li>NET_RXQUEUE_DMA_ALLOCATOR_CONFIG</li><li>NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT</li><li>NetRxQueueInitSetDmaAllocatorConfig</li><li>NetRxQueueQueryAllocatorCacheEnabled</li></ul> | DMA capabilities have been genericized for Rx queues and Tx queues in NetAdapterCx 1.2, obviating the need for specialized Rx queue DMA structures and methods. For more info, see [NET_ADAPTER_DMA_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_dma_capabilities), [NET_ADAPTER_RX_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_rx_capabilities), and [NET_ADAPTER_TX_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_tx_capabilities). |
| <ul><li>NetRxQueueGetBufferLayoutHint</li></ul> | TBD |
| <ul><li>NetRxQueueGetRingBuffer</li><li>NetTxQueueGetRingBuffer</li></ul> | NIC client drivers now retrieve ring buffers by using a queue's [NET_DATAPATH_DESCRIPTOR](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/ns-netdatapathdescriptor-_net_datapath_descriptor) structure. After calling **NetRx(Tx)QueueGetDatapathDescriptor** to get the descriptor, drivers can call either [NET_DATAPATH_DESCRIPTOR_GET_PACKET_RING_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_datapath_descriptor_get_packet_ring_buffer) or [NET_DATAPATH_DESCRIPTOR_GET_FRAGMENT_RING_BUFFER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netdatapathdescriptor/nf-netdatapathdescriptor-net_datapath_descriptor_get_fragment_ring_buffer) to get the ring buffer they need. |

## Compiling a NetAdapterCx 1.2 client driver

If you are porting an NDIS 6.x miniport driver to NetAdapter 1.2, first follow the compilation steps on [Porting NDIS miniport drivers to NetAdapterCx](porting-ndis-miniport-drivers-to-netadaptercx.md). Then, in the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **2**.

If you are porting a NetAdapterCx client driver from an earlier version of NetAdapterCx, in the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **2**.

If you are writing a new NetAdapterCx client driver, follow the steps on [Building a NetAdapterCx client driver](building-a-netadaptercx-client-driver.md) and, in Step 5, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **2**.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")