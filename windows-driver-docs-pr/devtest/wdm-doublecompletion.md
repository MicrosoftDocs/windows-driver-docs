---
title: DoubleCompletion rule (wdm)
description: The DoubleCompletion (WDM) rule specifies that the driver must not call the IoCompleteRequest routine twice for the same IRP.
ms.assetid: 68e912f4-08fa-49e3-bc76-b997e6f732c4
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["DoubleCompletion rule (wdm)"]
topic_type:
- apiref
api_name:
- DoubleCompletion
api_type:
- NA
---

# DoubleCompletion rule (wdm)


The **DoubleCompletion (WDM)** rule specifies that the driver must not call the [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) routine twice for the same IRP.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>DoubleCompletion</strong> rule.</p>
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

[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)
[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
 

 





