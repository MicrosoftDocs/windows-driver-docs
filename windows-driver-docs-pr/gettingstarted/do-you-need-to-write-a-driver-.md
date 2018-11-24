---
title: Do you need to write a driver
description: Microsoft Windows contains built-in drivers for many device types. If there is a built-in driver for your device type, you won't need to write your own driver. Your device can use the built-in driver.
ms.assetid: B08994F9-9E60-4C49-BD5C-F5C128075D33
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Do you need to write a driver?


Microsoft Windows contains built-in drivers for many device types. If there is a built-in driver for your device type, you won't need to write your own driver. Your device can use the built-in driver.

## <span id="Built-in_drivers_for_USB_devices"></span><span id="built-in_drivers_for_usb_devices"></span><span id="BUILT-IN_DRIVERS_FOR_USB_DEVICES"></span>Built-in drivers for USB devices


If your device belongs to a device class that is defined by the USB Device Working Group (DWG), there may already be an existing Windows USB class driver for it. For more information, see [Drivers for the Supported USB Device Classes](https://msdn.microsoft.com/library/windows/hardware/ff538820).

## <span id="Built-in_drivers_for_other_devices"></span><span id="built-in_drivers_for_other_devices"></span><span id="BUILT-IN_DRIVERS_FOR_OTHER_DEVICES"></span>Built-in drivers for other devices


Currently, Microsoft provides built-in drivers for the following other types of devices:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Device Technology and Driver</th>
<th align="left">Built-in driver</th>
<th align="left">Windows support</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ACPI: ACPI driver</p></td>
<td align="left"><p>Acpi.sys</p></td>
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Microsoft provides support for basic ACPI device functionality by means of the Acpi.sys driver and ACPI BIOS. To enhance the functionality of an ACPI device, the vendor can supply a WDM function driver. For more information about Windows ACPI support, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536161" data-raw-source="[Supporting ACPI Devices](https://msdn.microsoft.com/library/windows/hardware/ff536161)">Supporting ACPI Devices</a> in the ACPI Design Guide.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Audio: Microsoft Audio Class driver</p></td>
<td align="left"><p>PortCls.sys</p></td>
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Microsoft provides support for basic audio rendering and audio capture via its Port Class driver (PortCls). It is the responsibility of the hardware vendor of an audio device, to provide an adapter driver to work with PortCls. The adapter driver includes initialization code, driver-management code (including the DriverEntry function) and a collection of audio miniport drivers. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff536829" data-raw-source="[Introduction to Port Class](https://msdn.microsoft.com/library/windows/hardware/ff536829)">Introduction to Port Class</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Buses: Native SD bus driver, native SD storage class driver, and storage miniport driver</p></td>
<td align="left"><p>sdbus.sys, sffdisk.sys, sffp_sd.sys</p></td>
<td align="left"><p>Windows Vista and later</p></td>
<td align="left"><p>Microsoft provides support for SD card readers as follows: The operating system provides support for SD host controllers that connect directly to the PCI bus. When the system enumerates an SD host controller, it loads a native SD bus driver (sdbus.sys). If a user inserts an SD memory card, Windows loads a native SD storage class driver (sffdisk.sys) and storage miniport driver (sffp_sd.sys) on top of the bus driver. If a user inserts an SD card with a different kind of function, such as GPS or wireless LAN, Windows loads a vendor-supplied driver for the device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HID: HID I2C driver</p></td>
<td align="left"><p>HIDI2C.sys</p></td>
<td align="left"><p>Windows 8 and later</p></td>
<td align="left"><p>Microsoft provides support for HID over I2C devices on SoC systems that support Simple Peripheral Bus (SPB) and general-purpose I/O (GPIO). It does so by means of the HIDI2C.sys driver. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj127208" data-raw-source="[HID over I2C](https://msdn.microsoft.com/library/windows/hardware/jj127208)">HID over I2C</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HID: Legacy game port driver</p></td>
<td align="left"><p>HidGame.sys, Gameenum.sys</p></td>
<td align="left"><p>Windows Vista</p>
<p>Windows Server 2003</p>
<p>Windows XP</p></td>
<td align="left"><p>In Windows Vista and earlier, Microsoft provided support for legacy (non-USB, non-Bluetooth, non-I2C) game ports by means of the HidGame.sys and Gameenum.sys drivers. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/jj126201" data-raw-source="[HID Transports Supported in Windows](https://msdn.microsoft.com/library/windows/hardware/jj126201)">HID Transports Supported in Windows</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HID: Legacy keyboard class driver</p></td>
<td align="left"><p>Kbdclass.sys</p></td>
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Microsoft provides support for legacy (non-USB, non-Bluetooth, non-I2C) keyboards by means of the Kbdclass.sys driver. For more information, see Keyboard and mouse HID client drivers. To enhance the functionality of a legacy keyboard, the vendor can supply a keyboard filter driver. For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=618052" data-raw-source="[Kbfiltr sample](http://go.microsoft.com/fwlink/p/?LinkId=618052)">Kbfiltr sample</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HID: Legacy mouse class driver</p></td>
<td align="left"><p>Mouclass.sys</p></td>
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Microsoft provides support for legacy (non-USB, non-Bluetooth, non-I2C) mice by means of the Mouclass.sys driver. Keyboard and mouse HID client drivers. To enhance the functionality of a legacy mouse, the vendor can supply a mouse filter driver. For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=618052" data-raw-source="[Moufiltr sample](http://go.microsoft.com/fwlink/p/?LinkId=618052)">Moufiltr sample</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HID: PS/2 (i8042prt) driver</p></td>
<td align="left"><p>I8042prt.sys</p></td>
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Microsoft provides support for legacy PS/2 keyboards and mice by means of the I8042.sys driver. To enhance the functionality of a PS/2 mouse or keyboard, the vendor can supply a keyboard or mouse filter driver. For more information, see the <a href="http://go.microsoft.com/fwlink/p/?LinkId=618052" data-raw-source="[Kbfiltr sample](http://go.microsoft.com/fwlink/p/?LinkId=618052)">Kbfiltr sample</a> and <a href="http://go.microsoft.com/fwlink/p/?LinkId=618052" data-raw-source="[Moufiltr sample](http://go.microsoft.com/fwlink/p/?LinkId=618052)">Moufiltr sample</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Imaging: Web Services for Devices (WSD) scan class driver</p></td>
<td align="left"><p>WSDScan.sys</p></td>
<td align="left"><p>Windows Vista and later</p></td>
<td align="left"><p>Microsoft provides support for web services scanners (that is, scanners that are meant to be used over the web) by means of the WSD scan driver (wsdscan.sys). However, a web services scanner device that supports WSD Distributed Scan Management must implement two web services protocols. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff553313" data-raw-source="[WIA with Web Services for Devices](https://msdn.microsoft.com/library/windows/hardware/ff553313)">WIA with Web Services for Devices</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Print: Microsoft Plotter Driver</p></td>
<td align="left"><p>Msplot</p></td>
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Microsoft provides support for plotters that support the Hewlett-Packard Graphics Language by means of the Microsoft Plotter Driver (Msplot). To enhance the functionality of a plotter, you can create a minidriver, which consists of one or more plotter characterization data (PCD) files. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff559833" data-raw-source="[Plotter Driver Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff559833)">Plotter Driver Minidrivers</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Print: Microsoft PostScript Printer Driver</p></td>
<td align="left"><p>Pscript</p></td>
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Microsoft provides support for PostScript printers by means of the PostScript Printer Driver (Pscript). To enhance the functionality of a PostScript printer, you can create a minidriver, which consists of one or more PostScript Printer Description (PPD) files and font (NTF) files. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561810" data-raw-source="[Pscript Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff561810)">Pscript Minidrivers</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Print: Microsoft Universal Printer Driver</p></td>
<td align="left"><p>Unidrv</p></td>
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Microsoft provides support for non-PostScript printers by means of the Universal Printer Driver (Unidrv). To enhance the functionality of a non-PostScript printer, you can create a minidriver, which consists of one or more generic printer description (GPD) files. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff556567" data-raw-source="[Microsoft Universal Printer Driver](https://msdn.microsoft.com/library/windows/hardware/ff556567)">Microsoft Universal Printer Driver</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Print: Microsoft v4 Printer Driver</p></td>
<td align="left"></td>
<td align="left"><p>Windows 8 and later</p></td>
<td align="left"><p>Beginning with Windows 8, Microsoft provides a single in-box class driver that supports PostScript and non-PostScript printers as well as plotters. This driver supersedes the Microsoft Plotter Driver, Microsoft Universal Printer Driver, and Microsoft PostScript Printer Driver. Used on its own, without modification, this printer driver provides basic printing support. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh706306" data-raw-source="[V4 Printer Driver](https://msdn.microsoft.com/library/windows/hardware/hh706306)">V4 Printer Driver</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Print: Microsoft XPS Printer Driver</p></td>
<td align="left"><p>XPSDrv</p></td>
<td align="left"><p>Windows Vista and later</p></td>
<td align="left"><p>Microsoft provides support for printing the XPS document format with the XPS Printer Driver (XPSDrv). This driver extends Microsoft&#39;s GDI-based, version 3 printer driver architecture to support consuming XML Paper Specification (XPS) documents. With an XPSDrv printer driver, the XPS Document format is used as a spool file format and as a document file format. Used on its own, without modification, the XPSDrv printer driver provides support for basic XPS printing. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564289" data-raw-source="[XPSDrv Printer Drivers](https://msdn.microsoft.com/library/windows/hardware/ff564289)">XPSDrv Printer Drivers</a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Sensors: Sensor HID class driver</p></td>
<td align="left"><p>SensorsHIDClassDriver.dll</p></td>
<td align="left"><p>Windows 8 and later</p></td>
<td align="left"><p>Microsoft provides support for motion, activity and other types of sensors by means of a HID class driver. Because Windows 8 includes this HID class driver, along with corresponding HID I2C and HID USB miniport drivers, you do not need to implement your own driver. You only need to report the usages described in this white paper, in the firmware for your sensor. Windows will use your firmware and its own HID driver to enable and initialize your sensor, and then furnish the relevant Windows APIs with access to your sensor.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Touch: Windows pointer device driver</p></td>
<td align="left"></td>
<td align="left"><p>Windows 8 and later</p></td>
<td align="left"><p>Microsoft provides support for pen and touch devices by means of an HID class driver. Because Windows 8 includes this HID class driver and corresponding HID I2C and HID USB miniport drivers, you do not need to implement your own driver. You only need to report the usages described in this white paper in the firmware for your pointer device. Windows will use your firmware and its own HID driver to enable touch and pointer capabilities for your device and furnish the Windows touch and pointer APIs with access to your device.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WPD: Media Transfer Protocol class driver</p></td>
<td align="left"><p>WpdMtpDr.dll, WpdMtp.dll,WpdMtpUs.dll, WpdConns.dll, and WpdUsb.sys</p></td>
<td align="left"><p>Windows Vista and later</p></td>
<td align="left"><p>Microsoft provides support for portable devices that require connectivity with Windows, such as music players, digital cameras, cellular phones, and health-monitoring devices, by means of the Media Transfer Protocol class driver. A vendor that uses this class driver must implement the MTP class protocol on the device. (For digital still cameras, your MTP implementation should be backward compatible with PTP.) For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff597573" data-raw-source="[Guidance for the Hardware Vendor](https://msdn.microsoft.com/library/windows/hardware/ff597573)">Guidance for the Hardware Vendor</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 





