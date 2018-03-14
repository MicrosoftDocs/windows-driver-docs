---
title: NET_BUFFER_LIST_NEXT_NBL macro
author: windows-driver-content
description: NET_BUFFER_LIST_NEXT_NBL is a macro that NDIS drivers use to get the next NET_BUFFER_LIST structure in a linked list of NET_BUFFER_LIST structures.
ms.assetid: 5f0fc110-5e17-4030-b25b-e00d25b60b14
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_NEXT_NBL macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_NEXT\_NBL macro


NET\_BUFFER\_LIST\_NEXT\_NBL is a macro that NDIS drivers use to get the next [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure in a linked list of NET\_BUFFER\_LIST structures.

Syntax
------

```ManagedCPlusPlus
PNET_BUFFER_LIST NET_BUFFER_LIST_NEXT_NBL(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_NEXT\_NBL returns a pointer to the next NET\_BUFFER\_LIST structure in the linked list of NET\_BUFFER\_LIST structures, or it returns **NULL** if the end of the linked list is reached.

Remarks
-------

NET\_BUFFER\_LIST\_NEXT\_NBL gets the return value from the **Next** member of the [**NET\_BUFFER\_LIST\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568393) structure in the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure that the *\_NBL* parameter points to.

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

[**NET\_BUFFER\_LIST\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568393)

 

 




