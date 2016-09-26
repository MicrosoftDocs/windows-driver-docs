---
title: Legacy Touchpad Forced Detection
description: This topic describes the mechanism for forcing Windows 8.1 to detect a touchpad irrespective of connectivity as a legacy device on mobile form-factors.
ms.assetid: DB648700-4AEE-4689-9FD7-2019E030036A
---

#  Legacy Touchpad Forced Detection


This topic describes the mechanism for forcing Windows 8.1 to detect a touchpad irrespective of connectivity as a legacy device on mobile form-factors.

Any touchpad that is not identified as a certified Windows Precision Touchpad is classified as a legacy touchpad provided it is identified by the host as an integrated peripheral on a mobile form-factor. If an integrated touchpad is not identified by the host as a legacy touchpad, the following features will not be available:

-   Inbox Accidental Activation Prevention (AAP)
-   PC Settings Touchpad Page
    -   Including the ability to opt-in to settings beyond AAP
    -   See [Legacy Touchpad PC Settings Opt-In](windows-precision-touchpad-legacy-touchpad-pc-settings-opt-in.md) for additional information

There are circumstances in which a legacy touchpad integrated with a keyboard may not be identified correctly due to underlying issues in how the device is exposed to the host.

1.  Touchpad is connected via a USB port marked as removable
2.  Touchpad is connected via Bluetooth

In the above circumstances, Windows 8.1 will automatically assume the touchpad is an external mouse or touchpad and will not enable legacy touchpad features.

## <span id="Approved_List_Mechanism"></span><span id="approved_list_mechanism"></span><span id="APPROVED_LIST_MECHANISM"></span>Approved List Mechanism


Irrespective of how a device is exposed to the host, Windows 8.1 provides the ability to force legacy identification and feature enablement through an approved list mechanism.

By creating a registry entry under the following key and specifying the desired matching level, Windows 8.1 will force a matching device to be detected as a legacy touchpad.

**HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\PrecisionTouchPad\\LegacyDevices\\**

The value of that DWORD specifies what level of matching should be undertaken for a specific entry.

|                    |            |
|--------------------|------------|
| Matching Level     | Value      |
| VID/PID Only Match | 0x00000001 |
| VID/PID/REV Match  | 0x00000002 |
| Full HWID Match    | 0x00000003 |

 

For example if a device with HWID (ACPI\\MSFT0001) wanted to be exactly matched based on HWID, it would specify its entry as follows:

ACPI\\MSFT0001 0x00000003

For example if a touchpad with HWID (HID\\VID\_045E&PID\_003F&REV\_03FF&MI\_02&COL01) wanted to ensure a match irrespective MI and COL, it would specify its entry as follows:

HID\\VID\_045E&PID\_003F&REV\_03FF 0x00000002

For more information, see [HIDClass Hardware IDs for Top-Level Collections](http://msdn.microsoft.com/library/ff538842.aspx).

With reference to the above example, if the same touchpad wanted to ensure a match irrespective of version (RevID), it would specify its entry as follows:

HID\\VID\_045E&PID\_003F 0x00000001

Note that a full HWID string may be specified in the registry with the DWORD value indicating the level of matching, for instance the second example has a functional equivalent below:

HID\\VID\_045E&PID\_003F&REV\_03FF&MI\_02&COL01 0x00000002

**Note**  If importing or exporting from the registry, the “\\” will be duplicated as “\\\\” since this is a delimiting character. If pasting via registry editor, ignore the extra delimiter.

 

`Windows Registry Editor Version 5.00``[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\PrecisionTouchPad\LegacyDevices] "HID\\VID_045E&PID_003F&REV_03FF"=dword:00000002`

 

 




