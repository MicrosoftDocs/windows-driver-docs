---
title: Sending I/O Requests Asynchronously
description: Sending I/O Requests Asynchronously
keywords:
- general I/O targets WDK KMDF , sending I/O requests to
- sending I/O requests WDK KMDF
- sending I/O requests WDK KMDF , asynchronous
- asynchronously sending I/O requests WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sending I/O Requests Asynchronously





Before you can send an I/O request asynchronously to an I/O target, you must format the request. The following table lists the I/O target object methods that your driver can call to format I/O requests.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Method</th>
<th align="left">Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforread" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForRead&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforread)"><strong>WdfIoTargetFormatRequestForRead</strong></a></p></td>
<td align="left"><p>Formats a read request</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforwrite" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForWrite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforwrite)"><strong>WdfIoTargetFormatRequestForWrite</strong></a></p></td>
<td align="left"><p>Formats a write request</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforioctl" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForIoctl&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforioctl)"><strong>WdfIoTargetFormatRequestForIoctl</strong></a></p></td>
<td align="left"><p>Formats a device control request</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforinternalioctl" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForInternalIoctl&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforinternalioctl)"><strong>WdfIoTargetFormatRequestForInternalIoctl</strong></a></p></td>
<td align="left"><p>Formats an internal device control request</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforinternalioctlothers" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForInternalIoctlOthers&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforinternalioctlothers)"><strong>WdfIoTargetFormatRequestForInternalIoctlOthers</strong></a></p></td>
<td align="left"><p>Formats a non-standard internal device control request</p></td>
</tr>
</tbody>
</table>

 

To send an I/O request asynchronously, your driver must:

1.  Format the request.

    Use one of the methods that are listed in the previous table to format your requests. For detailed information about how to use these methods, see the methods' reference pages.

2.  Register a [*CompletionRoutine*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_completion_routine) callback function.

    If you send requests asynchronously, you typically want the framework to notify your driver when another driver completes each request. Your driver should define a [*CompletionRoutine*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_completion_routine) callback function and register it by calling [**WdfRequestSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsetcompletionroutine). For more information, see [Completing I/O Requests](completing-i-o-requests.md).

3.  Send the request.

    After your driver formats the request and registers a [*CompletionRoutine*](/windows-hardware/drivers/ddi/wdfrequest/nc-wdfrequest-evt_wdf_request_completion_routine) callback function, your driver must call [**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend). This method enables you to send requests either synchronously or asynchronously, depending on the flags set in the *RequestOptions* parameter. For a simpler way to send I/O requests synchronously, see [Sending I/O Requests Synchronously](sending-i-o-requests-synchronously.md). For information about how to get the completion status for an asynchronous request or for any request that is sent by calling **WdfRequestSend**, see [Completing I/O Requests](completing-i-o-requests.md).

A driver that calls [**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend) to send an I/O request can attempt to cancel the request later. For more information, see [Canceling I/O Requests](canceling-i-o-requests.md).

Some drivers might send a single I/O request to multiple devices, and thus to multiple I/O targets, by calling [**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend) more than once for each request. These drivers must call [**WdfRequestChangeTarget**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestchangetarget) before each call to **WdfRequestSend** after the first one to verify that the request can be sent to the next I/O target.

