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

In version 1.0, NetAdapterCx had one packet context per queue (or per packet on a queue), which limited client drivers' usability. For example, if you were using the DMA IO Helper for your transmit queue, it occupied the only packet context available to you. In version 1.1, however, you can now allocate as many packet contexts as you need. Each driver subsystem can now use a different context, creating flexibility and improving componentization.

For more info about setting attributes for each packet context, see [NET_PACKET_CONTEXT_ATTRIBUTES](net-packet-context-attributes.md) and [NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE](net-packet-context-attributes-init-type.md).

### Finer link state control

Two new methods, [NetAdapterSetPermanentLinkLayerAddress](netadaptersetpermanentlinklayeraddress.md) and [NetAdapterSetCurrentLinkLayerAddress](netadaptersetcurrentlinklayeraddress.md), have been added in NetAdapter 1.1 to enable NetAdapterCx client drivers to more easily set these separate addresses with dedicated methods. The driver can also query them with the updated [NetConfigurationQueryLinkLayerAddress](netconfigurationquerylinklayeraddress.md) method. This means that drivers can now report their *current* link state at runtime, as opposed to only when setting capabilities with [NetAdapterSetLinkLayerCapabilities](netadaptersetlinklayercapabilities.md).

### Improved receive buffer management and performance

If a client driver chose to let NetAdapterCx manage the receive buffer in version 1.0, it called a method called **NetRxQueueConfigureDmaAllocator**. However, it was not possible to specify further options for receive queue DMA allocation. In version 1.1, a new structure, [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG](net-rxqueue-dma-allocator-config.md), has been introduced to enable client drivers to customize DMA aspects such as cache enablement or the preferred NUMA node to be used when allocating memory. This structure is initialized with the new [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT](net-rxqueue-dma-allocator-config-init.md) method and is associated with the receive queue by calling [NetRxQueueInitSetDmaAllocatorConfig](netrxqueueinitsetdmaallocatorconfig.md), which replaced **NetRxQueueConfigureDmaAllocator**.

Client driver can also now query whether DMA allocator cache is enabled with the new [NetRxQueueQueryAllocatorCacheEnabled](netrxqueuequeryallocatorcacheenabled.md) method.

To improve performance in the receive queue, client drivers can now optionally call the [NetRxQueueGetBufferLayoutHint](netrxqueuegetbufferlayouthint.md) method to precalculate receive buffer padding and alignment.

## API and data structure changes

### New APIs and data structures

The following APIs and data structures are new in NetAdapterCx 1.1.

- [NET_ADAPTER_LINK_LAYER_ADDRESS_INIT method](net-adapter-link-layer-address-init.md)
- [NetAdapterSetPermanentLinkLayerAddress method](netadaptersetpermanentlinklayeraddress.md)
- [NetAdapterSetCurrentLinkLayerAddress method](netadaptersetcurrentlinklayeraddress.md)
- [NET_PACKET_CONTEXT_TOKEN](net-packet-context-token.md)
- [NET_PACKET_CONTEXT_ATTRIBUTES](net-packet-context-attributes.md)
- [NET_PACKET_CONTEXT_ATTRIBUTES_INIT_TYPE](net-packet-context-attributes-init-type.md)
- [NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN]
- [NetPacketGetContextFromToken]
- [NET_RXQUEUE_BUFFER_LAYOUT_HINT](net-rxqueue-buffer-layout-hint.md)
- [NetRxQueueGetBufferLayoutHint method](netrxqueuegetbufferlayouthint.md)
- [NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN]
- [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG](net-rxqueue-dma-allocator-config.md)
- [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT method](net-rxqueue-dma-allocator-config-init.md)
- [NetRxQueueGetPacketContextToken]
- [NetRxQueueInitAddPacketContextAttributes method](netrxqueueinitaddpacketcontextattributes.md)
- [NetRxQueueQueryAllocatorCacheEnabled](netrxqueuequeryallocatorcacheenabled.md)
- [NET_TXQUEUE_GET_PACKET_CONTEXT_TOKEN]
- [NetTxQueueGetPacketContextToken]
- [NetTxQueueInitAddPacketContextAttributes](nettxqueueinitaddpacketcontextattributes.md)

