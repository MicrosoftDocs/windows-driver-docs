---
title: CriticalRegions rule (wdm)
description: The CriticalRegions rule specifies that the driver must call KeEnterCriticalRegion before calling KeLeaveCriticalRegion and that the driver calls KeLeaveCriticalRegion before any subsequent calls to KeEnterCriticalRegion. (Nested calls are permitted.).
ms.assetid: 5976e24b-ca1c-440e-97c8-ccc2015d1172
ms.author: windowsdriverdev
ms.date: 5/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["CriticalRegions rule (wdm)"]
topic_type:
- apiref
api_name:
- CriticalRegions
api_type:
- NA
---

# CriticalRegions rule (wdm)


The **CriticalRegions** rule specifies that the driver must call [**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021) before calling [**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964) and that the driver calls **KeLeaveCriticalRegion** before any subsequent calls to **KeEnterCriticalRegion**. (Nested calls are permitted.)

This rule also specifies that the driver calls **KeLeaveCriticalRegion** to re-enable delivery of normal kernel asynchronous procedure calls (APCs) before it returns.

The WDK documentation of **KeEnterCriticalRegion** and **KeLeaveCriticalRegion** explains that the caller of these functions can be running at IRQL&lt;=APC\_LEVEL. In this situation, this rule enforces a best practice recommendation.

|              |     |
|--------------|-----|
| Driver model | WDM |

|                                   |                                                                                                                                       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187) (0x00040003) |

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
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>CriticalRegions</strong> rule.</p>
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

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At run time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) and select the [DDI compliance checking (additional)](https://msdn.microsoft.com/library/windows/hardware/hh454208#ddi-compliance-checking-additional) option.</p></td>
</tr>
</tbody>
</table>

 

Applies to
----------

[**ExEnterCriticalRegionAndAcquireResourceExclusive**](https://msdn.microsoft.com/library/windows/hardware/dn308550)
[**ExReleaseResourceAndLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/dn308551)
[**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021)
[**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964)
 

 





