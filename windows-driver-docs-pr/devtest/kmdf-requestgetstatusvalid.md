---
title: RequestGetStatusValid rule (kmdf)
description: The RequestGetStatusValid rule that specifies that WdfRequestGetStatus should be called for a request in one of the following situations When WdfRequestSend returns failure.When the request has been sent with WDF\_REQUEST\_SEND\_OPTION\_SYNCHRONOUS.
ms.assetid: 9EFC41AB-E5BD-4DE8-8936-E71EA64E5430
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["RequestGetStatusValid rule (kmdf)"]
topic_type:
- apiref
api_name:
- RequestGetStatusValid
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>RequestGetStatusValid</strong> rule.</p>
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

[**WdfRequestGetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff549974)
[**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027)
 

 





