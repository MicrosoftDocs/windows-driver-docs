---
title: MRxStop Routine
description: TheMRxStop routine is called by RDBSS to stop the network mini-redirector.
keywords: ["MRxStop routine Installable File System Drivers", "PMRX_CALLDOWN_CTX"]
topic_type:
- apiref
api_name:
- MRxStop
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 03/13/2023
ms.topic: reference
---

# MRxStop routine


The*MRxStop* routine is called by [RDBSS](./the-rdbss-driver-and-library.md) to stop the network mini-redirector.

## Syntax

```ManagedCPlusPlus
PMRX_CALLDOWN_CTX MRxStop;

NTSTATUS MRxStop(
  _Inout_ PRX_CONTEXT          RxContext,
  _Inout_ PRDBSS_DEVICE_OBJECT RxDeviceObject
)
{ ... }
```

## Parameters

*RxContext* \[in, out\]  
A pointer to the RX\_CONTEXT structure. This parameter contains the IRP that requested the network mini-redirector to stop.

*RxDeviceObject* \[in, out\]  
A pointer to the RDBSS\_DEVICE\_OBJECT structure for this network mini-redirector.

## Return value

*MRxStop* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><strong>STATUS_REDIRECTOR_HAS_OPEN_HANDLES</strong></td>
<td align="left"><p>The network mini-redirector has open handles that prevent it from stopping at this time.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_REDIRECTOR_NOT_STARTED</strong></td>
<td align="left"><p>The network mini-redirector was not started.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

*MRxStop* stops and uninitializes the network mini-redirector from the RDBSS perspective. Stopping the network mini-redirector may likely require releasing memory allocations and other system resources.

Before calling *MRxStop*, RDBSS modifies the following values:

The **MajorFunction** member in the RX\_CONTEXT structure pointed to by *RxContext* is set to the major function of the IRP.

The **LowIoContext.ParamsFor.FsCtl.FsControlCode** member in the RX\_CONTEXT structure pointed to by *RxContext* is set to the FSCTL code for the IRP if this was an FSTCL request used to stop the network mini-redirector.

The **StartStopContext.State** member of the RDBSS\_DEVICE\_OBJECT structure pointed to by *RxDeviceObject* is set to RDBSS\_STOP\_IN\_PROGRESS

The **StartStopContext.pStopContext** member of the RDBSS\_DEVICE\_OBJECT structure pointed to by *RxDeviceObject* is set to the *RxContext* parameter.

*MRxStop* is called by RDBSS from the [**RxStopMinirdr**](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxstopminirdr) routine.

If *MRxStop* returns STATUS\_SUCCESS, then the routine was successful. Any other return value indicates that an error occurred in stopping the network mini-redirector.

If *MRxStop* returns STATUS\_SUCCESS, RDBSS sets the state of RDBSS to RDBSS\_STARTABLE. This state is stored in the **StartStopContext.State** member of the RDBSS\_DEVICE\_OBJECT structure pointed to by *RxDeviceObject*.

A network mini-redirector would normally maintain an internal variable indicating whether the network mini-redirector is started. For example, a network mini-redirector might track when it is stopped, started, and when a start operation or stop operation is in progress.

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


[**MRxDevFcbXXXControlFile**](mrxdevfcbxxxcontrolfile.md)

[**MrxStart**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_calldown_ctx)

[**RxStopMinirdr**](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxstopminirdr)

 

