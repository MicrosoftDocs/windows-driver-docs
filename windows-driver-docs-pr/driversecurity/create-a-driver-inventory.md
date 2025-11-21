---
title: Create Installed Driver Package Inventory
description: Learn how to create an inventory of installed driver packages to identify unnecessary drivers and reduce security risks. Use PnPUtil to audit your system.
ms.date: 11/15/2025
ms.topic: how-to
---

# Create an inventory of installed driver packages

This article shows you how to create an inventory of installed third-party [driver packages](../install/driver-packages.md) and identify unnecessary drivers that increase security risks. You learn how to use PnPUtil and PowerShell to audit your system and remove unwanted driver packages.

## Driver security - security risk reduction

## Why reduce driver security risks?

Why reduce your driver footprint? Each unnecessary driver on your system:

- Poses potential security risks.
- Consumes memory and system resources.
- Can cause system crashes.

By maintaining only essential drivers, you improve both security and stability.

When evaluating the driver security risks, consider all [driver packages](../install/driver-packages.md) present on the system, whether or not they're installed on devices. Knowing which driver packages are present (and which are third-party vs Microsoft) can help identify unwanted or out-of-date driver packages that might pose security risks.

One approach is to create an initial report of installed driver packages on a new system and then run the report again at regular intervals to look for any unexpected driver packages.

## Inventory of installed driver packages - PnPUtil

PnPUtil is built into Windows and is the recommended tool for managing driver packages. No additional downloads are required.

**Next step:** Learn the basic commands in the following section, or [view advanced PnPUtil examples](../devtest/pnputil-examples.md).

### PnPUtil /enum-drivers

Use `enum-drivers` to list third-party [driver packages](../install/driver-packages.md) in the [driver store](../install/driver-store.md).

```dotnetcli
pnputil /enum-drivers
```

Use `/files` to list all third-party driver packages and display the associated driver files.

```dotnetcli
pnputil /enum-drivers /files
```

## Export driver inventory reports with PnPUtil

Use the `/format` and `/output-file` options to create reports of your installed driver footprint. Use these options to script gathering the driver packages on the system. Don't use scripts to process the default output or the 'text' /format option since that output can change and is localized. The output is different depending on the language installed on the system.

`/format` - format output as text, XML, or CSV.
`/output-file [<filename>]` - write output to optional filename.

This example command uses the PnPUtil utility to enumerate all third-party driver packages currently present on the system. It includes information about the associated driver files and outputs the results in CSV (Comma-Separated Values) format. The output is saved to a file named *MyDriverFileInventory.CSV*.

```dotnetcli
pnputil /enum-drivers /files /format CSV /output-file MyDriverFileInventory.CSV
```

## Use PowerShell scripts to obtain additional information

Use these PowerShell scripts to find specific drivers on your system:

### Example 1: Find unused driver packages

This script identifies OEM driver packages that aren't installed on any devices (devices count = 0).

```powershell
$pnputilOutput = pnputil /enum-drivers /devices /format xml
$pnputilOutput.pnputil.driver | where {$_.devices.count -eq 0}
```

### Example 2: Find driver packages with specific file types

This script finds all OEM driver packages that contain files of a certain file extension, such as `.sys`.

```powershell
$pnputilOutput = pnputil /enum-drivers /devices /files /format xml
$pnputilOutput.pnputil.driver | where {$_.Files.File.Name -like "*.sys"}
$sysDrivers = $pnputilOutput.pnputil.driver | Where-Object {$_.Files.File.Name -like "*.sys"}
Write-Host "Found $($sysDrivers.Count) driver(s) with .sys files.`n"
```

## Windows images and virtual hard disks

For Windows image (.wim) files or virtual hard disks (.vhd or .vhdx), first use the [Deployment Image Servicing and Management utility (DISM)](/windows-hardware/manufacture/desktop/what-is-dism) `/Mount-Image` command. 

```PowerShell
Mount-WindowsImage -ImagePath "D:\Images\Windows11.vhdx" -Index 1 -Path "C:\Mount"
```

Then use the [Get-WindowsDriver commandlet](/powershell/module/dism/get-windowsdriver) to display information. Specify the mount path that you used.

```PowerShell
Get-WindowsDriver -Path "C:\Mount" 
```

The [Get-WindowsDriver commandlet](/powershell/module/dism/get-windowsdriver) can also list drivers in the booted Windows environment by using the `-Online` option.

```PowerShell
GetWindowsDriver -Online
```

## Other driver tools

Other tools are available, but they have limitations. Use [PnPUtil](../devtest/pnputil.md) and the [Get-WindowsDriver commandlet](/powershell/module/dism/get-windowsdriver) instead.

The Device Manager GUI provides views of driver information organized by device (**View** -> **Drivers by device**), or devices organized by driver information (**View** -> **Devices by driver**). This information includes the device type, device status, manufacturer, device-specific properties, and information about the driver files for a specific device. Use **View** -> **Show hidden devices** to display additional information. For more information, see [Using Device Manager](../install/using-device-manager.md). 

The System Information (Msinfo32.exe) tool lists drivers under **Software Environment**, **System Drivers**. The displayed columns are sortable, allowing for grouping of driver state or type. For more information, see [Description of Microsoft System Information (Msinfo32.exe) Tool](https://support.microsoft.com/topic/description-of-microsoft-system-information-msinfo32-exe-tool-10d335d8-5834-90b4-8452-42c58e61f9fc). Msinfo32 doesn't provide a way to list and parse driver packages. Use [PnPUtil](../devtest/pnputil.md) instead.

Although `driverquery` is built into Windows, it can produce misleading output and isn't recommended. Use the more capable [PnPUtil](../devtest/pnputil.md) instead.

## Remove drivers with PnPUtil

Remove unnecessary drivers by using PnPUtil to reduce security risks and increase system reliability. Before removing any driver, verify it's not essential for system operation.

*If* you determine that a driver can be removed safely, use PnPUtil to remove it. Use a non-critical PC to test that all hardware and software functions correctly after the driver is removed. As always, make use of backups and establish a system restore point.

Locate the OEM driver name, such as *oem42.inf*, and use the following command to delete it:

```dotnetcli
pnputil /delete-driver oem42.inf /uninstall 
```

Explanation of parameters:

`/delete-driver <INF>`: Specifies the driver to remove.

`/uninstall`: Uninstalls the driver from any devices currently using it.

> [!IMPORTANT]
> Make sure the driver isn't critical to system operation before removing it. Removing essential drivers can cause system instability and data loss.

### See also

- [PnPUtil reference](../devtest/pnputil.md) - Complete command documentation
- [PnPUtil command syntax](../devtest/pnputil-command-syntax.md) - Detailed syntax guide
