---
title: Mapping Driver Files
description: Mapping Driver Files
ms.assetid: 9a13a6a9-b585-4be1-b7c8-da65fa3ba6c6
keywords: ["mapping driver files", "driver replacement map", "driver replacement map, overview", "driver replacement map, file format", "driver replacement map, replacing boot drivers", "boot driver replacement"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Mapping Driver Files


## <span id="ddk_mapping_driver_files_dbg"></span><span id="DDK_MAPPING_DRIVER_FILES_DBG"></span>


Replacing driver files can be difficult. Frequently, you have to boot to the Microsoft Windows *safe build*, replace the driver binary, and then boot again.

However, Windows XP and later versions of Windows support a simpler method of replacing driver files. You can use this method to replace any kernel-mode driver (including display drivers), any Windows subsystem driver, or any other kernel-mode module. For simplicity, these files are called *drivers* in this topic, even though you can use this method for any kernel-mode module.

You can use this method whenever WinDbg or KD is attached as a kernel debugger. You can also use this method on a boot driver, but it is more difficult. For more information about how to use this method with boot drivers, see Replacing Boot Drivers.

To use a driver replacement map to replace driver files, do the following:

1.  Create a *driver replacement map file*. This file is a text file that lists the drivers on the target computer and their replacement drivers on the host computer. You can replace any number of drivers. For example, you might create a file that is named Mymap.ini in the d:\\Map\_Files directory of your host computer that contains the following information.

    ```ini
    map
    \Systemroot\system32\drivers\videoprt.sys
    \\myserver\myshare\new_drivers\videoprt.sys
    ```

    For more information about the syntax of this file, see Driver Replacement Map File Format.

2.  Set up a kernel debugging connection to the target computer, and start the kernel debugger (KD or WinDbg) on your host computer. (You do not have to actually break in to the target computer.)

3.  Load the driver replacement map file by doing one of the following:
    -   Set the \_NT\_KD\_FILES [environment variable](environment-variables.md) before you start the kernel debugger.

        ```console
        D:\Debugging Tools for Windows> set _NT_KD_FILES=d:\Map_Files\mymap.ini
        D:\Debugging Tools for Windows> kd
        ```

    -   Use the [**.kdfiles (Set Driver Replacement Map)**](-kdfiles--set-driver-replacement-map-.md) command after you start the kernel debugger.

        ```console
        D:\Debugging Tools for Windows> kd
        kd> .kdfiles d:\Map_Files\mymap.ini
        KD file associations loaded from 'd:\Map_Files\mymap.ini'
        ```

        You can also use the **.kdfiles** command to display the current driver replacement map file or to delete the driver replacement map. If you do not use this command, the map persists until you exit the debugger.

After you complete this procedure, the driver replacement map takes effect.

Whenever the target computer is about to load a driver, it queries the kernel debugger to determine whether this driver has been mapped. If the driver has been mapped, the replacement file is sent over the kernel connection and copied over the old driver file. The new driver is then loaded.

### <span id="driver_replacement_map_file_format"></span><span id="DRIVER_REPLACEMENT_MAP_FILE_FORMAT"></span>Driver Replacement Map File Format

Each driver file replacement is indicated by three lines in the driver replacement map file.

-   The first line consists of the word "map".

-   The second line specifies the path and file name of the old driver on the target computer.

-   The third line specifies the full path of the new driver. This driver can be located on the host computer or on some other server.

You can repeat this pattern of information any number of times.

Paths and file names are case insensitive, and the actual driver file names can be different. The file that you specify on the third line is copied over the file that you specify on the second line when the target computer is about to load that driver.

Kdfiles will attempt to match the file name that is stored in the Service Control Manager (SCM) database. The name in the SCM database is identical to the name that was passed to MmLoadSystemImage.

In Windows 10 and later versions of the debugging tools, driver mapping works to match the driver name dynamically and determine the proper path. The full path does not need to be specified and the file extension is optional. You can use any of these entries to match the NT file system driver.

-   ntfs
-   NTFS
-   ntfs.sys
-   windows\\system32\\drivers\\ntfs.sys

You can use any of these entries to match the NT kernel driver.

-   ntoskrnl
-   NTOSKRNL
-   ntoskrnl.sys
-   windows\\system32\\drivers\\ntoskrnl.sys

The map file can include blank lines and can include comment lines that begin with a number sign (**\#**). However, after "map" appears in the file, the next two lines must be the old driver and the new driver. The blank lines and comment lines cannot break up the three-line map blocks.

The following example shows a driver replacement map file.

```text
map
\Systemroot\system32\drivers\videoprt.sys
e:\MyNewDriver\binaries\videoprt.sys
map
\Systemroot\system32\mydriver.sys
\\myserver\myshare\new_drivers\mydriver0031.sys

# Here is a comment
map
\??\c:\windows\system32\beep.sys
\\myserver\myshare\new_drivers\new_beep.sys
```

The driver replacement map file must be a text file, but you can use any file name and file name extension (.ini, .txt, .map, and so on).

### <span id="additional_notes"></span><span id="ADDITIONAL_NOTES"></span>Additional Notes

When driver substitution occurs, a message appears in the kernel debugger.

If you use [**CTRL+D**](ctrl-d--toggle-debug-info-.md) (in KD) or CTRL+ALT+D (in WinDbg), you see verbose information about the replacement request. This information can be useful if you are not sure whether the name that you have listed matches the one in the SCM database.

You can enable the bcdedit bootdebug option to view early boot information that is useful for replacing the kernel, the hal, or boot drivers.

```console
bcdedit -bootdebug on
```

For more information, see [BCDEdit Options Reference](https://msdn.microsoft.com/library/windows/hardware/ff542205).

If the kernel debugger exits, no more driver replacement occurs. However, any drivers that have already been replaced do not revert to their old binaries, because the driver files are actually overwritten.

This driver replacement feature automatically bypasses Windows File Protection (WFP).

You do not have to restart the target computer. Driver replacement occurs any time that the target computer loads a driver, regardless of whether it has been restarted. Of course, most drivers are loaded during the boot process, so in practice you should restart the target computer after the map file has been loaded.

If the \_NT\_KD\_FILES variable is defined, the specified driver replacement map file is read when the kernel debugger is started. If you issue the **.kdfiles** command, the specified file is read immediately. At this point, the debugger verifies that the file has the basic map/line/line format. But the actual paths and file names are not verified until substitution occurs.

After the map file has been read, the debugger stores its contents. If you change this file after this point, the changes have no effect (unless you reissue the **.kdfiles** command).

### <span id="replacing_boot_drivers"></span><span id="REPLACING_BOOT_DRIVERS"></span>Replacing Boot Drivers

If you want to replace a boot driver file by using this driver replacement method, you must connect the kernel debugger to the Windows boot loader (Ntldr), not to the Windows kernel. Before you can make this connection, you must install a special debugger-enabled version of Ntldr. You can find this version of Ntldr in the Windows Driver Kit (WDK), in the %DDKROOT%\\debug directory.

Because the target computer bypasses its Boot.ini file, you cannot set the kernel connection protocol in the typical manner. You must make the connection through the COM1 port on the target computer. The baud rate is 115200. Therefore, the kernel debugger on the host computer should be configured to use a COM connection at the 115200 speed.

This special method applies only to boot drivers (that is, Acpi.sys, Classpnp.sys, Disk.sys, and anything else that [**lm t n**](lm--list-loaded-modules-.md) displays at the initial Windows breakpoint). If you have to replace a standard driver that **MmLoadSystemImage** loads after the boot has been completed, you should use the standard method described earlier.

You cannot replace boot drivers on a computer that uses EFI firmware instead of the Boot.ini file.

 

 





