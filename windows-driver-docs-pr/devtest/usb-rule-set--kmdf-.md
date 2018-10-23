---
title: Usb rule set (KMDF)
description: Use these rules to verify that your driver correctly handles some specialized KMDF methods for USB devices.
ms.assetid: E07F4E18-CE93-43A8-AAB4-C3CF8CC790CC
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Usb rule set (KMDF)


Use these rules to verify that your driver correctly handles some specialized KMDF methods for USB devices.

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
<td align="left"><p>[<strong>FailD0EntryIoTargetState</strong>](kmdf-faild0entryiotargetstate.md)</p></td>
<td align="left"><p>The [<strong>FailD0EntryIoTargetState</strong>](kmdf-faild0entryiotargetstate.md) rule specifies that an I/O target for a USB continuous reader started within the [<em>EvtDeviceD0Entry</em>](https://msdn.microsoft.com/library/windows/hardware/ff540848) will get stopped appropriately from the same callback if the <em>EvtDeviceD0Entry</em> fails.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>UsbContReader</strong>](kmdf-usbcontreader.md)</p></td>
<td align="left"><p>The [<strong>UsbContReader</strong>](kmdf-usbcontreader.md) rule specifies that a continuous reader is configured correctly within a driver's [<em>EvtDevicePrepareHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540880) event callback function, where the driver makes a call to the [<strong>WdfUsbTargetPipeConfigContinuousReader</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551130) method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>UsbDeviceCreate</strong>](kmdf-usbdevicecreate.md)</p></td>
<td align="left"><p>The [<strong>UsbDeviceCreate</strong>](kmdf-usbdevicecreate.md) rule specifies that the [<strong>WdfUsbTargetDeviceCreate</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550077) and [<strong>WdfUsbTargetDeviceCreateWithParameters</strong>](https://msdn.microsoft.com/library/windows/hardware/hh439428) methods are not called outside of the [<em>EvtDevicePrepareHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540880) event callback function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>UsbDeviceCreateFail</strong>](kmdf-usbdevicecreatefail.md)</p></td>
<td align="left"><p>The [<strong>UsbDeviceCreateFail</strong>](kmdf-usbdevicecreatefail.md) rule specifies that the driver returns from the [<em>EvtDevicePrepareHardware</em>](https://msdn.microsoft.com/library/windows/hardware/ff540880) event callback function with an error status if creation of a WDFUSBDEVICE object fails.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>UsbDeviceCreateTarget</strong>](kmdf-usbdevicecreatetarget.md)</p></td>
<td align="left"><p>The [<strong>UsbDeviceCreateTarget</strong>](kmdf-usbdevicecreatetarget.md) rule specifies that multiple WDFUSBDEVICE objects are not created while WDFUSBDEVICE object(s) that are currently in the device context are leaked.</p></td>
</tr>
</tbody>
</table>

 

**To select the Usb rule set**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Usb**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Usb.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Usb.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





