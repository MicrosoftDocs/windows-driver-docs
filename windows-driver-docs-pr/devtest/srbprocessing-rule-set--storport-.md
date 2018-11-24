---
title: SrbProcessing rule set (Storport)
description: Use these rules to verify that your driver correctly processes SRB requests.
ms.assetid: A3BF2AA3-207F-4D74-94B0-6CA215341340
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# SrbProcessing rule set (Storport)


Use these rules to verify that your driver correctly processes SRB requests.

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
<td align="left"><p><a href="storport-spduplex.md" data-raw-source="[&lt;strong&gt;SpDuplex&lt;/strong&gt;](storport-spduplex.md)"><strong>SpDuplex</strong></a></p></td>
<td align="left"><p>This rule verifies that this miniport is in <strong>Full Duplex</strong> mode. Any driver built according to the StorPort-miniport model must be in <strong>Full Duplex</strong> mode. <strong>Half Duplex</strong> should only be used when porting an existing SCSI driver to StorPort.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-spnowait.md" data-raw-source="[&lt;strong&gt;SpNoWait&lt;/strong&gt;](storport-spnowait.md)"><strong>SpNoWait</strong></a></p></td>
<td align="left"><p>This rule verifies that waits or data allocation are not performed inside <strong>StartIo</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-spreturnvalue.md" data-raw-source="[&lt;strong&gt;SpReturnValue&lt;/strong&gt;](storport-spreturnvalue.md)"><strong>SpReturnValue</strong></a></p></td>
<td align="left"><p>This rule verifies that the driver&#39;s implementations of <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390" data-raw-source="[&lt;strong&gt;HwStorFindAdapter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557390)"><strong>HwStorFindAdapter</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff568008" data-raw-source="[&lt;strong&gt;VirtualHwStorFindAdapter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568008)"><strong>VirtualHwStorFindAdapter</strong></a> return a valid status. A valid status is one of the following: <strong>SP_RETURN_FOUND</strong>, <strong>SP_RETURN_ERROR</strong>, <strong>SP_RETURN_BAD_CONFIG</strong>, or <strong>SP_RETURN_NOT_FOUND</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storportallocatepool.md" data-raw-source="[&lt;strong&gt;StorPortAllocatePool&lt;/strong&gt;](storportallocatepool.md)"><strong>StorPortAllocatePool</strong></a></p></td>
<td align="left"><p>This rule verifies that the miniport must not attempt to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff567065" data-raw-source="[&lt;strong&gt;StorPortFreePool&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567065)"><strong>StorPortFreePool</strong></a> on an deallocated buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-storportallocatepool2.md" data-raw-source="[&lt;strong&gt;StorPortAllocatePool2&lt;/strong&gt;](storport-storportallocatepool2.md)"><strong>StorPortAllocatePool2</strong></a></p></td>
<td align="left"><p>This rule verifies that the miniport must not attempt to call <a href="https://msdn.microsoft.com/library/windows/hardware/ff567031" data-raw-source="[&lt;strong&gt;StorPortAllocatePool&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567031)"><strong>StorPortAllocatePool</strong></a> on an allocated buffer without deallocating it first.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-storportbuildio.md" data-raw-source="[&lt;strong&gt;StorPortBuildIo&lt;/strong&gt;](storport-storportbuildio.md)"><strong>StorPortBuildIo</strong></a></p></td>
<td align="left"><p>This rule verifies that if the StorPort miniport&#39;s <a href="storport-storportbuildio.md" data-raw-source="[&lt;strong&gt;StorPortBuildIo&lt;/strong&gt;](storport-storportbuildio.md)"><strong>StorPortBuildIo</strong></a> routine returns <strong>FALSE</strong>, the SRB in question is not passed to <strong>StartIo</strong>. (In such cases, the miniport driver must complete the SRB by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff567433" data-raw-source="[&lt;strong&gt;StorPortNotification&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567433)"><strong>StorPortNotification</strong></a> with a notification type of <strong>RequestComplete</strong> from <strong>StorPortBuildIo</strong> or someplace else).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-storportcompleterequest.md" data-raw-source="[&lt;strong&gt;StorPortCompleteRequest&lt;/strong&gt;](storport-storportcompleterequest.md)"><strong>StorPortCompleteRequest</strong></a></p></td>
<td align="left"><p>This rule verifies that no calls to <strong>StorPortCompleteRequest</strong> are made by the miniport. Usage of the <strong>StorPortCompleteRequest</strong> is not recommended; miniports should instead call <strong>StorPortNotification</strong> with <strong>notificationType = RequestComplete</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-storportenablepassive.md" data-raw-source="[&lt;strong&gt;StorPortEnablePassive&lt;/strong&gt;](storport-storportenablepassive.md)"><strong>StorPortEnablePassive</strong></a></p></td>
<td align="left"><p>This rule verifies that <strong>StorPortEnablePassiveInitialization</strong> is not called from any StorPort miniport driver routine other than <strong>HwInitialize</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-storportfindadapter.md" data-raw-source="[&lt;strong&gt;StorPortFindAdapter&lt;/strong&gt;](storport-storportfindadapter.md)"><strong>StorPortFindAdapter</strong></a></p></td>
<td align="left"><p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff557390" data-raw-source="[&lt;strong&gt;HwStorFindAdapter&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557390)"><strong>HwStorFindAdapter</strong></a> routine must set the <strong>MaximumTransferLength</strong> and the <strong>NumberOfPhysicalBreaks</strong> fields in the <strong>PORT_CONFIGURATION_INFORMATION</strong> structure. By default, the value of both these fields is <strong>SP_UNINITIALIZED_VALUE</strong>. If either of these fields is still set to <strong>SP_UNINITIALIZED_VALUE</strong> upon exit from <strong>FindAdapter</strong>, the driver fails the rule.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-storportnotification2.md" data-raw-source="[&lt;strong&gt;StorPortNotification2&lt;/strong&gt;](storport-storportnotification2.md)"><strong>StorPortNotification2</strong></a></p></td>
<td align="left"><p>This rule verifies that calls to <strong>StorPortNotification</strong> use only allowed (i.e. documented) notification types.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-storportpassivefromhwinit.md" data-raw-source="[&lt;strong&gt;StorPortPassiveFromHwInit&lt;/strong&gt;](storport-storportpassivefromhwinit.md)"><strong>StorPortPassiveFromHwInit</strong></a></p></td>
<td align="left"><p><strong>StorPortEnablePassiveInitialization</strong> should not be called within the HW Initialization entry point for Storport drivers if the HW Initialization entry point can be called directly from the HW Adapter Control entry point.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-storportperfopts.md" data-raw-source="[&lt;strong&gt;StorPortPerfOpts&lt;/strong&gt;](storport-storportperfopts.md)"><strong>StorPortPerfOpts</strong></a></p></td>
<td align="left"><p>This rule verifies that the <strong>PerfConfigData</strong> parameter that is passed to <strong>StorPortInitializePerfOpts</strong> is not NULL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="storport-storportstartio.md" data-raw-source="[&lt;strong&gt;StorPortStartIo&lt;/strong&gt;](storport-storportstartio.md)"><strong>StorPortStartIo</strong></a></p></td>
<td align="left"><p>Waits or data allocation must never be performed in the miniport&#39;s <strong>StartIo</strong> routine. The driver fails the rule if it calls <strong>StorPortStallExecution</strong> or another function that involves time-consuming operations. Since <strong>StartIo</strong> is synchronized, these calls should mostly be done in <strong>BuildIo</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="storport-storporttimer.md" data-raw-source="[&lt;strong&gt;StorPortTimer&lt;/strong&gt;](storport-storporttimer.md)"><strong>StorPortTimer</strong></a></p></td>
<td align="left"><p>The <strong>HW_TIMER</strong> routine must be defined if a call to <strong>StorPortNotification(RequestTimerCall)</strong> is made.</p></td>
</tr>
</tbody>
</table>

 

**To select the SrbProcessing rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **SrbProcessing**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **SrbProcessing.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:SrbProcessing.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