### Updated APIs and data structures

The following APIs and data structures were updated in NetAdapterCx 1.1.

- [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md)
- [NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT method](net-adapter-link-layer-capabilities-init.md)
- [NET_ADAPTER_CONFIG](net-adapter-config.md)
- [NET_PACKET_FRAGMENT](net-packet-fragment.md)
- [NetAdapterDriverWdmGetHandle method](netadapterdriverwdmgethandle.md)
- [NetConfigurationQueryLinkLayerAddress method](netconfigurationquerylinklayeraddress.md)
- [NetPowerSettingsGetWakePatternCount method](netpowersettingsgetwakepatterncount.md)
- [NetPowerSettingsGetWakePatternCountForType method](netpowersettingsgetwakepatterncountfortype.md)
- [NetPowerSettingsGetWakePattern method](netpowersettingsgetwakepattern.md)
- [NetPowerSettingsIsWakePatternEnabled method](netpowersettingsiswakepatternenabled.md)
- [NetPowerSettingsGetEnabledWakeUpFlags method](netpowersettingsgetenabledwakeupflags.md)
- [NetPowerSettingsGetEnabledProtocolOffloadFlags method](netpowersettingsgetenabledprotocoloffloadflags.md)
- [NetPowerSettingsGetEnabledMediaSpecificWakeUpEvents method](netpowersettingsgetenabledmediaspecificwakeupevents.md)
- [NetPowerSettingsGetProtocolOffloadCount method](netpowersettingsgetprotocoloffloadcount.md)
- [NetPowerSettingsGetProtocolOffloadCountForType method](netpowersettingsgetprotocoloffloadcountfortype.md)
- [NetPowerSettingsGetProtocolOffload method](netpowersettingsgetprotocoloffload.md)
- [NetPowerSettingsIsProtocolOffloadEnabled method](netpowersettingsisprotocoloffloadenabled.md)
- [NetRxQueueInitSetDmaAllocatorConfig](netrxqueueinitsetdmaallocatorconfig.md)
- [EVT_RXQUEUE_SET_NOTIFICATION_ENABLED](evt-rxqueue-set-notification-enabled.md)
- [NET_RXQUEUE_CONFIG](net-rxqueue-config.md)
- [EVT_TXQUEUE_SET_NOTIFICATION_ENABLED](evt-txqueue-set-notification-enabled.md)
- [NET_TXQUEUE_CONFIG](net-txqueue-config.md)

### Removed APIs and data structures

The following APIs and data structures were removed in NetAdapterCx 1.1 and were replaced with a different API or data structure. See each topic for details.

- [NET_ADAPTER_DRIVER_TYPE](net-adapter-driver-type.md)
- [NET_ADAPTER_PHYSICAL_ADDRESS](net-adapter-physical-address.md)
- [NET_ADAPTER_PHYSICAL_ADDRESS_INIT](net-adapter-physical-address-init.md)
- [NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT_NO_PHYSICAL_ADDRESS](net-adapter-link-layer-capabilities-init-no-physical-address.md)

## Compiling a NetAdapterCx 1.1 client driver

If you are porting an NDIS 6.x miniport driver to NetAdapter 1.1, first follow the compilation steps on [Porting NDIS miniport drivers to NetAdapterCx](porting-ndis-miniport-drivers-to-netadaptercx.md). Then, in the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **1**.

If you are porting a NetAdapterCx client driver from an earlier version of NetAdapterCx, in the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **1**.

If you are writing a new NetAdapterCx client driver, follow the steps on [Building a NetAdapterCx client driver](building-a-netadaptercx-client-driver.md) and, in Step 5, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **1**.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")