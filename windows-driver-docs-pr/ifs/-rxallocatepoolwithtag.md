---
title: \_RxAllocatePoolWithTag function
description: \_RxAllocatePoolWithTag allocates memory from a pool with a four-byte tag at the beginning of the block that can be used to help catch instances of memory trashing.
ms.assetid: 5e999d06-ebcf-433a-a714-f340a1c74be1
keywords: ["_RxAllocatePoolWithTag function Installable File System Drivers"]
topic_type:
- apiref
api_name:
- _RxAllocatePoolWithTag
api_location:
- ntrxdef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# \_RxAllocatePoolWithTag function


**\_RxAllocatePoolWithTag** allocates memory from a pool with a four-byte tag at the beginning of the block that can be used to help catch instances of memory trashing.

Syntax
------

```ManagedCPlusPlus
VOID* _RxAllocatePoolWithTag(
   ULONG Type,
   ULONG Size,
   ULONG Tag,
   PSZ   FileName,
   ULONG LineNumber
);
```

Parameters
----------

*Type*   
The type of the pool to be allocated. This parameter can be one of the following enumeration values for POOL\_TYPE:

<a href="" id="nonpagedpool"></a>**NonPagedPool**  
Nonpageable system memory that can be accessed from any IRQL. **NonPagedPool** memory is a scarce resource and drivers should allocate it only when necessary. The system can only allocate buffers larger than PAGE\_SIZE from **NonPagedPool** in multiples of PAGE\_SIZE. Requests for buffers larger than PAGE\_SIZE, but not a PAGE\_SIZE multiple, waste nonpageable memory.

<a href="" id="pagedpool"></a>**PagedPool**  
Pageable system memory that can only be allocated and accessed at IRQL &lt; DISPATCH\_LEVEL.

*Size*   
The size of the memory block, in bytes, to be allocated.

*Tag*   
The four-byte tag to be used to mark the allocated buffer. For a description of how to use tags, see [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520). The ASCII value of each character in the tag must be between 0 and 127.

*FileName*   
A pointer to the source file name where the memory allocation occurred. This parameter is not currently used.

*LineNumber*   
The line number in the source file where the memory allocation occurred. This parameter is not currently used.

Return value
------------

**RxAllocatePoolWithTag** returns **NULL** if there is insufficient memory in the free pool to satisfy the request. Otherwise, the routine returns a pointer to the allocated memory.

Remarks
-------

It is recommended that the **RxAllocatePoolWithTag** macro be called instead of using this routine directly. On retail builds, this macro is defined to call [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520). On checked builds, this macro is defined to call **\_RxAllocatePoolWithTag**.

The **\_RxAllocatePoolWithTag** routine calls **ExAllocatePoolWithTagPriority** with the priority (importance of the request) set to LowPoolPriority. The system may fail the request for LowPoolPriority when it runs low on resources. A driver should be prepared to recover from an allocation failure when using this routine.

When the system allocates a buffer from pool memory of PAGE\_SIZE or greater, it aligns the buffer on a page boundary. Memory requests smaller than PAGE\_SIZE are not necessarily aligned on page boundaries, but always fit within a single page, and are aligned on an 8-byte boundary. Any successful allocation that requests a block larger than PAGE\_SIZE that is not a multiple of PAGE\_SIZE wastes all unused bytes on the last-allocated page.

The system associates the pool tag with the allocated memory. Programming tools, such as WinDbg, can display the pool tag associated with each allocated buffer. The value of *Tag* is normally displayed in reverse order. For example, if a caller passes 'Fred' as a *Tag*, it would appear as 'derF' if memory is dumped or when tracking memory usage in the debugger.

Memory allocated with **\_RxAllocatePoolWithTag** should be released by calling [**\_RxFreePool**](-rxfreepool.md).

Callers of **\_RxAllocatePoolWithTag** must be executing at IRQL &lt;= DISPATCH\_LEVEL. A caller executing at DISPATCH\_LEVEL must specify a **NonPagedPool** value for the *Type* parameter. A caller executing at IRQL &lt;= APC\_LEVEL can specify any POOL\_TYPE value for the *Type* parameter.

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
<td align="left"><p>See Remarks section.</p></td>
</tr>
</tbody>
</table>

## See also


[**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520)

[**\_RxCheckMemoryBlock**](-rxcheckmemoryblock.md)

[**\_RxFreePool**](-rxfreepool.md)

 

 






