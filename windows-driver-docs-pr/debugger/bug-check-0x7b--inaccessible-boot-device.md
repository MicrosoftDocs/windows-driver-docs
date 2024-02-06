---
title: Bug Check 0x7B INACCESSIBLE_BOOT_DEVICE
description: Learn how the INACCESSIBLE_BOOT_DEVICE bug check indicates that the Microsoft Windows operating system has lost access to the system partition during startup.
keywords: ["Bug Check 0x7B INACCESSIBLE_BOOT_DEVICE", "INACCESSIBLE_BOOT_DEVICE"]
ms.date: 02/22/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- INACCESSIBLE_BOOT_DEVICE
api_type:
- NA
---

# Bug check 0x7B: INACCESSIBLE_BOOT_DEVICE

The INACCESSIBLE_BOOT_DEVICE bug check has a value of 0x0000007B. This bug check indicates that the Microsoft Windows operating system has lost access to the system partition during startup.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## Parameters

| Parameter | Description                                                                                              |
|-----------|----------------------------------------------------------------------------------------------------------|
| 1         | The address of a UNICODE_STRING structure, or the address of the device object that couldn't be mounted  |
| 2         | 0                                                                                                        |
| 3         | 0                                                                                                        |
| 4         | 0                                                                                                        |

To determine the meaning of Parameter 1, look at the data that it points to. If the first word (USHORT) at this address is even, Parameter 1 is the beginning of a Unicode string. If the first word (USHORT) at this address is 0x3, Parameter 1 is the first field (Type) of a device object.

- If this parameter points to a device object, the file system that was supposed to read the boot device failed to initialize or didn't recognize the data on the boot device as a file system structure. In this situation, the specified device object is the object that couldn't be mounted.

- If this parameter points to a Unicode string, you must read the first 8 bytes at this address. These bytes form the UNICODE_STRING structure. The following example shows how the structure is defined:

    ```cpp
    USHORT Length;
    USHORT MaximumLength;
    PWSTR Buffer;
    ```

    The **Length** field gives the actual length of the string. The **Buffer** field points to the beginning of the string. **Buffer** is always at least 0x80000000.

    The string contains the Advanced RISC Computing (ARC) specification name of the device that the boot was being attempted from. ARC names are a generic way to identify devices in the ARC environment.

## Cause

The INACCESSIBLE_BOOT_DEVICE bug check often occurs because of a boot device failure. During I/O system initialization, the boot device driver might have failed to initialize the boot device, typically a hard disk.

File system initialization might have failed because it didn't recognize the data on the boot device. Repartitioning the system partition, changing the BIOS configuration, or installing a disk controller can also cause this error.

This error can occur because of incompatible disk hardware. If the error occurred at the initial setup of the system, the system might have been installed on an unsupported disk controller. Some disk controllers require other drivers to be present when Windows starts.

This error can occur, when the storage hardware has failed, and is not able to respond to the request from Windows.

## Resolution

This error always occurs while the system is starting. This error frequently occurs before the debugger connection is established, so debugging can be difficult. The OS might not be accessible and the error logs might be empty, as the OS hasn't booted far enough to start those subsystems. The following sections explain resolutions for both situations, if you're unable to boot Windows and if you're able to boot Windows.

### If you're unable to boot Windows

If you receive this stop code and Windows doesn't boot forward into the OS, try the following resolutions:

