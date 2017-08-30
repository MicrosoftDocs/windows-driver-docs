---
title: NET_ADAPTER_LINK_LAYER_ADDRESS
description: NET_ADAPTER_LINK_LAYER_ADDRESS 
ms.assetid: D733EE67-A17B-4BC0-BF89-7858ECCD5E10
keywords:
- WDF Network Adapter Class Extension NET_ADAPTER_LINK_LAYER_ADDRESS, NetAdapterCx NET_ADAPTER_LINK_LAYER_ADDRESS, NetCx NET_ADAPTER_LINK_LAYER_ADDRESS
ms.author: windowsdriverdev
ms.date: 08/29/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NET_ADAPTER_LINK_LAYER_ADDRESS

The **NET_ADAPTER_LINK_LAYER_ADDRESS** typedef represents a physical link layer address for the network adapter.

## Syntax

```cpp
typedef NDIS_IF_PHYSICAL_ADDRESS NET_ADAPTER_LINK_LAYER_ADDRESS, *PNET_ADAPTER_LINK_LAYER_ADDRESS;
```

## Parameters

This typedef has no parameters.

## Return value

This typedef does not return a value.

## Remarks

**NET_ADAPTER_LINK_LAYER_ADDRESS** is initialized with the [NET_ADAPTER_LINK_LAYER_ADDRESS_INIT](net-adapter-link-layer-address-init.md) method.

## Requirements

|     |     |
| --- | --- |
| Minimum supported client | Windows 10, version 1709 |
| Minimum supported server | Windows Server 2016 |
| Minimum KMDF version | ? |
| Minimum NetAdapterCx version | 1.1 |
| Header | Netadapter.h (include NetAdapterCx.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")