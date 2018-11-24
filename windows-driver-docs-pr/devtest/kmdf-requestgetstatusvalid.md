---
title: RequestGetStatusValid rule (kmdf)
description: The RequestGetStatusValid rule that specifies that WdfRequestGetStatus should be called for a request in one of the following situations When WdfRequestSend returns failure.When the request has been sent with WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS.
ms.assetid: 9EFC41AB-E5BD-4DE8-8936-E71EA64E5430
ms.date: 05/21/2018
keywords: ["RequestGetStatusValid rule (kmdf)"]
topic_type:
- apiref
api_name:
- RequestGetStatusValid
api_type:
- NA
ms.localizationpriority: medium
---

# RequestGetStatusValid rule (kmdf)


The **RequestGetStatusValid** rule that specifies that [**WdfRequestGetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff549974) should be called for a request in one of the following situations:

-   When [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) returns failure.
-   When the request has been sent with WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>RequestGetStatusValid</strong> rule.</p>
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

[**WdfRequestGetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff549974)
[**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027)
 

 





