---
title: DDI usage rule set (WDM)
description: Use these rules to verify that your driver correctly uses WDM DDIs correctly.
ms.date: 10/21/2020
ms.localizationpriority: medium
---

# DDI usage rule set (WDM)


Use these rules to verify that your driver correctly uses WDM DDIs correctly.

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
<td align="left"><p><a href="wdm-debugbreakusage.md" data-raw-source="[&lt;strong&gt;DebugBreakUsage&lt;/strong&gt;](wdm-debugbreakusage.md)"><strong>DebugBreakUsage</strong></a></p></td>
<td align="left"><p>The <a href="wdm-debugbreakusage.md" data-raw-source="[&lt;strong&gt;DebugBreakUsage&lt;/strong&gt;](wdm-debugbreakusage.md)"><strong>DebugBreakUsage</strong></a> rule specifies that the driver must not call <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgbreakpoint" data-raw-source="[&lt;strong&gt;DbgBreakPoint&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgbreakpoint)"><strong>DbgBreakPoint</strong></a> or <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgbreakpointwithstatus" data-raw-source="[&lt;strong&gt;DbgBreakPointWithStatus&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-dbgbreakpointwithstatus)"><strong>DbgBreakPointWithStatus</strong></a>. This rule only applies when you are building a non-debug version of the driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-doublefetch.md" data-raw-source="[&lt;strong&gt;DoubleFetch&lt;/strong&gt;](wdm-doublefetch.md)"><strong>DoubleFetch</strong></a></p></td>
<td align="left"><p>The <a href="wdm-doublefetch.md" data-raw-source="[&lt;strong&gt;DoubleFetch&lt;/strong&gt;](wdm-doublefetch.md)"><strong>DoubleFetch</strong></a> rule checks for double fetch from user mode memory pointers. Double kernel mode accesses of user mode memory can lead to a race condition security issue. When accessing user mode data, kernel mode code needs to make a copy of the user mode data locally and avoid accessing the user mode data multiple times. Failing to do so results in a type of problem known as a “double fetch”, where the data may change after it was first accessed.</p>
</td>
</tr>
<tr class="odd">
<td align="left"><p><a href="nullcheckw.md" data-raw-source="[&lt;strong&gt;NullCheck&lt;/strong&gt;](nullcheckw.md)"><strong>NullCheck</strong></a></p></td>
<td align="left"><p>The <a href="nullcheckw.md" data-raw-source="[&lt;strong&gt;NullCheck&lt;/strong&gt;](nullcheckw.md)"><strong>NullCheck</strong></a> rule verifies that a NULL value inside the driver code is not dereferenced later in the driver. This rule reports a defect if either of these conditions is true:</p>
<ul>
<li>There is an assignment of NULL that is dereferenced later.</li>
<li>There is a global/parameter to a procedure in a driver that may be NULL that is dereferenced later, and there is an explicit check in the driver that suggests that the initial value of the pointer may be NULL.</li>
</ul>
<p>With NullCheck rule violations, the most relevant code statements are highlighted in the trace tree pane. For more information about working with report output, see <a href="/windows-hardware/drivers/devtest/static-driver-verifier-report" data-raw-source="[Static Driver Verifier Report](./static-driver-verifier-report.md)">Static Driver Verifier Report</a> and <a href="/windows-hardware/drivers/devtest/understanding-the-defect-viewer" data-raw-source="[Understanding the Trace Viewer](./understanding-the-defect-viewer.md)">Understanding the Trace Viewer</a>.</p>
<p></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wdm-safestrings.md" data-raw-source="[&lt;strong&gt;SafeStrings&lt;/strong&gt;](wdm-safestrings.md)"><strong>SafeStrings</strong></a></p></td>
<td align="left"><p>The <a href="wdm-safestrings.md" data-raw-source="[&lt;strong&gt;SafeStrings&lt;/strong&gt;](wdm-safestrings.md)"><strong>SafeStrings</strong></a> rule specifies that the driver calls only those string manipulations functions that protect the system from unintentional or malicious intrusion. These safe string functions for drivers are defined in Ntstrsafe.h.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="wdm-obsoleteddis.md" data-raw-source="[&lt;strong&gt;ObsoleteDDIs&lt;/strong&gt;](wdm-obsoleteddis.md)"><strong>ObsoleteDDIs</strong></a></p></td>
<td align="left"><p>The <a href="wdm-obsoleteddis.md" data-raw-source="[&lt;strong&gt;ObsoleteDDIs&lt;/strong&gt;](wdm-obsoleteddis.md)"><strong>ObsoleteDDIs</strong></a> rule specifies that drivers should not call <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlprivatelock" data-raw-source="[&lt;strong&gt;FsRtlPrivateLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlprivatelock)"><strong>FsRtlPrivateLock</strong></a>. This function is obsolete. Use <a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlfastlock" data-raw-source="[&lt;strong&gt;FsRtlFastLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlfastlock)"><strong>FsRtlFastLock</strong></a> instead.</p></td>
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

