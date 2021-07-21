---
title: IrqlExPassive rule (wdm)
description: The IrqlExPassive rule specifies that the driver calls the following executive support routines only at IRQL PASSIVE_LEVEL. The IrqlExPassive rule also specifies that the driver calls ExRaiseStatus at IRQL APC_LEVEL.
ms.date: 05/21/2018
keywords: ["IrqlExPassive rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlExPassive
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlExPassive rule (wdm)


The **IrqlExPassive** rule specifies that the driver calls the following executive support routines only at IRQL = PASSIVE\_LEVEL:

-   [**ExCreateCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-excreatecallback)

-   [**ExIsProcessorFeaturePresent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exisprocessorfeaturepresent)

-   [**ExRaiseAccessViolation**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exraiseaccessviolation)

-   [**ExRaiseDatatypeMisalignment**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exraisedatatypemisalignment)

-   [**ExRaiseStatus**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exraisestatus)

-   [**ExUuidCreate**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exuuidcreate)

The **IrqlExPassive** rule also specifies that the driver calls [**ExRaiseStatus**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exraisestatus) at IRQL &lt;= APC\_LEVEL.

**Driver model: WDM**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x00020008), [**Bug Check 0xA: IRQL\_NOT\_LESS\_OR\_EQUAL**](../debugger/bug-check-0xa--irql-not-less-or-equal.md)


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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>IrqlExPassive</strong> rule.</p>
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

[**ExCreateCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-excreatecallback)
[**ExIsProcessorFeaturePresent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exisprocessorfeaturepresent)
[**ExRaiseAccessViolation**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exraiseaccessviolation)
[**ExRaiseDatatypeMisalignment**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exraisedatatypemisalignment)
[**ExRaiseStatus**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exraisestatus)
[**ExUuidCreate**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exuuidcreate)
## See also

[**Managing Hardware Priorities**](../kernel/managing-hardware-priorities.md)
[**Preventing Errors and Deadlocks While Using Spin Locks**](../kernel/preventing-errors-and-deadlocks-while-using-spin-locks.md)
