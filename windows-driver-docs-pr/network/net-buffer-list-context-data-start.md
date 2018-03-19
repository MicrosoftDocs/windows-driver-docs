---
title: NET_BUFFER_LIST_CONTEXT_DATA_START macro
author: windows-driver-content
description: NET_BUFFER_LIST_CONTEXT_DATA_START is a macro that NDIS drivers use to get a pointer to the NET_BUFFER_LIST_CONTEXT context space that is associated with a NET_BUFFER_LIST structure.
ms.assetid: 165dc176-61fc-41d0-9342-803b45ad3bc1
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_CONTEXT_DATA_START macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_CONTEXT\_DATA\_START macro


NET\_BUFFER\_LIST\_CONTEXT\_DATA\_START is a macro that NDIS drivers use to get a pointer to the [**NET\_BUFFER\_LIST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff568389) context space that is associated with a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NET_BUFFER_LIST_CONTEXT_DATA_START(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_CONTEXT\_DATA\_START returns a pointer to the NET\_BUFFER\_LIST\_CONTEXT context space that is associated with the indicated NET\_BUFFER\_LIST structure.

Remarks
-------

NET\_BUFFER\_LIST\_CONTEXT\_DATA\_START returns a pointer to the start of the used context space in the **ContextData** member of the [**NET\_BUFFER\_LIST\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff568389) structure.

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

 

 




