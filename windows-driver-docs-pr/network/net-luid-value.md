---
title: NET_LUID Value
description: NET_LUID Value
ms.assetid: 9b9c63c1-f8b4-4e26-afc1-a3e4910609e2
keywords:
- NDIS network interfaces WDK , NET_LUID
- network interfaces WDK , NET_LUID
- NET_LUID
- index operations WDK network interface
- locally unique identifier WDK network interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NET\_LUID Value





A [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) value is a 64-bit value that identifies an NDIS network interface. The NET\_LUID data type is a union that can provide access to the NET\_LUID value as a single 64-bit value or as a structure that contains a NET\_LUID index and an interface type.

The **NetLuidIndex** member of the NET\_LUID union is a 24-bit NET\_LUID index that NDIS allocates when an interface provider calls the [**NdisIfAllocateNetLuidIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562695) function. NDIS and interface providers use this index to distinguish between multiple interfaces that have the same interface type. Therefore, this index is unique within a local computer.

The **IfType** member of the [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) union is a 16-bit value that contains an Internet Assigned Numbers Authority (IANA)-defined interface type. For a list of valid interface types, see [NDIS Interface Types](https://msdn.microsoft.com/library/windows/hardware/ff565767).

The NET\_LUID data type is equivalent to the *ifName* object in RFC 2863, because NDIS derives the *ifName* string from a NET\_LUID value.

To create a NET\_LUID value, an interface provider calls the [**NdisIfAllocateNetLuidIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562695) function to allocate a NET\_LUID index and then calls the [**NDIS\_MAKE\_NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff565890) macro to build the NET\_LUID value. For more information about creating NET\_LUID values, see [Using NET\_LUID Indexes](using-a-net-luid-index.md).

 

 





