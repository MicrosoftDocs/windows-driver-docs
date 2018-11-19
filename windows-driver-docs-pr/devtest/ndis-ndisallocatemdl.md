---
title: NdisAllocateMdl rule (ndis)
description: The NdisAllocateMdl rule specifies that NdisAllocateMdl and NdisFreeMdl are called in alternate order. The ultimate goal is to make sure all MDLs are freed when MiniportHaltEx ends.
ms.assetid: 8146E72B-0B63-4224-9677-5E6FEFCEB745
ms.date: 05/21/2018
keywords: ["NdisAllocateMdl rule (ndis)"]
topic_type:
- apiref
api_name:
- NdisAllocateMdl
api_type:
- NA
ms.localizationpriority: medium
---

# NdisAllocateMdl rule (ndis)


The **NdisAllocateMdl** rule specifies that [**NdisAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff561605) and [**NdisFreeMdl**](https://msdn.microsoft.com/library/windows/hardware/ff562575) are called in alternate order. The ultimate goal is to make sure all MDLs are freed when [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) ends.

The rule uses three different states. The state changes when an MDL is allocated or freed. If an MDL is still allocated when the [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) exits, the rule reports the defect.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>NdisAllocateMdl</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh454281" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
</tr>
</tbody>
</table>

Applies to
----------

[**NdisAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff561605)
[**NdisFreeMdl**](https://msdn.microsoft.com/library/windows/hardware/ff562575)
 

 





