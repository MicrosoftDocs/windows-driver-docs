---
Description: This topic lists the Microsoft-provided drivers for the supported USB device classes.
title: USB device class drivers included in Windows
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB device class drivers included in Windows


**Summary**

-   Microsoft-provided drivers for USB-IF approved device classes.
-   For composite devices, use [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) that creates physical device objects (PDOs) for each function.
-   For non-composite devices or a function of a composite device, use [WinUSB (Winusb.sys)](winusb.md).

This topic lists the Microsoft-provided drivers for the supported USB device classes.

**If you are installing USB drivers:  ** You do not need to download USB device class drivers. They are installed automatically. These drivers and their installation files are included in Windows. They are available in the \\Windows\\System32\\DriverStore\\FileRepository folder. The drivers are updated through Windows Update.

**If you are writing a custom driver:  **Before writing a driver for your USB device, determine whether a Microsoft-provided driver meets the device requirements. If a Microsoft-provided driver is not available for the USB device class to which your device belongs, then consider using generic drivers, Winusb.sys or Usbccgp.sys. Write a driver only when necessary. More guidelines are included in [Choosing a driver model for developing a USB client driver](winusb-considerations.md).

## USB Device classes


*USB Device classes* are categories of devices with similar characteristics and that perform common functions. Those classes and their specifications are defined by the USB-IF. Each device class is identified by USB-IF approved class, subclass, and protocol codes, all of which are provided by the IHV in device descriptors in the firmware. Microsoft provides in-box drivers for several of those device classes, called *USB device class drivers*. If a device that belongs to a supported device class is connected to a system, Windows automatically loads the class driver, and the device functions with no additional driver required.

Hardware vendors should not write drivers for the supported device classes. Windows class drivers might not support all of the features that are described in a class specification. If some of the device's capabilities are not implemented by the class driver, vendors should provide supplementary drivers that work in conjunction with the class driver to support the entire range of functionality provided by the device.

