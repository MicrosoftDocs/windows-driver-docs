---
title: NET_BUFFER_SHARED_MEM_NEXT_SEGMENT macro
author: windows-driver-content
description: The NET_BUFFER_SHARED_MEM_NEXT_SEGMENT macro gets the next shared memory segment from a NET_BUFFER_SHARED_MEMORY structure.
ms.assetid: 6c2445c5-166e-42c9-aa95-d7c6878571e3
ms.author: windowsdriverdev 
ms.date: 0718/2017 
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_SHARED_MEM_NEXT_SEGMENT%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


