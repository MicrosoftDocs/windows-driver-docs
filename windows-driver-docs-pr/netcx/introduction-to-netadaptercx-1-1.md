---
title: Introduction to NetAdapterCx 1.1
description: Introduction to NetAdapterCx 1.1
ms.assetid: A998353A-8910-4E57-AA47-BEF5A2AF76BD
keywords:
- WDF Network Adapter Class Extension version 1.1, NetAdapterCx 1.1, NetCx 1.1
ms.author: windowsdriverdev
ms.date: 08/25/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to NetAdapterCx 1.1

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

This topic introduces version 1.1 of the WDF Network Adapter Class Extension (NetAdapterCx). NetAdapterCx 1.1 is included in Windows 10, version 1709.

## Feature updates

NetAdapterCx 1.1 features advancements in performance over version 1.0, as well several other new features.

### More packet context options 

In version 1.0, NetAdapterCx had one packet context per packet on each datapath queue, but client drivers could not allocate additional packet contexts. This limited client drivers' usability. For example, if you were using the DMA IO Helper for your transmit queue, it occupied the only packet context available to you for that queue. In version 1.1, however, you can now allocate as many packet contexts as you need for each datapath queue, creating more flexibility for transmit and receive operations elsewhere in the driver.

For more info about declaring packet contexts and setting their attributes, see [NET_PACKET_CONTEXT_ATTRIBUTES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/ns-netadapterpacket-_net_packet_context_attributes) and [NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-net_packet_context_attributes_init_type).

For more info about adding packet context attributes to transmit or receive queues, see [NetTxQueueInitAddPacketContextAttributes](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-nettxqueueinitaddpacketcontextattributes) or [NetRxQueueInitAddPacketContextAttributes](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueueinitaddpacketcontextattributes) respectively.

For more info and an example about using a NET_PACKET_CONTEXT_TOKEN to retrieve packet contexts on a queue with more than one packet context, see [NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-net_packet_declare_context_type_with_name), [NET_TXQUEUE_GET_PACKET_CONTEXT_TOKEN](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-net_txqueue_get_packet_context_token), and [NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-net_rxqueue_get_packet_context_token).

An example of defining and adding a custom packet context for a transmit queue is explained on [NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-net_packet_context_attributes_init_type) and [EVT_NET_ADAPTER_CREATE_TXQUEUE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nc-netadapter-evt_net_adapter_create_txqueue).

### Finer link state control

Two new methods, [NetAdapterSetPermanentLinkLayerAddress](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptersetpermanentlinklayeraddress) and [NetAdapterSetCurrentLinkLayerAddress](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptersetcurrentlinklayeraddress), have been added in NetAdapter 1.1 to enable NetAdapterCx client drivers to more easily set these separate addresses with dedicated methods. The driver can also query them with the updated [NetConfigurationQueryLinkLayerAddress](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netconfiguration/nf-netconfiguration-netconfigurationquerylinklayeraddress) method. This means that drivers can now report their *current* link state at runtime, as opposed to only when setting capabilities with [NetAdapterSetLinkLayerCapabilities](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptersetlinklayercapabilities).

### Improved receive buffer management and performance

If a client driver chose to let NetAdapterCx manage the receive buffer in version 1.0, it called a method called **NetRxQueueConfigureDmaAllocator**. However, it was not possible to specify further options for receive queue DMA allocation. In version 1.1, a new structure, NET_RXQUEUE_DMA_ALLOCATOR_CONFIG, has been introduced to enable client drivers to customize DMA aspects such as cache enablement or the preferred NUMA node to be used when allocating memory. This structure is initialized with the new NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT method and is associated with the receive queue by calling NetRxQueueInitSetDmaAllocatorConfig, which replaced **NetRxQueueConfigureDmaAllocator**.

Client drivers can also now query whether DMA allocator cache is enabled with the new NetRxQueueQueryAllocatorCacheEnabled method.

To improve performance in the receive queue, client drivers can also now optionally call the NetRxQueueGetBufferLayoutHint method to precalculate receive buffer padding and alignment.

## DDI and data structure changes

### New DDIs and data structures

The following DDIs and data structures are new in NetAdapterCx 1.1.

