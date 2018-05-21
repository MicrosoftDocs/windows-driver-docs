---
title: StorPortTimer rule (storport)
description: The HW\_TIMER routine must be defined if a call to StorPortNotification(RequestTimerCall) is made.
ms.assetid: 863AA6C2-A3EC-41F9-88D9-6852A42D2636
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["StorPortTimer rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortTimer
api_type:
- NA
---

# StorPortTimer rule (storport)


The **HW\_TIMER** routine must be defined if a call to **StorPortNotification(RequestTimerCall)** is made.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortTimer</strong> rule.</p>
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
 

 





