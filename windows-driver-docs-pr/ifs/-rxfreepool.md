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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 






