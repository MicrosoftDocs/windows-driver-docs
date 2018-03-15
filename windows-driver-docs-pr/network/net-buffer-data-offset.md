---
title: NET_BUFFER_DATA_OFFSET macro
author: windows-driver-content
description: NET_BUFFER_DATA_OFFSET is a macro that NDIS drivers use to get the current offset from the beginning of the data space to the start of the used data space in a NET_BUFFER structure.
ms.assetid: 08c2238e-5583-4c09-b8ee-d40335a33c28
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_DATA_OFFSET macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_DATA\_OFFSET macro


NET\_BUFFER\_DATA\_OFFSET is a macro that NDIS drivers use to get the current offset from the beginning of the data space to the start of the *used data space* in a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

Syntax
------

```ManagedCPlusPlus
ULONG NET_BUFFER_DATA_OFFSET(
   PNET_BUFFER _NB
);
```

Parameters
----------

*\_NB*   
A pointer to a NET\_BUFFER structure.

Return value
------------

NET\_BUFFER\_DATA\_OFFSET returns the offset, in bytes, from the beginning of the data space to the start of the *used data space* of the indicated NET\_BUFFER structure. This value also represents the size of the *unused data space* (available backfill).

Remarks
-------

NET\_BUFFER\_DATA\_OFFSET gets the return value from the **DataOffset** member of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure.

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

 

 




