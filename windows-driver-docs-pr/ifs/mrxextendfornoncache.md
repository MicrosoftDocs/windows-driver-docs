---
title: MRxExtendForNonCache routine
description: The MRxExtendForNonCache routine is called by RDBSS to request that a network mini-redirector extend a file when the file is not being cached by the cache manager.
ms.assetid: 80ec5142-7188-45ba-a1cb-73be99ce1ac4
keywords: ["MRxExtendForNonCache routine Installable File System Drivers", "PMRX_EXTENDFILE_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxExtendForNonCache
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxExtendForNonCache routine


The *MRxExtendForNonCache* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector extend a file when the file is not being cached by the cache manager.

Syntax
------

```ManagedCPlusPlus
PMRX_EXTENDFILE_CALLDOWN MRxExtendForNonCache;

ULONG MRxExtendForNonCache(
  _Inout_ PRX_CONTEXT    RxContext,
  _Inout_ PLARGE_INTEGER pNewFileSize,
  _Out_   PLARGE_INTEGER pNewAllocationSize
)
{ ... }
```

Parameters
----------

*RxContext* \[in, out\]  
A pointer to the RX\_CONTEXT structure. This parameter contains the IRP that is requesting the operation.

*pNewFileSize* \[in, out\]  
A pointer to the LARGE\_INTEGER value indicating the byte count of the new file size.

*pNewAllocationSize* \[out\]  
A pointer to the LARGE\_INTEGER for storing the new allocation size when [**MRxExtendForCache**](https://msdn.microsoft.com/library/windows/hardware/ff549878) returns.

Return value
------------

*MRxExtendForNonCache* returns STATUS\_SUCCESS on success or an error code on failure.

Remarks
-------

*MRxExtendForNonCache* handles network requests to extend the file for non-cached I/O.

Before calling *MRxExtendForNonCache*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

**LowIoContext.Operation** is set to LOWIO\_OP\_WRITE

**LowIoContext.ParamsFor.ReadWrite.Flags** has the LOWIO\_READWRITEFLAG\_EXTENDING\_FILESIZE bit set

A network mini-redirector that caches file or directory information may need to invalidate its cache information when the file is extended.

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
<td align="left">Mrx.h (include Mrx.h)</td>
</tr>
</tbody>
</table>

## See also


[**MRxAreFilesAliased**](https://msdn.microsoft.com/library/windows/hardware/ff549838)

[**MRxCleanupFobx**](https://msdn.microsoft.com/library/windows/hardware/ff549841)

[**MRxCloseSrvOpen**](https://msdn.microsoft.com/library/windows/hardware/ff549845)

[**MRxCollapseOpen**](mrxcollapseopen.md)

[**MRxCreate**](mrxcreate.md)

[**MRxDeallocateForFcb**](https://msdn.microsoft.com/library/windows/hardware/ff549871)

[**MRxDeallocateForFobx**](https://msdn.microsoft.com/library/windows/hardware/ff549872)

[**MRxExtendForCache**](https://msdn.microsoft.com/library/windows/hardware/ff549878)

[**MRxFlush**](mrxflush.md)

[**MRxForceClosed**](https://msdn.microsoft.com/library/windows/hardware/ff550677)

[**MRxIsLockRealizable**](https://msdn.microsoft.com/library/windows/hardware/ff550691)

[**MRxShouldTryToCollapseThisOpen**](mrxshouldtrytocollapsethisopen.md)

[**MRxTruncate**](mrxtruncate.md)

[**MRxZeroExtend**](mrxzeroextend.md)

 

 






