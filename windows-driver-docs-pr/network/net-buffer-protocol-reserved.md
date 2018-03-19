---
title: NET_BUFFER_PROTOCOL_RESERVED macro
author: windows-driver-content
description: NET_BUFFER_PROTOCOL_RESERVED is a macro that NDIS drivers use to get the ProtocolReserved member of a NET_BUFFER structure.
ms.assetid: ab46cce0-c77f-4e08-9522-6a6674d557e8
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_PROTOCOL_RESERVED macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_PROTOCOL\_RESERVED macro


NET\_BUFFER\_PROTOCOL\_RESERVED is a macro that NDIS drivers use to get the **ProtocolReserved** member of a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Syntax
------

```ManagedCPlusPlus
PVOID NET_BUFFER_PROTOCOL_RESERVED(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_PROTOCOL\_RESERVED returns the value of the **ProtocolReserved** member of the specified NET\_BUFFER structure.

Remarks
-------

Protocol drivers and NDIS intermediate drivers can use this area for their own purposes. Protocol drivers typically use **ProtocolReserved** to maintain [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure context information for outstanding transfers.

**Note**  Only one driver can use **ProtocolReserved** . Therefore, if an another driver has used **ProtocolReserved**, an intermediate driver cannot use it.

 

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

 

 




