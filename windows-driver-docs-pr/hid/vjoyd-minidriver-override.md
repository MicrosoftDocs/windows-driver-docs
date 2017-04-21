---
title: VJoyD Minidriver Override
author: windows-driver-content
description: VJoyD Minidriver Override
ms.assetid: a77d2464-7785-44a9-b527-2224d261feac
keywords:
- joysticks WDK HID , overrides
- virtual joystick drivers WDK HID , overrides
- VJoyD WDK HID , overrides
- overriding virtual minidrivers WDK joysticks
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# VJoyD Minidriver Override


## <a href="" id="ddk-vjoyd-mini-driver-override-di"></a>


USB/HID devices that do not load the JoyHID.VxD device driver can sometimes display duplicate device entries present in the Gaming Options control panel when used with other USB/HID devices. This occurs when a JoyHID-compliant device is attached to the system at the same time as a non-JoyHID device.

If your device uses a VJoyD minidriver other than JoyHID--presumably developed by the device manufacturer or an affiliate--you can prevent these issues by properly setting up your device type key and related named values in the registry. The features described in this topic are available only to devices with type keys in the form "VID\_*vvvv*&PID\_*pppp*", where the letters *v* and *p* are zero-padded vendor and product ID values for the product.

Given a properly formatted type key, the following steps prevent JoyHID from attempting to retrieve data from the device or displaying unnecessary device entries in Control Panel/add list.

-   Set OEMData to JOY\_HWS\_AUTOLOAD. This prevents the device name from being displayed in the add list for devices.

-   Set OEMCallout to the driver that should be loaded for the device. This prevents JoyHID.VxD from being loaded for the device.

-   Set OEMName to the name appropriate for the device.

If needed, you can set registry values to arbitrary values to prevent JoyHID from reading data from the device. For example, you might use the following values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>OEMName</p></td>
<td><p>&quot;Unused entry for IHV device X, do not remove&quot;</p></td>
</tr>
<tr class="even">
<td><p>OEMData</p></td>
<td><p>OEMData is a binary registry field containing two DWORDs. The first is a set of JOY_HWS_* flags, the second is the number of buttons on the device. The value of the flag JOY_HWS_AUTOLOAD is defined in dinput.h to be 0x10000000. Since the number of buttons in this case is irrelevant, the eight bytes (in hex) should be 00,00,00,10,00,00,00,00.</p></td>
</tr>
<tr class="odd">
<td><p>OEMCallout</p></td>
<td><p>&quot;unused&quot;</p></td>
</tr>
</tbody>
</table>

 

Note that values like these merely prevent JoyHID from attempting to read data from the device. If your device uses a VJoyD minidriver, you should set the preceding values to properly reflect the device name and driver to be loaded.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20VJoyD%20Minidriver%20Override%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


