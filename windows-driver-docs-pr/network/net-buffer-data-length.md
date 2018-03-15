---
title: NET_BUFFER_DATA_LENGTH macro
author: windows-driver-content
description: NET_BUFFER_DATA_LENGTH is a macro that NDIS drivers use to get the amount of used data space in a NET_BUFFER structure.
ms.assetid: 7fa9f67e-7b81-4bab-914b-cd02028fb21e
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_DATA_LENGTH macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_DATA\_LENGTH macro


NET\_BUFFER\_DATA\_LENGTH is a macro that NDIS drivers use to get the amount of *used data space* in a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Syntax
------

```ManagedCPlusPlus
ULONG NET_BUFFER_DATA_LENGTH(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_DATA\_LENGTH returns the amount of *used data space* in a NET\_BUFFER structure.

Remarks
-------

NET\_BUFFER\_DATA\_LENGTH gets the return value from the **DataLength** member of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

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
</tbody>
</table>

## See also


[**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376)

 

 




