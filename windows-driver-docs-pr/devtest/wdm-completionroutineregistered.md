---
title: CompletionRoutineRegistered rule (wdm)
description: The CompletionRoutineRegistered rule specifies that if the dispatch routine registers an IoCompletion routine using IoSetCompletionRoutineEx, the dispatch routine must thereafter call IoCallDriver or PoCallDriver.
ms.assetid: ee0d813c-3bcc-4688-902c-1a2d15ddfd09
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["CompletionRoutineRegistered rule (wdm)"]
topic_type:
- apiref
api_name:
- CompletionRoutineRegistered
api_type:
- NA
ms.localizationpriority: medium
---

# CompletionRoutineRegistered rule (wdm)


The **CompletionRoutineRegistered** rule specifies that if the dispatch routine registers an [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine using [**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686), the dispatch routine must thereafter call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654).

The **IoSetCompletionRoutineEx** routine allocates memory that remains allocated until the **IoCompletion** routine executes. Drivers must ensure that their **IoCompletion** routine executes by calling **IoCallDriver** or **PoCallDriver**; otherwise, the kernel will leak memory.

|              |     |
|--------------|-----|
| Driver model | WDM |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>CompletionRoutineRegistered</strong> rule.</p>
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

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)
[**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679)
[**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)
[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)
 

 





