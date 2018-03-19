---
title: NET_BUFFER_LIST_NBL_FLAGS macro
author: windows-driver-content
description: The NET_BUFFER_LIST_NBL_FLAGS macro retrieves the NblFlags member of a NET_BUFFER_LIST structure.
ms.assetid: 3ae4336d-4b62-476e-9b20-bf41fc308dc4
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_NBL_FLAGS macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_NBL\_FLAGS macro


The NET\_BUFFER\_LIST\_NBL\_FLAGS macro retrieves the **NblFlags** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
VOID NET_BUFFER_LIST_NBL_FLAGS(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

None

Remarks
-------

NDIS network drivers should use the NET\_BUFFER\_LIST\_NBL\_FLAGS macro to get the **NblFlags** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

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
<td><p>Supported in NDIS 6.1 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388)

 

 




