---
title: Miscellaneous rule set (KMDF)
description: Use these rules to verify that your driver correctly follows a general set of requirements for the proper handling of device objects, keys, and that the driver does not makes calls to DDIs that are not appropriate for a non-PnP driver or for a non-FDO driver that is not a power policy owner.
ms.assetid: B8F9FBE1-ED27-47EC-ACFC-8BD354A5E72D
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
<td align="left"><p>[<strong>AccessHardwareKey</strong>](kmdf-accesshardwarekey.md)</p></td>
<td align="left"><p>The [<strong>AccessHardwareKey</strong>](kmdf-accesshardwarekey.md) rule specifies that a bus driver should not try to access the hardware key of a child device from [<em>EvtChildListCreateDevice</em>](https://msdn.microsoft.com/library/windows/hardware/ff540828).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>AddPdotoStaticChildlist</strong>](kmdf-addpdotostaticchildlist.md)</p></td>
<td align="left"><p>The AddPdotoStaticChildlist rule specifies that for a PDO device, the framework function [<strong>WdfFdoAddStaticChild</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547225) must be called after the driver calls [<strong>WdfPdoInitAllocate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548786) and [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) successfully.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ChildListConfiguration</strong>](kmdf-childlistconfiguration.md)</p></td>
<td align="left"><p>The [<strong>ChildListConfiguration</strong>](kmdf-childlistconfiguration.md) rule specifies that drivers that support [Dynamic Enumeration](https://msdn.microsoft.com/library/windows/hardware/ff540812) must call [<strong>WdfFdoInitSetDefaultChildListConfig</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547258) before calling the [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>Cleanup4CtlDeviceRegistered</strong>](kmdf-cleanup4ctldeviceregistered.md)</p></td>
<td align="left"><p>The [<strong>Cleanup4CtlDeviceRegistered</strong>](kmdf-cleanup4ctldeviceregistered.md) rule specifies that if a Plug and Play (PnP) driver calls [<strong>WdfDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545926) for the control device object, the driver must register one of the required event callback functions.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>NonFDONotPowerPolicyOwnerAPI</strong>](kmdf-nonfdonotpowerpolicyownerapi.md)</p></td>
<td align="left"><p>The [<strong>NonFDONotPowerPolicyOwnerAPI</strong>](kmdf-nonfdonotpowerpolicyownerapi.md) rule specifies that if a non-FDO driver is not a power policy owner, certain DDIs cannot be called.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>NonPnPDrvPowerPolicyOwnerAPI</strong>](kmdf-nonpnpdrvpowerpolicyownerapi.md)</p></td>
<td align="left"><p>The [<strong>NonPnPDrvPowerPolicyOwnerAPI</strong>](kmdf-nonpnpdrvpowerpolicyownerapi.md) rule specifies that non-PnP drivers cannot call certain DDIs related to power management.</p></td>
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

 

 





