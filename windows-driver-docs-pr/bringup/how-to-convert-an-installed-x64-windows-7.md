---
title: How to convert an installed x64 Windows 7 system
description: How to convert an installed x64 Windows 7 system
ms.date: 01/28/2019
ms.localizationpriority: medium
---

# How to convert an installed x64 Windows 7 system

The following steps are intended for use by an ITPro in a scenario where they need to convert from Legacy MBR+CSM to UEFI+GPT. Usually this process starts with a system that has Windows 7 x64 installed.

For x86 OS systems, see the section in the [Firmware WEG FAQ](frequently-asked-questions.yml) about "What is the dependency on 32-bit vs. 64-bit UEFI?".

Installed in BIOS mode to Legacy MBR boot disk with CSM enabled, and you know or have checked with the OEM to ensure that the system has the following:

1. Ability to enable and disable the CSM
1. Has UEFI firmware 2.3.1c or later
1. The security features that you are interested in (Secure boot, HVCI, and Credential Guard) have all the correct components already configured on the system.
    > [!NOTE]
    > Microsoft does not currently have a mechanism to convert Legacy MBR boot disks to GPT disks without first wiping or cleaning an existing file system and creating the new file system on the clean disk.

For example, you will need to use Diskpart.exe to **clean** the existing partition before running the **convert GPT** command on that disk. The **clean** command will wipe the entire disk.

1. Ensure all data is backed up from the primary boot device, and the user or ITPro has confirmed that primary boot device is Disk 0
1. Primary boot device has been completely backed up (any data left on disk will be wiped)
1. Reboot to BIOS (contact the manufacturer for steps to switch BIOS boot mode to UEFI boot mode) aand switch to UEFI+CSM
1. Boot to the USB flash drive  that contains x64 WinPE
1. After booting into WinPE, at the command prompt:
    1. Open Diskpart.exe
    1. select disk 0
    1. list par
    1. list VOL <= to identify current drive letters so you know where existing OS is assigned (identify drive letter for OS, used later)
    1. convert GPT
    1. select partition 1
    1. create par EFI size=800 (mg)
    1. format fs=fat32 label=System
    1. assign letter S
    1. create par MSR
    1. list par
    1. exit
1. Back at the command prompt, type in the following:
    1. s:
    1. BCDboot c:\\windows /s s: /f UEFI
       > [!NOTE]
       > This is the drive letter identified in step c and d above
    1. dir /a
    1. You should see s:\\EFI
    1. Reboot and attempt to boot to OS

## Verify system is booted in UEFI mode

Use one of the following methods to verify system is booted in UEFI mode.

### MSINFO32

On Windows 10 systems:

1. Press \<Windows key\> + \<R\> to open the **Run** dialog
1. Type Msinfo32 and click **OK**

The System Summary page will open by default.

Look for the following information:

![Systems Summary page.](images/system-summary-page.png)

To run as an administrator, use the following steps:

1. Press \<Windows key\> + \<R\> to open the **Run** dialog
1. Start typing "System Information"

If **System Information** is highlighted, hold \<CTRL\> + \<SHIFT\> and hit \<ENTER\>, or use your mouse to right-click and select **Run as Administrator**.

You will be prompted by User Access Control (UAC) with the following message: **Do You want this app to make changes to your desktop?**

### BCDEDIT

On Windows 7 and later systems:

1. Start an elevated command prompt
1. Run "BCDedit /enum {current}"
    > [!NOTE]
    > If booted from WinPE, use the "/store" switch in BCDedit.exe.
    > If you have UEFI, the path will show Winload.efi.
    > If you have CSM, the path will show Winload.exe as listed in sample output.

#### Sample output

```cmd
Windows Boot Loader
-------------------
identifier {current}
device partition=C:
path \WINDOWS\system32\winload.efi
```

### NOTEPAD and SETUPACT.LOG

1. Start an elevated command prompt
1. Run "notepad c:\\windows\\panther\\setupact.log"
1. Press \<CTRL\> + \<F\> for find (or search)
1. Search for "Callback\_BootEnvironmentDetect"

    - Results would look something like this:

        ```cmd
        Callback_BootEnvironmentDetect:FirmwareType 1

        Callback_BootEnvironmentDetect: Detected boot environment: BIOS
        ```

        Or

        ```cmd
        Callback_BootEnvironmentDetect:FirmwareType 2

        Callback_BootEnvironmentDetect: Detected boot environment: UEFI
        ```

You may need to consult with the OEM for configuration details on your specific system.

> [!WARNING]
> Using diskpart.exe or Setup to clean or wipe the hard disk drive partition information will all destroy data on the disk. Consult the PC manufacturer concerning factory image recovery methods or data backup options prior to making any of these changes.

## Related resources

[Recommended UEFI-Based Disk-Partition Configurations](/previous-versions/windows/it-pro/windows-7/dd744301(v=ws.10))

[Win7 Back up your programs, system settings, and files](https://support.microsoft.com/help/17127/windows-back-up-restore#1TC=windows-7)

[Win7 Protect your files and PC with Windows 7 Backup](https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/bg-p/FileCAB)