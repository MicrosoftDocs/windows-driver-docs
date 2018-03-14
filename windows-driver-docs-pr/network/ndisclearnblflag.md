---
title: NdisClearNblFlag macro
author: windows-driver-content
description: The NdisClearNblFlag macro clears a flag in a NET_BUFFER_LIST structure.
ms.assetid: a9f85e1c-b96e-4e2b-b0f6-ef2676ac2ef5
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NdisClearNblFlag macro Network Drivers Starting with Windows Vista
---

# NdisClearNblFlag macro


The **NdisClearNblFlag** macro clears a flag in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
VOID NdisClearNblFlag(
    _NBL,
    _F
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

*\_F*   
The flag in the **NblFlags** member of the NET\_BUFFER\_LIST structure to clear.

Return value
------------

None

Remarks
-------

NDIS drivers use the **NdisClearNblFlag** macro to clear the specified flag ( *\_F* ) in the **NblFlags** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

For more information about the flags, see the **NblFlags** member on the NET\_BUFFER\_LIST topics.

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

 

 




