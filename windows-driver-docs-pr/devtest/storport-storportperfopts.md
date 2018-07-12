---
title: StorPortPerfOpts rule (storport)
description: This rule verifies that the PerfConfigData parameter that is passed to StorPortInitializePerfOpts is not NULL.
ms.assetid: 0BF93331-28D5-442D-8D27-B1F21DC0F5EA
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["StorPortPerfOpts rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortPerfOpts
api_type:
- NA
---

# StorPortPerfOpts rule (storport)


This rule verifies that the **PerfConfigData** parameter that is passed to **StorPortInitializePerfOpts** is not NULL.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortPerfOpts</strong> rule.</p>
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

[**StorPortInitializePerfOpts**](https://msdn.microsoft.com/library/windows/hardware/ff567114)
 

 





