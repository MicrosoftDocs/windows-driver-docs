---
title: VJoyD Minidriver Override
description: VJoyD Minidriver Override
ms.assetid: a77d2464-7785-44a9-b527-2224d261feac
keywords:
- joysticks WDK HID , overrides
- virtual joystick drivers WDK HID , overrides
- VJoyD WDK HID , overrides
- overriding virtual minidrivers WDK joysticks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# VJoyD Minidriver Override





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

 

 




