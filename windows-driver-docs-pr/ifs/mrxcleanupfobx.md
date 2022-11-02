---
title: MRxCleanupFobx routine (Windows Drivers)
description: Learn more about the MRxCleanupFobx routine.
keywords:
- mrx/MRxCleanupFobx
- MRxCleanupFobx
- PMRX_CALLDOWN
ms.date: 11/02/2022
---

# MRxCleanupFobx routine

The *MRxCleanupFobx* routine is called by [RDBSS](the-rdbss-driver-and-library.md) to request the network mini-redirector to close a file system object extension. RDBSS issues this call in response to receiving an [**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md) request on a file object.

## Syntax

``` c++
PMRX_CALLDOWN MRxCleanupFobx;

NTSTATUS MRxCleanupFobx(
  _Inout_ PRX_CONTEXT RxContext
)
{ ... }
```

## Parameters

- *RxContext* \[in, out\]  
  A pointer to the RX\_CONTEXT structure. This parameter contains the IRP that is requesting the operation.

## Return value

*MRxCleanupFobx* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as the following:

<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_INTERNAL_ERROR</strong></td>
<td><p>An internal error occurred in the network mini-redirector.</p></td>
</tr>
</tbody>
</table>

## Remarks

*MRxCleanupFobx* is called by RDBSS as part of cleanup and close operations on a file object.

*MRxCleanupFobx* cannot return a value of STATUS\_RETRY indicating that the call should be retried. If a retry loop is necessary, it must be handled internally in the *MRxCleanupFobx* routine by the network mini-redirector.

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Mrx.h (include Mrx.h)</td>
</tr>
</tbody>
</table>

## See also

[**MRxAreFilesAliased**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_chkfcb_calldown)

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

[**MRxShouldTryToCollapseThisOpen**](mrxshouldtrytocollapsethisopen.md)

[**MRxTruncate**](mrxtruncate.md)

[**MRxZeroExtend**](mrxzeroextend.md)
