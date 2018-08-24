---
title: StorPortDDIsPortOnly rule (storport)
description: This rule contains a list of StorPort port-only DDIs (excluding interlocked functions) that should not be called in StorPort miniports.
ms.assetid: 55922047-5029-4EB8-B363-61C098339F2E
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["StorPortDDIsPortOnly rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortDDIsPortOnly
api_type:
- NA
ms.localizationpriority: medium
---

# StorPortDDIsPortOnly rule (storport)


This rule contains a list of StorPort port-only DDIs (excluding interlocked functions) that should not be called in StorPort miniports.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortDDIsPortOnly</strong> rule.</p>
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

[**StorPortCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff567042)
 

 





