---
title: NDIS\_CURRENT\_IRQL macro
description: The NDIS\_CURRENT\_IRQL macro returns the current interrupt request level (IRQL).
MS-HAID:
- 'ndis\_interrupts\_sync\_macros\_ref\_af078fda-a4a5-4283-ba1a-b9430ce076d1.xml'
- 'netvista.ndis\_current\_irql'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 002c751c-6106-47bc-ab11-610fbcd84ffa
keywords: ["NDIS_CURRENT_IRQL macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_CURRENT_IRQL
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NDIS\_CURRENT\_IRQL macro


The NDIS\_CURRENT\_IRQL macro returns the current interrupt request level (IRQL).

Syntax
------

```ManagedCPlusPlus
KIRQL NDIS_CURRENT_IRQL(
    None
);
```

Parameters
----------

*None*   

Return value
------------

NDIS\_CURRENT\_IRQL returns the current IRQL as a KIRQL-type value.

Remarks
-------

NDIS drivers should use the NDIS\_CURRENT\_IRQL macro to obtain the caller's current IRQL.

This macro is an NDIS wrapper for the [**KeGetCurrentIrql**](https://msdn.microsoft.com/library/windows/hardware/ff552054) routine

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
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>Any level</p></td>
</tr>
</tbody>
</table>

## See also


[**KeGetCurrentIrql**](https://msdn.microsoft.com/library/windows/hardware/ff552054)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_CURRENT_IRQL%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





