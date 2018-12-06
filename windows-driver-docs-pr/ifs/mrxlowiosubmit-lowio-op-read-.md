---
title: MRxLowIOSubmit\ LOWIO\_OP\_READ\ routine
description: The MRxLowIOSubmit\ LOWIO\_OP\_READ\ routine is called by RDBSS to issue a read request to the network mini-redirector.
ms.assetid: 26a173d8-e3ab-4c63-8390-133afd35b51a
keywords: ["MRxLowIOSubmit LOWIO_OP_READ routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxLowIOSubmit LOWIO_OP_READ
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxLowIOSubmit\[LOWIO\_OP\_READ\] routine


The *MRxLowIOSubmit\[LOWIO\_OP\_READ\]* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to issue a read request to the network mini-redirector.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxLowIOSubmit[LOWIO_OP_READ];

NTSTATUS MRxLowIOSubmit[LOWIO_OP_READ](
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

*MRxLowIOSubmit\[LOWIO\_OP\_READ\]* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><strong>STATUS_FILE_CLOSED</strong></td>
<td align="left"><p>The FCB structure was acquired, but the associated SRV_OPEN structure has been closed.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td align="left"><p>There were insufficient resources to complete the request.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_INVALID_DEVICE_REQUEST</strong></td>
<td align="left"><p>An invalid device request was specified.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INVALID_PARAMETER</strong></td>
<td align="left"><p>An invalid parameter was specified in <em>RxContext</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_NOT_IMPLEMENTED</strong></td>
<td align="left"><p>This routine is not implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_NOT_SUPPORTED</strong></td>
<td align="left"><p>The specified request is not supported by the network mini-redirector.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

RDBSS calls *MRxLowIOSubmit\[LOWIO\_OP\_READ\]* in response to receiving an [**IRP\_MJ\_READ**](irp-mj-read.md) request.

Before calling *MRxLowIOSubmit\[LOWIO\_OP\_READ\]*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **LowIoContext.Operation** member is set to LOWIO\_OP\_READ.

The **LowIoContext.ResourceThreadId** member is set to the thread of the process that initiated the operation in RDBSS.

The **LowIoContext.ParamsFor.ReadWrite.Key** member is set to the value of **IrpSp-&gt;Parameters.Read.Key**.

The **ParamsFor.ReadWrite.Flags** member has the LOWIO\_READWRITEFLAG\_PAGING\_IO bit is set on if **Irp-&gt;Flags** has the IRP\_PAGING\_IO bit on.

The **ParamsFor.ReadWrite.Buffer** member is set to the user buffer locked for IoReadAccess.

The **LowIoContext.ParamsFor.ReadWrite.ByteCount** member is set to the value of IrpSp-&gt;Parameters.Read.Length.

A read request is normally implemented by a network mini-redirector as an asynchronous operation because it can take considerable time. The operation usually consists of sending a network request to the remote server. The response is obtained when the read request is completed on the server. This is an example of an operation for which the network mini-redirector may need to register a context for handling cancellations initiated locally.

While the *MRxLowIOSubmit\[LOWIO\_OP\_READ\]* routine is processing, the **LowIoContext.ResourceThreadId** member of RX\_CONTEXT is guaranteed to indicate the thread of the process that initiated the operation in RDBSS. The **LowIoContext.ResourceThreadId** member can be used to release the FCB structure on behalf of another thread. When an asynchronous routine completes, the FCB structure that was acquired from the initial thread can be released. The FCB structure can be released by calling [**RxReleaseFcbResourceForThreadInMRx**](https://msdn.microsoft.com/library/windows/hardware/ff554694).

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

[**MRxLowIOSubmit\[LOWIO\_OP\_SHAREDLOCK\]**](mrxlowiosubmit-lowio-op-sharedlock-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\]**](mrxlowiosubmit-lowio-op-unlock-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\_MULTIPLE\]**](mrxlowiosubmit-lowio-op-unlock-multiple-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_WRITE\]**](mrxlowiosubmit-lowio-op-write-.md)

[**RxReleaseFcbResourceForThreadInMRx**](https://msdn.microsoft.com/library/windows/hardware/ff554694)

 

 






