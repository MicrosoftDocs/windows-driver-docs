---
title: NdisMDeregisterInterruptEx rule (ndis)
description: After NdisMDeregisterInterruptEx returns control, the miniport driver cannot call the NdisMSynchronizeWithInterruptEx function.
ms.assetid: 49AC090C-157C-4CD2-9C7A-BDD5F3C6D58F
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["NdisMDeregisterInterruptEx rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisMDeregisterInterruptEx
api_type:
- NA
---

# NdisMDeregisterInterruptEx rule (ndis)


After [**NdisMDeregisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575) returns control, the miniport driver cannot call the [**NdisMSynchronizeWithInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563681) function.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NdisMDeregisterInterruptEx</strong> rule.</p>
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

[**NdisMDeregisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563575)
[**NdisMRegisterInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563649)
[**NdisMSynchronizeWithInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff563681)
 

 





