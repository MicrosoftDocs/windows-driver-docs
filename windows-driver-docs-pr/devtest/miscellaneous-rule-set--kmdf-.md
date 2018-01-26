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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Miscellaneous%20rule%20set%20%28KMDF%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




