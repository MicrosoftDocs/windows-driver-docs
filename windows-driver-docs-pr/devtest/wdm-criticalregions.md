---
title: CriticalRegions rule (wdm)
description: The CriticalRegions rule specifies that the driver must call KeEnterCriticalRegion before calling KeLeaveCriticalRegion and that the driver calls KeLeaveCriticalRegion before any subsequent calls to KeEnterCriticalRegion. (Nested calls are permitted.).
ms.date: 05/21/2018
keywords: ["CriticalRegions rule (wdm)"]
topic_type:
- apiref
api_name:
- CriticalRegions
api_type:
- NA
ms.localizationpriority: medium
---

# CriticalRegions rule (wdm)


The **CriticalRegions** rule specifies that the driver must call [**KeEnterCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keentercriticalregion) before calling [**KeLeaveCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleavecriticalregion) and that the driver calls **KeLeaveCriticalRegion** before any subsequent calls to **KeEnterCriticalRegion**. (Nested calls are permitted.)

This rule also specifies that the driver calls **KeLeaveCriticalRegion** to re-enable delivery of normal kernel asynchronous procedure calls (APCs) before it returns.

The WDK documentation of **KeEnterCriticalRegion** and **KeLeaveCriticalRegion** explains that the caller of these functions can be running at IRQL&lt;=APC\_LEVEL. In this situation, this rule enforces a best practice recommendation.

**Driver model: WDM**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00040003)


## How to test

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>CriticalRegions</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ddi-compliance-checking#ddi-compliance-checking-additional" data-raw-source="[DDI compliance checking (additional)](./ddi-compliance-checking.md#ddi-compliance-checking-additional)">DDI compliance checking (additional)</a> option.</p></td>
</tr>
</tbody>
</table>

 

## Applies to

[**ExEnterCriticalRegionAndAcquireResourceExclusive**](/previous-versions/windows/hardware/drivers/dn308550(v=vs.85))
[**ExReleaseResourceAndLeaveCriticalRegion**](/previous-versions/windows/hardware/drivers/dn308551(v=vs.85))
[**KeEnterCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keentercriticalregion)
[**KeLeaveCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleavecriticalregion)
