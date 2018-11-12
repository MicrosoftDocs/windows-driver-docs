---
title: Bug Check 0x7B INACCESSIBLE_BOOT_DEVICE
description: The INACCESSIBLE_BOOT_DEVICE bug check has a value of 0x0000007B. This bug check indicates that the Microsoft Windows operating system has lost access to the system partition during startup.
ms.assetid: 0dfcb519-4ea3-4419-a1c3-60fdff96404d
keywords: ["Bug Check 0x7B INACCESSIBLE_BOOT_DEVICE", "INACCESSIBLE_BOOT_DEVICE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- INACCESSIBLE_BOOT_DEVICE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x7B: INACCESSIBLE\_BOOT\_DEVICE


The INACCESSIBLE\_BOOT\_DEVICE bug check has a value of 0x0000007B. This bug check indicates that the Microsoft Windows operating system has lost access to the system partition during startup.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## INACCESSIBLE\_BOOT\_DEVICE Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>The address of a UNICODE_STRING structure, or the address of the device object that could not be mounted</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

To determine the meaning of Parameter 1, look at the data that it points to. If the first word (USHORT) at this address is even, Parameter 1 is the beginning of a Unicode string. If the first word (USHORT) at this address is 0x3, Parameter 1 is the first field (Type) of a device object.

-   If this parameter points to a device object, the file system that was supposed to read the boot device failed to initialize or simply did not recognize the data on the boot device as a file system structure. In this situation, the specified device object is the object that could not be mounted.

-   If this parameter points to a Unicode string, you must read the first 8 bytes at this address. These bytes form the UNICODE\_STRING structure, which is defined as follows:

    ```cpp
    USHORT Length;
    USHORT MaximumLength;
    PWSTR Buffer;
    ```

    The **Length** field gives the actual length of the string. The **Buffer** field points to the beginning of the string (**Buffer** is always be at least 0x80000000.)

    The actual string contains the Advanced RISC Computing (ARC) specification name of the device that the boot was being attempted from. ARC names are a generic way to identify devices in the ARC environment.

Cause
-----

The INACCESSIBLE\_BOOT\_DEVICE bug check frequently occurs because of a boot device failure. During I/O system initialization, the boot device driver might have failed to initialize the boot device (typically a hard disk).

File system initialization might have failed because it did not recognize the data on the boot device. Also, repartitioning the system partition, changing the BIOS configuration, or installing a disk controller might induce this error.

This error can also occur because of incompatible disk hardware. If the error occurred at the initial setup of the system, the system might have been installed on an unsupported disk controller. Some disk controllers require additional drivers to be present when Windows starts.

Resolution
----------

This error always occurs while the system is starting. This error frequently occurs before the debugger connection is established, so debugging can be difficult. In addition, the OS may not be accessible and the error logs may be empty as the OS has not booted far enough to start those sub-systems.

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\\***

**If you are unable to boot Windows**

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\\***

If you receive this stop code and Windows doesn't boot forward into the OS, try the following:

**Revert any recent hardware changes**

Remove any recently added hardware, especially hard disk drives or controllers, to see if the error is resolved. If the problematic hardware is a hard disk drive, the disk firmware version might be incompatible with your version of the Windows operating system. Contact the manufacturer for updates. If you removed another piece of hardware and the error is resolved, IRQ or I/O port conflicts may exist. Reconfigure the new device according to the manufacturer's instructions.

If you have recently made changes to BIOS settings, such as changing the controller mode from legacy to AHCI in the BIOS, revert those changes. For more information, see <https://en.wikipedia.org/wiki/Advanced_Host_Controller_Interface>

**Check for storage device compatibility**

Confirm that all hard disk drivers, hard disk controllers, and any other storage adapters are compatible with the installed version of Windows. For example, you can get information about compatibility at [Windows 10 Specifications](https://www.microsoft.com/windows/windows-10-specifications).

**Update BIOS and Firmware**

Check the availability of updates for the system BIOS and storage controller firmware.

**Use the Media Creation Tool to create a bootable USB thumb drive or DVD**

Use Media Creation Tool, using another computer to create a bootable USB thumb drive or DVD. Use it to perform a clean install, by clicking on the setup file or booting from the USB.

For more information, see [Get Windows 10](https://www.microsoft.com/software-download/windows10).

Be aware that you may need to disable features, such as quick BIOS boot, or you may not be able to reach the boot device priority menu. Change your boot sequence priority in the BIOS menu to boot from FDD (FlashDiskDrive) or DVD instead of HDD.

**Common Boot Menu Keys**

The boot menu key varies per manufacturer, these keys are commonly used. Check the system documentation to determine what boot key is used.

F12
ESC
F9
F10
F8
**Common BIOS Setup Keys**

The BIOS setup key varies per manufacturer, these keys are commonly used. Check the system documentation to determine what setup key is used.

ESC
DEL
F2
**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\\***

**If you can boot Windows**

**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\\***

-   **Boot to Safe Mode and then Boot Normally**

    Complete the following steps to boot into Safe Mode. Booting into safe mode loads a core set of storage drivers that may allow for the storage system to be accessed once again.

    To enter Safe Mode, use **Update and Security** in Settings. Select **Recovery**-&gt;**Advanced startup** to boot to maintenance mode. At the resulting menu, choose **Troubleshoot**-&gt; **Advanced Options** -&gt; **Startup Settings** -&gt; **Restart**. After Windows restarts to the **Startup Settings** screen, select option, 4, 5 or 6 to boot to Safe Mode.

    Once Windows is loaded in Safe Mode, restart your PC to see if the proper storage drivers will be loaded and that the storage device is recognized.

    Safe Mode may also be available by pressing a function key on boot, for example F8. Refer to information from the system manufacturer for specific startup options.

-   Use the scan disk utility to confirm that there are no file system errors. Right click on the drive you want to scan and select **Properties**. Click on **Tools**. Click the **Check now** button.
-   Run a virus detection program. Viruses can infect all types of hard disks formatted for Windows, and resulting disk corruption can generate system bug check codes. Make sure the virus detection program checks the Master Boot Record for infections.

-   For IDE devices, define the onboard IDE port as Primary only. Also check each IDE device for the proper **master/subordinate/stand alone** setting. Try removing all IDE devices except for hard disks. Finally, check the System Log in Event Viewer for additional error messages that might help identify the device or driver that is causing the error.

-   Confirm that there is sufficient free space on the hard drive. The operating system and some applications require sufficient free space to create swap files and for other functions. Based on the system configuration, the exact requirement varies, but it is normally a good idea to have 10% to 15% free space available.

-   Look in **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in driver properties for any faulting driver. Try updating the related driver.

-   Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://windows.microsoft.com/windows/what-information-event-logs-event-viewer#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

-   You can try running the hardware diagnostics supplied by the system manufacturer.

-   Use the System File Checker tool to repair missing or corrupted system files. The System File Checker is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the following command to run the System File Checker tool (SFC.exe).

    ```console
    SFC /scannow
    ```

    For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/kb/929833).

-   After automatic repair, on the Choose an option screen, select **Troubleshoot &gt; Advanced options &gt; System Restore**. This option takes your PC back to an earlier point in time, called a system restore point. Restore points are generated when you install a new app, driver, update, or when you create a restore point manually. Choose a restore point before you experienced the error.

-   Use the kernel debugger to attach to the system and further analyze the failure as described in remarks.

Remarks
-------

**Investigating the storage system configuration**

It is helpful to know as much as possible about the boot device that Windows is installed on. For example, you can investigate the following items:

-   Find out what type of controller the boot device is connected to (SATA, IDE, etc). If you can boot the system, you can use device manager to examine the controller and disk driver properties and see the associated driver file as well as error events.

-   Indicate if other devices are attached to the same controller that the boot device is on (SSD, DVD, and so on).

-   Note the file system that is used on the drive, typically NTFS.

**To analyze this error using the kernel debugger:** Run an [**lm (List Loaded Modules)**](lm--list-loaded-modules-.md) command in the debugger to see which modules are loaded to attempt to isolate the specific driver. Verify that the following drivers were loaded.

*disk*

```dbgcmd
           
0: kd> lm m disk
Browse full module list
start             end                 module name
fffff806`bd0b0000 fffff806`bd0cd000   disk       (deferred)
```

*partmgr*

```dbgcmd
0: kd> lm m partmgr
Browse full module list
start             end                 module name
fffff806`bc5a0000 fffff806`bc5c1000   partmgr    (deferred)
```

*NTFS*

```dbgcmd
0: kd> lm m ntfs
Browse full module list
start             end                 module name
fffff806`bd3f0000 fffff806`bd607000   NTFS       (deferred)
```

*classpnp*

```dbgcmd
 0: kd> lm m classpnp
Browse full module list
start             end                 module name
fffff806`bd0d0000 fffff806`bd131000   CLASSPNP   (deferred)
```

*pci*

```dbgcmd
0: kd> lm m pci
Browse full module list
start             end                 module name
fffff806`bc440000 fffff806`bc494000   pci        (deferred) 
```

Also make sure your controller drivers are loaded. For example for a SATA RAID Controller, this might be the *iaStorA.Sys* driver, or it could be the *EhStorClass* driver.

```dbgcmd
0: kd> lm m EhStorClass
Browse full module list
start             end                 module name
fffff806`bcbb0000 fffff806`bcbcb000   EhStorClass   (deferred) 
```

List the drivers that contain "stor", storahci, may be present.

```dbgcmd
0: kd> lm m stor*
Browse full module list
start             end                 module name
fffff806`bcb00000 fffff806`bcb23000   storahci   (deferred)             
fffff806`bcb30000 fffff806`bcbaa000   storport   (deferred)             
fffff806`c0770000 fffff806`c0788000   storqosflt   (deferred)
```

**Booting with a debugger attached**

If you can boot the target system with a debugger connected, issue [**!devnode 0 1**](-devnode.md) when the bugcheck occurs. You'll see which device lacks a driver or could not start, and the reason for not starting may be apparent.

One cause, might be that Plug and Play cannot assign resources to the boot device. You can verify this restriction by finding an entry for the service. If the status flags include DNF\_INSUFFICIENT\_RESOURCES or do not include DNF\_STARTED or DNF\_ENUMERATED, you may have located the problem. Try **!devnode 0 1 storahci** to save some time, instead of dumping the whole device tree.

```dbgcmd
0: kd> !devnode 0 1 storahci
Dumping IopRootDeviceNode (= 0xffffb9053d94d850)
DevNode 0xffffb9053e8dea50 for PDO 0xffffb9053e8da060
  InstancePath is "PCI\VEN_8086&DEV_3B22&SUBSYS_304A103C&REV_05\3&21436425&0&FA"
  ServiceName is "storahci"
  State = DeviceNodeStarted (0x308)
  Previous State = DeviceNodeEnumerateCompletion (0x30d)
  DevNode 0xffffb9053e88db30 for PDO 0xffffb9053e890060
    InstancePath is "SCSI\Disk&Ven_&Prod_ST3500418AS\4&23d99fa2&0&000000"
    ServiceName is "disk"
    State = DeviceNodeStarted (0x308)
    Previous State = DeviceNodeEnumerateCompletion (0x30d)
  DevNode 0xffffb9053e88d850 for PDO 0xffffb9053e88e060
    InstancePath is "SCSI\CdRom&Ven_hp&Prod_DVD-RAM_GH60L\4&23d99fa2&0&010000"
    ServiceName is "cdrom"
    TargetDeviceNotify List - f 0xffffdf0ae9bbb0e0  b 0xffffdf0aea874710
    State = DeviceNodeStarted (0x308)
    Previous State = DeviceNodeEnumerateCompletion (0x30d)
```

 

 




