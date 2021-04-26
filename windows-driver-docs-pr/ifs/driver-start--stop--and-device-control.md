---
title: Driver Start, Stop, and Device Control
description: Driver Start, Stop, and Device Control
keywords:
- mini-redirectors WDK , starting
- mini-redirectors WDK , stopping
- mini-redirectors WDK , device controls
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Start, Stop, and Device Control


Driver registration is handled in the **DriverEntry** routine of a network mini-redirector driver. When a network mini-redirector first starts (in its **DriverEntry** routine), the driver must call the RDBSS [**RxRegisterMinirdr**](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxregisterminirdr) routine to register the network mini-redirector with RDBSS. The network mini-redirector passes in a MINIRDR\_DISPATCH structure which includes configuration data and a table of routine pointers (a dispatch table) to the routines that the network mini-redirector driver implements.

The [**MRxStart**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_calldown_ctx) and [**MRxStop**](./mrxstop.md) routines must be implemented by the network mini-redirector driver to allow the driver to be started and stopped.

The sequence to start or stop the network mini-redirector is complex. This sequence is normally initiated by a user-mode application or service supplied with network mini-redirector driver to control the driver for administration and management purposes. The network mini-redirector can use a service that is configured to start automatically when the operating system starts. This service can request that the network mini-redirector be started whenever the operating system starts.

[**MRxStart**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_calldown_ctx) is called by RDBSS when the [**RxStartMinirdr**](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxstartminirdr) routine is called. The **RxStartMinirdr** routine is usually called as a result of an FSCTL or IOCTL request from a user-mode application or service to start the network mini-redirector. The call to **RxStartMinirdr** cannot be made from the **DriverEntry** routine of the network mini-redirector after a successful call to [**RxRegisterMinirdr**](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxregisterminirdr)because some of the start processing requires that the driver initialization be completed. Once the **RxStartMinirdr** call is received, RDBSS completes the start process by calling the **MRxStart** routine of the network mini-redirector. If the call to **MRxStart** returns success, RDBSS sets the internal state of the mini-redirector in RDBSS to RDBSS\_STARTED.

[**MRxStop**](./mrxstop.md) is called by RDBSS when the [**RxStopMinirdr**](/windows-hardware/drivers/ddi/mrx/nf-mrx-rxstopminirdr) routine is called. The RDBSS **RxStopMinirdr** routine is usually called as a result of an FSCTL or IOCTL request from a user-mode application or service to stop the network mini-redirector. This call can also be made from the network mini-redirector or, as part of shutdown process, by the operating system. Once the **RxStopMinirdr** call is received, RDBSS completes the process by calling the **MRxStop** routine of the network mini-redirector.

The [**MRxDevFcbXXXControlFile**](./mrxdevfcbxxxcontrolfile.md) routine is used to receive requests from a user-mode application or service to control the network mini-redirector by making IOCTL or FSCTL calls on a device FCB.

In addition, there are two low I/O routines that handle IOCTL and FSCTL operations on the driver object: [**MRxLowIOSubmit\[LOWIO\_OP\_FSCTL\]**](./mrxlowiosubmit-lowio-op-fsctl-.md) and [**MRxLowIOSubmit\[LOWIO\_OP\_IOCTL\]**](./mrxlowiosubmit-lowio-op-ioctl-.md).

A network mini-redirector can also use these low I/O routines to provide control and management of the network mini-redirector from a user-mode application or service.

The following table lists the routines that can be implemented by a network mini-redirector for start, stop, and device control operations.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxdevfcbxxxcontrolfile" data-raw-source="[&lt;strong&gt;MRxDevFcbXXXControlFile&lt;/strong&gt;](./mrxdevfcbxxxcontrolfile.md)"><strong>MRxDevFcbXXXControlFile</strong></a></td>
<td align="left"><p>RDBSS calls this routine to pass a device FCB control request to the network mini-redirector. RDBSS issues this call in response to receiving an IRP_MJ_DEVICE_CONTROL, IRP_MJ_FILE_SYSTEM_CONTROL, or IRP_MJ_INTERNAL_DEVICE_CONTROL on a device FCB.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_calldown_ctx" data-raw-source="[&lt;strong&gt;MRxStart&lt;/strong&gt;](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_calldown_ctx)"><strong>MRxStart</strong></a></td>
<td align="left"><p>RDBSS calls this routine to start the network mini-redirector.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ifs/mrxstop" data-raw-source="[&lt;strong&gt;MRxStop&lt;/strong&gt;](./mrxstop.md)"><strong>MRxStop</strong></a></td>
<td align="left"><p>RDBSS calls this routine to stop the network mini-redirector.</p></td>
</tr>
</tbody>
</table>

 

