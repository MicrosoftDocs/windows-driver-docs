---
title: MRxShouldTryToCollapseThisOpen routine
description: The MRxShouldTryToCollapseThisOpen routine is called by RDBSS to request that a network mini-redirector indicate if RDBSS should try and collapse an open request onto an existing file system object.
ms.assetid: a68755c1-73f5-4134-b506-2a0163637a13
keywords: ["MRxShouldTryToCollapseThisOpen routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxShouldTryToCollapseThisOpen
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

# MRxShouldTryToCollapseThisOpen routine


The *MRxShouldTryToCollapseThisOpen* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector indicate if RDBSS should try and collapse an open request onto an existing file system object.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxShouldTryToCollapseThisOpen;

NTSTATUS MRxShouldTryToCollapseThisOpen(
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

*MRxShouldTryToCollapseThisOpen* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as the following:

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
<td align="left"><strong>STATUS_MORE_PROCESSING_REQUIRED</strong></td>
<td align="left"><p>A network mini-redirector returns this value to disable collapsing of this open request.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

*MRxShouldTryToCollapseThisOpen* is called to determine if an open request should not be collapsed.

Before calling *MRxShouldTryToCollapseThisOpen*, RDBSS modifies the following member in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **pRelevantSrvOpen** member is set to the SRV\_OPEN.

The call to *MRxShouldTryToCollapseThisOpen* could be a change notify request for a directory. Therefore, the network mini-redirector might not allow collapsing open requests so that change notification works correctly.

RDBSS disallows collapsing opens if the **Create.NtCreateParameters.CreateOptions** member of the RX\_CONTEXT structure has the FILE\_OPEN\_FOR\_BACKUP\_INTENT option or the FILE\_DELETE\_ON\_CLOSE option set.

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

[**MRxTruncate**](mrxtruncate.md)

[**MRxZeroExtend**](mrxzeroextend.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20MRxShouldTryToCollapseThisOpen%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





