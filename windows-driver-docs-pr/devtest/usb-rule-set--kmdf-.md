---
title: Usb rule set (KMDF)
description: Use these rules to verify that your driver correctly handles some specialized KMDF methods for USB devices.
ms.assetid: E07F4E18-CE93-43A8-AAB4-C3CF8CC790CC
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20Usb%20rule%20set%20%28KMDF%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




