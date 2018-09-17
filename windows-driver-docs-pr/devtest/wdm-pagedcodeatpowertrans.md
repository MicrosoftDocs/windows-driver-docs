---
title: PagedCodeAtPowerTrans rule (wdm)
description: The PagedCodeAtPowerTrans rule specifies that a driver should not call PAGED\_CODE while responding to a system IRP\_MJ\_POWER Irp (IRP\_MN\_SET\_POWER) and to a device IRP\_MJ\_POWER Irp (IRP\_MN\_SET\_POWER).
ms.assetid: D94B0E13-9640-4FBF-B1E7-AF8DFED42542
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["PagedCodeAtPowerTrans rule (wdm)"]
topic_type:
- apiref
api_name:
- PagedCodeAtPowerTrans
api_type:
- NA
ms.localizationpriority: medium
---

# PagedCodeAtPowerTrans rule (wdm)


The **PagedCodeAtPowerTrans** rule specifies that a driver should not call [**PAGED\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff558773) while responding to a system IRP\_MJ\_POWER Irp (IRP\_MN\_SET\_POWER) and to a device IRP\_MJ\_POWER Irp (IRP\_MN\_SET\_POWER).

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>PagedCodeAtPowerTrans</strong> rule.</p>
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

[**PAGED\_CODE**](https://msdn.microsoft.com/library/windows/hardware/ff558773)
 

 





