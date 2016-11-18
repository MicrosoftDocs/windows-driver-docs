---
title: Selective suspend for HID over USB devices
author: windows-driver-content
description: Revision 2.0 of the Universal Serial Bus Specification specifies a USB selective suspend feature.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: A4560D7C-8A32-4A91-95B6-4377E0F0D0C1
---

# Selective suspend for HID over USB devices


Revision 2.0 of the *Universal Serial Bus Specification* specifies a USB selective suspend feature. By using this feature, the Windows operating system can selectively suspend idle USB devices. This allows Windows to efficiently manage the power requirements of the overall system. For more information about how Windows supports the USB selective suspend feature, see [USB Selective Suspend](https://msdn.microsoft.com/library/windows/hardware/ff540144). (This resource may not be available in some languages and countries.)

By default, USB selective suspend is disabled by Windows in order to provide a consistent user experience and to avoid resume latency from selective suspend.

A HID device that supports selective suspend must be designed to:

-   Retain the first input, touch, movement or key press when resuming from selective suspend.
-   Wake from selective suspend on movement.
-   Maintain the wireless link (if applicable).
-   Maintain power to any active status LEDs, such as NUM lock or CAPS lock.
-   Resume from selective suspend without any perceived delay by the user.

Windows 8 supports two methods for enabling Selective Suspend for HID USB devices. They are as follows:

1.  **Microsoft OS Descriptor \[PREFERRED\]**: The Microsoft OS Descriptor’s Extended Properties descriptor can be used to write the necessary registry key(s) to support USB HID Selective Suspend.
2.  **Vendor Provided INF**: The Hardware manufacturer can provide an INF file (that matches on the USB Hardware ID for the HID devnode) to install the appropriate registry keys.

Microsoft recommends that hardware vendors and PC manufacturers use the first option to enable USB HID Selective Suspend. The advantages of this option are:

-   Hardware vendors and PC manufacturers do not have to install an additional INF file.
-   The necessary registry setting is automatically populated on new Windows 8 installations.
-   The necessary registry setting is preserved on an upgrade to Windows 8.
-   The user cannot lose (or disable) Selective Suspend functionality by uninstalling the INF.

However, hardware vendors and PC manufacturers who wish to still use the INF approach, can use the example below. The following is a sample INF file that shows how to enable this USB feature for HID devices in Windows:

```ManagedCPlusPlus
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

1.  The [**INF Version section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) should have the **CLASSGUID** and **DriverVer** directives set as follows:

    -   The **CLASSGUID** directive must specify the Microsoft class GUID for HID devices. This GUID has the value {745a17a0-74d3-11d0-b6fe-00a0c90f57da}.

    -   The **DriverVer** directive must have a value that has a newer date and greater version number than the value specified by the **DriverVer** directive in Input.inf.

2.  2. The VendorXYZDevice\* sections specify the hardware identifier (ID) for the vendor's HID device. The hardware ID consists of a vendor identifier (VID) and product identifier (PID). Each hardware ID for a device must have VID/PID values that are unique to the vendor and device. This ensures that the same hardware ID does not correspond to multiple names and settings

3.  3. The VendorXYZDevice\_Install.NT and VendorXYZDevice\_Install.NT.HW sections are [**INF DDInstall sections**](https://msdn.microsoft.com/library/windows/hardware/ff547344). In this example, these sections contain INF **Include** and **Needs** directives.

    The **Include** directives reference the system-supplied Input.inf file, which contains INF sections needed to enable the USB selective suspend feature for the vendor's HID device.

    The **Needs** directives indicate which sections from Input.inf should be processed during device installation. In this case, the HID\_SelSus\_Inst section is selected instead of the default HID\_Inst section, which does not support selective suspend.

4.  4. The VendorXYZDevice\_Install.NT.Services section is an [**INF DDInstall.HW section**](https://msdn.microsoft.com/library/windows/hardware/ff547330). In this example, the section also contains the same values for the INF **Include** and **Needs** directives.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Selective%20suspend%20for%20HID%20over%20USB%20devices%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


