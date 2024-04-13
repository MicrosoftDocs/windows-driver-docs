---
title: DDI Usage Rule Set (Storport)
description: Use these rules to verify that your driver correctly uses Storport DDIs correctly.
ms.date: 05/21/2018
---

# DDI usage rule set (Storport)


Use these rules to verify that your driver correctly uses Storport DDIs correctly.

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
<td align="left"><p><a href="storport-hwstorportprohibitedddis.md" data-raw-source="[&lt;strong&gt;HwStorPortProhibitedDDIs&lt;/strong&gt;](storport-hwstorportprohibitedddis.md)"><strong>HwStorPortProhibitedDDIs</strong></a></p></td>
<td align="left"><p>This rule contains a list of WDM DDIs (excluding interlocked functions) that should not be called in physical StorPort miniport drivers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="nullchecks.md" data-raw-source="[&lt;strong&gt;NullCheck&lt;/strong&gt;](nullchecks.md)"><strong>NullCheck</strong></a></p></td>
<td align="left"><p>The NullCheck rule verifies that a NULL value inside the driver code is not dereferenced later in the driver. This rule reports a defect if either of these conditions is true:</p>
<ul>
<li>There is an assignment of NULL that is dereferenced later.</li>
<li>There is a global/parameter to a procedure in a driver that may be NULL that is dereferenced later, and there is an explicit check in the driver that suggests that the initial value of the pointer may be NULL.</li>
</ul>
<p>With NullCheck rule violations, the most relevant code statements are highlighted in the trace tree pane. For more information about working with report output, see <a href="/windows-hardware/drivers/devtest/static-driver-verifier-report" data-raw-source="[Static Driver Verifier Report](./static-driver-verifier-report.md)">Static Driver Verifier Report</a> and <a href="/windows-hardware/drivers/devtest/understanding-the-defect-viewer" data-raw-source="[Understanding the Trace Viewer](./understanding-the-defect-viewer.md)">Understanding the Trace Viewer</a>.</p>
<p></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-storportddisportonly.md" data-raw-source="[&lt;strong&gt;StorPortDDIsPortOnly&lt;/strong&gt;](storport-storportddisportonly.md)"><strong>StorPortDDIsPortOnly</strong></a></p></td>
<td align="left"><p>This rule contains a list of StorPort port-only DDIs (excluding interlocked functions) that should not be called in StorPort miniports.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-storportdeprecated.md" data-raw-source="[&lt;strong&gt;StorPortDeprecated&lt;/strong&gt;](storport-storportdeprecated.md)"><strong>StorPortDeprecated</strong></a></p></td>
<td align="left"><p>This rule verifies that the driver does not call either of these deprecated routines: <strong>StorPortValidateRange</strong> or <strong>StorPortLogError</strong>.</p></td>
</tr>
</tbody>
</table>

 

**To select the DDI usage rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **DDIUsage**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **DDIUsage.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:DDIUsage.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md) and [Static Driver Verifier commands (MSBuild)](./-static-driver-verifier-commands--msbuild-.md).

