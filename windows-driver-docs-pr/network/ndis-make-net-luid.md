---
title: NDIS_MAKE_NET_LUID macro
author: windows-driver-content
description: The NDIS_MAKE_NET_LUID macro builds a NET_LUID value from an interface type and a NET_LUID index.
ms.assetid: 57b04978-8f02-4d35-9e4a-0929cb79aabb
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_MAKE_NET_LUID macro Network Drivers Starting with Windows Vista
---

# NDIS\_MAKE\_NET\_LUID macro


The NDIS\_MAKE\_NET\_LUID macro builds a [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) value from an interface type and a NET\_LUID index.

Syntax
------

```ManagedCPlusPlus
VOID NDIS_MAKE_NET_LUID(
   PNET_LUID _pNetLuid,
   ULONG64   _IfType,
   ULONG64   _NetLuidIndex
);
```

Parameters
----------

*\_pNetLuid*   
A pointer to a caller-supplied [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) union. NDIS\_MAKE\_NET\_LUID returns the newly created NET\_LUID value in this variable.

*\_IfType*   
The Internet Assigned Numbers Authority (IANA) interface type. NDIS\_MAKE\_NET\_LUID writes the value at *\_IfType* to the **IfType** member of the NET\_LUID union that the caller provided at *\_pNetLuid* . For a list of interface types, see [NDIS Interface Types](https://msdn.microsoft.com/library/windows/hardware/ff565767).

*\_NetLuidIndex*   
A NET\_LUID index that the caller allocated with the [**NdisIfAllocateNetLuidIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562695) function. NDIS\_MAKE\_NET\_LUID writes the value at *\_NetLuidIndex* to the **NetLuidIndex** member of the NET\_LUID union that the caller provided at *\_pNetLuid* .

Return value
------------

None

Remarks
-------

NDIS network interface providers should use the NDIS\_MAKE\_NET\_LUID macro to build a [**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747) value. The provider passes the resulting NET\_LUID value to the [**NdisIfRegisterInterface**](https://msdn.microsoft.com/library/windows/hardware/ff562715) function to register the interface with NDIS.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ntddndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NdisIfAllocateNetLuidIndex**](https://msdn.microsoft.com/library/windows/hardware/ff562695)

[**NdisIfRegisterInterface**](https://msdn.microsoft.com/library/windows/hardware/ff562715)

[**NET\_LUID**](https://msdn.microsoft.com/library/windows/hardware/ff568747)

 

 




