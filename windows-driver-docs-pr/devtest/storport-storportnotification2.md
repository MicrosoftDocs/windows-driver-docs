---
title: StorPortNotification2 rule (storport)
description: This rule verifies that calls to StorPortNotification use only allowed (i.e. documented) notification types.
ms.assetid: 74363E6D-1D1B-484D-A558-8996DFE02FA8
keywords: ["StorPortNotification2 rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortNotification2
api_type:
- NA
---

# StorPortNotification2 rule (storport)


This rule verifies that calls to **StorPortNotification** use only allowed (i.e. documented) notification types.

The allowed notification types are:

**BufferOverrunDetected**
**BusChangeDetected**
**LinkDown**
**LinkUp**
**QueryTickCount**
**RequestComplete**
**RequestTimerCall**
**ResetDetected**
**WMIEvent**
**WMIReregister**
|              |          |
|--------------|----------|
| Driver model | Storport |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortNotification2</strong> rule.</p>
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

[**StorPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff567433)
 

 





