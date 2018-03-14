---
title: NET_BUFFER_SHARED_MEM_NEXT_SEGMENT macro
author: windows-driver-content
description: The NET_BUFFER_SHARED_MEM_NEXT_SEGMENT macro gets the next shared memory segment from a NET_BUFFER_SHARED_MEMORY structure.
ms.assetid: 6c2445c5-166e-42c9-aa95-d7c6878571e3
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_SHARED_MEM_NEXT_SEGMENT macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_SHARED\_MEM\_NEXT\_SEGMENT macro


The **NET\_BUFFER\_SHARED\_MEM\_NEXT\_SEGMENT** macro gets the next shared memory segment from a [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure.

Syntax
------

```ManagedCPlusPlus
PNET_BUFFER_SHARED_MEMORY NET_BUFFER_SHARED_MEM_NEXT_SEGMENT(
   PNET_BUFFER_SHARED_MEMORY _SHI
);
```

Parameters
----------

*\_SHI*   
A pointer to a [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure.

Return value
------------

**NET\_BUFFER\_SHARED\_MEM\_NEXT\_SEGMENT** returns a pointer to a [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure or returns **NULL**.

Remarks
-------

An NDIS 6.20 or later driver can use the **NET\_BUFFER\_SHARED\_MEM\_NEXT\_SEGMENT** macro to get the next shared memory segment in a linked list of [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structures that are associated with a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure. **NET\_BUFFER\_SHARED\_MEM\_NEXT\_SEGMENT** gets a pointer to the next **NET\_BUFFER\_SHARED\_MEMORY** structure from the **NextSharedMemorySegment** member of the **NET\_BUFFER\_SHARED\_MEMORY** structure. The **SharedMemoryInfo** member of the **NET\_BUFFER** structure contains the first **NET\_BUFFER\_SHARED\_MEMORY** structure in the linked list.

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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376)

[**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419)

 

 




