---
title: NdisQueryMdlOffset macro
author: windows-driver-content
description: The NdisQueryMdlOffset macro retrieves the offset within a physical page at which a given MDL buffer begins and the length of the buffer.
ms.assetid: d6f23e9c-5015-4087-b7a2-badee00bdafa
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NdisQueryMdlOffset macro Network Drivers Starting with Windows Vista
---

# NdisQueryMdlOffset macro


The **NdisQueryMdlOffset** macro retrieves the offset within a physical page at which a given MDL buffer begins and the length of the buffer.

Syntax
------

```ManagedCPlusPlus
VOID NdisQueryMdlOffset(
    _Mdl,
    _Offset,
    _Length
);
```

Parameters
----------

*\_Mdl*   
A pointer to an MDL.

*\_Offset*   
A pointer to a caller-supplied variable in which this macro returns the zero-based byte offset within the physical page that contains the MDL-specified buffer.

*\_Length*   
A pointer to a caller-supplied variable in which this macro returns the length, in bytes, of the virtual address range that is specified by the MDL.

Return value
------------

None

Remarks
-------

The **NdisQueryMdlOffset** macro provides an MDL-based version of the [**NdisQueryBufferOffset**](https://msdn.microsoft.com/library/windows/hardware/ff554411) function.

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
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>&lt;= DISPATCH_LEVEL</p></td>
</tr>
<tr class="odd">
<td><p>DDI compliance rules</p></td>
<td>[<strong>Irql_NetBuffer_Function</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547985)</td>
</tr>
</tbody>
</table>

## See also


[**NdisQueryBufferOffset**](https://msdn.microsoft.com/library/windows/hardware/ff554411)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NdisQueryMdlOffset%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


