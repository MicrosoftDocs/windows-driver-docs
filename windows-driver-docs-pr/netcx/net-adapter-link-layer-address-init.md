---
title: NET_ADAPTER_LINK_LAYER_ADDRESS_INIT method
description: NET_ADAPTER_LINK_LAYER_ADDRESS_INIT method
ms.assetid: C862B086-E736-484B-823E-8ADE71250C75
keywords:
- WDF Network Adapter Class Extension NET_ADAPTER_LINK_LAYER_ADDRESS_INIT, NetAdapterCx NET_ADAPTER_LINK_LAYER_ADDRESS_INIT, NetCx NET_ADAPTER_LINK_LAYER_ADDRESS_INIT
ms.author: windowsdriverdev
ms.date: 08/29/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_ADAPTER_LINK_LAYER_ADDRESS_INIT method

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The NET_ADAPTER_LINK_LAYER_ADDRESS_INIT method initializes a link layer address.

## Syntax

```cpp
FORCEINLINE VOID NET_ADAPTER_LINK_LAYER_ADDRESS_INIT(
    _Out_                                       PNET_ADAPTER_LINK_LAYER_ADDRESS LinkLayerAddress,
    _In_range_(1,NDIS_MAX_PHYS_ADDRESS_LENGTH)  USHORT                          Length,
    _In_reads_bytes_(Length)                    PCUCHAR                         AddressBuffer
);
```

## Parameters

*LinkLayerAddress* [out]  
A pointer to the driver-allocated NET_ADAPTER_LINK_LAYER_ADDRESS to be initialized.

*Length* [in]  
The length of the link layer address, in bytes.

*AddressBuffer* [in]  
A pointer to the buffer containing the link layer address.

## Return value

This method does not return a value.

## Remarks

**NET_ADAPTER_LINK_LAYER_ADDRESS_INIT** is used to initialize either a permanent or current link layer address, stored in a **NET_ADAPTER_LINK_LAYER_ADDRESS** allocated by the driver. This **NET_ADAPTER_LINK_LAYER_ADDRESS** is then passed as a parameter to either the [NetAdapterSetPermanentLinkLayerAddress](netadaptersetpermanentlinklayeraddress.md) method or the [NetAdapterSetCurrentLinkLayerAddress](netadaptersetcurrentlinklayeraddress.md) method, depending on the type of address that was initialized and is being set.

## Requirements

|     |     |
| --- | --- |
| Minimum supported client | Windows 10, version 1709 |
| Minimum supported server | Windows Server 2016 |
| Header | NetAdapter.h (include NetAdapterCx.h) |
| IRQL | PASSIVE_LEVEL |

