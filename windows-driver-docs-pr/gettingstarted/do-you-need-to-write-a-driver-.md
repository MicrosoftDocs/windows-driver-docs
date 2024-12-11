---
title: Built-in Drivers for Windows Devices
description: Microsoft Windows contains built-in drivers for many device types. If there is a built-in driver for your device type, you won't need to write your own driver. Your device can use the built-in driver.
ms.date: 12/09/2024
ai-usage: ai-assisted
---

# Built-in Drivers for Windows Devices

Microsoft Windows contains built-in drivers for many device types. If there is a built-in driver for your device type, you won't need to write your own driver. Your device can use the built-in driver.

This article describes the built-in drivers that are available in Windows. It also describes the device types for which you can use these built-in drivers.

## Built-in drivers for USB devices

If your device belongs to a device class that is defined by the USB Device Working Group (DWG), there may already be an existing Windows USB class driver for it. For more information, see [Drivers for the Supported USB Device Classes](../usbcon/supported-usb-classes.md).

## Built-in drivers for other devices

Currently, Microsoft provides built-in drivers for the following other types of devices:

| Device Technology and Driver | Built-in Driver | Description|
| ----------| ----------- | -------------- | 
| ACPI: ACPI driver   | Acpi.sys  | Microsoft provides support for basic ACPI device functionality by means of the Acpi.sys driver and ACPI BIOS. To enhance the functionality of an ACPI device, the vendor can supply a WDM function driver. For more information about Windows ACPI support, see [Supporting ACPI Devices](../acpi/supporting-acpi-devices.md) in the ACPI Design Guide. |
| Audio: High Definition Audio       | Hdaudio.sys     | This driver supports High Definition Audio devices, enabling playback and recording of high-quality audio. It is compatible with a wide range of audio hardware. |
| Audio: Microsoft Audio Class driver | PortCls.sys | Microsoft provides support for basic audio rendering and audio capture via its Port Class driver (PortCls). It is the responsibility of the hardware vendor of an audio device, to provide an adapter driver to work with PortCls. The adapter driver includes initialization code, driver-management code (including the DriverEntry function) and a collection of audio miniport drivers. For more information, see [Introduction to Port Class](../audio/introduction-to-port-class.md). |
| Bluetooth: Bluetooth driver        | Bthport.sys     | The Bthport.sys driver enables Bluetooth functionality, allowing devices to connect wirelessly for data transfer and communication. It supports a variety of Bluetooth profiles. |
| Buses: Native SD bus driver, native SD storage class driver, and storage miniport driver | sdstor.sys | Microsoft provides support for SD card readers. If a user inserts an SD card with a different kind of function, such as GPS or wireless LAN, Windows loads a vendor-supplied driver for the device. |
| Display: Graphics driver           | dxgkrnl.sys     | The dxgkrnl.sys driver is part of the DirectX graphics kernel, providing support for rendering graphics in applications and games. It works with various graphics hardware to deliver high-performance visuals. |
| Network: Ethernet driver           | E1000.sys       | This driver supports Intel Ethernet network adapters, providing connectivity to wired networks. It includes features for network performance and reliability. |
| HID: HID I2C driver | HIDI2C.sys | Microsoft provides support for HID over I2C devices on SoC systems that support Simple Peripheral Bus (SPB) and general-purpose I/O (GPIO). It does so by means of the HIDI2C.sys driver. For more information, see [HID over I2C](../hid/hid-over-i2c-guide.md). |
| Imaging: Web Services for Devices (WSD) scan class driver              | WSDScan.sys|  Microsoft provides support for web services scanners (that is, scanners that are meant to be used over the web) by means of the WSD scan driver (wsdscan.sys). However, a web services scanner device that supports WSD Distributed Scan Management must implement two web services protocols. For more information, see [WIA with Web Services for Devices](../image/wia-with-web-services-for-devices.md).|
| Storage: SATA AHCI controller      | storahci.sys    | This driver supports Serial ATA (SATA) Advanced Host Controller Interface (AHCI) devices, enabling communication between the operating system and storage devices like hard drives and solid-state drives. |
| Sensors: Sensor HID class driver | SensorsHIDClassDriver.dll | Microsoft provides support for motion, activity and other types of sensors by means of a HID class driver. |
| Touch: Windows pointer device driver    | Microsoft provides support for pen and touch devices by means of an HID class driver.   |
| Windows Portable Devices| WinUsb.sys | Microsoft provides support for portable devices that require connectivity with Windows, such as music players, digital cameras, cellular phones, and health-monitoring devices.|







