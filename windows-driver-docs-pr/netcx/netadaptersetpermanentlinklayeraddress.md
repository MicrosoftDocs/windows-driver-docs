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

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

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
A NET_ADAPTER_LINK_LAYER_ADDRESS object that the driver initialized in a prior call to [NET_ADAPTER_LINK_LAYER_ADDRESS_INIT](net-adapter-link-layer-address-init.md).

## Return value

This method does not return a value.

## Requirements

|     |     |
| --- | --- |
| Target platform | Universal |
| Minimum KMDF version | 1.23 |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netadapter.h (include NetAdapterCx.h) |
| IRQL | PASSIVE_LEVEL |

