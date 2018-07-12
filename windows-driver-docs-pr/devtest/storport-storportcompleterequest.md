---
title: StorPortCompleteRequest rule (storport)
description: This rule verifies that no calls to StorPortCompleteRequest are made by the miniport. Usage of the StorPortCompleteRequest is not recommended; miniports should instead call StorPortNotification with notificationType RequestComplete.
ms.assetid: 6DDAC83F-C4D5-4600-B5F3-AA7F216BB797
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["StorPortCompleteRequest rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortCompleteRequest
api_type:
- NA
---

# StorPortCompleteRequest rule (storport)


This rule verifies that no calls to **StorPortCompleteRequest** are made by the miniport. Usage of the **StorPortCompleteRequest** is not recommended; miniports should instead call **StorPortNotification** with **notificationType = RequestComplete**.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortCompleteRequest</strong> rule.</p>
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
 

 





