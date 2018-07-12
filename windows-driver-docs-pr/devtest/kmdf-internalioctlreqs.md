---
title: InternalIoctlReqs rule (kmdf)
description: The InternalIoctlReqs rule specifies that internal IOCTL requests are not passed to inappropriate KMDF request-send device driver interfaces (DDIs).
ms.assetid: a6d75752-21eb-486b-b73a-8d810b392e6b
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["InternalIoctlReqs rule (kmdf)"]
topic_type:
- apiref
api_name:
- InternalIoctlReqs
api_type:
- NA
---

# InternalIoctlReqs rule (kmdf)


The **InternalIoctlReqs** rule specifies that internal IOCTL requests are not passed to inappropriate KMDF request-send device driver interfaces (DDIs).

All requests presented to the driver in the EVT\_WDF\_IO\_QUEUE\_IO\_INTERNAL\_DEVICE\_CONTROL callback function are guaranteed to be internal IOCTL requests. Therefore, these IOCTLs cannot be sent by using DDIs that are specific to sending read, write, or IOCTL, requests, such as **WdfIoTargetSendReadSynchronously**, **WdfIoTargetSendWriteSynchronously**, **WdfIoTargetSendIoctlSynchronously**, **WdfUsbTargetPipeWriteSynchronously**.

|              |      |
|--------------|------|
| Driver model | KMDF |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>InternalIoctlReqs</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548660)
[**WdfIoTargetSendReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548669)
[**WdfIoTargetSendWriteSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548672)
[**WdfUsbTargetPipeReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551155)
[**WdfUsbTargetPipeWriteSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551163)
 

 





