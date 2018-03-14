---
title: NET_BUFFER_SHARED_MEM_LENGTH macro
author: windows-driver-content
description: The NET_BUFFER_SHARED_MEM_LENGTH macro gets the shared memory offset from a NET_BUFFER_SHARED_MEMORY structure.
ms.assetid: 651143e7-9198-4cc6-92a8-d5247f6e32f9
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_SHARED_MEM_LENGTH macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_SHARED\_MEM\_LENGTH macro


The **NET\_BUFFER\_SHARED\_MEM\_LENGTH** macro gets the shared memory offset from a [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure.

Syntax
------

```ManagedCPlusPlus
ULONG NET_BUFFER_SHARED_MEM_LENGTH(
   PNET_BUFFER_SHARED_MEMORY _SHI
);
```

Parameters
----------

*\_SHI*   
A pointer to a [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure.

Return value
------------

**NET\_BUFFER\_SHARED\_MEM\_LENGTH** returns a ULONG value for the length, in bytes, of the shared memory.

Remarks
-------

An NDIS 6.20 or later driver can use the **NET\_BUFFER\_SHARED\_MEM\_LENGTH** macro to get shared memory length that is associated with a [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure. **NET\_BUFFER\_SHARED\_MEM\_LENGTH** gets the length from the **SharedMemoryLength** member of the **NET\_BUFFER\_SHARED\_MEMORY** structure. The **SharedMemoryInfo** member of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure contains the first **NET\_BUFFER\_SHARED\_MEMORY** structure in a linked list.

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

 

 




