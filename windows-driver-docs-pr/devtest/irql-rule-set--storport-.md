---
title: Irql rule set (Storport)
description: Use these rules to verify that your driver makes DDI calls at the required IRQL.A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.
ms.assetid: 3322200A-2073-4568-B1FC-481B216D8F61
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Irql rule set (Storport)


Use these rules to verify that your driver makes DDI calls at the required IRQL.

A driver that does not follow the IRQL rules can cause serious problems during operation that can lead to deadlock conditions or computer crashes.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="storport-irqldispatch.md" data-raw-source="[&lt;strong&gt;IrqlDispatch&lt;/strong&gt;](storport-irqldispatch.md)"><strong>IrqlDispatch</strong></a></p></td>
<td align="left"><p>This rule verifies that the following routines are only called at <strong>IRQL = DISPATCH_LEVEL</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-irqlkereleasespinlock.md" data-raw-source="[&lt;strong&gt;IrqlKeReleaseSpinLock&lt;/strong&gt;](storport-irqlkereleasespinlock.md)"><strong>IrqlKeReleaseSpinLock</strong></a></p></td>
<td align="left"><p>This rule verifies that <strong>KeReleaseSpinLock</strong> is called at <strong>IRQL = DISPATCH_LEVEL</strong> only. It must also set the IRQL to the previous IRQL level. Typically this call would be preceded by a call to <strong>KeAcquireSpinLock</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-spchangeirql.md" data-raw-source="[&lt;strong&gt;SpChangeIrql&lt;/strong&gt;](storport-spchangeirql.md)"><strong>SpChangeIrql</strong></a></p></td>
<td align="left"><p>This rule verifies that the StorPort callback routines return at the same IRQL level as the level at which they are called.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-spirql.md" data-raw-source="[&lt;strong&gt;SpIrql&lt;/strong&gt;](storport-spirql.md)"><strong>SpIrql</strong></a></p></td>
<td align="left"><p>This rule verifies that the routines <strong>TdiRegisterPnPHandlers</strong> and <strong>TdiDeregisterPnPHandlers</strong> are only called at IRQL lower than <strong>DISPATCH_LEVEL</strong>. However, if <strong>ExFreeToNPagedLookasideList</strong> is called, the rule passes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-storportirql.md" data-raw-source="[&lt;strong&gt;StorPortIrql&lt;/strong&gt;](storport-storportirql.md)"><strong>StorPortIrql</strong></a></p></td>
<td align="left"><p>The <a href="storport-storportirql.md" data-raw-source="[&lt;strong&gt;StorPortIrql&lt;/strong&gt;](storport-storportirql.md)"><strong>StorPortIrql</strong></a> rule checks that StorPort routines are called at the correct IRQL levels.</p></td>
</tr>
</tbody>
</table>

 

**To select the Irql rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Irql**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Irql.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Irql.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





