---
title: StorPortVirtualDevice2 rule (storport)
description: This rule verifies that upon exit from the HwStorFindAdapter routine, the VirtualDevice field in the PORT\_CONFIGURATION\_INFORMATION (Storport) structure has been set to TRUE. The rule applies only to virtual StorPort miniports.
ms.assetid: CBD1FAD0-9D85-4989-9CCA-00F5698F5383
ms.date: 05/21/2018
keywords: ["StorPortVirtualDevice2 rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortVirtualDevice2
api_type:
- NA
ms.localizationpriority: medium
---

# StorPortVirtualDevice2 rule (storport)


This rule verifies that upon exit from the [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine, the **VirtualDevice** field in the [**PORT\_CONFIGURATION\_INFORMATION (Storport)**](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure has been set to **TRUE**. The rule applies only to virtual StorPort miniports.

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
<td align="left"><p>Run <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and specify the <strong>StorPortVirtualDevice2</strong> rule.</p>
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

 

 





