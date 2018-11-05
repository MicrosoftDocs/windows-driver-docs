---
title: WriteReqs rule (kmdf)
description: The WriteReqs rule specifies that a write request is not passed to inappropriate KMDF methods.
ms.assetid: 8f5718ec-ab3a-4e4f-8401-9113bf0d9552
ms.date: 05/21/2018
keywords: ["WriteReqs rule (kmdf)"]
topic_type:
- apiref
api_name:
- WriteReqs
api_type:
- NA
ms.localizationpriority: medium
---

# WriteReqs rule (kmdf)


The **WriteReqs** rule specifies that a write request is not passed to inappropriate KMDF methods.

All requests presented to the driver in the [*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813) event callback function callback are guaranteed to be write requests. These requests cannot be sent by using KMDF methods that are specifically designed to send read or IOCTL requests.

The write requests cannot be sent to the following methods

[**WdfUsbTargetPipeReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551155)

[**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548660),

[**WdfIoTargetSendInternalIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548656),

[**WdfIoTargetSendInternalIoctlOthersSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548651),

[**WdfIoTargetSendReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548669).

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>WriteReqs</strong> rule.</p>
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

[**WdfIoTargetSendInternalIoctlOthersSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548651)
[**WdfIoTargetSendInternalIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548656)
[**WdfIoTargetSendIoctlSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548660)
[**WdfIoTargetSendReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff548669)
[**WdfUsbTargetPipeReadSynchronously**](https://msdn.microsoft.com/library/windows/hardware/ff551155)
 

 





