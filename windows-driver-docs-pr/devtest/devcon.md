---
title: Manage devices with DevCon command-line tool
description: Learn how to use DevCon (Devcon.exe), the Device Console command-line tool, to manage, configure, and troubleshoot Windows devices effectively.
keywords:
- DevCon WDK
- Device Console WDK
- driver testing WDK , DevCon
- testing drivers WDK , DevCon
- device information WDK DevCon
- searches WDK DevCon
- displaying device information
- change device configurations WDK DevCon
- manipulating devices WDK DevCon
- status changes WDK DevCon
- restarting devices
- device management WDK DevCon
- listing device information WDK
ms.date: 11/03/2025
ai-usage: ai-assisted
ms.topic: overview
---

# Manage devices with DevCon command-line tool

DevCon (Device Console) is a command-line tool that helps Windows driver developers and system administrators manage devices.

This tool is particularly useful for automating device management tasks, testing driver installations, and verifying device configurations in development and testing environments.

> [!IMPORTANT]
> Microsoft recommends using [PnPUtil](pnputil.md) instead of DevCon for new projects. PnPUtil ships with every Windows release and uses more reliable and secure APIs. For migration guidance, see [Replacing DevCon](devcon-migration.md).

## Quick start: Get DevCon running in five minutes

Ready to start managing devices with DevCon? Follow these steps:

1. **Download and install** the Windows Driver Kit (WDK) from [Windows Hardware Downloads](/windows-hardware/drivers/download-the-wdk).
2. **Navigate** to the installation directory (typically `C:\Program Files (x86)\Windows Kits\10\Tools\[version]\x64\`).
3. **Open Command Prompt** as Administrator.
4. **Run your first command**: `devcon find *` to list all devices.

For detailed installation paths and examples, see the sections below.

## Where to download DevCon

DevCon (Devcon.exe) is included when you install the WDK, Visual Studio, and the Windows SDK for desktop apps. For information about downloading the kits, see [Windows Hardware Downloads](/windows-hardware/drivers/download-the-wdk).

**Windows Driver Kit (WDK) 10 version** (installation path)

- *%WdkDir%\10\Tools\X.Y\x64\devcon.exe*
- *%WdkDir%\10\Tools\X.Y\x86\devcon.exe*
- *%WdkDir%\10\Tools\X.Y\arm64\devcon.exe*

The `%WdkDir%` represents the directory where you installed the WDK and `X.Y` refers to the version of the Windows Driver Kit. For example, if you have a recent WDK, the DevCon tool is located in the directory path `C:\Program Files (x86)\Windows Kits\10\Tools\10.0.26100.0\x64\devcon.exe` for 64-bit systems.

## What you can do with DevCon

Windows driver developers and testers can use DevCon to verify that a driver is installed and configured correctly, including the proper INF files, driver stack, driver files, and driver package. You can also use the DevCon commands (enable, disable, install, start, stop, and continue) in scripts to test the driver.

DevCon is a command-line tool that performs device management functions on local computers.

Devcon features include:

- **Display driver and device info** DevCon can display the following properties of drivers and devices on local computers:
  - Hardware IDs, compatible IDs, and device instance IDs. These identifiers are described in detail in [Device Identification Strings](../install/device-identification-strings.md).
  - [Device setup classes](../install/overview-of-device-setup-classes.md)
  - The devices in a device setup class
  - INF files and device driver files
  - Details of [driver packages](../install/components-of-a-driver-package.md)
  - Hardware resources
  - Device status
  - Expected driver stack
  - Third-party driver packages in the driver store
- **Search for devices** DevCon can search for devices on a local computer by hardware ID, device instance ID, or device setup class.

- **Change device settings** DevCon can change the status or configuration of Plug and Play (PnP) devices on the local computer in the following ways:
  - Enable a device
  - Disable a device
  - Update drivers (interactive and noninteractive)
  - Install a device (create a devnode and install software)
  - Remove a device from the device tree and delete its device stack
  - Rescan for Plug and Play devices
  - Add, delete, and reorder the hardware IDs of root-enumerated devices
  - Change the upper and lower filter drivers for a device setup class
  - Add and delete third-party driver packages from the driver store
- **Restart the device or computer** DevCon can restart a local device, reboot the local system on demand, or reboot the local system if required for another DevCon operation.

## DevCon capabilities and features

DevCon provides three main categories of device management functionality:

### View device information
- Display hardware IDs, compatible IDs, and device instance IDs
- Show device setup classes and driver details
- List INF files, driver files, and driver packages
- View hardware resources and device status

### Search and find devices
- Search by hardware ID, device instance ID, or device setup class
- List all devices or filter by specific criteria

### Modify device configuration
- **Enable or disable devices**—Control device state without Device Manager
- **Update drivers**—Install new drivers interactively or silently  
- **Install devices**—Create device nodes and install software
- **Remove devices**—Clean up device tree and driver stack
- **Manage driver packages**—Add or remove third-party drivers from the driver store
- **Restart devices**—Reboot devices or the entire system when needed

## DevCon source code

You can also access the DevCon source code to examine the methods that DevCon uses to retrieve and change setup and configuration data. DevCon illustrates the use of [general setup functions](/previous-versions/ff544985(v=vs.85)), [device installation functions](/previous-versions/ff541299(v=vs.85)), and [PnP Configuration Manager functions](/previous-versions/ff549713(v=vs.85)). The source code for the [Device Console (DevCon) Tool](https://github.com/Microsoft/Windows-driver-samples/tree/main/setup/devcon) is available in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) repository on GitHub.

## Related topics

### Essential guides

- **[DevCon Commands](devcon-general-commands.md)**—Complete command reference with syntax
- **[DevCon Examples](devcon-examples.md)**—Real-world usage scenarios and code samples

### Migration and alternatives  

- **[Replacing DevCon](devcon-migration.md)**—Transition to PnPUtil for new projects
- **[PnPUtil](pnputil.md)**—Microsoft's recommended modern alternative
