---
title: Miscellaneous rule set (KMDF)
description: Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of device objects, keys, and that the driver does not makes calls to DDIs that are not appropriate for a non-PnP driver or for a non-FDO driver that is not a power policy owner.
ms.assetid: B8F9FBE1-ED27-47EC-ACFC-8BD354A5E72D
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Miscellaneous rule set (KMDF)


Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of device objects, keys, and that the driver does not makes calls to DDIs that are not appropriate for a non-PnP driver or for a non-FDO driver that is not a power policy owner.

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
<td align="left"><p><a href="kmdf-accesshardwarekey.md" data-raw-source="[&lt;strong&gt;AccessHardwareKey&lt;/strong&gt;](kmdf-accesshardwarekey.md)"><strong>AccessHardwareKey</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-accesshardwarekey.md" data-raw-source="[&lt;strong&gt;AccessHardwareKey&lt;/strong&gt;](kmdf-accesshardwarekey.md)"><strong>AccessHardwareKey</strong></a> rule specifies that a bus driver should not try to access the hardware key of a child device from <a href="https://msdn.microsoft.com/library/windows/hardware/ff540828" data-raw-source="[&lt;em&gt;EvtChildListCreateDevice&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540828)"><em>EvtChildListCreateDevice</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-addpdotostaticchildlist.md" data-raw-source="[&lt;strong&gt;AddPdotoStaticChildlist&lt;/strong&gt;](kmdf-addpdotostaticchildlist.md)"><strong>AddPdotoStaticChildlist</strong></a></p></td>
<td align="left"><p>The AddPdotoStaticChildlist rule specifies that for a PDO device, the framework function <a href="https://msdn.microsoft.com/library/windows/hardware/ff547225" data-raw-source="[&lt;strong&gt;WdfFdoAddStaticChild&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547225)"><strong>WdfFdoAddStaticChild</strong></a> must be called after the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548786" data-raw-source="[&lt;strong&gt;WdfPdoInitAllocate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548786)"><strong>WdfPdoInitAllocate</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> successfully.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-childlistconfiguration.md" data-raw-source="[&lt;strong&gt;ChildListConfiguration&lt;/strong&gt;](kmdf-childlistconfiguration.md)"><strong>ChildListConfiguration</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-childlistconfiguration.md" data-raw-source="[&lt;strong&gt;ChildListConfiguration&lt;/strong&gt;](kmdf-childlistconfiguration.md)"><strong>ChildListConfiguration</strong></a> rule specifies that drivers that support <a href="https://msdn.microsoft.com/library/windows/hardware/ff540812" data-raw-source="[Dynamic Enumeration](https://msdn.microsoft.com/library/windows/hardware/ff540812)">Dynamic Enumeration</a> must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff547258" data-raw-source="[&lt;strong&gt;WdfFdoInitSetDefaultChildListConfig&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547258)"><strong>WdfFdoInitSetDefaultChildListConfig</strong></a> before calling the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-cleanup4ctldeviceregistered.md" data-raw-source="[&lt;strong&gt;Cleanup4CtlDeviceRegistered&lt;/strong&gt;](kmdf-cleanup4ctldeviceregistered.md)"><strong>Cleanup4CtlDeviceRegistered</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-cleanup4ctldeviceregistered.md" data-raw-source="[&lt;strong&gt;Cleanup4CtlDeviceRegistered&lt;/strong&gt;](kmdf-cleanup4ctldeviceregistered.md)"><strong>Cleanup4CtlDeviceRegistered</strong></a> rule specifies that if a Plug and Play (PnP) driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545926" data-raw-source="[&lt;strong&gt;WdfDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545926)"><strong>WdfDeviceCreate</strong></a> for the control device object, the driver must register one of the required event callback functions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-nonfdonotpowerpolicyownerapi.md" data-raw-source="[&lt;strong&gt;NonFDONotPowerPolicyOwnerAPI&lt;/strong&gt;](kmdf-nonfdonotpowerpolicyownerapi.md)"><strong>NonFDONotPowerPolicyOwnerAPI</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-nonfdonotpowerpolicyownerapi.md" data-raw-source="[&lt;strong&gt;NonFDONotPowerPolicyOwnerAPI&lt;/strong&gt;](kmdf-nonfdonotpowerpolicyownerapi.md)"><strong>NonFDONotPowerPolicyOwnerAPI</strong></a> rule specifies that if a non-FDO driver is not a power policy owner, certain DDIs cannot be called.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-nonpnpdrvpowerpolicyownerapi.md" data-raw-source="[&lt;strong&gt;NonPnPDrvPowerPolicyOwnerAPI&lt;/strong&gt;](kmdf-nonpnpdrvpowerpolicyownerapi.md)"><strong>NonPnPDrvPowerPolicyOwnerAPI</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-nonpnpdrvpowerpolicyownerapi.md" data-raw-source="[&lt;strong&gt;NonPnPDrvPowerPolicyOwnerAPI&lt;/strong&gt;](kmdf-nonpnpdrvpowerpolicyownerapi.md)"><strong>NonPnPDrvPowerPolicyOwnerAPI</strong></a> rule specifies that non-PnP drivers cannot call certain DDIs related to power management.</p></td>
</tr>
</tbody>
</table>

 

**To select the Miscellaneous rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Miscellaneous**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Miscellaneous.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Miscellaneous.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





