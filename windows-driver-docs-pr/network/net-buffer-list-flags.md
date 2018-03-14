---
title: NET_BUFFER_LIST_FLAGS macro
author: windows-driver-content
description: NET_BUFFER_LIST_FLAGS is a macro that NDIS drivers use to get the flags associated with a NET_BUFFER_LIST structure.
ms.assetid: 2ad9b515-4bce-463c-893f-047554e9cbd0
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_FLAGS macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_FLAGS macro


NET\_BUFFER\_LIST\_FLAGS is a macro that NDIS drivers use to get the flags associated with a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
ULONG NET_BUFFER_LIST_FLAGS(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_FLAGS returns the **Flags** member of the indicated NDIS\_BUFFER\_LIST structure.

Remarks
-------

For definitions of the possible NET\_BUFFER\_LIST structure flags, see [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388).

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

 

 




