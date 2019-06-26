---
title: Device and Driver Technologies
description: This section contains information about each of the supported Windows driver technologies.
ms.assetid: 1ef3e216-1322-42c3-b070-94cddfb2133c
ms.date: 01/30/2018
ms.localizationpriority: medium
---

# Device and Driver Technologies

This section contains information about each of the supported Windows driver technologies. The majority of the driver technology information is the same for all editions of Windows 10. When you must make special considerations for a particular edition of Windows, such as for Windows 10 Mobile, we explicitly called these out in each technology area. For general information about developing drivers see [Write your first driver](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/writing-your-first-driver).

## Universal Windows drivers

You can create a Universal Windows driver—a driver that uses a subset of the interfaces that are available to a Windows driver—to run on all editions of Windows 10. Where possible, use a Universal Windows driver to enable deployment of your drivers on multiple devices. For more information about how to build, install, deploy, and debug a Universal Windows driver for Windows 10, see [Getting Started with Universal Windows drivers](https://docs.microsoft.com/windows-hardware/drivers/develop/getting-started-with-universal-drivers) and [Deploying a Driver to a Test Computer](https://docs.microsoft.com/windows-hardware/drivers/develop/deploying-a-driver-to-a-test-computer).

## Device drivers and Windows 10 for desktop computers

For information about the tools used to develop desktop drivers, see [Driver Development Tools](https://docs.microsoft.com/windows-hardware/drivers/devtest/) and [Tools for Verifying Drivers](https://docs.microsoft.com/windows-hardware/drivers/devtest/tools-for-verifying-drivers). For information about deploying drivers to Windows 10 on a desktop, see [Distributing a driver package](https://docs.microsoft.com/windows-hardware/drivers/develop/distributing-a-driver-package-win8). For information about troubleshooting driver configuration, see [Troubleshoot Driver Configuration](https://docs.microsoft.com/windows-hardware/drivers/develop/troubleshooting-configuration-of-driver-deployment--testing-and-debugging).

## Device drivers and Windows 10 Mobile

Windows 10 Mobile is optimized for the unique needs of mobile devices. Instead of copying the driver to the desktop or installing it using Device Manager, you add a driver to the OS on a mobile device by using a package. For more information about working with packages see [Creating mobile packages](https://docs.microsoft.com/previous-versions/windows/hardware/packaging/dn756642(v=vs.85)). Also, a driver on a mobile device needs to be signed using a specific process to maintain integrity of the OS, as explained in [Mobile code signing](https://docs.microsoft.com/previous-versions/windows/hardware/code-signing/dn756634(v=vs.85)). For a walkthrough of adding a device driver to a mobile device such as a phone, see [Adding a driver to a test image](https://docs.microsoft.com/previous-versions/mt131832(v=vs.85)).

## In this section

- [3D print devices](3dprint/index.md)
- [Advanced Configuration and Power Interface (ACPI)](acpi/index.md)
- [Audio devices](audio/index.md)
- [Battery devices](battery/index.md)
- [Biometric devices](biometric/index.md)
- [Bluetooth devices](bluetooth/index.md)
- [Display devices (adapters and monitors)](display/index.md)
- [GNSS devices (location)](gnss/index.md)
- [Hardware notifications](gpiobtn/index.md)
- [Human Input Devices (HID)](hid/index.md)
- [Imaging devices (scanner)](image/index.md)
- [Installable File System Drivers](ifs/index.md)
- [Kernel-mode driver technology](kernel/index.md)
- [Mobile broadband](mobilebroadband/index.md)
- [Multifunction device drivers](multifunction/index.md)
- [NetAdapterCx drivers](netcx/index.md)
- [Network drivers](network/index.md)
- [NFC device drivers](nfc/index.md)
- [Parallel port drivers](parports/index.md)
- [Partner application development](partnerapps/index.md)
- [PCI drivers](pci/index.md)
- [PCMCIA drivers](pcmcia/index.md)
- [Point of Service (POS) drivers](pos/index.md)
- [Power management technologies](powermeter/index.md)
- [Print devices](print/index.md)
- [SD card bus drivers](sd/index.md)
- [Sensor drivers](sensors/index.md)
- [Serial port drivers](serports/index.md)
- [Smart card reader device drivers](smartcard/index.md)
- [Simple Peripheral Bus (SPB) drivers](spb/index.md)
- [Storage device drivers](storage/index.md)
- [Streaming media device drivers](stream/index.md)
- [Test Authoring and Execution Framework (TAEF)](taef/index.md)
- [Universal Serial Bus (USB)](usbcon/index.md)
- [Windows Device Testing Framework (WDTF)](wdtf/index.md)
- [Windows Hardware Error Architecture (WHEA)](whea/index.md)
