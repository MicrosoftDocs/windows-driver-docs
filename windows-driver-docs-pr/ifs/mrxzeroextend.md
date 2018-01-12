---
title: MRxZeroExtend routine
description: The MRxZeroExtend routine is called by RDBSS to request that a network mini-redirector truncate the contents of a file system object.
ms.assetid: d4a7c201-3c7d-40e9-a7da-17f40862c258
keywords: ["MRxZeroExtend routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxZeroExtend
api_location:
- mrx.h
api_type:
- UserDefined
---

# MRxZeroExtend routine


The *MRxZeroExtend* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector truncate the contents of a file system object.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxZeroExtend;

NTSTATUS MRxZeroExtend(
  _Inout_ PRX_CONTEXT RxContext
)
{ ... }
```

Parameters
----------

*RxContext* \[in, out\]  
A pointer to the RX\_CONTEXT structure. This parameter contains the IRP that is requesting the operation.

Return value
------------

*MRxZeroExtend* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>STATUS_NOT_IMPLEMENTED</strong></td>
<td align="left"><p>This routine is not implemented.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

*MRxZeroExtend* is called as part of cleanup operations if the file object was not marked for deletion and the file object is not a paging file. *MRxZeroExtend* is called to ensure that the portion between the valid data length and the file size is zero-extended. After calling *MRxZeroExtend*, RDBSS sets the **Header.ValidDataLength.QuadPart** member of the structure of an FCB structure equal to the **Header.FileSize.QuadPart** member of the FCB structure.

A call to *MRxZeroExtend* will be followed by a call to [**MRxCleanupFobx**](https://msdn.microsoft.com/library/windows/hardware/ff549841) as part of the cleanup operation.

RDBSS ignores the return value from *MRxZeroExtend*.

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

[**MRxExtendForNonCache**](mrxextendfornoncache.md)

[**MRxFlush**](mrxflush.md)

[**MRxForceClosed**](https://msdn.microsoft.com/library/windows/hardware/ff550677)

[**MRxIsLockRealizable**](https://msdn.microsoft.com/library/windows/hardware/ff550691)

[**MRxShouldTryToCollapseThisOpen**](mrxshouldtrytocollapsethisopen.md)

[**MRxTruncate**](mrxtruncate.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20MRxZeroExtend%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





