---
title: NDIS\_CURRENT\_PROCESSOR\_NUMBER macro
description: The NDIS\_CURRENT\_PROCESSOR\_NUMBER macro returns the system-assigned number of the current processor that the caller is running on.
MS-HAID:
- 'ndis\_interrupts\_sync\_macros\_ref\_88272c34-db17-46b0-9d2c-f447d831f44f.xml'
- 'netvista.ndis\_current\_processor\_number'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 83a9861c-f8c1-404b-baa3-c5e9f3d760bb
keywords: ["NDIS_CURRENT_PROCESSOR_NUMBER macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_CURRENT_PROCESSOR_NUMBER
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NDIS\_CURRENT\_PROCESSOR\_NUMBER macro


The **NDIS\_CURRENT\_PROCESSOR\_NUMBER** macro returns the system-assigned number of the current processor that the caller is running on.

Syntax
------

```ManagedCPlusPlus
ULONG NDIS_CURRENT_PROCESSOR_NUMBER(
    None
);
```

Parameters
----------

*None*   

Return value
------------

NDIS\_CURRENT\_PROCESSOR\_NUMBER returns a ULONG value that represents the processor that the caller is currently running on.

Remarks
-------

An NDIS driver might call NDIS\_CURRENT\_PROCESSOR\_NUMBER if it maintains some per-processor data.

The number of processors in a symmetric multiprocessor (SMP) computer is a zero-based value.

The NDIS\_CURRENT\_PROCESSOR\_NUMBER wraps the [**KeGetCurrentProcessorNumber**](https://msdn.microsoft.com/library/windows/hardware/ff552063) routine.

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
<td><p>Supported in NDIS 6.0 and NDIS 6.1. For NDIS 6.20 and later, use [<strong>NdisCurrentProcessorIndex</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561737) instead.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>&gt;= DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**KeGetCurrentProcessorNumber**](https://msdn.microsoft.com/library/windows/hardware/ff552063)

[**NdisCurrentProcessorIndex**](https://msdn.microsoft.com/library/windows/hardware/ff561737)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_CURRENT_PROCESSOR_NUMBER%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





