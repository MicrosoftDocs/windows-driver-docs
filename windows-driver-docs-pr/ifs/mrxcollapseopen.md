---
title: MRxCollapseOpen routine
description: The MRxCollapseOpen routine is called by RDBSS to request that the network mini-redirector collapse an open file system request onto an existing SRV\_OPEN structure.
keywords: ["MRxCollapseOpen routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxCollapseOpen
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxCollapseOpen routine


The *MRxCollapseOpen* routine is called by [RDBSS](./the-rdbss-driver-and-library.md) to request that the network mini-redirector collapse an open file system request onto an existing SRV\_OPEN structure.

## Syntax

```ManagedCPlusPlus
PMRX_CALLDOWN MRxCollapseOpen;

NTSTATUS MRxCollapseOpen(
  _Inout_ PRX_CONTEXT RxContext
)
{ ... }
```

## Parameters

*RxContext* \[in, out\]  
A pointer to the RX\_CONTEXT structure. This parameter contains the IRP that is requesting the operation.

## Return value

*MRxCollapseOpen* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as the following:

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
<td align="left"><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td align="left"><p>There were insufficient resources to complete the operation.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

*MRxCollapseOpen* is called by RDBSS to collapse an SRV\_OPEN structure locally. The network mini-redirector is consulted to determine if a collapse is possible so there is no reason to call the network mini-redirector twice. If the network mini-redirector decides to collapse the SRV\_OPEN structure, then it will do so and pass back a returnable status. A return value of STATUS\_SUCCESS is a terminating return value. A different return value, for example, STATUS\_MORE\_PROCESSING\_REQUIRED, is considered a non-terminating return value.

Before calling *MRxCollapseOpen*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

**pRelevantSrvOpen** is set to the SRV\_OPEN structure to collapse.

**Create.pSrvCall** is set to the SRV\_CALL structure associated with the SRV\_OPEN.

If the network mini-redirector decides to collapse the SRV\_OPEN structure, then the **SrvOpen** member of the RX\_CONTEXT structure must be set to the collapsed SRV\_OPEN structure.

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

 

