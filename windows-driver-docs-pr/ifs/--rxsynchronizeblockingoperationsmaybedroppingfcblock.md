---
title: \_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock function
description: \_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock synchronizes blocking I/O requests to the same work queue.
keywords: ["__RxSynchronizeBlockingOperationsMaybeDroppingFcbLock function Installable File System Drivers"]
topic_type:
- apiref
api_name:
- __RxSynchronizeBlockingOperationsMaybeDroppingFcbLock
api_location:
- rxcontx.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# \_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock function


**\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock** synchronizes blocking I/O requests to the same work queue.

## Syntax

```ManagedCPlusPlus
NTSTATUS __RxSynchronizeBlockingOperationsMaybeDroppingFcbLock(
  _Inout_ PRX_CONTEXT RxContext,
  _Inout_ PLIST_ENTRY BlockingIoQ,
  _In_    BOOLEAN     DropFcbLock
);
```

## Parameters

*RxContext* \[in, out\]  
A pointer to the RX\_CONTEXT of the operation being synchronized.

*BlockingIoQ* \[in, out\]  
A pointer to the LIST\_ENTRY for the queue.

*DropFcbLock* \[in\]  
A Boolean value that indicates if the FCB resource should be released. If this parameter is **TRUE**, then the FCB resource will be released.

## Return value

**\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock** returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value such as one of the following:

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
<td align="left"><strong>STATUS_CANCELLED</strong></td>
<td align="left"><p>The I/O request and the associated RX_CONTEXT was canceled.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_PENDING</strong></td>
<td align="left"><p>The <em>RxContext</em> was for an asynchronous operation and the <em>RxContext</em> has been added to the queue.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock** routine synchronizes blocking I/O requests to the same work queue. RDBSS uses **\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock** internally to synchronize named pipe operations. The work queue is the queue referenced by the file object extension (FOBX) associated with the **pFcb** member of the RX\_CONTEXT structure pointed to by *RxContext*.

A network mini-redirector may use **\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock** to synchronize operations on a separate queue that is maintained by the network mini-redirector.

If *RxContext* is marked for an asynchronous operation, **\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock** will add the *RxContext* to the queue and return STATUS\_PENDING. If *RxContext* is marked for a synchronous operation, **\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock** will block and *RxContext* is resumed when a call is made to [**RxResumeBlockedOperations\_Serially**](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxresumeblockedoperations_serially).

If the blocking I/O request was canceled, **\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock** returns STATUS\_CANCELLED to indicate the error.

The **SyncEvent** member of the RX\_CONTEXT structure pointed to by *RxContext* must have been reset before calling **\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock**. The FCB resource must be locked before calling **\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock** if the *DropFcbLock* parameter is set to **TRUE**.

The following two macros are defined on Windows XP and Windows 2000 for calling **\_\_RxSynchronizeBlockingOperationsMaybeDroppingFcbLock** :

**RxSynchronizeBlockingOperations** - calls with the *DropFcbLock* parameter set to **FALSE**.

**RxSynchronizeBlockingOperationsAndDropFcbLock** - calls with the *DropFcbLock* parameter set to **TRUE**.

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
<td align="left"><p>Version</p></td>
<td align="left"><p>The __RxSynchronizeBlockingOperationsMaybeDroppingFcbLock routine is only available on Windows XP and Windows 2000.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Rxcontx.h (include Rxcontx.h)</td>
</tr>
</tbody>
</table>

## See also


[**RxCompleteRequest\_Real**](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxcompleterequest_real)

[**RxCreateRxContext**](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxcreaterxcontext)

[**RxDereference**](/windows-hardware/drivers/ddi/rxprocs/nf-rxprocs-rxdereference)

[**RxDereferenceAndDeleteRxContext\_Real**](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxdereferenceanddeleterxcontext_real)

[**RxInitializeContext**](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxinitializecontext)

[**RxPrepareContextForReuse**](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxpreparecontextforreuse)

[**RxResumeBlockedOperations\_Serially**](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-rxresumeblockedoperations_serially)

[**\_\_RxSynchronizeBlockingOperations**](/windows-hardware/drivers/ddi/rxcontx/nf-rxcontx-__rxsynchronizeblockingoperations)

 

