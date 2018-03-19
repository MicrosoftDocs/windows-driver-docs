---
title: NdisTestNblFlags macro
author: windows-driver-content
description: The NdisTestNblFlags macro tests the setting of a set of flags in a NET_BUFFER_LIST structure.
ms.assetid: adddae72-11ff-44f0-ac90-5792e0203b64
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NdisTestNblFlags macro Network Drivers Starting with Windows Vista
---

# NdisTestNblFlags macro


The **NdisTestNblFlags** macro tests the setting of a set of flags in a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
BOOLEAN NdisTestNblFlags(
    _NBL,
    _F
);
```

Parameters
----------

*\_NBL*   
A pointer to a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

*\_F*   
The flags, combined with a bitwise OR operation, in the **NblFlags** member of the NET\_BUFFER\_LIST structure to test.

Return value
------------

**NdisTestNblFlags** returns **TRUE** if all flags that are specified in the *\_F* parameter are set. Otherwise, this macro returns **FALSE**.

Remarks
-------

NDIS drivers use the **NdisTestNblFlags** macro to retrieve the state of the specified flags ( *\_F* ) in the **NblFlags** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Use **NdisTestNblFlags** to determine whether a set of specified flags are all set.

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

 

 




