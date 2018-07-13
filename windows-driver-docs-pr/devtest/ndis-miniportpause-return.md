---
title: MiniportPause\_Return rule (ndis)
description: The MiniportPause\_Return rule specifies that the MiniportPause callback function should return only NDIS\_STATUS\_SUCCESS if the pause operation is complete, or NDIS\_STATUS\_PENDING if the miniport driver is in the pausing state.
ms.assetid: f3751636-6ba2-4126-88e2-1f347bd7dd45
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["MiniportPause_Return rule (ndis)"]
topic_type:
- apiref
api_name:
- MiniportPause_Return
api_type:
- NA
---

# MiniportPause\_Return rule (ndis)


The **MiniportPause\_Return** rule specifies that the [*MiniportPause*](https://msdn.microsoft.com/library/windows/hardware/ff559418) callback function should return only NDIS\_STATUS\_SUCCESS if the pause operation is complete, or NDIS\_STATUS\_PENDING if the miniport driver is in the pausing state. Any other returned status is invalid.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>MiniportPause_Return</strong> rule.</p>
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

 

 





