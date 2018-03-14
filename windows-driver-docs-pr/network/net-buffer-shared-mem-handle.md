---
title: NET_BUFFER_SHARED_MEM_HANDLE macro
author: windows-driver-content
description: The NET_BUFFER_SHARED_MEM_HANDLE macro gets the shared memory handle from a NET_BUFFER_SHARED_MEMORY structure.
ms.assetid: 4bec976b-2cee-405d-889b-b0a3e293840e
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NET_BUFFER_SHARED_MEM_HANDLE macro Network Drivers Starting with Windows Vista
---

# NET\_BUFFER\_SHARED\_MEM\_HANDLE macro


The **NET\_BUFFER\_SHARED\_MEM\_HANDLE** macro gets the shared memory handle from a [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure.

Syntax
------

```ManagedCPlusPlus
NDIS_HANDLE NET_BUFFER_SHARED_MEM_HANDLE(
   PNET_BUFFER_SHARED_MEMORY _SHI
);
```

Parameters
----------

*\_SHI*   
A pointer to a [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure.

Return value
------------

**NET\_BUFFER\_SHARED\_MEM\_HANDLE** returns an NDIS shared memory handle.

Remarks
-------

An NDIS 6.20 or later driver can use the **NET\_BUFFER\_SHARED\_MEM\_HANDLE** macro to get shared memory handle that is associated with a [**NET\_BUFFER\_SHARED\_MEMORY**](https://msdn.microsoft.com/library/windows/hardware/ff568419) structure. **NET\_BUFFER\_SHARED\_MEM\_HANDLE** gets the handle from the **SharedMemoryHandle** member of the **NET\_BUFFER\_SHARED\_MEMORY** structure. The **SharedMemoryInfo** member of the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure contains the first **NET\_BUFFER\_SHARED\_MEMORY** structure in a linked list.

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

 

 




