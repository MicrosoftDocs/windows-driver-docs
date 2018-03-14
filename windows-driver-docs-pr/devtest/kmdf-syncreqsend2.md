---
title: SyncReqSend2 rule (kmdf)
description: The SyncReqSend2 rule specifies that synchronous request sends have a nonzero time-out value set.
ms.assetid: c72b909f-6160-47da-8e7e-84e0dea785c2
keywords: ["SyncReqSend2 rule (kmdf)"]
topic_type:
- apiref
api_name:
- SyncReqSend2
api_type:
- NA
---

# SyncReqSend2 rule (kmdf)


The **SyncReqSend2** rule specifies that synchronous request sends have a nonzero time-out value set.

If the driver calls [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027) without setting a valid time-out in the request options, the thread can be stalled if hardware does not respond promptly.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SyncReqSend2</strong> rule.</p>
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

[**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027)
 

 





