---
title: \_RxCheckMemoryBlock routine
description: \_RxCheckMemoryBlock checks a memory block for a special RX\_POOL\_HEADER header signature.
ms.assetid: 972cef55-e541-450c-8128-1d026042c4ca
keywords: ["_RxCheckMemoryBlock routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- _RxCheckMemoryBlock
api_location:
- ntrxdef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# \_RxCheckMemoryBlock routine


**\_RxCheckMemoryBlock** checks a memory block for a special RX\_POOL\_HEADER header signature. Note that a network mini-redirector driver would need to add this special signature block to memory allocated in order to use the routine. This routine should not be used since this special header block has not been implemented.

Syntax
------

```ManagedCPlusPlus
BOOLEAN _RxCheckMemoryBlock(
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
A pointer to the source file name where the memory allocation occurred.

*LineNumber*   
The line number in the source file where the memory allocation occurred.

Return value
------------

**RxCheckMemoryBlock** returns **TRUE** if the memory block passes the checks, or **FALSE** if it fails.

Remarks
-------

It is recommended that the **RxCheckMemoryBlock** macro be called instead of using this routine directly. On retail builds, this macro is defined to nothing. On checked builds, this macro is defined to call **\_RxCheckMemoryBlock**.

This routine should not be used since the special memory header block (RX\_POOL\_HEADER) that this routine checks is not added when calling the **\_RxAllocatePoolWithTag** routine. A network mini-redirector driver would need to add this special signature block to memory allocated in order to use this routine.

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

[**\_RxFreePool**](-rxfreepool.md)

 

 






