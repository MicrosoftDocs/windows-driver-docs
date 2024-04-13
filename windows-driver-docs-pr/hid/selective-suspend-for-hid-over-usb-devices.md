---
title: Selective Suspend for HID Over USB Devices
description: Revision 2.0 of the Universal Serial Bus Specification specifies a USB selective suspend feature.
ms.date: 01/11/2024
---

# Selective suspend for HID over USB devices

Revision 2.0 of the *Universal Serial Bus Specification* specifies a USB selective suspend feature. By using this feature, the Windows operating system can selectively suspend idle USB devices. This allows Windows to efficiently manage the power requirements of the overall system. For more information about how Windows supports the USB selective suspend feature, see [USB selective suspend](../usbcon/usb-selective-suspend.md). (This resource may not be available in some languages and countries.)

By default, USB selective suspend is disabled by Windows in order to provide a consistent user experience and to avoid resume latency from selective suspend.

A HID device that supports selective suspend must be designed to:

- Retain the first input, touch, movement or key press when resuming from selective suspend.
- Wake from selective suspend on movement.
- Maintain the wireless link (if applicable).
- Maintain power to any active status LEDs, such as NUM lock or CAPS lock.
- Resume from selective suspend without any perceived delay by the user.

Windows 8 supports two methods for enabling Selective Suspend for HID USB devices. They are as follows:

1. **Microsoft OS Descriptor \[PREFERRED\]**: The Microsoft OS Descriptor's Extended Properties descriptor can be used to write the necessary registry key(s) to support USB HID Selective Suspend.
2. **Vendor Provided INF**: The Hardware manufacturer can provide an INF file (that matches on the USB Hardware ID for the HID devnode) to install the appropriate registry keys.

Microsoft recommends that hardware vendors and PC manufacturers use the first option to enable USB HID Selective Suspend. The advantages of this option are:

- Hardware vendors and PC manufacturers do not have to install an additional INF file.
- The necessary registry setting is automatically populated on new Windows 8 installations.
- The necessary registry setting is preserved on an upgrade to Windows 8.
- The user cannot lose (or disable) Selective Suspend functionality by uninstalling the INF.

However, hardware vendors and PC manufacturers who wish to still use the INF approach, can use the example below. The following is a sample INF file that shows how to enable this USB feature for HID devices in Windows:

```inf
; Vendor INF File for USB HID devices
;
; A sample INF for a stand-alone USB HID device that supports
; selective suspend

[Version]
Signature   ="$WINDOWS NT$"
Class       =HIDClass
ClassGuid   ={745a17a0-74d3-11d0-b6fe-00a0c90f57da}
Provider    =%VendorName%
DriverVer   =09/19/2008,6.0.0.0
CatalogFile =VendorXYZ.cat
PnpLockdown =1

; ================= Class section =====================
[ControlFlags]
ExcludeFromSelect=*

[SourceDisksNames]
1 = %DiskName%,,,""

;*****************************************
; Install Section
;*****************************************

[Manufacturer]
%VendorName% = VendorXYZDevice,NTx86,NTamd64,NTarm

[VendorXYZDevice.NTx86]
%VendorXYZ.DeviceDesc% = VendorXYZDevice_Install, USB\VID_045E&PID_00B4

[VendorXYZDevice.NTamd64]
%VendorXYZ.DeviceDesc% = VendorXYZDevice_Install, USB\VID_045E&PID_00B4

[VendorXYZDevice.NTarm]
%VendorXYZ.DeviceDesc% = VendorXYZDevice_Install, USB\VID_045E&PID_00B4


[VendorXYZDevice_Install.NT]
include     = input.inf
needs       = HID_SelSus_Inst.NT

[VendorXYZDevice_Install.NT.HW]
include     = input.inf
needs       = HID_SelSus_Inst.NT.HW

[VendorXYZDevice_Install.NT.Services]
include     = input.inf
needs       = HID_SelSus_Inst.NT.Services

[Strings]
VendorName = "Vendor XYZ"
DiskName   = "Vendor XYZ Installation Disk"
VendorXYZ.DeviceDesc = "VendorXYZ Device"
```

Where:

1. The [**INF Version section**](../install/inf-version-section.md) should have the **CLASSGUID** and **DriverVer** directives set as follows:

    - The **CLASSGUID** directive must specify the Microsoft class GUID for HID devices. This GUID has the value {745a17a0-74d3-11d0-b6fe-00a0c90f57da}.

    - The **DriverVer** directive must have a value that has a newer date and greater version number than the value specified by the **DriverVer** directive in Input.inf.

2. The VendorXYZDevice\* sections specify the hardware identifier (ID) for the vendor's HID device. The hardware ID consists of a vendor identifier (VID) and product identifier (PID). Each hardware ID for a device must have VID/PID values that are unique to the vendor and device. This ensures that the same hardware ID does not correspond to multiple names and settings

3. The VendorXYZDevice\_Install.NT and VendorXYZDevice\_Install.NT.HW sections are [**INF DDInstall sections**](../install/inf-ddinstall-section.md). In this example, these sections contain INF **Include** and **Needs** directives.

    The **Include** directives reference the system-supplied Input.inf file, which contains INF sections needed to enable the USB selective suspend feature for the vendor's HID device.

    The **Needs** directives indicate which sections from Input.inf should be processed during device installation. In this case, the HID\_SelSus\_Inst section is selected instead of the default HID\_Inst section, which does not support selective suspend.

4. The VendorXYZDevice\_Install.NT.Services section is an [**INF DDInstall.HW section**](../install/inf-ddinstall-hw-section.md). In this example, the section also contains the same values for the INF **Include** and **Needs** directives.
