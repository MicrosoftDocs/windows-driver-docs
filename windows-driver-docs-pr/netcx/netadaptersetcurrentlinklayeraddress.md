---
title: NetAdapterSetCurrentLinkLayerAddress method
description: NetAdapterSetCurrentLinkLayerAddress method
ms.assetid: D0FD3D0E-3C25-4B5D-A944-16A08A3E9D44
keywords:
- WDF Network Adapter Class Extension NetAdapterSetCurrentLinkLayerAddress, NetAdapterCx NetAdapterSetCurrentLinkLayerAddress, NetCx NetAdapterSetCurrentLinkLayerAddress
ms.author: windowsdriverdev
ms.date: 08/29/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NetAdapterSetCurrentLinkLayerAddress method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NetAdapterSetCurrentLinkLayerAddress method sets the current link layer address for the network adapter.

## Syntax

```cpp
VOID FORCEINLINE NetAdapterSetCurrentLinkLayerAddress(
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

