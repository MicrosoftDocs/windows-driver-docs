---
title: Installing a Boot-Start Driver
description: Installing a Boot-Start Driver
ms.assetid: 0b93233b-266c-4d2e-a5d8-01d2d477dd13
keywords:
- Device setup WDK device installations , boot drivers
- device installations WDK , boot drivers
- installing devices WDK , boot drivers
- boot drivers WDK device installations
- boot driver distribution disks WDK device installations
- distribution disks WDK
- platform-specific distribution disks WDK
- cross-platform distribution disks WDK
- vendor-supplied boot drivers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Boot-Start Driver





A [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) is a driver for a device that must be installed to start the Microsoft Windows operating system. Most boot-start drivers are included "in-the-box" with Windows, and Windows automatically installs these boot-start drivers during the text-mode setup phase of Windows installation. If a boot-start driver for a device is not included "in-the-box" with Windows, a user can install an additional vendor-supplied boot-start driver for the device during text-mode setup.

To install a device that is required to start Windows, but whose driver is not included with the operating system, a user must do the following:

1.  Install the device hardware and turn on the computer.

2.  Begin your Windows installation (run the Windows setup program). During the text-mode phase of the installation (at the beginning of the installation), Windows displays a message that indicates that you can press a specific **F***n* key to install a boot-start driver.

3.  When Windows displays this message, press the specified **F***n* key to install the boot-start driver and then insert a [boot-start driver distribution disk](#boot-start-driver-distribution-disk).

**Note**  This procedure demonstrates how you can install a driver that is not included "in-the-box" with Windows. Do not use this procedure to replace or update a driver that is included with Windows. Instead, wait until Windows starts and use Device Manager to perform an "update driver" operation on the device.



When Windows fails to start, certain error messages that are displayed can indicate that a boot-start driver is missing. The following table describes several error messages and their possible causes.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Error message</th>
<th align="left">Possible cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Inaccessible boot device</p></td>
<td align="left"><p>The boot disk is a third-party mass-storage device that requires a driver that is not included with Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Setup could not determine your machine type</p></td>
<td align="left"><p>A new HAL driver is required. This error does not occur on most machines, but it might occur on a high-end server.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Setup could not find any hard drives in your computer</p></td>
<td align="left"><p>The required boot device drivers for the hard drives are not loaded.</p></td>
</tr>
</tbody>
</table>



### <a href="" id="boot-start-driver-distribution-disk"></a> Boot-Start Driver Distribution Disk

A *boot-start driver distribution disk* is a medium, such as a floppy disk or USB flash drive, that contains a *TxtSetup.oem* file and the related driver files. The *TxtSetup.oem* file is a text file that contains a list of hardware components, a list of files on the distribution disk that will be copied to the system, and a list of registry keys and values that will be created. A sample *TxtSetup.oem* file is provided with the Windows Driver Kit (WDK), under the \\src directory of the WDK. For details about the contents of a *TxtSetup.oem* file, see [TxtSetup.oem File Format](https://msdn.microsoft.com/library/windows/hardware/ff553509).

The following requirements and recommendations apply to platform-specific and cross-platform distributions disks:

- Platform-specific distribution disks (Windows Server 2003 and earlier)

  Windows requires a platform-specific distribution disk for each platform that a driver supports. A platform-specific distribution disk contains one *TxtSetup.oem* file and the related driver files. The *TxtSetup.oem* file must be located in the root directory of the distribution disk.

- Cross-platform and platform-specific distribution disks (Windows Server 2003 Service Pack 1 (SP1) and later versions)

  Windows supports cross-platform distribution disks that contain two or more platform-specific *TxtSetup.oem* files and the related driver files.

  To distinguish between platforms on a cross-platform distribution disk, use the platform directories that are listed in the following table.

  <table>
  <colgroup>
  <col width="33%" />
  <col width="33%" />
  <col width="33%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th align="left">Platform</th>
  <th align="left">Platform directory</th>
  <th align="left">Default directory</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td align="left"><p>x86-based</p></td>
  <td align="left"><p>A:\i386</p></td>
  <td align="left"><p>A:\\</p></td>
  </tr>
  <tr class="even">
  <td align="left"><p>Itanium-based</p></td>
  <td align="left"><p>A:\ia64</p></td>
  <td align="left"><p>A:\\</p></td>
  </tr>
  <tr class="odd">
  <td align="left"><p>x64-based</p></td>
  <td align="left"><p>A:\amd64</p></td>
  <td align="left"><p>A:\\</p></td>
  </tr>
  </tbody>
  </table>




On a cross-platform distribution disk, Windows uses the platform-specific *TxtSetup.oem* file that is located in the platform directory that corresponds to the platform on which Windows is running. If a corresponding platform directory that contains a platform-specific *TxtSetup.oem* file does not exist, Windows uses the *TxtSetup.oem* file in the default directory, if one is present.

Windows also supports platform-specific distribution disks. A platform-specific distribution disk contains one platform-specific *TxtSetup.oem* file and the related driver files. The *TxtSetup.oem* file must be located either in its corresponding platform directory, as is done for cross-platform distribution disks, or in the default directory of the distribution disk.

The driver files for a given platform on a cross-platform distribution disk or on a platform-specific distribution disk must be located relative to the directory that contains the platform-specific *TxtSetup.oem* file.

**Tip**  Although not required, we recommend that a *TxtSetup.oem* file always be placed in a corresponding platform directory. Using platform directories eliminates the possibility that Windows might attempt to use a *TxtSetup.oem* file that is incompatible with the platform on which Windows is running. For example, if a user attempts an unattended installation on a platform with a distribution disk that does not contain a corresponding platform directory, Windows cannot determine whether the *TxtSetup.oem* file in the default directory is compatible with the platform. If a driver fails to load because the driver is incompatible with the platform, Windows displays an error message and terminates the unattended installation.












