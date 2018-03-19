---
title: NET_BUFFER_FIRST_MDL macro
author: windows-driver-content
description: NET_BUFFER_FIRST_MDL is a macro that NDIS drivers use to get the first MDL in a NET_BUFFER structure.
ms.assetid: d62c7183-ef28-408a-b862-6a2d97026b35
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_FIRST_MDL macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_FIRST\_MDL macro


NET\_BUFFER\_FIRST\_MDL is a macro that NDIS drivers use to get the first MDL in a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Syntax
------

```ManagedCPlusPlus
PMDL NET_BUFFER_FIRST_MDL(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_FIRST\_MDL returns a pointer to the first MDL in a linked list of MDLs that is associated with the indicated NET\_BUFFER structure.

Remarks
-------

NET\_BUFFER\_FIRST\_MDL gets the return value from the **MdlChain** member of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

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

 

 




