---
title: Sending I/O Requests to a General I/O Target in UMDF
description: Sending I/O Requests to a General I/O Target in UMDF
keywords:
- general I/O targets WDK UMDF , sending I/O requests to
- sending I/O requests WDK UMDF
ms.date: 04/20/2017
---

# Sending I/O Requests to a General I/O Target in UMDF


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

A UMDF driver can send I/O requests to general I/O targets either synchronously or asynchronously.

If a driver sends I/O requests synchronously, a driver thread sends the requests one at a time. The thread waits for each request to complete before it sends the next one. This process is simpler than sending the I/O requests asynchronously. The driver can send I/O requests synchronously if it does not send many requests and if system or device performance is not reduced while the driver waits for each I/O request.

If a driver sends I/O requests asynchronously, a driver thread sends each request as soon as the request is ready to be sent, without waiting for previously sent requests to finish. If the driver must handle many I/O requests in short periods of time, the driver probably cannot wait for each request to complete before sending the next request. Otherwise, the driver might lose data or the performance of its devices and, possibly, of the entire system might be reduced.

Before a UMDF driver can send an I/O request to an I/O target, the driver must format the request. The following table lists the methods that the driver can call to format I/O requests. The driver can use these methods to format a request that the driver received in one of its I/O queues or that the driver created.

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
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-formatusingcurrenttype" data-raw-source="[&lt;strong&gt;IWDFIoRequest::FormatUsingCurrentType&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-formatusingcurrenttype)"><strong>IWDFIoRequest::FormatUsingCurrentType</strong></a></p></td>
<td align="left"><p>Formats a request that the driver received from the framework so that the driver can send the request, unmodified, to the target</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforioctl" data-raw-source="[&lt;strong&gt;IWDFIoTarget::FormatRequestForIoctl&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforioctl)"><strong>IWDFIoTarget::FormatRequestForIoctl</strong></a></p></td>
<td align="left"><p>Formats a device control request</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforread" data-raw-source="[&lt;strong&gt;IWDFIoTarget::FormatRequestForRead&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforread)"><strong>IWDFIoTarget::FormatRequestForRead</strong></a></p></td>
<td align="left"><p>Formats a read request</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforwrite" data-raw-source="[&lt;strong&gt;IWDFIoTarget::FormatRequestForWrite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget-formatrequestforwrite)"><strong>IWDFIoTarget::FormatRequestForWrite</strong></a></p></td>
<td align="left"><p>Formats a write request</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget2-formatrequestforflush" data-raw-source="[&lt;strong&gt;IWDFIoTarget2::FormatRequestForFlush&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget2-formatrequestforflush)"><strong>IWDFIoTarget2::FormatRequestForFlush</strong></a></p></td>
<td align="left"><p>Formats a request to flush buffers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget2-formatrequestforqueryinformation" data-raw-source="[&lt;strong&gt;IWDFIoTarget2::FormatRequestForQueryInformation&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget2-formatrequestforqueryinformation)"><strong>IWDFIoTarget2::FormatRequestForQueryInformation</strong></a></p></td>
<td align="left"><p>Formats a request to obtain file information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget2-formatrequestforsetinformation" data-raw-source="[&lt;strong&gt;IWDFIoTarget2::FormatRequestForSetInformation&lt;/strong&gt;](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiotarget2-formatrequestforsetinformation)"><strong>IWDFIoTarget2::FormatRequestForSetInformation</strong></a></p></td>
<td align="left"><p>Formats a request to set file information.</p></td>
</tr>
</tbody>
</table>

 

To send the I/O request to the I/O target, the driver calls the [**IWDFIoRequest::Send**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-send) method. To send the I/O request synchronously, the driver passes the WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS flag to the *Flags* parameter. Otherwise, the driver sends the I/O request asynchronously. If the driver sends the I/O request asynchronously, the driver typically requires notification when another driver completes the request. The driver should define a [**IRequestCallbackRequestCompletion::OnCompletion**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-irequestcallbackrequestcompletion-oncompletion) callback function and register it by calling the [**IWDFIoRequest::SetCompletionCallback**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-setcompletioncallback) method. For more information, see [Completing I/O Requests](completing-i-o-requests.md).

A driver that calls **IWDFIoRequest::Send** to send an I/O request can attempt to cancel the request later by calling the [**IWDFIoRequest::CancelSentRequest**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-cancelsentrequest) method. If the driver cancels an I/O request that the driver received from the framework, the driver must always complete the request by calling the [**IWDFIoRequest::Complete**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-complete) or [**IWDFIoRequest::CompleteWithInformation**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfiorequest-completewithinformation) method with the *CompletionStatus* parameter set to STATUS\_CANCELLED. If the driver created the request object, the driver calls [**IWDFObject::DeleteWdfObject**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfobject-deletewdfobject) instead of completing the request.

