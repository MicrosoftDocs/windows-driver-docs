---
title: Printer Installation and the Plug and Play Manager
description: Printer Installation and the Plug and Play Manager
ms.assetid: 1edc92f1-fcd9-4af0-957d-cd7ff2e40125
keywords:
- Plug and Play manager WDK print
- duplicate installation detection WDK print
- detecting duplicate printer installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Printer Installation and the Plug and Play Manager





The Plug and Play manager handles all Plug and Play events for the machine, and is generic to all devices. The Plug and Play manager is documented in [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125). [Introduction to Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff548102) gives an overview of Plug and Play installation, and of how the various kernel-mode and user-mode components interact.

### <a href="" id="printer-installation-differences-between-windows-98-me-and-windows-200"></a>Printer Installation Differences between Windows 98/Me and Windows 2000 and Later

The Plug and Play architecture on Windows 2000 and later differs from that on Windows 95/98/Me. The most significant differences are:

-   The drivers included with Windows 2000 and later are contained in a file, driver.cab, that is installed when the operating system is installed. This file contains all of the Plug and Play in-box drivers for all types of devices, so the user normally does not need the original installation media to install a driver.

-   Little or no user intervention is required to install a particular driver. If a Windows 2000 or later driver that is digitally signed by Microsoft is in driver.cab or already installed on the machine, Plug and Play verifies the driver's signature and installs the driver with no user intervention. This type of installation is called server-side installation. If the driver is not available on the system, or it is not signed, or the driver installation requires interaction with the user (through user interface elements), Plug and Play reverts to a client-side installation. For more information about each type of installation, see the discussion of the user-mode PnP manager in [Device Installation Components](https://msdn.microsoft.com/library/windows/hardware/ff541277). In most cases, when a machine is booted with a new Plug and Play device connected to it, the device is installed and ready to use by the time the user logs on.

If the user must be able to choose which driver to install, you can use an InteractiveInstall directive in the [**INF ControlFlags section**](https://msdn.microsoft.com/library/windows/hardware/ff546342). This directive can be used only in the following two circumstances:

1.  To install devices that have incorrectly defined hardware IDs. This can occur when a hardware device has a corrupted hardware ID, or when a hardware vendor assigns the same hardware ID to two different devices, which is an error in hardware design.

2.  To install a driver for a device that cannot use the generic class installer or a driver supplied with the operating system.

If hardware IDs or compatible IDs are listed with the InteractiveInstall directive, Setup defers installation of printers matching those IDs to the client side, so the installation is delayed until an administrator logs on. The administrator is prompted to install the correct driver files. This is useful if two printer drivers share the same [*device ID*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-id), but require different drivers.

In contrast to Windows 2000 and later, Windows 95/98/Me Plug and Play installs devices without user intervention only if there is a [*hardware ID*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-id) (rank-0) match. When there is a [*compatible ID*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-compatible-id) (rank-1) match for the driver of a Plug and Play device, but no hardware ID match, the user is prompted to select the correct driver from the installation media. (This means that the user must have the installation media in order to install the driver.)

Also on Windows 95/98/Me, when a driver is written for multiple devices (or for similar devices on multiple buses), the user is always prompted for installation if only the compatible ID was listed, unless every possible hardware ID is listed with a duplicate driver entry in the INF file.

### Duplicate Installation Detection

When Setup calls the printer class installer to install a printer, the class installer determines whether the printer has already been manually installed. It does this by looking for exact matches between the driver and port names of currently installed printers and those listed in the INF file. If the class installer finds an installed print queue whose driver and port names match these two parameters, it does not install a second print queue, but instead associates it with the [*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode) entry. This prevents creating a second print queue for the same device.

A number of popular printer models share the same hardware ID (the HP DeskJet series, for example). On Windows 95/98/Me, if a user manually installs a DeskJet model that is subsequently detected by Plug and Play, a second print queue is installed if the user selects the appropriate driver. If the user does not select a driver, then he or she is prompted to do so every time the computer reboots.

Windows 2000 and later avoids this behavior by listing all printers with both a [*hardware ID*](https://msdn.microsoft.com/library/windows/hardware/ff556288#wdkgloss-hardware-id) and [*compatible ID*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-compatible-id) match. When multiple matches are found, the class installer checks to see whether there is already a print queue with the same hardware ID match. If there is, the Plug and Play manager does not install a second queue. If not, the hardware ID match is downgraded to a compatible ID match. If these hardware IDs are also listed in the InteractiveInstall entry (see [**INF ControlFlags Section**](https://msdn.microsoft.com/library/windows/hardware/ff546342)) of the INF file, the user is prompted to select a driver.

 

 




