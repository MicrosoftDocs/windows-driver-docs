---
title: Revise Code That Issues I/O Requests
description: Revise Code That Issues I/O Requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Revise Code That Issues I/O Requests


WDF defines several methods that a driver can use to create and format I/O requests. The following table summarizes these methods:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">KMDF method</th>
<th align="left">Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforioctl" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForIoctl&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforioctl)"><strong>WdfIoTargetFormatRequestForIoctl</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforinternalioctl" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForInternalIoctl&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforinternalioctl)"><strong>WdfIoTargetFormatRequestForInternalIoctl</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforinternalioctlothers" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForInternalIoctlOthers&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforinternalioctlothers)"><strong>WdfIoTargetFormatRequestForInternalIoctlOthers</strong></a></p></td>
<td align="left">Similar to manually formatting the next I/O stack location.</td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforread" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForRead&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforread)"><strong>WdfIoTargetFormatRequestForRead</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforwrite" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForWrite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforwrite)"><strong>WdfIoTargetFormatRequestForWrite</strong></a></p></td>
<td align="left">Similar to <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildasynchronousfsdrequest" data-raw-source="[&lt;strong&gt;IoBuildAsynchronousFsdRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildasynchronousfsdrequest)"><strong>IoBuildAsynchronousFsdRequest</strong></a>.</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendioctlsynchronously" data-raw-source="[&lt;strong&gt;WdfIoTargetSendIoctlSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendioctlsynchronously)"><strong>WdfIoTargetSendIoctlSynchronously</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendinternalioctlsynchronously" data-raw-source="[&lt;strong&gt;WdfIoTargetSendInternalIoctlSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendinternalioctlsynchronously)"><strong>WdfIoTargetSendInternalIoctlSynchronously</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendinternalioctlotherssynchronously" data-raw-source="[&lt;strong&gt;WdfIoTargetSendInternalIoctlOthersSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendinternalioctlotherssynchronously)"><strong>WdfIoTargetSendInternalIoctlOthersSynchronously</strong></a></p></td>
<td align="left">Similar to <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest" data-raw-source="[&lt;strong&gt;IoBuildDeviceIoControlRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest)"><strong>IoBuildDeviceIoControlRequest</strong></a>, followed by <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)"><strong>IoCallDriver</strong></a>.</td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendreadsynchronously" data-raw-source="[&lt;strong&gt;WdfIoTargetSendReadSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendreadsynchronously)"><strong>WdfIoTargetSendReadSynchronously</strong></a></p>
<p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendwritesynchronously" data-raw-source="[&lt;strong&gt;WdfIoTargetSendWriteSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetsendwritesynchronously)"><strong>WdfIoTargetSendWriteSynchronously</strong></a></p></td>
<td align="left">Similar to <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildsynchronousfsdrequest" data-raw-source="[&lt;strong&gt;IoBuildSynchronousFsdRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildsynchronousfsdrequest)"><strong>IoBuildSynchronousFsdRequest</strong></a>, followed by <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)"><strong>IoCallDriver</strong></a>.</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcancelsentrequest" data-raw-source="[&lt;strong&gt;WdfRequestCancelSentRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcancelsentrequest)"><strong>WdfRequestCancelSentRequest</strong></a></p></td>
<td align="left">Similar to <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocancelirp" data-raw-source="[&lt;strong&gt;IoCancelIrp&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocancelirp)"><strong>IoCancelIrp</strong></a> for a PIRP that was sent with <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)"><strong>IoCallDriver</strong></a>. The framework provides locks to ensure that the PIRP is not completed or freed between the calls to <strong>IoCallDriver</strong> and <strong>IoCancelIrp</strong>.</td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcreate" data-raw-source="[&lt;strong&gt;WdfRequestCreate&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcreate)"><strong>WdfRequestCreate</strong></a></td>
<td align="left">Similar to <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp" data-raw-source="[&lt;strong&gt;IoAllocateIrp&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp)"><strong>IoAllocateIrp</strong></a>. Creates a new WDFREQUEST object, sets attributes, and returns handle to caller.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestformatrequestusingcurrenttype" data-raw-source="[&lt;strong&gt;WdfRequestFormatRequestUsingCurrentType&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestformatrequestusingcurrenttype)"><strong>WdfRequestFormatRequestUsingCurrentType</strong></a></td>
<td align="left">Similar to <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioforwardirpsynchronously" data-raw-source="[&lt;strong&gt;IoForwardIrpSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioforwardirpsynchronously)"><strong>IoForwardIrpSynchronously</strong></a> but does not call <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)"><strong>IoCallDriver</strong></a>; driver must call <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend" data-raw-source="[&lt;strong&gt;WdfRequestSend&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)"><strong>WdfRequestSend</strong></a>.</td>
</tr>
<tr class="even">
<td align="left"><a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend" data-raw-source="[&lt;strong&gt;WdfRequestSend&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)"><strong>WdfRequestSend</strong></a></td>
<td align="left">Similar to <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioforwardirpsynchronously" data-raw-source="[&lt;strong&gt;IoForwardIrpSynchronously&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioforwardirpsynchronously)"><strong>IoForwardIrpSynchronously</strong></a> but does not call <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)"><strong>IoCallDriver</strong></a>; driver must call <a href="/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend" data-raw-source="[&lt;strong&gt;WdfRequestSend&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend)"><strong>WdfRequestSend</strong></a>.</td>
</tr>
</tbody>
</table>

 

To send a request to another device stack, a WDF driver uses a remote I/O target. For information about how to initialize a remote I/O target, see [Initializing a General I/O Target](initializing-a-general-i-o-target.md).

To get the completion status for an asynchronous request or for any request that is sent by calling [**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend), the driver calls [**WdfRequestGetStatus**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestgetstatus). For a synchronous request, it can retrieve status immediately. For an asynchronous request, the driver’s I/O completion callback typically retrieves status. For more information about sending requests synchronously or asynchronously, see [Sending I/O Requests to General I/O Targets](sending-i-o-requests-to-general-i-o-targets.md).

