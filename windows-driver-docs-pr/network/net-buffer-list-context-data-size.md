---
title: NET_BUFFER_LIST_CONTEXT_DATA_SIZE macro
author: windows-driver-content
description: NET_BUFFER_LIST_CONTEXT_DATA_SIZE is a macro that NDIS drivers use to get the size of the NET_BUFFER_LIST_CONTEXT data buffer that is associated with a NET_BUFFER_LIST structure.
ms.assetid: 28966e3d-db1d-4caf-b7e2-b79e97ed25cb
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_CONTEXT_DATA_SIZE macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_CONTEXT\_DATA\_SIZE macro


NET\_BUFFER\_LIST\_CONTEXT\_DATA\_SIZE is a macro that NDIS drivers use to get the size of the [**NET\_BUFFER\_LIST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff568389) data buffer that is associated with a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
USHORT NET_BUFFER_LIST_CONTEXT_DATA_SIZE(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_CONTEXT\_DATA\_SIZE returns the size, in bytes, of the NET\_BUFFER\_LIST\_CONTEXT data buffer that is associated with the indicated NET\_BUFFER\_LIST structure.

Remarks
-------

NET\_BUFFER\_LIST\_CONTEXT\_DATA\_SIZE gets the return value from the **Size** member of the first [**NET\_BUFFER\_LIST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure.

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

[**NET\_BUFFER\_LIST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff568389)

 

 




