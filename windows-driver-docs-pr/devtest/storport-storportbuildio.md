---
title: StorPortBuildIo rule (storport)
description: This rule verifies that if the StorPort miniport's StorPortBuildIo routine returns FALSE, the SRB in question is not passed to StartIo.
ms.assetid: C35954F9-9C59-408B-BF80-2B8DCD328F9C
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["StorPortBuildIo rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortBuildIo
api_type:
- NA
ms.localizationpriority: medium
---

# StorPortBuildIo rule (storport)


This rule verifies that if the StorPort miniport's **StorPortBuildIo** routine returns **FALSE**, the SRB in question is not passed to **StartIo**. (In such cases, the miniport driver must complete the SRB by calling [**StorPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff567433) with a notification type of **RequestComplete** from **StorPortBuildIo** or someplace else).

> [!NOTE]
> This rule is testing StorPort's correct operation, not the miniport's.

 

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortBuildIo</strong> rule.</p>
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

 

 





