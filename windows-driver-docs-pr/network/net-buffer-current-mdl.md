---
title: NET_BUFFER_CURRENT_MDL macro
author: windows-driver-content
description: NET_BUFFER_CURRENT_MDL is a macro that NDIS drivers use to get the CurrentMdl member of a NET_BUFFER_DATA structure in a NET_BUFFER structure.
ms.assetid: c2fc283f-13b7-4c04-96c2-4bc1ea811a17
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_CURRENT_MDL macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_CURRENT\_MDL macro


NET\_BUFFER\_CURRENT\_MDL is a macro that NDIS drivers use to get the **CurrentMdl** member of a [**NET\_BUFFER\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568381) structure in a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Syntax
------

```ManagedCPlusPlus
PMDL NET_BUFFER_CURRENT_MDL(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_CURRENT\_MDL returns the value of the **CurrentMdl** member of the indicated NET\_BUFFER structure.

Remarks
-------

The return value is a pointer to the first MDL that the current driver is using. This pointer provides an optimization that improves performance by skipping over any MDLs that the current driver is not using.

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

[**NET\_BUFFER\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568381)

 

 




