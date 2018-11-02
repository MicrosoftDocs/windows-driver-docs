---
title: RequestForUrbXrb rule (kmdf)
ms.assetid: 8BFFB73D-106A-4CD0-93F2-D295D969729E
ms.date: 05/21/2018
description: 
keywords: ["RequestForUrbXrb rule (kmdf)"]
topic_type:
- apiref
api_name:
- RequestForUrbXrb
api_type:
- NA
ms.localizationpriority: medium
---

# RequestForUrbXrb rule (kmdf)


If the client driver calls [**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428) and specifies the client contract version USBD\_CLIENT\_CONTRACT\_VERSION\_602 in the WDF\_USB\_DEVICE\_CREATE\_CONFIG structure (to use the new capabilities of the USB driver stack for Windows 8), DDIs that use a URB internally would only use *URB context* if any of the following preconditions apply:

-   Request parameter has the Wdf device in its parent object tree.
-   Request is represented via the I/O queue.
-   Request has another I/O queue represented request in its parent object tree.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>RequestForUrbXrb</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951)
[**WdfUsbTargetDeviceCreateWithParameters**](https://msdn.microsoft.com/library/windows/hardware/hh439428)
[**WdfUsbTargetDeviceFormatRequestForControlTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff550082)
[**WdfUsbTargetDeviceFormatRequestForString**](https://msdn.microsoft.com/library/windows/hardware/ff550086)
[**WdfUsbTargetDeviceSendControlTransferSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff550104)
[**WdfUsbTargetPipeAbortSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551129)
[**WdfUsbTargetPipeFormatRequestForAbort**](https://msdn.microsoft.com/library/windows/hardware/ff551132)
[**WdfUsbTargetPipeFormatRequestForReset**](https://msdn.microsoft.com/library/windows/hardware/ff551138)
[**WdfUsbTargetPipeResetSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551156)
 

 





