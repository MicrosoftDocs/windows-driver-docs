---
title: ReqCompletionRoutine rule (kmdf)
description: The ReqCompletionRoutine rule specifies that a completion routine must be set before a request is sent to an I/O target.
ms.assetid: 0ddf6980-0540-4224-9800-3cd534f03230
ms.date: 05/21/2018
keywords: ["ReqCompletionRoutine rule (kmdf)"]
topic_type:
- apiref
api_name:
- ReqCompletionRoutine
api_type:
- NA
ms.localizationpriority: medium
---

# ReqCompletionRoutine rule (kmdf)


The **ReqCompletionRoutine** rule specifies that a completion routine must be set before a request is sent to an I/O target.

If a request is not sent synchronously, or is not sent as send and forget, (specified by the **WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET** flag), the driver should set a completion routine so that the I/O target can notify the driver when the request is completed.

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>ReqCompletionRoutine</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**WdfRequestSend**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestsend)
[**WdfRequestSetCompletionRoutine**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/nf-wdfrequest-wdfrequestsetcompletionroutine)
See also
--------

[Completing I/O Requests](https://docs.microsoft.com/windows-hardware/drivers/wdf/completing-i-o-requests)
[Synchronizing Cancel and Completion Code](https://docs.microsoft.com/windows-hardware/drivers/wdf/synchronizing-cancel-and-completion-code)
[**WDF\_REQUEST\_SEND\_OPTIONS\_FLAGS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/ne-wdfrequest-_wdf_request_send_options_flags)
[**WDF\_REQUEST\_SEND\_OPTIONS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfrequest/ns-wdfrequest-_wdf_request_send_options)
 

 





