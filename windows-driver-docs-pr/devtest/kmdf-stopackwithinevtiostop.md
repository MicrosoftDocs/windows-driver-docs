---
title: StopAckWithinEvtIoStop rule (kmdf)
description: The StopAckWithinEvtIoStop rule specifies that the WdfRequestStopAcknowledge function is only called from within EvtIoStop callback function.
ms.assetid: 10b6278d-a298-41f0-8232-e374bfeb0ab7
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["StopAckWithinEvtIoStop rule (kmdf)"]
topic_type:
- apiref
api_name:
- StopAckWithinEvtIoStop
api_type:
- NA
ms.localizationpriority: medium
---

# StopAckWithinEvtIoStop rule (kmdf)


The **StopAckWithinEvtIoStop** rule specifies that the [**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033) function is only called from within [*EvtIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541788) callback function.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StopAckWithinEvtIoStop</strong> rule.</p>
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

[**WdfRequestStopAcknowledge**](https://msdn.microsoft.com/library/windows/hardware/ff550033)
 

 





