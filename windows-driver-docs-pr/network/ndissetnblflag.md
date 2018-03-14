---
title: NdisSetNblFlag macro
author: windows-driver-content
description: The NdisSetNblFlag macro sets a flag in a NET_BUFFER_LIST structure.
ms.assetid: 0a92b689-fe82-4ac6-a674-5e249dd8e1f1
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NdisSetNblFlag macro Network Drivers Starting with Windows Vista
---

# NdisSetNblFlag macro


The **NdisSetNblFlag** macro sets a flag in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
VOID NdisSetNblFlag(
    _NBL,
    _F
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

*\_F*   
The flag in the **NblFlags** member of the NET\_BUFFER\_LIST structure to set.

Return value
------------

None

Remarks
-------

NDIS drivers use the **NdisSetNblFlag** macro to set the specified flag ( *\_F* ) in the **NblFlags** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

For more information about the flags, see the **NblFlags** member on the NET\_BUFFER\_LIST topic.

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

 

 