- [NET_ADAPTER_LINK_LAYER_ADDRESS_INIT method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_link_layer_address_init)
- [NetAdapterSetPermanentLinkLayerAddress method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptersetpermanentlinklayeraddress)
- [NetAdapterSetCurrentLinkLayerAddress method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadaptersetcurrentlinklayeraddress)
- NET_PACKET_CONTEXT_TOKEN
- [NET_PACKET_CONTEXT_ATTRIBUTES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/ns-netadapterpacket-_net_packet_context_attributes)
- [NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-net_packet_context_attributes_init_type)
- NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN
- [NetPacketGetContextFromToken method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-netpacketgetcontextfromtoken)
- [NET_RXQUEUE_BUFFER_LAYOUT_HINT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/ns-netrxqueue-_net_rxqueue_buffer_layout_hint)
- NetRxQueueGetBufferLayoutHint method
- NET_RXQUEUE_DMA_ALLOCATOR_CONFIG
- NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT method
- [NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-net_rxqueue_get_packet_context_token)
- [NetRxQueueGetPacketContextToken method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueuegetpacketcontexttoken)
- [NetRxQueueInitAddPacketContextAttributes method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nf-netrxqueue-netrxqueueinitaddpacketcontextattributes)
- NetRxQueueQueryAllocatorCacheEnabled
- [NET_TXQUEUE_GET_PACKET_CONTEXT_TOKEN](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-net_txqueue_get_packet_context_token)
- [NetTxQueueGetPacketContextToken method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-nettxqueuegetpacketcontexttoken)
- [NetTxQueueInitAddPacketContextAttributes](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nf-nettxqueue-nettxqueueinitaddpacketcontextattributes)

### Updated DDIs and data structures

The following DDIs and data structures were updated in NetAdapterCx 1.1.

- [NET_ADAPTER_LINK_LAYER_CAPABILITIES](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_link_layer_capabilities)
- [NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-net_adapter_link_layer_capabilities_init)
- [NET_ADAPTER_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/ns-netadapter-_net_adapter_config)
- [NET_PACKET_DECLARE_CONTEXT_TYPE_WITH_NAME](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapterpacket/nf-netadapterpacket-net_packet_declare_context_type_with_name)
- [NET_PACKET_FRAGMENT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpacket/ns-netpacket-_net_packet_fragment)
- [NetAdapterDriverWdmGetHandle method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netadapter/nf-netadapter-netadapterdriverwdmgethandle)
- [NetConfigurationQueryLinkLayerAddress method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netconfiguration/nf-netconfiguration-netconfigurationquerylinklayeraddress)
- [NetPowerSettingsGetWakePatternCount method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsgetwakepatterncount)
- [NetPowerSettingsGetWakePatternCountForType method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsgetwakepatterncountfortype)
- [NetPowerSettingsGetWakePattern method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsgetwakepattern)
- [NetPowerSettingsIsWakePatternEnabled method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsiswakepatternenabled)
- [NetPowerSettingsGetEnabledWakeUpFlags method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsgetenabledwakeupflags)
- [NetPowerSettingsGetEnabledProtocolOffloadFlags method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsgetenabledprotocoloffloadflags)
- [NetPowerSettingsGetEnabledMediaSpecificWakeUpEvents method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsgetenabledmediaspecificwakeupevents)
- [NetPowerSettingsGetProtocolOffloadCount method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsgetprotocoloffloadcount)
- [NetPowerSettingsGetProtocolOffloadCountForType method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsgetprotocoloffloadcountfortype)
- [NetPowerSettingsGetProtocolOffload method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsgetprotocoloffload)
- [NetPowerSettingsIsProtocolOffloadEnabled method](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netpowersettings/nf-netpowersettings-netpowersettingsisprotocoloffloadenabled)
- NetRxQueueInitSetDmaAllocatorConfig
- [EVT_RXQUEUE_SET_NOTIFICATION_ENABLED](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/nc-netrxqueue-evt_rxqueue_set_notification_enabled)
- [NET_RXQUEUE_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/netrxqueue/ns-netrxqueue-_net_rxqueue_config)
- [EVT_TXQUEUE_SET_NOTIFICATION_ENABLED](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/nc-nettxqueue-evt_txqueue_set_notification_enabled)
- [NET_TXQUEUE_CONFIG](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/nettxqueue/ns-nettxqueue-_net_txqueue_config)

### Removed DDIs and data structures

The following DDIs and data structures were removed in NetAdapterCx 1.1 and were replaced with a different DDI or data structure. See each topic for details.

- NET_ADAPTER_DRIVER_TYPE
- NET_ADAPTER_PHYSICAL_ADDRESS
- NET_ADAPTER_PHYSICAL_ADDRESS_INIT
- NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT_NO_PHYSICAL_ADDRESS

## Compiling a NetAdapterCx 1.1 client driver

If you are porting an NDIS 6.x miniport driver to NetAdapter 1.1, first follow the compilation steps on [Porting NDIS miniport drivers to NetAdapterCx](porting-ndis-miniport-drivers-to-netadaptercx.md). Then, in the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **1**.

If you are porting a NetAdapterCx client driver from an earlier version of NetAdapterCx, in the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **1**.

If you are writing a new NetAdapterCx client driver, follow the steps on [Building a NetAdapterCx client driver](building-a-netadaptercx-client-driver.md) and, in Step 5, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **1**.

