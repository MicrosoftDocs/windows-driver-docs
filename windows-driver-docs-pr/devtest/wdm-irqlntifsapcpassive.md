---
title: IrqlNtifsApcPassive rule (wdm)
description: The IrqlNtifsApcPassive rule specifies that the driver calls the DDIs listed in the rule only when it is executing either at IRQL = PASSIVE_LEVEL or at IRQL <= APC_LEVEL.
ms.date: 04/03/2020
keywords: ["IrqlNtifsApcPassive rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlNtifsApcPassive
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlNtifsApcPassive rule (wdm)

The **IrqlNtifsApcPassive** rule specifies that the driver calls the DDIs listed in the rule only when it is executing either at IRQL = PASSIVE_LEVEL or at IRQL <= APC_LEVEL.

**Driver model: WDM**

**Bug check(s) found with this rule**: [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md) (0x20024)


## Example

The following code violates this rule:

```cpp
//
// KeAcquireSpinLock raises the IRQL to DISPATCH_LEVEL.
//

KeAcquireSpinLock (&Lock, &OldIrql);

//
// ERROR: ZwWriteFile can only be called at IRQL == PASSIVE_LEVEL.
//

ZwWriteFile (Handle,
             NULL,
             NULL,
             NULL,
             IoStatusBlock,
             Buffer,
             BufferLength,
             NULL,
             NULL);

KeReleaseSpinLock (&Lock, OldIrql);
```

For more information about IRQL levels, see [Dispatch Routines and IRQLs](../kernel/dispatch-routines-and-irqls.md) and [Managing Hardware Priorities](../kernel/managing-hardware-priorities.md).

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
<td align="left"><p>Run <a href="/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](./static-driver-verifier.md)">Static Driver Verifier</a> and specify the <strong>IrqlNtifsApcPassive</strong> rule.</p>
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
<td align="left">
<p>You can activate the DDI Compliance - Additional IRQL rules for one or more drivers by using the Verifier.exe command line. For details, see <a href="/windows-hardware/drivers/devtest/selecting-driver-verifier-options" data-raw-source="[Selecting Driver Verifier Options](./ddi-compliance-checking.md)">Selecting Driver Verifier Options</a>. You must restart the computer to activate or deactivate the DDI Compliance - Additional IRQL rules.</p>
<p>At the command line, DDI Compliance - Additional IRQL checking is represented by a rule class value of 35. For example:</p>
<p><code>verifier /ruleclasses 35 /driver MyDriver.sys</code></p>
<p>OR</p>
<p><code>verifier /rc 35 /driver MyDriver.sys</code></p>
<p>The additional IRQL checking will be active after the PC is rebooted.</p>
</td>
</tr>
</tbody>
</table>

## Applies to

NtSetInformationFile

NtWriteFile

NtCreateFile

ZwWriteFile

CcCopyWrite

CcCopyWriteEx

CcDeferWrite

CcFastCopyWrite
