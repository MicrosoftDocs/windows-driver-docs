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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_MAKE_NET_LUID%20macro%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


