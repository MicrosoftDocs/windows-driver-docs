---
title: Flags\_Irql rule (ndis)
description: The Flags\_Irql rule specifies that KeGetCurrentIrql must not be called within callback functions that have a dispatch level flag parameter that indicates the current IRQL.
ms.assetid: 19c5c497-9648-4be9-87d1-82f4fa295351
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["Flags_Irql rule (ndis)"]
topic_type:
- apiref
api_name:
- Flags_Irql
api_type:
- NA
ms.localizationpriority: medium
---

# Flags\_Irql rule (ndis)


The **Flags\_Irql** rule specifies that **KeGetCurrentIrql** must not be called within callback functions that have a dispatch level flag parameter that indicates the current IRQL.

The correct use of the dispatch level flag can help you avoid unnecessary attempts to set the IRQL. For more information about how to use this flag, see [Dispatch IRQL Tracking](https://msdn.microsoft.com/library/windows/hardware/ff546448).

|              |      |
|--------------|------|
| Driver model | NDIS |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>Flags_Irql</strong> rule.</p>
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

 

 





