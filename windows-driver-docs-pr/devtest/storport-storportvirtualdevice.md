---
title: StorPortVirtualDevice rule (storport)
description: This rule verifies that upon exit from the HwStorFindAdapter routine, the VirtualDevice field in the PORT\_CONFIGURATION\_INFORMATION (Storport) structure has been set to FALSE. The rule applies only to physical StorPort miniports.
ms.assetid: AC0550F8-117B-4942-8F8B-E7FE71D5AF71
ms.date: 05/21/2018
keywords: ["StorPortVirtualDevice rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortVirtualDevice
api_type:
- NA
ms.localizationpriority: medium
---

# StorPortVirtualDevice rule (storport)


This rule verifies that upon exit from the [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine, the **VirtualDevice** field in the [**PORT\_CONFIGURATION\_INFORMATION (Storport)**](https://msdn.microsoft.com/library/windows/hardware/ff563901) structure has been set to **FALSE**. The rule applies only to physical StorPort miniports.

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortVirtualDevice</strong> rule.</p>
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

 

 





