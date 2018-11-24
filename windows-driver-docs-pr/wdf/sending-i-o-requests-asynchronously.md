---
title: Sending I/O Requests Asynchronously
description: Sending I/O Requests Asynchronously
ms.assetid: 9f6fb85e-96aa-4945-8c8a-13277beff140
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548612" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForRead&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548612)"><strong>WdfIoTargetFormatRequestForRead</strong></a></p></td>
<td align="left"><p>Formats a read request</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548620" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForWrite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548620)"><strong>WdfIoTargetFormatRequestForWrite</strong></a></p></td>
<td align="left"><p>Formats a write request</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548604" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForIoctl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548604)"><strong>WdfIoTargetFormatRequestForIoctl</strong></a></p></td>
<td align="left"><p>Formats a device control request</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548595" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForInternalIoctl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548595)"><strong>WdfIoTargetFormatRequestForInternalIoctl</strong></a></p></td>
<td align="left"><p>Formats an internal device control request</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff548599" data-raw-source="[&lt;strong&gt;WdfIoTargetFormatRequestForInternalIoctlOthers&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548599)"><strong>WdfIoTargetFormatRequestForInternalIoctlOthers</strong></a></p></td>
<td align="left"><p>Formats a non-standard internal device control request</p></td>
</tr>
</tbody>
</table>

 

To send an I/O request asynchronously, your driver must:

1.  Format the request.

    Use one of the methods that are listed in the previous table to format your requests. For detailed information about how to use these methods, see the methods' reference pages.

2.  Register a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function.

    If you send requests asynchronously, you typically want the framework to notify your driver when another driver completes each request. Your driver should define a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function and register it by calling [**WdfRequestSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff550030). For more information, see [Completing I/O Requests](completing-i-o-requests.md).

3.  Send the request.

    After your driver formats the request and registers a [*CompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff540745) callback function, your driver must call [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027). This method enables you to send requests either synchronously or asynchronously, depending on the flags set in the *RequestOptions* parameter. For a simpler way to send I/O requests synchronously, see [Sending I/O Requests Synchronously](sending-i-o-requests-synchronously.md). For information about how to get the completion status for an asynchronous request or for any request that is sent by calling **WdfRequestSend**, see [Completing I/O Requests](completing-i-o-requests.md).

A driver that calls [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) to send an I/O request can attempt to cancel the request later. For more information, see [Canceling I/O Requests](canceling-i-o-requests.md).

Some drivers might send a single I/O request to multiple devices, and thus to multiple I/O targets, by calling [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) more than once for each request. These drivers must call [**WdfRequestChangeTarget**](https://msdn.microsoft.com/library/windows/hardware/ff549943) before each call to **WdfRequestSend** after the first one to verify that the request can be sent to the next I/O target.

 

 





