---
title: \_RxFreePool function
description: \_RxFreePool releases memory that was previously allocated using \_RxAllocatePoolWithTag.
ms.assetid: 383deda9-6151-420b-afa9-445cd05e998b
keywords: ["_RxFreePool function Installable File System Drivers"]
topic_type:
- apiref
api_name:
- _RxFreePool
api_location:
- ntrxdef.h
api_type:
- HeaderDef
---

# \_RxFreePool function


**\_RxFreePool** releases memory that was previously allocated using **\_RxAllocatePoolWithTag**.

Syntax
------

```ManagedCPlusPlus
VOID _RxFreePool(
   PVOID Buffer,
   PSZ   FileName,
   ULONG LineNumber
);
```

Parameters
----------

*Buffer*   
A pointer to the buffer of pool memory to be released.

*FileName*   
A pointer to the source file name where the memory allocation occurred. This parameter is not currently used.

*LineNumber*   
The line number in the source file where the memory allocation occurred. This parameter is not currently used.

Return value
------------

None

Remarks
-------

It is recommended that the **RxFreePool** macro be called instead of using this routine directly. On retail builds, this macro is defined to call **ExFreePool**.

Memory allocated with [**\_RxAllocatePoolWithTag**](-rxallocatepoolwithtag.md) should be released by calling **\_RxFreePool**.

The **\_RxFreePool** routine calls **ExFreePool**.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntrxdef.h (include Ntrxdef.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;= APC_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**\_RxAllocatePoolWithTag**](-rxallocatepoolwithtag.md)

[**\_RxCheckMemoryBlock**](-rxcheckmemoryblock.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20_RxFreePool%20function%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





