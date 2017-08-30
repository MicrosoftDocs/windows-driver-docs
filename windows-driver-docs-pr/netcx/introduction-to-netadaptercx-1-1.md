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

This topic introduces version 1.1 of the WDF Network Adapter Class Extension (NetAdapterCx). NetAdapterCx 1.1 is included in Windows 10, version 1709.

## Feature updates

NetAdapterCx 1.1 features advancements in performance over version 1.0, as well several other new features.

### Better context management 

In version 1.0, NetAdapterCx had one packet context per queue, which limited client drivers' usability. For example, if you were using the DMA IO Helper for your transmit queue, that was the only packet context available to you. In version 1.1, however, you can now allocate as many packet contexts as you need. Each driver subsystem can now use a different context, creating flexibility and improving componentization.

### Finer link layer address control

Two new methods, [NetAdapterSetPermanentLinkLayerAddress](netadaptersetpermanentlinklayeraddress.md) and [NetAdapterSetCurrentLinkLayerAddress](netadaptersetcurrentlinklayeraddress.md), have been added in NetAdapter 1.1 to allow NIC client drivers to more easily set these separate addresses with dedicated methods. Previously, in version 1.0, this functionality was embedded in the [NetAdapterSetLinkLayerCapabilities](netadaptersetlinklayercapabilities.md) method and required additional complexity in allocating and initializing that method's [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md) structure.

## API changes

### New APIs

The following APIs are new in NetAdapterCx 1.1.

- [NET_ADAPTER_LINK_LAYER_ADDRESS_INIT](net-adapter-link-layer-address-init.md)
- [NetAdapterSetPermanentLinkLayerAddress](netadaptersetpermanentlinklayeraddress.md)
- [NetAdapterSetCurrentLinkLayerAddress](netadaptersetcurrentlinklayeraddress.md)
- [NET_PACKET_CONTEXT_TOKEN]
- [NET_PACKET_CONTEXT_ATTRIBUTES]
- [NET_PACKET_DECLARE_CASTING_FUNCTION_FROM_TOKEN]
- [NetPacketGetContextFromToken]
- [NetConfigurationQueryLinkLayerAddress]
- [NET_RXQUEUE_BUFFER_LAYOUT_HINT]
- [NET_RXQUEUE_GET_PACKET_CONTEXT_TOKEN]
- [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG]
- [NET_RXQUEUE_DMA_ALLOCATOR_CONFIG_INIT]
- [NetRxQueueQueryAllocatorCacheEnabled]
- [NetRxQueueGetPacketContextToken]
- [NetRxQueueInitAddPacketContextAttributes]
- [NetRxQueueInitSetDmaAllocatorConfig]
- [NetRxQueueGetBufferLayoutHint]
- [NET_TXQUEUE_GET_PACKET_CONTEXT_TOKEN]
- [NetTxQueueGetPacketContextToken]
- [NetTxQueueInitAddPacketContextAttributes]

### Updated APIs

The following APIs were updated in NetAdapterCx 1.1.

- [NET_ADAPTER_LINK_LAYER_CAPABILITIES](net-adapter-link-layer-capabilities.md)
- [NET_ADAPTER_LINK_LAYER_CAPABILITIES_INIT](net-adapter-link-layer-capabilities-init.md)
- [NET_ADAPTER_CONFIG](net-adapter-config.md)
- [NET_ADAPTER_CONFIG_INIT](net-adapter-config-init.md)
- [NetAdapterDriverWdmGetHandle](netadapterdriverwdmgethandle.md)
- [NetPowerSettingsGetWakePatternCount](netpowersettingsgetwakepatterncount.md)
- [NetPowerSettingsGetWakePatternCountForType](netpowersettingsgetwakepatterncountfortype.md)
- [NetPowerSettingsGetWakePattern](netpowersettingsgetwakepattern.md)
- [NetPowerSettingsIsWakePatternEnabled](netpowersettingsiswakepatternenabled.md)
- [NetPowerSettingsGetEnabledWakeUpFlags](netpowersettingsgetenabledwakeupflags.md)
- [NetPowerSettingsGetEnabledProtocolOffloadFlags](netpowersettingsgetenabledprotocoloffloadflags.md)
- [NetPowerSettingsGetEnabledMediaSpecificWakeUpEvents](netpowersettingsgetenabledmediaspecificwakeupevents.md)
- [NetPowerSettingsGetProtocolOffloadCount](netpowersettingsgetprotocoloffloadcount.md)
- [NetPowerSettingsGetProtocolOffloadCountForType](netpowersettingsgetprotocoloffloadcountfortype.md)
- [NetPowerSettingsGetProtocolOffload](netpowersettingsgetprotocoloffload.md)
- [NetPowerSettingsIsProtocolOffloadEnabled](netpowersettingsisprotocoloffloadenabled.md)
- [EVT_RXQUEUE_SET_NOTIFICATION_ENABLED](evt-rxqueue-set-notification-enabled.md)
- [NET_RXQUEUE_CONFIG](net-rxqueue-config.md)
- [EVT_TXQUEUE_SET_NOTIFICATION_ENABLED](evt-txqueue-set-notification-enabled.md)
- [NET_TXQUEUE_CONFIG](net-txqueue-config.md)

### Removed APIs

The following APIs were removed in NetAdapterCx 1.1. Many of them were replaced with a different API. See each topic for details.

- [NET_ADAPTER_PHYSICAL_ADDRESS](net-adapter-physical-address.md)
- [NET_ADAPTER_PHYSICAL_ADDRESS_INIT](net-adapter-physical-address-init.md)
- [NET_ADAPTER_LINK_LAYER_CAPABILITIES_NO_PHYSICAL_ADDRESS](net-adapter-link-layer-capabilities-init-no-physical-address.md)
- [NetConfigurationQueryNetworkAddress](netconfigurationquerynetworkaddress.md)
- [NetRxQueueConfigureDmaAllocator](netrxqueueconfiguredmaallocator.md)

## Compiling a NetAdapterCx 1.1 client driver

If you are porting an NDIS 6.x miniport driver to NetAdapter 1.1, first follow the compilation steps on [Porting NDIS miniport drivers to NetAdapterCx](porting-ndis-miniport-drivers-to-netadaptercx.md). Then, in the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **1**.

If you are porting a NetAdapterCx client driver from an earlier version of NetAdapterCx, in the **Configuration Properties > Driver Settings > Network Adapter Driver** dialog box, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **1**.

If you are writing a new NetAdapterCx client driver, follow the steps on [Building a NetAdapterCx client driver](building-a-netadaptercx-client-driver.md) and, in Step 5, set **Network Adapter Major Version** to **1** and **Network Adapter Minor Version** to **1**.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")