---
title: NDIS_CURRENT_PROCESSOR_NUMBER macro
author: windows-driver-content
description: The NDIS_CURRENT_PROCESSOR_NUMBER macro returns the system-assigned number of the current processor that the caller is running on.
ms.assetid: 83a9861c-f8c1-404b-baa3-c5e9f3d760bb
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_CURRENT_PROCESSOR_NUMBER macro Network Drivers Starting with Windows Vista
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

 

 




