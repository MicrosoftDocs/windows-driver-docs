---
title: NetAdapterSetPermanentLinkLayerAddress method
description: NetAdapterSetPermanentLinkLayerAddress method
ms.assetid: 2D34FC6D-C9BC-4402-B4D9-822613D1CE3E
keywords:
- WDF Network Adapter Class Extension NetAdapterSetPermanentLinkLayerAddress, NetAdapterCx NetAdapterSetPermanentLinkLayerAddress, NetCx NetAdapterSetPermanentLinkLayerAddress
ms.author: windowsdriverdev
ms.date: 08/29/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetAdapterSetPermanentLinkLayerAddress method

The NetAdapterSetPermanentLinkLayerAddress method sets the permanent link layer address for the network adapter.

## Syntax

```cpp
VOID FORCEINLINE NetAdapterSetPermanentLinkLayerAddress(
    _In_    NETADAPTER                      Adapter,
    _In_    PNET_ADAPTER_LINK_LAYER_ADDRESS LinkLayerAddress
);
```

## Parameters

*Adapter* [in]  
The network adapter object that the driver created in a prior call to [NetAdapterCreate](netadaptercreate.md).

*LinkLayerAddress*  
A [NET_ADAPTER_LINK_LAYER_ADDRESS](net-adapter-link-layer-address.md) object that the driver initialized in a prior call to [NET_ADAPTER_LINK_LAYER_ADDRESS_INIT](net-adapter-link-layer-address-init.md).

## Return value

This method does not return a value.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum supported client | Windows 10, version 1709 |
| Minimum supported server | Windows Server 2016 |
| Minimum KMDF version | ? |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netadapter.h (include NetAdapterCx.h) |
| IRQL | PASSIVE_LEVEL |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")