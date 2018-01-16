---
title: MRxLowIOSubmit\ LOWIO\_OP\_IOCTL\ routine
description: The MRxLowIOSubmit\ LOWIO\_OP\_IOCTL\ routine is called by RDBSS to issue an I/O system control request to the network mini-redirector.
ms.assetid: b416e2b4-6024-45ec-adf5-90743d417ad5
keywords: ["MRxLowIOSubmit LOWIO_OP_IOCTL routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxLowIOSubmit LOWIO_OP_IOCTL
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

# MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\] routine


The *MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to issue an I/O system control request to the network mini-redirector.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxLowIOSubmit[LOWIO_OP_IOCTL];

NTSTATUS MRxLowIOSubmit[LOWIO_OP_IOCTL](
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

*MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><p>There were insufficient resources to complete the request.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INVALID_DEVICE_REQUEST</strong></td>
<td align="left"><p>An invalid device request was specified.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_INVALID_PARAMETER</strong></td>
<td align="left"><p>An invalid parameter was specified in <em>RxContext</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_NOT_IMPLEMENTED</strong></td>
<td align="left"><p>This routine is not implemented.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_NOT_SUPPORTED</strong></td>
<td align="left"><p>The IOCTL that was specified is not supported by the network mini-redirector.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

RDBSS calls *MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]* in response to receiving an [**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md) or [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](irp-mj-internal-device-control.md) requests.

Before calling *MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **LowIoContext.Operation** member is set to LOWIO\_OP\_IOCTL.

The **LowIoContext.ResourceThreadId** member is set to the thread of the process that initiated the operation in RDBSS.

The **LowIoContext.ParamsFor.IoCtl.IoControlCode** member is set to the IOCTL control code.

The **LowIoContext.ParamsFor.IoCtl.pInputBuffer** member is set to the input buffer.

The **LowIoContext.ParamsFor.IoCtl.InputBufferLength** member is set to the input buffer length.

The **LowIoContext.ParamsFor.IoCtl.pOutputBuffer** member is set to the output buffer.

The **LowIoContext.ParamsFor.IoCtl.OutputBufferLength** member is set to the output buffer length.

While the *MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]* routine is processing, the **LowIoContext.ResourceThreadId** member of RX\_CONTEXT is guaranteed to indicate the thread of the process that initiated the operation in RDBSS. The **LowIoContext.ResourceThreadId** member of RX\_CONTEXT can be used to release the input resource on behalf of another thread. When an asynchronous routine completes, the input resource that was acquired from the initial thread can be released.

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

[**MRxLowIOSubmit\[LOWIO\_OP\_NOTIFY\_CHANGE\_DIRECTORY\]**](mrxlowiosubmit-lowio-op-notify-change-directory-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_READ\]**](mrxlowiosubmit-lowio-op-read-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_SHAREDLOCK\]**](mrxlowiosubmit-lowio-op-sharedlock-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\]**](mrxlowiosubmit-lowio-op-unlock-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_UNLOCK\_MULTIPLE\]**](mrxlowiosubmit-lowio-op-unlock-multiple-.md)

[**MRxLowIOSubmit\[LOWIO\_OP\_WRITE\]**](mrxlowiosubmit-lowio-op-write-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20MRxLowIOSubmit%5BLOWIO_OP_IOCTL%5D%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





