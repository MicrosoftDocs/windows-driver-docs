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

The **NET_ADAPTER_LINK_LAYER_ADDRESS_INIT** method initializes a link layer address.

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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
