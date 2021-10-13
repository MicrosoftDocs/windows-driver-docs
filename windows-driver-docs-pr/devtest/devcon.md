---
title: Windows Device Console (Devcon.exe)
description: DevCon (Devcon.exe), the Device Console, is a command-line tool that displays detailed information about devices on computers running Windows.
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
ms.date: 04/20/2017
ms.localizationpriority: high 
---

# Windows Device Console (Devcon.exe)

> [!NOTE]
> Please use the [PnPUtil](pnputil.md) tool instead of DevCon.

DevCon (Devcon.exe), the Device Console, is a command-line tool that displays detailed information about devices on computers running Windows. You can use DevCon to enable, disable, install, configure, and remove devices.

DevCon runs on Microsoft Windows 2000 and later versions of Windows.

## Where can I download DevCon?

DevCon (Devcon.exe) is included when you install the WDK, Visual Studio, and the Windows SDK for desktop apps. For information about downloading the kits, see [Windows Hardware Downloads](../download-the-wdk.md).

- **Windows Driver Kit (WDK) 8 and Windows Driver Kit (WDK) 8.1** (installation path)
- *%WindowsSdkDir%\tools\x64\devcon.exe*
- *%WindowsSdkDir%\tools\x86\devcon.exe*
- *%WindowsSdkDir%\tools\arm\devcon.exe*

> [!NOTE]
> The Visual Studio environment variable, *%WindowsSdkDir%*, represents the path to the Windows kits directory where the kits are installed, for example, *C:\Program Files (x86)\Windows Kits\8.1*.

## In this section

- [DevCon Commands](devcon-general-commands.md)
- [DevCon Examples](devcon-examples.md)

## <span id="What_you_can_do_with_DevCon"></span><span id="what_you_can_do_with_devcon"></span><span id="WHAT_YOU_CAN_DO_WITH_DEVCON"></span>What you can do with DevCon


Windows driver developers and testers can use DevCon to verify that a driver is installed and configured correctly, including the proper INF files, driver stack, driver files, and driver package. You can also use the DevCon commands (enable, disable, install, start, stop, and continue) in scripts to test the driver.

DevCon is a command-line tool that performs device management functions on local computers and remote computers.

> [!NOTE]
> To run DevCon commands on a remote computer, the Group Policy setting must allow the Plug and Play service to run on the remote computer. On computers that run Windows Vista and Windows 7, the Group Policy disables remote access to the service by default. On computers that run Windows 8 and later operating systems, the remote access is unavailable.
 

Devcon features include:

-   **Display driver and device info** DevCon can display the following properties of drivers and devices on local computers, and remote computers (running Windows XP and earlier):
    -   Hardware IDs, compatible IDs, and device instance IDs. These identifiers are described in detail in [Device Identification Strings](../install/device-identification-strings.md).
    -   [Device setup classes](../install/overview-of-device-setup-classes.md)
    -   The devices in a device setup class
    -   INF files and device driver files
    -   Details of [driver packages](../install/components-of-a-driver-package.md)
    -   Hardware resources
    -   Device status
    -   Expected driver stack
    -   Third-party driver packages in the driver store
-   **Search for devices** DevCon can search for devices on a local or remote computer by hardware ID, device instance ID, or device setup class.

-   **Change device settings** DevCon can change the status or configuration of Plug and Play (PnP) devices on the local computer in the following ways:
    -   Enable a device
    -   Disable a device
    -   Update drivers (interactive and noninteractive)
    -   Install a device (create a devnode and install software)
    -   Remove a device from the device tree and delete its device stack
    -   Rescan for Plug and Play devices
    -   Add, delete, and reorder the hardware IDs of root-enumerated devices
    -   Change the upper and lower filter drivers for a device setup class
    -   Add and delete third-party driver packages from the driver store
-   **Restart the device or computer** DevCon can restart a local device, reboot the local system on demand, or reboot the local system if required for another DevCon operation.

## <span id="DevCon_source_code"></span><span id="devcon_source_code"></span><span id="DEVCON_SOURCE_CODE"></span>DevCon source code


The DevCon source code is also available so that you can examine the methods that DevCon uses to retrieve and change setup and configuration data. DevCon illustrates the use of [general setup functions](/previous-versions/ff544985(v=vs.85)), [device installation functions](/previous-versions/ff541299(v=vs.85)), and [PnP Configuration Manager functions](/previous-versions/ff549713(v=vs.85)). The source code for the [Device Console (DevCon) Tool](https://github.com/Microsoft/Windows-driver-samples/tree/master/setup/devcon) is available in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) repository on GitHub.

## <span id="related_topics"></span>Related topics


[DevCon Commands](devcon-general-commands.md)

[DevCon Examples](devcon-examples.md)

