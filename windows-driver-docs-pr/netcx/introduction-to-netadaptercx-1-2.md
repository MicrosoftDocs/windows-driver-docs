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

## Feature updates



## New APIs and data structures

The following APIs and data structures are new in NetAdapterCx 1.2. They are grouped according to the new feature they support.

### Packet extensions

- NetPacketExtension
- NET_PACKET_EXTENSION
- NET_PACKET_EXTENSION_INI
- NET_PACKET_EXTENSION_QUERY
- NET_PACKET_EXTENSION_QUERY_INIT
- NetRxQueueGetPacketExtensionOffset
- NetTxQueueGetPacketExtensionOffset

### Offloads

- NetPacketGetPacketChecksum
- NetPacketGetPacketLargeSendSegmentation
- NetPacketGetPacketReceiveSetmentCoalescence
- NET_PACKET_LARGE_SEND_SEGMENTATION
- NET_PACKET_RECEIVE_SEGMENT_COALESCENCE

### Multi-level ring buffer

- NetRingBufferReturnAllPackets
- NetPacketGetFragmentCount
- NetRxQueueGetDatapathDescriptor
- NetTxQueueGetDatapathDescriptor
- PCNET_DATAPATH_DESCRIPTOR
- NET_DATAPATH_DESCRIPTOR
- NET_DATAPATH_RING_BUFFER_INDEX

### Multiple NetAdapter objects per device

- NetAdapterStart
- NetAdapterStop

### Buffer Manager

- NET_ADAPTER_DMA_CAPABILITIES
- NET_ADAPTER_DMA_CAPABILITIES_INIT
- NET_ADAPTER_RX_CAPABILITIES
- NET_ADAPTER_RX_CAPABILITIES_INIT_DRIVER_MANAGED
- NET_ADAPTER_RX_CAPABILITIES_INIT_SYSTEM_MANAGED
- NET_ADAPTER_RX_CAPABILITIES_INIT_SYSTEM_MANAGED_DMA
- NET_MEMORY_MAPPING_REQUIREMENT
- NET_RX_FRAGMENT_BUFFER_ALLOCATION_MODE
- NET_RX_FRAGMENT_BUFFER_ATTACHMENT_MODE
- NET_ADAPTER_TX_CAPABILITIES
- NET_ADAPTER_TX_CAPABILITIES_INIT
- NET_ADAPTER_TX_CAPABILITIES_INIT_FOR_DMA

### NetAdapter RSS

- NetAdapterGetReceiveScalingHashSecretKey
- NetAdapterGetReceiveScalingHashType
- NetAdapterGetReceiveScalingProtocolTypes
- NetAdapterSetReceiveScalingCapabilities
- EVT_NET_ADAPTER_CREATE_RSSQUEUE_GROUP
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

### Other new APIs and data structures

- SIZE_T
- NetRequestGetAdapter
- NETADAPTER
- NetPacketIsIpv4
- NetPacketIsIpv6

## Updated APIs and data structures

The following APIs and data structures were updated in NetAdapterCx 1.2.

- [NetAdapterSetDataPathCapabilities](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptersetdatapathcapabilities)
- [NET_ADAPTER_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_config)
- [NetPacketGetContextFromToken]((https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netpacketgetcontextfromtoken)
- [NetPacketGetTypedContext](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netpacketgettypedcontext)
- [NET_PACKET](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet)
- [NET_PACKET_FRAGMENT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet_fragment)
- [NET_RXQUEUE_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/ns-netrxqueue-_net_rxqueue_config)
- [NET_TXQUEUE_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/ns-nettxqueue-_net_txqueue_config)

## Removed APIs and data structures

The following APIs and data structures were removed in NetAdapterCx 1.2. Their reference topics are no longer available. Instructions for which new or updated APIs or data structures to use instead are provided.

- NET_ADAPTER_DATAPATH_CAPABILITIES
- NET_ADAPTER_DATAPATH_CAPABILITIES_INIT
    - TBD
- NET_RXQUEUE_DMA_ALLOCATOR_CONFIG
- NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT
- NetRxQueueInitSetDmaAllocatorConfig
- NetRxQueueQueryAllocatorCacheEnabled
    - TBD
- NetRxQueueGetBufferLayoutHint
    - TBD
- NetRxQueueGetRingBuffer
    - TBD
- NetTxQueueGetRingBuffer
    - TBD

## Compiling a NetAdapterCx 1.2 client driver

If you are porting an NDIS 6.x miniport driver to NetAdapter 1.2, first follow the compilation steps on [Porting NDIS miniport drivers to NetAdapterCx](porting-ndis-miniport-drivers-to-netadaptercx.md). Then, in the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **2**.

If you are porting a NetAdapterCx client driver from an earlier version of NetAdapterCx, in the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **2**.

If you are writing a new NetAdapterCx client driver, follow the steps on [Building a NetAdapterCx client driver](building-a-netadaptercx-client-driver.md) and, in Step 5, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **2**.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")