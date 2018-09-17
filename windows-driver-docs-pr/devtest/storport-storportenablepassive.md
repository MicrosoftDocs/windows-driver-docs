---
title: StorPortEnablePassive rule (storport)
description: This rule verifies that StorPortEnablePassiveInitialization is not called from any StorPort miniport driver routine other than HwInitialize.
ms.assetid: 3B6EDA79-B17D-43A7-B1A3-BCC7134D13EA
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["StorPortEnablePassive rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortEnablePassive
api_type:
- NA
ms.localizationpriority: medium
---

# StorPortEnablePassive rule (storport)


This rule verifies that **StorPortEnablePassiveInitialization** is not called from any StorPort miniport driver routine other than **HwInitialize**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortEnablePassive</strong> rule.</p>
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

[**StorPortEnablePassiveInitialization**](https://msdn.microsoft.com/library/windows/hardware/ff567056)
 

 





