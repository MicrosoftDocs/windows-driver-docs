---
title: USB device class drivers included in Windows
description: This topic lists the Microsoft-provided drivers for the supported USB device classes.
ms.date: 02/17/2023
---

# USB device class drivers included in Windows

> [!IMPORTANT]
> This topic is for programmers. If you are a customer experiencing USB problems, see [Troubleshoot common USB problems](https://support.microsoft.com/help/17614/windows-10-troubleshoot-common-usb-problems)

This topic lists the Microsoft-provided drivers for the supported USB device classes.

- Microsoft-provided drivers for USB-IF approved device classes.
- For composite devices, use [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md) that creates physical device objects (PDOs) for each function.
- For non-composite devices or a function of a composite device, use [WinUSB (Winusb.sys)](winusb.md).

**If you are installing USB drivers:** You do not need to download USB device class drivers. They are installed automatically. These drivers and their installation files are included in Windows. They are available in the \\Windows\\System32\\DriverStore\\FileRepository folder. The drivers are updated through Windows Update.

**If you are writing a custom driver:** Before writing a driver for your USB device, determine whether a Microsoft-provided driver meets the device requirements. If a Microsoft-provided driver is not available for the USB device class to which your device belongs, then consider using generic drivers, Winusb.sys or Usbccgp.sys. Write a driver only when necessary. More guidelines are included in [Choosing a driver model for developing a USB client driver](winusb-considerations.md).

## USB device classes

*USB device classes* are categories of devices with similar characteristics and that perform common functions. Those classes and their specifications are defined by the USB-IF. Each device class is identified by USB-IF approved class, subclass, and protocol codes, all of which are provided by the IHV in device descriptors in the firmware. Microsoft provides in-box drivers for several of those device classes, called *USB device class drivers*. If a device that belongs to a supported device class is connected to a system, Windows automatically loads the class driver, and the device functions with no additional driver required.

Hardware vendors should not write drivers for the supported device classes. Windows class drivers might not support all of the features that are described in a class specification. If some of the device's capabilities are not implemented by the class driver, vendors should provide supplementary drivers that work in conjunction with the class driver to support the entire range of functionality provided by the device.

For general information about USB-IF approved device classes see the [USB Common Class Specification](https://usb.org/sites/default/files/usbccs10.pdf)

The current list of USB class specifications and class codes is documented in the [USB-IF Defined Class Code List](https://www.usb.org/defined-class-codes).

## Device setup classes

Windows categorizes devices by *device setup classes*, which indicate the functionality of the device.

Microsoft defines setup classes for most devices. IHVs and OEMs can define new device setup classes, but only if none of the existing classes apply. For more information, see [System-Defined Device Setup Classes](../install/system-defined-device-setup-classes-reserved-for-system-use.md).

Two important device setup classes for USB devices are as follows:

- **USBDevice** {88BAE032-5A81-49f0-BC3D-A4FF138216D6}: IHVs must use this class for custom devices that do not belong to another class. This class is not used for USB host controllers and hubs.

- **USB** {36fc9e60-c465-11cf-8056-444553540000}: IHVs must not use this class for their custom devices. This is reserved for USB host controllers and USB hubs.

The device setup classes are different from USB device classes discussed earlier. For example, an audio device has a USB device class code of 01h in its descriptor. When connected to a system, Windows loads the Microsoft-provided class driver, *Usbaudio.sys*. In Device Manager, the device is shown under is **Sound, video and game controllers**, which indicates that the device setup class is Media.

## Microsoft-provided USB device class drivers

| USB-IF class code | Device setup class | Microsoft-provided<br>driver and INF | Windows support | Description |
|---|---|---|---|---|
| Audio (01h) | **Media**<br>{4d36e96c-e325-11ce-bfc1-08002be10318} | Usbaudio.sys<br>Wdma_usb.inf | Windows 11<br><br>Windows 10 for desktop editions (Home, Pro, Enterprise, and Education)<br><br>Windows 10 Mobile<br><br>Windows 8.1 | Microsoft provides support for the USB audio device class by means of the Usbaudio.sys driver. For more information, see "USBAudio Class System Driver" in [Kernel-Mode WDM Audio Components](/windows-hardware/drivers/audio/kernel-mode-wdm-audio-components). For more information about Windows audio support, see the [Audio Device Technologies for Windows](/windows-hardware/drivers/audio/) website. |
| Communications and CDC Control (02h) | **Ports**<br>{4D36E978-E325-11CE-BFC1-08002BE10318} | Usbser.sys<br>Usbser.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 10 Mobile | In Windows 10, a new INF, Usbser.inf, has been added that loads Usbser.sys automatically as the function driver.<br><br>For more information, see [USB serial driver (Usbser.sys)](usb-driver-installation-based-on-compatible-ids.md) |
| Communications and CDC Control (02h) | **Modem**<br>{4D36E96D-E325-11CE-BFC1-08002BE10318}<br><br>Supports Subclass 02h (ACM) | Usbser.sys<br><br>Custom INF that references mdmcpq.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 8.1 | In Windows 8.1 and earlier versions, Usbser.sys is not automatically loaded. To load the driver, you need to write an INF that references the modem INF (mdmcpq.inf) and includes [Install] and [Needs] sections.You can enable CDC and Wireless Mobile CDC (WMCDC) support by setting a registry value, as described in [Support for the Wireless Mobile Communication Device Class](support-for-interface-collections.md).When CDC support is enabled, the [USB Common Class Generic Parent Driver](usb-common-class-generic-parent-driver.md) enumerates interface collections that correspond to CDC and WMCDC Control Models, and assigns physical device objects (PDO) to these collections. |
| Communications and CDC Control (02h) | **Net**<br>{4d36e972-e325-11ce-bfc1-08002be10318}<br><br>Supports Subclass 0Dh (NCM) | UsbNcm.sys<br>UsbNcm.inf | Windows 11<br><br>Windows Server 2022 | Microsoft provides the UsbNcm.sys driver to operate devices that comply with [Usb NCM](https://www.usb.org/document-library/network-control-model-devices-specification-v10-and-errata-and-adopters-agreement). The source code for this driver is available at [NCM-Driver-for-Windows](https://github.com/microsoft/NCM-Driver-for-Windows). |
| Communications and CDC Control (02h) | **Net**<br>{4d36e972-e325-11ce-bfc1-08002be10318}<br><br>Supports Subclass 0Eh (MBIM) | cxwmbclass.sys<br>wmbclass.sys<br>Netwmbclass.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 8.1 | Microsoft provides the wmbclass.sys driver, for mobile broadband devices. See, [MB Interface Model](/windows-hardware/drivers/network/mb-interface-model). |
| HID (Human Interface Device) (03h) | **HIDClass**<br>{745a17a0-74d3-11d0-b6fe-00a0c90f57da} | Hidclass.sys<br>Hidusb.sys<br>Input.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 10 Mobile<br><br>Windows 8.1 | Microsoft provides the HID class driver (Hidclass.sys) and the miniclass driver (Hidusb.sys) to operate devices that comply with the [USB HID Standard](https://go.microsoft.com/fwlink/p/?LinkId=761243). For more information, see [HID Architecture](/windows-hardware/drivers/hid/hid-architecture) and [Minidrivers and the HID class driver](/windows-hardware/drivers/hid/minidriver-operations). For further information about Windows support for input hardware, see the [Input and HID - Architecture and Driver Support](/windows-hardware/drivers/hid/) website. |
| Physical (05h) | - | - | - | Recommended driver: [WinUSB (Winusb.sys)](winusb.md) |
| Image (06h) | **Image**<br>{6bdd1fc6-810f-11d0-bec7-08002be2092f} | Usbscan.sys<br>Sti.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 8.1 | Microsoft provides the Usbscan.sys driver that manages USB digital cameras and scanners for Windows XP and later operating systems. This driver implements the USB component of the Windows Imaging Architecture (WIA). For more information about WIA, see [Windows Image Acquisition Drivers](/windows-hardware/drivers/image/windows-image-acquisition-drivers) and the [Windows Imaging Component](/windows-hardware/drivers/image/) website. For a description of the role that Usbscan.sys plays in the WIA, see [WIA Core Components](/windows-hardware/drivers/image/wia-core-components). |
| Printer (07h) | **USB**<br>Usbprint.sys enumerates printer devices under the device set up class: **Printer** {4d36e979-e325-11ce-bfc1-08002be10318}. | Usbprint.sys<br>Usbprint.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 8.1 | Microsoft provides the Usbprint.sys class driver that manages USB printers. For information about implementation of the printer class in Windows, see the [Printing - Architecture and Driver Support](/windows-hardware/drivers/print/) website. |
| Mass Storage (08h) | **USB** | Usbstor.sys | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 10 Mobile<br><br>Windows 8.1 | Microsoft provides the Usbstor.sys port driver to manage USB mass storage devices with Microsoft's native storage class drivers. For an example device stack that is managed by this driver, see [Device Object Example for a USB Mass Storage Device](/windows-hardware/drivers/storage/device-object-example-for-a-usb-mass-storage-device). For information about Windows storage support, see the [Storage Technologies](/windows-hardware/drivers/storage/) website. |
| Mass Storage (08h) | **SCSIAdapter**<br>{4d36e97b-e325-11ce-bfc1-08002be10318} | SubClass (06) and Protocol (62)Uaspstor.sys<br>Uaspstor.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 10 Mobile<br><br>Windows 8.1 | Uaspstor.sys is the class driver for SuperSpeed USB devices that support bulk stream endpoints. |
| Hub (09h) | **USB**<br>{36fc9e60-c465-11cf-8056-444553540000} | Usbhub.sys<br>Usb.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 10 Mobile<br><br>Windows 8.1 | Microsoft provides the Usbhub.sys driver for managing USB hubs. For more information about the relationship between the hub class driver and the USB stack, see [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md). |
| Hub (09h) | **USB**<br>{36fc9e60-c465-11cf-8056-444553540000} | Usbhub3.sys<br>Usbhub3.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 8.1 | Microsoft provides the Usbhub3.sys driver for managing SuperSpeed (USB 3.0) USB hubs.The driver is loaded when a SuperSpeed hub is attached to an xHCI controller. See [USB host-side drivers in Windows](usb-3-0-driver-stack-architecture.md). |
| CDC-Data (0Ah) | - | - | - | Recommended driver: [WinUSB (Winusb.sys)](winusb.md) |
| Smart Card (0Bh) | **SmartCardReader**<br>{50dd5230-ba8a-11d1-bf5d-0000f805f530} | Usbccid.sys (Obsolete) | Windows 10 for desktop editions | Microsoft provides the Usbccid.sys mini-class driver to manage USB smart card readers. For more information about smart card drivers in Windows, see [Smart Card Design Guide](/windows-hardware/drivers/smartcard/index).<br><br>Usbccid.sys driver has been replaced by UMDF driver, WUDFUsbccidDriver.dll. |
| Smart Card (0Bh) | **SmartCardReader**<br>{50dd5230-ba8a-11d1-bf5d-0000f805f530} | WUDFUsbccidDriver.dll<br>WUDFUsbccidDriver.inf | Windows 8.1 | WUDFUsbccidDriver.dll is a user-mode driver for USB CCID Smart Card Reader devices. |
| Content Security (0Dh) | - | - | - | Recommended driver: [USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md). Some content security functionality is implemented in Usbccgp.sys. See [Content Security Features in Usbccgp.sys](content-security-features-in-the-composite-client-generic-parent-drive.md). |
| Video (0Eh) | **Image**<br>{6bdd1fc6-810f-11d0-bec7-08002be2092f} | Usbvideo.sys<br>Usbvideo.inf | Windows 11<br><br>Windows 10 for desktop editions | Microsoft provides USB video class support by means of the Usbvideo.sys driver. For more information, see "USB Video Class Driver" under [AVStream Minidrivers](/windows-hardware/drivers/stream/avstream-minidrivers-design-guide). |
| Personal Healthcare (0Fh) | - | - | - | Recommended driver: [WinUSB (Winusb.sys)](winusb.md) |
| Audio/Video Devices (10h) | - | - | - | - |
| Diagnostic Device (DCh) | - | - | - | Recommended driver: [WinUSB (Winusb.sys)](winusb.md) |
| Wireless Controller (E0h)<br><br>Supports Subclass 01h and Protocol 01h | Bluetooth{e0cbf06c-cd8b-4647-bb8a-263b43f0f974} | Bthusb.sys<br>Bth.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 10 Mobile | Microsoft provides the Bthusb.sys miniport driver to manage USB Bluetooth radios. For more information, see [Bluetooth Design Guide](/previous-versions/windows/hardware/drivers/ff536596(v=vs.85)). |
| Miscellaneous (EFh) | **Net**<br>{4d36e972-e325-11ce-bfc1-08002be10318}<br><br>Supports SubClass 04h and Protocol 01h | Rndismp.sys<br>Rndismp.inf | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 8.1 | Microsoft recommends that hardware vendors build USB NCM compatible devices instead. USB NCM is a public USB-IF protocol that offers better throughput performance.<br><br>The RNDIS facility centers the management of all 802-style network cards in a single class driver, Rndismp.sys. For a detailed discussion of remote NDIS, see [Overview of Remote NDIS](/windows-hardware/drivers/network/overview-of-remote-ndis--rndis-). The mapping of remote NDIS to USB is implemented in the Usb8023.sys driver. For further information about networking support in Windows, see [Networking and Wireless Technologies](/windows-hardware/drivers/network/). |
| Application Specific (FEh) | - | - | - | Recommended driver: [WinUSB (Winusb.sys)](winusb.md) |
| Vendor Specific (FFh) | - | - | Windows 11<br><br>Windows 10 for desktop editions<br><br>Windows 10 Mobile | Recommended driver: [WinUSB (Winusb.sys)](winusb.md) |

## Related topics

- [Microsoft-provided USB drivers](system-supplied-usb-drivers.md)
