---
title: VJoyD minidriver override
description: VJoyD minidriver override
keywords:
- joysticks WDK HID , overrides
- virtual joystick drivers WDK HID , overrides
- VJoyD WDK HID , overrides
- overriding virtual minidrivers WDK joysticks
ms.date: 10/12/2022
---

# VJoyD minidriver override

USB/HID devices that do not load the JoyHID.VxD device driver can sometimes display duplicate device entries present in the Gaming Options control panel when used with other USB/HID devices. This occurs when a JoyHID-compliant device is attached to the system at the same time as a non-JoyHID device.

If your device uses a VJoyD minidriver other than JoyHID--presumably developed by the device manufacturer or an affiliate--you can prevent these issues by properly setting up your device type key and related named values in the registry. The features described in this topic are available only to devices with type keys in the form "VID_*vvvv*&PID_*pppp*", where the letters *v* and *p* are zero-padded vendor and product ID values for the product.

Given a properly formatted type key, the following steps prevent JoyHID from attempting to retrieve data from the device or displaying unnecessary device entries in Control Panel/add list.

- Set OEMData to JOY_HWS_AUTOLOAD. This prevents the device name from being displayed in the add list for devices.

- Set OEMCallout to the driver that should be loaded for the device. This prevents JoyHID.VxD from being loaded for the device.

- Set OEMName to the name appropriate for the device.

If needed, you can set registry values to arbitrary values to prevent JoyHID from reading data from the device. For example, you might use the following values:

| Name | Value |
|--|--|
| OEMName | "Unused entry for IHV device X, do not remove" |
| OEMData | OEMData is a binary registry field containing two DWORDs. The first is a set of JOY_HWS_* flags, the second is the number of buttons on the device. The value of the flag JOY_HWS_AUTOLOAD is defined in dinput.h to be 0x10000000. Since the number of buttons in this case is irrelevant, the eight bytes (in hex) should be 00,00,00,10,00,00,00,00. |
| OEMCallout | "unused" |

Values like these merely prevent JoyHID from attempting to read data from the device. If your device uses a VJoyD minidriver, you should set the preceding values to properly reflect the device name and driver to be loaded.
