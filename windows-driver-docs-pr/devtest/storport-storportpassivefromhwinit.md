---
title: StorPortPassiveFromHwInit rule (storport)
description: StorPortEnablePassiveInitialization should not be called within the HW Initialization entry point for Storport drivers if the HW Initialization entry point can be called directly from the HW Adapter Control entry point.
ms.assetid: F6AD52D5-4964-4406-AF5F-2820273D337C
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["StorPortPassiveFromHwInit rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortPassiveFromHwInit
api_type:
- NA
---

# StorPortPassiveFromHwInit rule (storport)


**StorPortEnablePassiveInitialization** should not be called within the HW Initialization entry point for Storport drivers if the HW Initialization entry point can be called directly from the HW Adapter Control entry point.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortPassiveFromHwInit</strong> rule.</p>
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
 

 





