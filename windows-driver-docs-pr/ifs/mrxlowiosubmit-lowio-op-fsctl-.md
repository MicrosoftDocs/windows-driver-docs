---
title: MRxLowIOSubmit\ LOWIO\_OP\_FSCTL\ routine
description: The MRxLowIOSubmit\ LOWIO\_OP\_FSCTL\ routine is called by RDBSS to request that a network mini-redirector issue file system control request on remote file.
ms.assetid: 6bbb4b65-c447-47d8-9d05-f2adfb607099
keywords: ["MRxLowIOSubmit LOWIO_OP_FSCTL routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxLowIOSubmit LOWIO_OP_FSCTL
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxLowIOSubmit\[LOWIO\_OP\_FSCTL\] routine


The *MRxLowIOSubmit\[LOWIO\_OP\_FSCTL\]* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector issue file system control request on remote file.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxLowIOSubmit[LOWIO_OP_FSCTL];

NTSTATUS MRxLowIOSubmit[LOWIO_OP_FSCTL](
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

*MRxLowIOSubmit\[LOWIO\_OP\_FSCTL\]* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><strong>STATUS_INVALID_DEVICE_REQUEST</strong></td>
<td align="left"><p>An invalid device request was specified.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INVALID_NETWORK_RESPONSE</strong></td>
<td align="left"><p>An invalid response was received from the remote server.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_INVALID_PARAMETER</strong></td>
<td align="left"><p>An invalid parameter was specified in <em>RxContext</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_LINK_FAILED</strong></td>
<td align="left"><p>The attempt to reconnect to a remote server to complete the request failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_NOT_IMPLEMENTED</strong></td>
<td align="left"><p>This routine is not implemented.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_NOT_SUPPORTED</strong></td>
<td align="left"><p>The FSCTL that was specified is not supported by the network mini-redirector.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_UNSUCCESSFUL</strong></td>
<td align="left"><p>The call was unsuccessful.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

RDBSS calls *MRxLowIOSubmit\[LOWIO\_OP\_FSCTL\]* in response to receiving an [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md) request.

Before calling *MRxLowIOSubmit\[LOWIO\_OP\_FSCTL\]*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **LowIoContext.Operation** member is set to LOWIO\_OP\_FSCTL.

The **LowIoContext.ResourceThreadId** member is set to the thread of the process that initiated the operation in RDBSS.

The **LowIoContext.ParamsFor.FsCtl.FsControlCode** member is set to the FSCTL major control code.

The **LowIoContext.ParamsFor.FsCtl.MinorFunction** member is set to the FSCTL minor control code.

The **LowIoContext.ParamsFor.FsCtl.pInputBuffer** member is set to the input buffer.

The **LowIoContext.ParamsFor.FsCtl.InputBufferLength** member is set to the input buffer length.

The **LowIoContext.ParamsFor.FsCtl.pOutputBuffer** member is set to the output buffer.

The **LowIoContext.ParamsFor.FsCtl.OutputBufferLength** member is set to the output buffer length.

The file system control code (FSCTL) requests handled by a network mini-redirector can be classified into one of several categories:

-   FSCTLs that are implemented and used by RDBSS and the network mini redirector

-   FSCTLs that are implemented and used only by the network mini-redirector

-   FSCTLs which should never be seen by the network mini-redirector. These FSCTLs are solely intended as a debugging aid.

While the *MRxLowIOSubmit\[LOWIO\_OP\_FSCTL\]* routine is processing, the **LowIoContext.ResourceThreadId** member of RX\_CONTEXT is guaranteed to indicate the thread of the process that initiated the operation in RDBSS. The **LowIoContext.ResourceThreadId** member of RX\_CONTEXT can be used to release the input resource on behalf of another thread. When an asynchronous routine completes, the input resource that was acquired from the initial thread can be released.

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

[**MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]**](mrxlowiosubmit-lowio-op-ioctl-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_NOTIFY\_CHANGE\_DIRECTORY\]**](mrxlowiosubmit-lowio-op-notify-change-directory-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_READ\]**](mrxlowiosubmit-lowio-op-read-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_SHAREDLOCK\]**](mrxlowiosubmit-lowio-op-sharedlock-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\]**](mrxlowiosubmit-lowio-op-unlock-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\_MULTIPLE\]**](mrxlowiosubmit-lowio-op-unlock-multiple-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_WRITE\]**](mrxlowiosubmit-lowio-op-write-.md)

 

 






