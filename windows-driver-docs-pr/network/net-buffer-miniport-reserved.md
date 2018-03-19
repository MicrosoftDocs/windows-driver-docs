---
title: NET_BUFFER_MINIPORT_RESERVED macro
author: windows-driver-content
description: NET_BUFFER_MINIPORT_RESERVED is a macro that NDIS drivers use to access the MiniportReserved member of a NET_BUFFER structure.
ms.assetid: 609b2d69-61bd-458b-865b-29c8305dd841
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_MINIPORT_RESERVED macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_MINIPORT\_RESERVED macro


NET\_BUFFER\_MINIPORT\_RESERVED is a macro that NDIS drivers use to access the **MiniportReserved** member of a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NET_BUFFER_MINIPORT_RESERVED(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_MINIPORT\_RESERVED returns a pointer to the start of the **MiniportReserved** member of the specified NET\_BUFFER structure.

Remarks
-------

Miniport drivers and NDIS intermediate drivers can use **MiniportReserved** for their own purposes. Miniport drivers typically use **MiniportReserved** to maintain [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure context information for outstanding transfers.

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


[**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376)

 

 




