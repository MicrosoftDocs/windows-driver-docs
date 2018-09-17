---
title: DebugBreakUsage rule (wdm)
description: The DebugBreakUsage rule specifies that the driver must not call DbgBreakPoint or DbgBreakPointWithStatus. This rule only applies when you are building a non-debug version of the driver.
ms.assetid: 1f634b7c-6939-41ea-8eed-5207f40e5476
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["DebugBreakUsage rule (wdm)"]
topic_type:
- apiref
api_name:
- DebugBreakUsage
api_type:
- NA
ms.localizationpriority: medium
---

# DebugBreakUsage rule (wdm)


The **DebugBreakUsage** rule specifies that the driver must not call [**DbgBreakPoint**](https://msdn.microsoft.com/library/windows/hardware/ff543626) or [**DbgBreakPointWithStatus**](https://msdn.microsoft.com/library/windows/hardware/ff543629). This rule only applies when you are building a non-debug version of the driver.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DebugBreakUsage</strong> rule.</p>
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

 

 





