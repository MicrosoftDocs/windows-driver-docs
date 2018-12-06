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
<td align="left"><p><a href="kmdf-faild0entryiotargetstate.md" data-raw-source="[&lt;strong&gt;FailD0EntryIoTargetState&lt;/strong&gt;](kmdf-faild0entryiotargetstate.md)"><strong>FailD0EntryIoTargetState</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-faild0entryiotargetstate.md" data-raw-source="[&lt;strong&gt;FailD0EntryIoTargetState&lt;/strong&gt;](kmdf-faild0entryiotargetstate.md)"><strong>FailD0EntryIoTargetState</strong></a> rule specifies that an I/O target for a USB continuous reader started within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540848" data-raw-source="[&lt;em&gt;EvtDeviceD0Entry&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540848)"><em>EvtDeviceD0Entry</em></a> will get stopped appropriately from the same callback if the <em>EvtDeviceD0Entry</em> fails.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-usbcontreader.md" data-raw-source="[&lt;strong&gt;UsbContReader&lt;/strong&gt;](kmdf-usbcontreader.md)"><strong>UsbContReader</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-usbcontreader.md" data-raw-source="[&lt;strong&gt;UsbContReader&lt;/strong&gt;](kmdf-usbcontreader.md)"><strong>UsbContReader</strong></a> rule specifies that a continuous reader is configured correctly within a driver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff540880" data-raw-source="[&lt;em&gt;EvtDevicePrepareHardware&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540880)"><em>EvtDevicePrepareHardware</em></a> event callback function, where the driver makes a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130" data-raw-source="[&lt;strong&gt;WdfUsbTargetPipeConfigContinuousReader&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551130)"><strong>WdfUsbTargetPipeConfigContinuousReader</strong></a> method.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-usbdevicecreate.md" data-raw-source="[&lt;strong&gt;UsbDeviceCreate&lt;/strong&gt;](kmdf-usbdevicecreate.md)"><strong>UsbDeviceCreate</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-usbdevicecreate.md" data-raw-source="[&lt;strong&gt;UsbDeviceCreate&lt;/strong&gt;](kmdf-usbdevicecreate.md)"><strong>UsbDeviceCreate</strong></a> rule specifies that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550077" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceCreate&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550077)"><strong>WdfUsbTargetDeviceCreate</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428" data-raw-source="[&lt;strong&gt;WdfUsbTargetDeviceCreateWithParameters&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439428)"><strong>WdfUsbTargetDeviceCreateWithParameters</strong></a> methods are not called outside of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540880" data-raw-source="[&lt;em&gt;EvtDevicePrepareHardware&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540880)"><em>EvtDevicePrepareHardware</em></a> event callback function.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="kmdf-usbdevicecreatefail.md" data-raw-source="[&lt;strong&gt;UsbDeviceCreateFail&lt;/strong&gt;](kmdf-usbdevicecreatefail.md)"><strong>UsbDeviceCreateFail</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-usbdevicecreatefail.md" data-raw-source="[&lt;strong&gt;UsbDeviceCreateFail&lt;/strong&gt;](kmdf-usbdevicecreatefail.md)"><strong>UsbDeviceCreateFail</strong></a> rule specifies that the driver returns from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540880" data-raw-source="[&lt;em&gt;EvtDevicePrepareHardware&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540880)"><em>EvtDevicePrepareHardware</em></a> event callback function with an error status if creation of a WDFUSBDEVICE object fails.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="kmdf-usbdevicecreatetarget.md" data-raw-source="[&lt;strong&gt;UsbDeviceCreateTarget&lt;/strong&gt;](kmdf-usbdevicecreatetarget.md)"><strong>UsbDeviceCreateTarget</strong></a></p></td>
<td align="left"><p>The <a href="kmdf-usbdevicecreatetarget.md" data-raw-source="[&lt;strong&gt;UsbDeviceCreateTarget&lt;/strong&gt;](kmdf-usbdevicecreatetarget.md)"><strong>UsbDeviceCreateTarget</strong></a> rule specifies that multiple WDFUSBDEVICE objects are not created while WDFUSBDEVICE object(s) that are currently in the device context are leaked.</p></td>
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

 

 