For general information about USB-IF approved device classes, see the [USB Technology](http://www.usb.org/developers/defined_class/) website.

For the current list of USB class specifications and class codes, visit the [USB DWG website](http://www.usb.org/about/dwg_charter/).

## Device setup classes


Windows categorizes devices by *device setup classes*, which indicate the functionality of the device.

Microsoft defines setup classes for most devices. IHVs and OEMs can define new device setup classes, but only if none of the existing classes apply. For more information, see [System-Defined Device Setup Classes](https://msdn.microsoft.com/library/windows/hardware/ff553419).

Two important device setup classes for USB devices are as follows:

-   **USBDevice** {88BAE032-5A81-49f0-BC3D-A4FF138216D6}: IHVs must use this class for custom devices that do not belong to another class. This class is not used for USB host controllers and hubs.

-   **USB** {36fc9e60-c465-11cf-8056-444553540000}: IHVs must not use this class for their custom devices. This is reserved for USB host controllers and USB hubs.

The device setup classes are different from USB device classes discussed earlier. For example, an audio device has a USB device class code of 01h in its descriptor. When connected to a system, Windows loads the Microsoft-provided class driver, Usbaudio.sys. In Device Manager, the device is shown under is **Sound, video and game controllers**, which indicates that the device setup class is Media.

## Microsoft-provided USB device class drivers


USB-IF class code
Device setup class
Microsoft-provided driver and INF
Windows support
Description
Audio (01h)
**Media**

{4d36e96c-e325-11ce-bfc1-08002be10318}

Usbaudio.sys

Wdma\_usb.inf

Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)

Windows 10 Mobile
Windows 8.1

Windows 8

Windows 7

Windows Server 2008

Windows Vista

Microsoft provides support for the USB audio device class by means of the Usbaudio.sys driver. For more information, see "USBAudio Class System Driver" in [Kernel-Mode WDM Audio Components](https://msdn.microsoft.com/library/windows/hardware/ff537039). For more information about Windows audio support, see the [Audio Device Technologies for Windows](http://go.microsoft.com/fwlink/p/?linkid=8751) website.

Communications and CDC Control (02h)
**Ports**

{4D36E978-E325-11CE-BFC1-08002BE10318}

Usbser.sys

Usbser.inf

Windows 10 for desktop editions

Windows 10 Mobile
In Windows 10, a new INF, Usbser.inf, has been added that loads Usbser.sys automatically as the function driver.

For more information, see [USB serial driver (Usbser.sys)](usb-driver-installation-based-on-compatible-ids.md).

**Modem**

{4D36E96D-E325-11CE-BFC1-08002BE10318}

**Note**  Supports Subclass 02h (ACM)

 

Usbser.sys

Custom INF that references mdmcpq.inf

Windows 10 for desktop editions

Windows 8.1

Windows 8

Windows 7

Windows Server 2008

Windows Vista

In Windows 8.1 and earlier versions, Usbser.sys is not automatically loaded. To load the driver, you need to write an INF that references the modem INF (mdmcpq.inf) and includes \[Install\] and \[Needs\] sections.

Starting with Windows Vista, you can enable CDC and Wireless Mobile CDC (WMCDC) support by setting a registry value, as described in [Support for the Wireless Mobile Communication Device Class](support-for-the-wireless-mobile-communication-device-class--wmcdc-.md).

When CDC support is enabled, the [USB Common Class Generic Parent Driver](usb-common-class-generic-parent-driver.md) enumerates interface collections that correspond to CDC and WMCDC Control Models, and assigns physical device objects (PDO) to these collections.

**Net**

{4d36e972-e325-11ce-bfc1-08002be10318}

**Note**  Supports Subclass 0Eh (MBIM)

 

wmbclass.sys

Netwmbclass.inf

Windows 10 for desktop editions

Windows 8.1

Windows 8

Starting in Windows 8, Microsoft provides the wmbclass.sys driver, for mobile broadband devices. See, [MB Interface Model](https://msdn.microsoft.com/library/windows/hardware/dn265427).
HID (Human Interface Device) (03h)
**HIDClass**

{745a17a0-74d3-11d0-b6fe-00a0c90f57da}

Hidclass.sys

Hidusb.sys

Input.inf

Windows 10 for desktop editions

Windows 10 Mobile
Windows 8.1

Windows 8

Windows 7

Windows Server 2008

Windows Vista

Microsoft provides the HID class driver (Hidclass.sys) and the miniclass driver (Hidusb.sys) to operate devices that comply with the [USB HID Standard](http://go.microsoft.com/fwlink/p/?LinkId=761243). For more information, see [HID Architecture](https://msdn.microsoft.com/library/windows/hardware/jj126193) and [Minidrivers and the HID class driver](https://msdn.microsoft.com/library/windows/hardware/jj131708). For further information about Windows support for input hardware, see the [Input and HID - Architecture and Driver Support](http://go.microsoft.com/fwlink/p/?linkid=8709) website.
Physical (05h)
-
-
-
Recommended driver: [WinUSB (Winusb.sys)](winusb.md)
Image (06h)
**Image**

{6bdd1fc6-810f-11d0-bec7-08002be2092f}

Usbscan.sys

Sti.inf

Windows 10 for desktop editions

Windows 8.1

Windows 8

Windows 7

Windows Server 2008

Windows Vista

Microsoft provides the Usbscan.sys driver that manages USB digital cameras and scanners for Windows XP and later operating systems. This driver implements the USB component of the Windows Imaging Architecture (WIA). For more information about WIA, see [Windows Image Acquisition Drivers](https://msdn.microsoft.com/library/windows/hardware/ff553346) and the [Windows Imaging Component](http://go.microsoft.com/fwlink/p/?linkid=8768) website. For a description of the role that Usbscan.sys plays in the WIA, see [WIA Core Components](https://msdn.microsoft.com/library/windows/hardware/ff550215).
Printer (07h)
**USB**

**Note**  Usbprint.sys enumerates printer devices under the device set up class: **Printer** {4d36e979-e325-11ce-bfc1-08002be10318}.

 

Usbprint.sys

Usbprint.inf

Windows 10 for desktop editions

Windows 8.1

Windows 8

Windows 7

Windows Server 2008

Windows Vista

Microsoft provides the Usbprint.sys class driver that manages USB printers. For information about implementation of the printer class in Windows, see the [Printing - Architecture and Driver Support](http://go.microsoft.com/fwlink/p/?linkid=8764) website.
Mass Storage (08h)
**USB**

Usbstor.sys

Windows 10 for desktop editions

Windows 10 Mobile
Windows 8.1

Windows 8

Windows 7

Windows Server 2008

Windows Vista

Microsoft provides the Usbstor.sys port driver to manage USB mass storage devices with Microsoft's native storage class drivers. For an example device stack that is managed by this driver, see [Device Object Example for a USB Mass Storage Device](https://msdn.microsoft.com/library/windows/hardware/ff552547). For information about Windows storage support, see the [Storage Technologies](http://go.microsoft.com/fwlink/p/?linkid=8766) website.
**SCSIAdapter**

{4d36e97b-e325-11ce-bfc1-08002be10318}

SubClass (06) and Protocol (62)

Uaspstor.sys

Uaspstor.inf

Windows 10 for desktop editions

Windows 10 Mobile
Windows 8.1

Windows 8

Uaspstor.sys is the class driver for SuperSpeed USB devices that support bulk stream endpoints. For more information see:
-   [Loading a UASP Storage Driver as a Class Driver on xHCI](https://msdn.microsoft.com/library/windows/hardware/gg585600.aspx)
-   [USB Attached SCSI (UAS) Best Practices for Windows 8](https://msdn.microsoft.com/library/windows/hardware/jj248714.aspx)

Hub (09h)
**USB**

{36fc9e60-c465-11cf-8056-444553540000}

Usbhub.sys

Usb.inf

Windows 10 for desktop editions

Windows 10 Mobile
Windows 8.1

Windows 8

Windows 7

Windows Server 2008

Windows Vista

Microsoft provides the Usbhub.sys driver for managing USB hubs. For more information about the relationship between the hub class driver and the USB stack, see [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md).
Usbhub3.sys

Usbhub3.inf

Windows 10 for desktop editions

Windows 8.1

Windows 8

Microsoft provides the Usbhub3.sys driver for managing SuperSpeed (USB 3.0) USB hubs.

The driver is loaded when a SuperSpeed hub is attached to an xHCI controller. See [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md).

CDC-Data (0Ah)
-
-
-
Recommended driver: [WinUSB (Winusb.sys)](winusb.md)
Smart Card (0Bh)
**SmartCardReader**

{50dd5230-ba8a-11d1-bf5d-0000f805f530}

Usbccid.sys (Obsolete)
Windows 10 for desktop editions

Windows 7

Windows Server 2008

Windows Vista

Microsoft provides the Usbccid.sys mini-class driver to manage USB smart card readers. For more information about smart card drivers in Windows, see [Smart Card Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff549003).

Note that for Windows Server 2003, Windows XP, and Windows 2000, special instructions are required for loading this driver because it might have been released later than the operating system.

**Note**  
Usbccid.sys driver has been replaced by UMDF driver, WUDFUsbccidDriver.dll.

 

WUDFUsbccidDriver.dll

WUDFUsbccidDriver.inf

Windows 8.1

Windows 8

WUDFUsbccidDriver.dll is a user-mode driver for USB CCID Smart Card Reader devices.
Content Security (0Dh)
-
-
-
Recommended driver: [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md). Some content security functionality is implemented in Usbccgp.sys. See [Content Security Features in Usbccgp.sys](content-security-features-in-the-composite-client-generic-parent-drive.md).
Video (0Eh)
**Image**

{6bdd1fc6-810f-11d0-bec7-08002be2092f}

Usbvideo.sys

Usbvideo.inf

Windows 10 for desktop editions

Windows Vista

Microsoft provides USB video class support by means of the Usbvideo.sys driver. For more information, see "USB Video Class Driver" under [AVStream Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff554228).
Note that for Windows XP, special instructions are required for loading this driver because it might have been released later than the operating system.

Personal Healthcare (0Fh)
-
-
-
Recommended driver: [WinUSB (Winusb.sys)](winusb.md)
Audio/Video Devices (10h)
-
-
-
Diagnostic Device (DCh)
-
-
-
Recommended driver: [WinUSB (Winusb.sys)](winusb.md)
Wireless Controller (E0h)
**Note**  Supports Subclass 01h and Protocol 01h

 

**Bluetooth**

{e0cbf06c-cd8b-4647-bb8a-263b43f0f974}

Bthusb.sys

Bth.inf

Windows 10 for desktop editions

Windows 10 Mobile
Windows 8.1

Windows 8

Windows 7

Windows Vista

Microsoft provides the Bthusb.sys miniport driver to manage USB Bluetooth radios. For more information, see [Bluetooth Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff536596).
Miscellaneous (EFh)
**Net**

{4d36e972-e325-11ce-bfc1-08002be10318}

**Note**  Supports SubClass 04h and Protocol 01h

 

Rndismp.sys

Rndismp.inf

Windows 10 for desktop editions

Windows 8.1

Windows 8

Windows 7

Windows Vista

Prior to Windows Vista, support for CDC is limited to the RNDIS-specific implementation of the Abstract Control Model (ACM) with a vendor-unique protocol (**bInterfaceProtocol**) value of 0xFF. The RNDIS facility centers the management of all 802-style network cards in a single class driver, Rndismp.sys. For a detailed discussion of remote NDIS, see [Overview of Remote NDIS](https://msdn.microsoft.com/library/windows/hardware/ff569967). The mapping of remote NDIS to USB is implemented in the Usb8023.sys driver. For further information about networking support in Windows, see the [Networking and Wireless Technologies](http://go.microsoft.com/fwlink/p/?linkid=8759) website.

Application Specific (FEh)
-
-
Recommended driver: [WinUSB (Winusb.sys)](winusb.md)
Vendor Specific (FFh)
-
-
Windows 10 for desktop editions

Windows 10 Mobile
Recommended driver: [WinUSB (Winusb.sys)](winusb.md)
 

## Related topics
[Microsoft-provided USB drivers](system-supplied-usb-drivers.md)  



