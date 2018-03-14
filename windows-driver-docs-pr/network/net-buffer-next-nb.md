---
title: NET_BUFFER_NEXT_NB macro
author: windows-driver-content
description: NET_BUFFER_NEXT_NB is a macro that NDIS drivers use to get a pointer to the next NET_BUFFER structure in a linked list of NET_BUFFER structures.
ms.assetid: 2c9bf3eb-4aa9-4983-91a8-c78f100b2d5f
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_NEXT_NB macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_NEXT\_NB macro


NET\_BUFFER\_NEXT\_NB is a macro that NDIS drivers use to get a pointer to the next [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure in a linked list of NET\_BUFFER structures.

Syntax
------

```ManagedCPlusPlus
PVOID NET_BUFFER_NEXT_NB(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_NEXT\_NB returns a pointer to the next NET\_BUFFER structure in the linked list of NET\_BUFFER structures, or it returns **NULL** if the end of the linked list is reached.

Remarks
-------

NET\_BUFFER\_NEXT\_NB gets the return value from the **Next** member of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

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

 

 




