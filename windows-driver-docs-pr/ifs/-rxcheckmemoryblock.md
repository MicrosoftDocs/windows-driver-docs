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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20_RxCheckMemoryBlock%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





