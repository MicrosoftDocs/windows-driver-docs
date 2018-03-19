---
title: NET_BUFFER_LIST_STATUS macro
author: windows-driver-content
description: NET_BUFFER_LIST_STATUS is a macro that NDIS drivers use to access the StatusCode member of a NET_BUFFER_LIST structure.
ms.assetid: 0101c6f1-4690-4d53-a28d-d13995dc2691
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_STATUS macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_STATUS macro


NET\_BUFFER\_LIST\_STATUS is a macro that NDIS drivers use to access the **StatusCode** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
NDIS_STATUS NET_BUFFER_LIST_STATUS(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_STATUS returns the value of the **StatusCode** member of the indicated NET\_BUFFER\_LIST structure.

Remarks
-------

Miniport drivers and NDIS intermediate drivers can use **StatusCode** for their own purposes.

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


[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




