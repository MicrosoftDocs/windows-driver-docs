---
title: IrqlIoRtlZwPassive rule (wdm)
description: The IrqlIoRtlZwPassive rule specifies that the driver calls the DDIs listed in the rule only when it is executing at IRQL = PASSIVE_LEVEL.
ms.assetid: 9BAE267F-CA57-4743-8C8D-08716C134E16
ms.date: 04/03/2020
keywords: ["IrqlIoRtlZwPassive rule (wdm)"]
topic_type:
- apiref
api_name:
- IrqlIoRtlZwPassive
api_type:
- NA
ms.localizationpriority: medium
---

# IrqlIoRtlZwPassive rule (wdm)

The **IrqlIoRtlZwPassive** rule specifies that the driver calls the DDIs listed in the rule only when it is executing at IRQL = PASSIVE_LEVEL.

This rule augments the DDI Compliance Checking IRQL rules for PASSIVE_LEVEL. For more information, see [Irql rule set (WDM)](https://docs.microsoft.com/windows-hardware/drivers/devtest/irql-rule-set--wdm-).

**Driver model: WDM**

|                                   |                                                                                                                                    |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Bug check(s) found with this rule | [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://docs.microsoft.com/windows-hardware/drivers/debugger/bug-check-0xc4--driver-verifier-detected-violation) (0x20023) |

Example
-------

The following code violates this rule:

```cpp
//
// KeAcquireSpinLock raises the IRQL to DISPATCH_LEVEL.
//

KeAcquireSpinLock (&Lock, &OldIrql);

//
// ERROR: IoGetDriverDirectory can only be called at IRQL == PASSIVE_LEVEL.
//

IoGetDriverDirectory (DriverObject,
                      DriverDirectoryData,
                      0,
                      &DirectoryHandle);

KeReleaseSpinLock (&Lock, OldIrql);
```

For more information about IRQL levels, see [Dispatch Routines and IRQLs](https://docs.microsoft.com/windows-hardware/drivers/kernel/dispatch-routines-and-irqls) and [Managing Hardware Priorities](https://docs.microsoft.com/windows-hardware/drivers/kernel/managing-hardware-priorities).

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
<td align="left"><p>Run <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier" data-raw-source="[Static Driver Verifier](https://docs.microsoft.com/windows-hardware/drivers/devtest/static-driver-verifier)">Static Driver Verifier</a> and specify the <strong>IrqlIoRtlZwPassive</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code" data-raw-source="[Prepare your code (use role type declarations).](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#preparing-your-source-code)">Prepare your code (use role type declarations).</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier" data-raw-source="[Run Static Driver Verifier.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#running-static-driver-verifier)">Run Static Driver Verifier.</a></li>
<li><a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results" data-raw-source="[View and analyze the results.](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers#viewing-and-analyzing-the-results)">View and analyze the results.</a></li>
</ol>
<p>For more information, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers" data-raw-source="[Using Static Driver Verifier to Find Defects in Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/using-static-driver-verifier-to-find-defects-in-drivers)">Using Static Driver Verifier to Find Defects in Drivers</a>.</p></td>
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
<p>You can activate the DDI Compliance - Additional IRQL rules for one or more drivers by using the Verifier.exe command line. For details, see <a href="https://docs.microsoft.com/windows-hardware/drivers/devtest/selecting-driver-verifier-options" data-raw-source="[Selecting Driver Verifier Options](https://docs.microsoft.com/windows-hardware/drivers/devtest/ddi-compliance-checking)">Selecting Driver Verifier Options</a>. You must restart the computer to activate or deactivate the DDI Compliance - Additional IRQL rules.</p>
<p>At the command line, DDI Compliance - Additional IRQL checking is represented by a rule class value of 35. For example:</p>
<p><code>verifier /ruleclasses 35 /driver MyDriver.sys</code></p>
<p>OR</p>
<p><code>verifier /rc 35 /driver MyDriver.sys</code></p>
<p>The additional IRQL checking will be active after the PC is rebooted.</p>
</td>
</tr>
</tbody>
</table>

Applies to
----------

  IoCreateFileEx

  IoCreateFileSpecifyDeviceObjectHint

  IoGetDeviceDirectory

  IoGetDriverDirectory

  IoOpenDeviceInterfaceRegistryKey

  IoOpenDeviceRegistryKey

  RtlCreateRegistryKey

  RtlCreateSystemVolumeInformationFolder

  RtlWriteRegistryValue

  ZwCreateDirectoryObject

  ZwCreateFile

  ZwCreateKeyTransacted

  ZwDeleteFile

  ZwDeleteValueKey

  ZwFlushBuffersFileEx
  
  ZwFlushBuffersFile
  
  ZwRenameKey

  ZwSetEaFile

  ZwSetInformationFile

  ZwSetInformationKey