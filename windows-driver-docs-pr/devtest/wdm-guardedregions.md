---
title: GuardedRegions rule (wdm)
description: The GuardedRegions rule verifies that calls to KeEnterGuardedRegion and KeLeaveGuardedRegion are used in strict alternation.
ms.date: 05/21/2018
keywords: ["GuardedRegions rule (wdm)"]
topic_type:
- apiref
api_name:
- GuardedRegions
api_type:
- NA
ms.localizationpriority: medium
---

# GuardedRegions rule (wdm)


The **GuardedRegions** rule verifies that calls to [**KeEnterGuardedRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keenterguardedregion) and [**KeLeaveGuardedRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleaveguardedregion) are used in strict alternation.

Each call to [**KeEnterGuardedRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keenterguardedregion) must have a matching call to [**KeLeaveGuardedRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleaveguardedregion).

**Driver model: WDM**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x0004000E)


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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>GuardedRegions</strong> rule.</p>
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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/driver-verifier" data-raw-source="[Driver Verifier](./driver-verifier.md)">Driver Verifier</a> and select the <a href="/windows-hardware/drivers/devtest/ddi-compliance-checking" data-raw-source="[DDI compliance checking](./ddi-compliance-checking.md)">DDI compliance checking</a> option.</p></td>
</tr>
</tbody>
</table>

 

## Applies to

[**KeEnterGuardedRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keenterguardedregion)
[**KeLeaveGuardedRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleaveguardedregion)
## See also

[Critical Regions and Guarded Regions](../kernel/critical-regions-and-guarded-regions.md)
