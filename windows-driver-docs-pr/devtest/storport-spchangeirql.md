---
title: SpChangeIrql rule (storport)
description: This rule verifies that the StorPort callback routines return at the same IRQL level as the level at which they are called.
ms.assetid: 7F54D12B-D027-4A59-97A5-97287571AAF3
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["SpChangeIrql rule (storport)"]
topic_type:
- apiref
api_name:
- SpChangeIrql
api_type:
- NA
ms.localizationpriority: medium
---

# SpChangeIrql rule (storport)


This rule verifies that the StorPort callback routines return at the same IRQL level as the level at which they are called.

Applies to any DDI that changes the IRQL level within Storport miniport entry points or callback routines.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>SpChangeIrql</strong> rule.</p>
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

 

 





