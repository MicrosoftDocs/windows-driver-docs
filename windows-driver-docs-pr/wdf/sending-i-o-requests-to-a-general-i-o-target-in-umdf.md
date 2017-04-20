---
title: Sending I/O Requests to a General I/O Target in UMDF
author: windows-driver-content
description: Sending I/O Requests to a General I/O Target in UMDF
ms.assetid: f373afa8-292a-47bb-af6f-5035287d1e8c
keywords:
- general I/O targets WDK UMDF , sending I/O requests to
- sending I/O requests WDK UMDF
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sending I/O Requests to a General I/O Target in UMDF


\[This topic applies to UMDF 1.*x*.\]

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
<td align="left"><p>[<strong>IWDFIoRequest::FormatUsingCurrentType</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559077)</p></td>
<td align="left"><p>Formats a request that the driver received from the framework so that the driver can send the request, unmodified, to the target</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IWDFIoTarget::FormatRequestForIoctl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559230)</p></td>
<td align="left"><p>Formats a device control request</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IWDFIoTarget::FormatRequestForRead</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559233)</p></td>
<td align="left"><p>Formats a read request</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IWDFIoTarget::FormatRequestForWrite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559236)</p></td>
<td align="left"><p>Formats a write request</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IWDFIoTarget2::FormatRequestForFlush</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559182)</p></td>
<td align="left"><p>Formats a request to flush buffers.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IWDFIoTarget2::FormatRequestForQueryInformation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559184)</p></td>
<td align="left"><p>Formats a request to obtain file information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IWDFIoTarget2::FormatRequestForSetInformation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559191)</p></td>
<td align="left"><p>Formats a request to set file information.</p></td>
</tr>
</tbody>
</table>

 

To send the I/O request to the I/O target, the driver calls the [**IWDFIoRequest::Send**](https://msdn.microsoft.com/library/windows/hardware/ff559149) method. To send the I/O request synchronously, the driver passes the WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS flag to the *Flags* parameter. Otherwise, the driver sends the I/O request asynchronously. If the driver sends the I/O request asynchronously, the driver typically requires notification when another driver completes the request. The driver should define a [**IRequestCallbackRequestCompletion::OnCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff556905) callback function and register it by calling the [**IWDFIoRequest::SetCompletionCallback**](https://msdn.microsoft.com/library/windows/hardware/ff559153) method. For more information, see [Completing I/O Requests](completing-i-o-requests.md).

A driver that calls **IWDFIoRequest::Send** to send an I/O request can attempt to cancel the request later by calling the [**IWDFIoRequest::CancelSentRequest**](https://msdn.microsoft.com/library/windows/hardware/ff559067) method. If the driver cancels an I/O request that the driver received from the framework, the driver must always complete the request by calling the [**IWDFIoRequest::Complete**](https://msdn.microsoft.com/library/windows/hardware/ff559070) or [**IWDFIoRequest::CompleteWithInformation**](https://msdn.microsoft.com/library/windows/hardware/ff559074) method with the *CompletionStatus* parameter set to STATUS\_CANCELLED. If the driver created the request object, the driver calls [**IWDFObject::DeleteWdfObject**](https://msdn.microsoft.com/library/windows/hardware/ff560210) instead of completing the request.

 

 





