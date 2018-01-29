---
title: SrbProcessing rule set (Storport)
description: Use these rules to verify that your driver correctly processes SRB requests.
ms.assetid: A3BF2AA3-207F-4D74-94B0-6CA215341340
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
<td align="left"><p>[<strong>SpDuplex</strong>](storport-spduplex.md)</p></td>
<td align="left"><p>This rule verifies that this miniport is in <strong>Full Duplex</strong> mode. Any driver built according to the StorPort-miniport model must be in <strong>Full Duplex</strong> mode. <strong>Half Duplex</strong> should only be used when porting an existing SCSI driver to StorPort.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SpNoWait</strong>](storport-spnowait.md)</p></td>
<td align="left"><p>This rule verifies that waits or data allocation are not performed inside <strong>StartIo</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SpReturnValue</strong>](storport-spreturnvalue.md)</p></td>
<td align="left"><p>This rule verifies that the driver's implementations of [<strong>HwStorFindAdapter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557390) and [<strong>VirtualHwStorFindAdapter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568008) return a valid status. A valid status is one of the following: <strong>SP_RETURN_FOUND</strong>, <strong>SP_RETURN_ERROR</strong>, <strong>SP_RETURN_BAD_CONFIG</strong>, or <strong>SP_RETURN_NOT_FOUND</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortAllocatePool</strong>](storportallocatepool.md)</p></td>
<td align="left"><p>This rule verifies that the miniport must not attempt to call [<strong>StorPortFreePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567065) on an deallocated buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortAllocatePool2</strong>](storport-storportallocatepool2.md)</p></td>
<td align="left"><p>This rule verifies that the miniport must not attempt to call [<strong>StorPortAllocatePool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567031) on an allocated buffer without deallocating it first.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortBuildIo</strong>](storport-storportbuildio.md)</p></td>
<td align="left"><p>This rule verifies that if the StorPort miniport's [<strong>StorPortBuildIo</strong>](storport-storportbuildio.md) routine returns <strong>FALSE</strong>, the SRB in question is not passed to <strong>StartIo</strong>. (In such cases, the miniport driver must complete the SRB by calling [<strong>StorPortNotification</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567433) with a notification type of <strong>RequestComplete</strong> from <strong>StorPortBuildIo</strong> or someplace else).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortCompleteRequest</strong>](storport-storportcompleterequest.md)</p></td>
<td align="left"><p>This rule verifies that no calls to <strong>StorPortCompleteRequest</strong> are made by the miniport. Usage of the <strong>StorPortCompleteRequest</strong> is not recommended; miniports should instead call <strong>StorPortNotification</strong> with <strong>notificationType = RequestComplete</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortEnablePassive</strong>](storport-storportenablepassive.md)</p></td>
<td align="left"><p>This rule verifies that <strong>StorPortEnablePassiveInitialization</strong> is not called from any StorPort miniport driver routine other than <strong>HwInitialize</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortFindAdapter</strong>](storport-storportfindadapter.md)</p></td>
<td align="left"><p>The [<strong>HwStorFindAdapter</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557390) routine must set the <strong>MaximumTransferLength</strong> and the <strong>NumberOfPhysicalBreaks</strong> fields in the <strong>PORT_CONFIGURATION_INFORMATION</strong> structure. By default, the value of both these fields is <strong>SP_UNINITIALIZED_VALUE</strong>. If either of these fields is still set to <strong>SP_UNINITIALIZED_VALUE</strong> upon exit from <strong>FindAdapter</strong>, the driver fails the rule.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortNotification2</strong>](storport-storportnotification2.md)</p></td>
<td align="left"><p>This rule verifies that calls to <strong>StorPortNotification</strong> use only allowed (i.e. documented) notification types.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortPassiveFromHwInit</strong>](storport-storportpassivefromhwinit.md)</p></td>
<td align="left"><p><strong>StorPortEnablePassiveInitialization</strong> should not be called within the HW Initialization entry point for Storport drivers if the HW Initialization entry point can be called directly from the HW Adapter Control entry point.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortPerfOpts</strong>](storport-storportperfopts.md)</p></td>
<td align="left"><p>This rule verifies that the <strong>PerfConfigData</strong> parameter that is passed to <strong>StorPortInitializePerfOpts</strong> is not NULL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>StorPortStartIo</strong>](storport-storportstartio.md)</p></td>
<td align="left"><p>Waits or data allocation must never be performed in the miniport's <strong>StartIo</strong> routine. The driver fails the rule if it calls <strong>StorPortStallExecution</strong> or another function that involves time-consuming operations. Since <strong>StartIo</strong> is synchronized, these calls should mostly be done in <strong>BuildIo</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>StorPortTimer</strong>](storport-storporttimer.md)</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20SrbProcessing%20rule%20set%20%28Storport%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




