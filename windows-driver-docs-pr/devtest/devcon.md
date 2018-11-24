---
title: Windows Device Console (Devcon.exe)
description: DevCon (Devcon.exe), the Device Console, is a command-line tool that displays detailed information about devices on computers running Windows.
ms.assetid: ac74200e-e2ae-40db-9fb7-5ea2e7760613
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
ms.localizationpriority: medium
---

# Windows Device Console (Devcon.exe)


DevCon (Devcon.exe), the Device Console, is a command-line tool that displays detailed information about devices on computers running Windows. You can use DevCon to enable, disable, install, configure, and remove devices.

DevCon runs on Microsoft Windows 2000 and later versions of Windows.

## <span id="ddk_devcon_tools"></span><span id="DDK_DEVCON_TOOLS"></span>


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Where can I download DevCon?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DevCon (Devcon.exe) is included when you install the WDK, Visual Studio, and the Windows SDK for desktop apps. For information about downloading the kits, see <a href="http://go.microsoft.com/fwlink/p/?linkid=290798" data-raw-source="[Windows Hardware Downloads](http://go.microsoft.com/fwlink/p/?linkid=290798)">Windows Hardware Downloads</a>.</p>
<p><strong>Windows Driver Kit (WDK) 8 and Windows Driver Kit (WDK) 8.1</strong> (installation path)</p>
<p>%WindowsSdkDir%\tools\x64\devcon.exe</p>
<p>%WindowsSdkDir%\tools\x86\devcon.exe</p>
<p>%WindowsSdkDir%\tools\arm\devcon.exe</p>
<div class="alert">
<strong>Note</strong>  The Visual Studio environment variable, %WindowsSdkDir%, represents the path to the Windows kits directory where the kits are installed, for example, C:\Program Files (x86)\Windows Kits\8.1.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

This section includes:

[DevCon Commands](devcon-general-commands.md)

[DevCon Examples](devcon-examples.md)

## <span id="What_you_can_do_with_DevCon"></span><span id="what_you_can_do_with_devcon"></span><span id="WHAT_YOU_CAN_DO_WITH_DEVCON"></span>What you can do with DevCon


Windows driver developers and testers can use DevCon to verify that a driver is installed and configured correctly, including the proper INF files, driver stack, driver files, and driver package. You can also use the DevCon commands (enable, disable, install, start, stop, and continue) in scripts to test the driver.

DevCon is a command-line tool that performs device management functions on local computers and remote computers.

**Note**  To run DevCon commands on a remote computer, the Group Policy setting must allow the Plug and Play service to run on the remote computer. On computers that run Windows Vista and Windows 7, the Group Policy disables remote access to the service by default. On computers that run WDK 8.1 and WDK 8, the remote access is unavailable.

 

Devcon features include:

-   **Display driver and device info** DevCon can display the following properties of drivers and devices on local computers, and remote computers (running Windows XP and earlier):
    -   Hardware IDs, compatible IDs, and device instance IDs. These identifiers are described in detail in [Device Identification Strings](https://msdn.microsoft.com/library/windows/hardware/ff541224).
    -   [Device setup classes](https://msdn.microsoft.com/library/windows/hardware/ff541509)
    -   The devices in a device setup class
    -   INF files and device driver files
    -   Details of [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff539954)
    -   Hardware resources
    -   Device status
    -   Expected driver stack
    -   Third-party driver packages in the driver store
-   **Search for devices** DevCon can search for installed and uninstalled devices on a local or remote computer by hardware ID, device instance ID, or device setup class.

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


The DevCon source code is also available so that you can examine the methods that DevCon uses to retrieve and change setup and configuration data. DevCon illustrates the use of [general setup functions](https://msdn.microsoft.com/library/windows/hardware/ff544985), [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299), and [PnP Configuration Manager functions](https://msdn.microsoft.com/library/windows/hardware/ff549713). The source code for the [Device Console (DevCon) Tool](http://go.microsoft.com/fwlink/p/?LinkId=617966) is available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

## <span id="related_topics"></span>Related topics


[DevCon Commands](devcon-general-commands.md)

[DevCon Examples](devcon-examples.md)

 

 






