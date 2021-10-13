---
title: MRxShouldTryToCollapseThisOpen routine
description: The MRxShouldTryToCollapseThisOpen routine is called by RDBSS to request that a network mini-redirector indicate if RDBSS should try and collapse an open request onto an existing file system object.
keywords: ["MRxShouldTryToCollapseThisOpen routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxShouldTryToCollapseThisOpen
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxShouldTryToCollapseThisOpen routine


The *MRxShouldTryToCollapseThisOpen* routine is called by [RDBSS](./the-rdbss-driver-and-library.md) to request that a network mini-redirector indicate if RDBSS should try and collapse an open request onto an existing file system object.

## Syntax

```ManagedCPlusPlus
PMRX_CALLDOWN MRxShouldTryToCollapseThisOpen;

NTSTATUS MRxShouldTryToCollapseThisOpen(
  _Inout_ PRX_CONTEXT RxContext
)
{ ... }
```

## Parameters

*RxContext* \[in, out\]  
A pointer to the RX\_CONTEXT structure. This parameter contains the IRP that is requesting the operation.

## Return value

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

 

## Remarks

*MRxShouldTryToCollapseThisOpen* is called to determine if an open request should not be collapsed.

Before calling *MRxShouldTryToCollapseThisOpen*, RDBSS modifies the following member in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **pRelevantSrvOpen** member is set to the SRV\_OPEN.

The call to *MRxShouldTryToCollapseThisOpen* could be a change notify request for a directory. Therefore, the network mini-redirector might not allow collapsing open requests so that change notification works correctly.

RDBSS disallows collapsing opens if the **Create.NtCreateParameters.CreateOptions** member of the RX\_CONTEXT structure has the FILE\_OPEN\_FOR\_BACKUP\_INTENT option or the FILE\_DELETE\_ON\_CLOSE option set.

## Requirements

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


[**MRxAreFilesAliased**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_chkfcb_calldown)

[**MRxCleanupFobx**](/previous-versions/windows/hardware/drivers/ff549841(v=vs.85))

[**MRxCloseSrvOpen**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_calldown)

[**MRxCollapseOpen**](mrxcollapseopen.md)

[**MRxCreate**](mrxcreate.md)

[**MRxDeallocateForFcb**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_deallocate_for_fcb)

[**MRxDeallocateForFobx**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_deallocate_for_fobx)

[**MRxExtendForCache**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_extendfile_calldown)

[**MRxExtendForNonCache**](mrxextendfornoncache.md)

[**MRxFlush**](mrxflush.md)

[**MRxForceClosed**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_forceclosed_calldown)

[**MRxIsLockRealizable**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_is_lock_realizable)

[**MRxTruncate**](mrxtruncate.md)

[**MRxZeroExtend**](mrxzeroextend.md)

 

