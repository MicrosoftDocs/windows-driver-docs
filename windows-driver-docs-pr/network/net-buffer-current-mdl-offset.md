---
title: NET_BUFFER_CURRENT_MDL_OFFSET macro
author: windows-driver-content
description: NET_BUFFER_CURRENT_MDL_OFFSET is a macro that NDIS drivers use to get the CurrentMdlOffset member of a NET_BUFFER structure.
ms.assetid: 49b14d42-584f-40de-8ba7-d0a74800886a
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_CURRENT_MDL_OFFSET macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_CURRENT\_MDL\_OFFSET macro


NET\_BUFFER\_CURRENT\_MDL\_OFFSET is a macro that NDIS drivers use to get the **CurrentMdlOffset** member of a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Syntax
------

```ManagedCPlusPlus
ULONG NET_BUFFER_CURRENT_MDL_OFFSET(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_CURRENT\_MDL\_OFFSET returns the value of the **CurrentMdlOffset** member of the indicated NET\_BUFFER structure.

Remarks
-------

The return value specifies the offset, in bytes, to the beginning of the used data space in the MDL that is specified by the **CurrentMdl** member of the NET\_BUFFER structure.

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

 

 




