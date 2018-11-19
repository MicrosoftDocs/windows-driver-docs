---
title: MRxLowIOSubmit\ LOWIO\_OP\_UNLOCK\_MULTIPLE\ routine
description: The MRxLowIOSubmit\ LOWIO\_OP\_UNLOCK\_MULTIPLE\ routine is called by RDBSS to request that the network mini-redirector remove multiple locks held on a file object.
ms.assetid: 50f7abdf-a3f7-4625-ac54-75e80807d05e
keywords: ["MRxLowIOSubmit LOWIO_OP_UNLOCK_MULTIPLE routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxLowIOSubmit LOWIO_OP_UNLOCK_MULTIPLE
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\_MULTIPLE\] routine


The *MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\_MULTIPLE\]* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that the network mini-redirector remove multiple locks held on a file object.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxLowIOSubmit[LOWIO_OP_UNLOCK_MULTIPLE];

NTSTATUS MRxLowIOSubmit[LOWIO_OP_UNLOCK_MULTIPLE](
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

*MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\_MULTIPLE\]* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><strong>STATUS_CONNECTION_DISCONNECTED</strong></td>
<td align="left"><p>The connection was disconnected.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td align="left"><p>There were insufficient resources to complete the request.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_INVALID_NETWORK_RESPONSE</strong></td>
<td align="left"><p>An invalid response was received from the remote server.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INVALID_PARAMETER</strong></td>
<td align="left"><p>An invalid parameter was specified in <em>RxContext</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_LINK_FAILED</strong></td>
<td align="left"><p>The attempt to reconnect to a remote server to complete the request failed.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_NOT_IMPLEMENTED</strong></td>
<td align="left"><p>This routine is not implemented.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_SHARING_VIOLATION</strong></td>
<td align="left"><p>A sharing violation occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_UNSUCCESSFUL</strong></td>
<td align="left"><p>The call was unsuccessful.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

RDBSS calls *MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\_MULTIPLE\]* in response to receiving an [**IRP\_MJ\_LOCK\_CONTROL**](irp-mj-lock-control.md) request with a minor code of IRP\_MN\_UNLOCK\_ALL or IRP\_MN\_UNLOCK\_ALL\_BY\_KEY.

Before calling *MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\_MULTIPLE\]*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **LowIoContext.Operation** member is set to LOWIO\_OP\_UNLOCK\_MULTIPLE.

The **LowIoContext.ResourceThreadId** member is set to the thread of the process that initiated the operation in RDBSS.

The **LowIoContext.ParamsFor.Locks.LockList** member is set to a list of LOWIO\_LOCK\_LIST elements. Each element specifies a range to be unlocked.

The byte ranges to be unlocked are specified in the **LowIoContext.ParamsFor.Locks.LockList** member of the RX\_CONTEXT structure. The LOWIO\_LOCK\_LIST structure is as follows:

``` syntax
typedef struct _LOWIO_LOCK_LIST {
  struct  _LOWIO_LOCK_LIST  *Next;
  ULONG  LockNumber;
  RXVBO  ByteOffset;
  LONGLONG  Length;
  ULONG  Key;
  BOOLEAN  ExclusiveLock;
} LOWIO_LOCK_LIST, *PLOWIO_LOCK_LIST;
```

The **LowIoContext.Operation** member of RX\_CONTEXT specifies the low I/O operation to perform. It is possible for several of the low I/O routines to point to the same routine in a network mini-redirector because the **LowIoContext.Operation** member can be used to differentiate the low I/O operation that is requested. For example, all the I/O calls related to file locks could call the same low I/O routine in the network mini-redirector and this routine could use the **LowIoContext.Operation** member to differentiate between the lock and unlock operation that is requested.

If the *MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\_MULTIPLE\]* routine can take a long time to complete, the network mini-redirector driver should release the FCB structure before initiating the network communication. The FCB structure can be released by calling [**RxReleaseFcbResourceForThreadInMRx**](https://msdn.microsoft.com/library/windows/hardware/ff554694). While the *MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\_MULTIPLE\]* routine is processing, the **LowIoContext.ResourceThreadId** member of RX\_CONTEXT is guaranteed to indicate the thread of the process that initiated the operation in RDBSS.

The **LowIoContext.ResourceThreadId** member of RX\_CONTEXT can be used to release the FCB structure on behalf of another thread. When an asynchronous routine completes, the FCB structure that was acquired from the initial thread can be released.

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


[**MRxLowIOSubmit\[LOWIO\_OP\_EXCLUSIVELOCK\]**](mrxlowiosubmit-lowio-op-exclusivelock-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_FSCTL\]**](mrxlowiosubmit-lowio-op-fsctl-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]**](mrxlowiosubmit-lowio-op-ioctl-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_NOTIFY\_CHANGE\_DIRECTORY\]**](mrxlowiosubmit-lowio-op-notify-change-directory-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_READ\]**](mrxlowiosubmit-lowio-op-read-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_SHAREDLOCK\]**](mrxlowiosubmit-lowio-op-sharedlock-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\]**](mrxlowiosubmit-lowio-op-unlock-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_WRITE\]**](mrxlowiosubmit-lowio-op-write-.md)

[**RxReleaseFcbResourceForThreadInMRx**](https://msdn.microsoft.com/library/windows/hardware/ff554694)

 

 






