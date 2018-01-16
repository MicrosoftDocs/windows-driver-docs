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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20MRxExtendForNonCache%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





