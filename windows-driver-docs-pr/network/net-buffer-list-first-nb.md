---
title: NET_BUFFER_LIST_FIRST_NB macro
author: windows-driver-content
description: NET_BUFFER_LIST_FIRST_NB is a macro that NDIS drivers use to get the first NET_BUFFER structure in a NET_BUFFER_LIST structure.
ms.assetid: 695cb2ea-04aa-49e8-9910-01f8d85b7338
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_FIRST_NB macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_FIRST\_NB macro


NET\_BUFFER\_LIST\_FIRST\_NB is a macro that NDIS drivers use to get the first [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
PNET_BUFFER NET_BUFFER_LIST_FIRST_NB(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_FIRST\_NB returns a pointer to the first NET\_BUFFER structure in the indicated NET\_BUFFER\_LIST structure.

Remarks
-------

NET\_BUFFER\_LIST\_FIRST\_NB gets the return value from the **FirstNetBuffer** member of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

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

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




