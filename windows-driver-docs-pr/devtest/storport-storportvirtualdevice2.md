---
title: StorPortVirtualDevice2 rule (storport)
description: This rule verifies that upon exit from the HwStorFindAdapter routine, the VirtualDevice field in the PORT\_CONFIGURATION\_INFORMATION (Storport) structure has been set to TRUE. The rule applies only to virtual StorPort miniports.
ms.assetid: CBD1FAD0-9D85-4989-9CCA-00F5698F5383
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["StorPortVirtualDevice2 rule (storport)"]
topic_type:
- apiref
api_name:
- StorPortVirtualDevice2
api_type:
- NA
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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>StorPortVirtualDevice2</strong> rule.</p>
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

 

 





