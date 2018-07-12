---
title: EvtIoStopGetParam rule (kmdf)
description: The EvtIoStopGetParam rule checks that WdfRequestGetParameters is not called within EvtIoStop callback.
ms.assetid: 4693DA4D-2298-45C3-8F07-24C861DD85BB
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["EvtIoStopGetParam rule (kmdf)"]
topic_type:
- apiref
api_name:
- EvtIoStopGetParam
api_type:
- NA
---

# EvtIoStopGetParam rule (kmdf)


The **EvtIoStopGetParam** rule checks that [**WdfRequestGetParameters**](https://msdn.microsoft.com/library/windows/hardware/ff549969) is not called within [*EvtIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541788) callback.

|              |      |
|--------------|------|
| Driver model | KMDF |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>EvtIoStopGetParam</strong> rule.</p>
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

[**WdfRequestGetParameters**](https://msdn.microsoft.com/library/windows/hardware/ff549969)
 

 





