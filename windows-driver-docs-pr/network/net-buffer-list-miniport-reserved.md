---
title: NET_BUFFER_LIST_MINIPORT_RESERVED macro
author: windows-driver-content
description: NET_BUFFER_LIST_MINIPORT_RESERVED is a macro that NDIS drivers use to access the MiniportReserved member of a NET_BUFFER_LIST structure.
ms.assetid: 1f790c34-e235-4e19-9dd9-62f54703206c
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_LIST_MINIPORT_RESERVED macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_LIST\_MINIPORT\_RESERVED macro


NET\_BUFFER\_LIST\_MINIPORT\_RESERVED is a macro that NDIS drivers use to access the **MiniportReserved** member of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NET_BUFFER_LIST_MINIPORT_RESERVED(
   PNET_BUFFER_LIST _NBL
);
```

Parameters
----------

*\_NBL*   
A pointer to a NET\_BUFFER\_LIST structure.

Return value
------------

NET\_BUFFER\_LIST\_MINIPORT\_RESERVED returns a pointer to the start of the **MiniportReserved** member of the indicated NET\_BUFFER\_LIST structure.

Remarks
-------

Miniport drivers and NDIS intermediate drivers can use **MiniportReserved** for their own purposes.

**Note**  Only one driver can use **MiniportReserved** . Therefore, if another driver has used **MiniportReserved**, an intermediate driver cannot use it.

 

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

 

 




