---
title: CriticalRegions rule (wdm)
description: The CriticalRegions rule specifies that the driver must call KeEnterCriticalRegion before calling KeLeaveCriticalRegion and that the driver calls KeLeaveCriticalRegion before any subsequent calls to KeEnterCriticalRegion. (Nested calls are permitted.).
ms.assetid: 5976e24b-ca1c-440e-97c8-ccc2015d1172
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
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20CriticalRegions%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




