---
title: NDIS_CURRENT_IRQL macro
author: windows-driver-content
description: The NDIS_CURRENT_IRQL macro returns the current interrupt request level (IRQL).
ms.assetid: 002c751c-6106-47bc-ab11-610fbcd84ffa
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_CURRENT_IRQL macro Network Drivers Starting with Windows Vista
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

 

 




