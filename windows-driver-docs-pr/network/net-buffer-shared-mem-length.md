---
title: NET\_BUFFER\_SHARED\_MEM\_LENGTH macro
description: The NET\_BUFFER\_SHARED\_MEM\_LENGTH macro gets the shared memory offset from a NET\_BUFFER\_SHARED\_MEMORY structure.
MS-HAID:
- 'ndis\_netbuf\_macros\_media\_specific\_83656962-7d42-4568-8f2b-7f203173e3b6.xml'
- 'netvista.net\_buffer\_shared\_mem\_length'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 651143e7-9198-4cc6-92a8-d5247f6e32f9
keywords: ["NET_BUFFER_SHARED_MEM_LENGTH macro Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_BUFFER_SHARED_MEM_LENGTH
api_location:
- Ndis.h
api_type:
- HeaderDef
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_BUFFER_SHARED_MEM_LENGTH%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