- **Revert any recent hardware changes.**

  Remove any recently added hardware, especially hard disk drives or controllers, to see if the error is resolved. If the problematic hardware is a hard disk drive, the disk firmware version might be incompatible with your version of the Windows operating system. Contact the manufacturer for updates. If you removed another piece of hardware and the error is resolved, IRQ or I/O port conflicts might exist. Reconfigure the new device according to the manufacturer's instructions.

  If you have recently made changes to UEFI (BIOS) settings, such as changing the controller mode from legacy to AHCI in UEFI, revert those changes. For more information, see [Advanced host controller interface](https://en.wikipedia.org/wiki/Advanced_Host_Controller_Interface).

- **Check for storage device compatibility.**

  Confirm that all hard disk drivers, hard disk controllers, and any other storage adapters are compatible with the installed version of Windows. For example, you can get information about compatibility at [Windows 10 specifications](https://www.microsoft.com/windows/windows-10-specifications).

- **Update UEFI (BIOS) and firmware.**

  Check the availability of updates for the system UEFI (BIOS) and storage controller firmware.

- **Use the Windows Media Creation Tool to create a bootable USB thumb drive or DVD.**

  Use the Media Creation Tool on another computer to create a bootable USB thumb drive or DVD. Use this tool to perform a clean install by selecting the setup file or booting from the USB.

  For more information, see [Get Windows 10](https://www.microsoft.com/software-download/windows10).

  You might need to disable features, or change your boot sequence priority in the UEFI (BIOS) menu to boot from USB, FDD (FlashDiskDrive) or DVD instead of HDD.

  **Common boot menu keys**

  The boot menu keys vary per manufacturer. These keys are commonly used. Check the PC documentation to determine what boot key is used.

  Frequently used boot menu keys are:  
  F12  
  ESC  
  F9  
  F10  
  F8  

  **Common UEFI (BIOS) setup keys**

  UEFI (BIOS) setup keys vary per manufacturer. These keys are commonly used. Check the PC documentation to determine what setup key is used.

  Frequently used UEFI (BIOS) setup keys are:  
  ESC  
  DEL  
  F2  

### If you're able to boot Windows

If you receive this stop code and Windows does boot, try the following resolutions:

- **Boot to Safe Mode and then boot normally.**

    Booting into Safe Mode loads a core set of storage drivers that can allow for the storage system to be accessed once again. Complete the following steps to boot into Safe Mode:

    1. In **Settings**, select **Update and Security**.
    1. Select **Recovery > Advanced startup** to boot to maintenance mode.
    1. At the resulting menu, choose **Troubleshoot > Advanced Options > Startup Settings > Restart**.
    1. After Windows restarts to the **Startup Settings** screen, select option 4, 5, or 6 to boot to Safe Mode.

    Once Windows is loaded in Safe Mode, restart your PC to see if the proper storage drivers are loaded and that the storage device is recognized.

    Safe Mode might also be available by pressing a function key on boot, for example F8. Refer to information from the system manufacturer for specific startup options.

- Use the scan disk utility to confirm that there are no file system errors. Select and hold (or right-click) on the drive that you want to scan and select **Properties > Tools > Check now**.

- Run a virus detection program. Viruses can infect all types of hard disks formatted for Windows and the resulting disk corruption can generate system bug check codes. Make sure the virus detection program checks the Master Boot Record for infections.

- For IDE devices, define the onboard IDE port as Primary only. Also check each IDE device for the proper **master/subordinate/stand alone** setting. Try removing all IDE devices except for hard disks. Finally, check the System Log in Event Viewer for other error messages that might help identify the device or driver that's causing the error.

- Confirm that there's sufficient free space on the hard drive. The operating system and some applications require sufficient free space to create swap files and perform other functions. Based on the system configuration, the exact requirement varies, but it's a good idea to have 10% to 15% of free space available.

- Look in **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in the driver properties for a faulting driver. Try updating the related driver.

- Check the System Log in Event Viewer for other error messages that might help pinpoint the device or driver that's causing the error. For more information, see [Open Event Viewer](/microsoft-365/security/defender-endpoint/event-error-codes). Look for critical errors in the system log that occurred in the same time frame as the blue screen.

- You can try running the hardware diagnostics supplied by the system manufacturer.

- Use the System File Checker tool to repair missing or corrupted system files. The System File Checker is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the following command to run the System File Checker tool (SFC.exe).

    ```console
    SFC /scannow
    ```

    For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system).

- After automatic repair, on the **Choose an option** screen, select **Troubleshoot > Advanced options > System Restore**. This option takes your PC back to an earlier point in time, called a system restore point. Restore points are generated when you install a new app, driver, update, or when you create a restore point manually. Choose a restore point before you experienced the error.

- Use the kernel debugger to attach to the system and further analyze the failure as described in remarks.

## Remarks

**Investigate the storage system configuration.**  
To narrow down a cause, it's helpful to know as much as possible about the boot device that Windows is installed on. For example, you can investigate the following items:

- Find out what type of controller the boot device is connected to, like SATA or IDE. If you can boot the system, you can use the device manager to examine the controller and disk driver properties. You can see the associated driver file and error events.

- Indicate if other devices are attached to the same controller that the boot device is on, like SSD or DVD.

- Note the file system that's used on the drive, typically NTFS.

### Windows Debugger

To analyze this error using the kernel debugger, run an [lm (List loaded modules)](../debuggercmds/lm--list-loaded-modules-.md) command in the debugger to see which modules are loaded to attempt to isolate the specific driver. Verify that the following drivers were loaded.

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

Make sure your controller drivers are loaded. For example, for a SATA RAID Controller, the driver might be the *iaStorA.Sys* driver, or it could be the *EhStorClass* driver.

```dbgcmd
0: kd> lm m EhStorClass
Browse full module list
start             end                 module name
fffff806`bcbb0000 fffff806`bcbcb000   EhStorClass   (deferred) 
```

The drivers that contain "stor", such as storahci, might be present.

```dbgcmd
0: kd> lm m stor*
Browse full module list
start             end                 module name
fffff806`bcb00000 fffff806`bcb23000   storahci   (deferred)             
fffff806`bcb30000 fffff806`bcbaa000   storport   (deferred)             
fffff806`c0770000 fffff806`c0788000   storqosflt   (deferred)
```

**Boot with a debugger attached.**

If you can boot the target system with a debugger connected, issue [!devnode 0 1](../debuggercmds/-devnode.md) when the bug check occurs. You can see which device lacks a driver or doesn't start, and the reason for not starting might be apparent.

One cause might be that Plug and Play can't assign resources to the boot device. You can verify this restriction by finding an entry for the service. If the status flags include DNF_INSUFFICIENT_RESOURCES or don't include DNF_STARTED or DNF_ENUMERATED, you might have located the problem. Try `!devnode 0 1 storahci` to save some time, instead of dumping the whole device tree.

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

 

 



