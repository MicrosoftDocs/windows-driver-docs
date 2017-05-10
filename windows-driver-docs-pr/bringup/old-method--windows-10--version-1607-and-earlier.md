---
title: TBD
description: TBD
ms.author: windowsdriverdev
ms.date: 05/05/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---



# Old Method Pre-Windows 10 Creators Update


In an upgrade scenario (Windows 7 to Windows 10); a technician needs to change OS and firmware from Win7SPn Legacy boot+CSM to Win10 UEFI-CSM (minus CSM) and has Win7 SPn x64 installation media. This process may look something like this (more details below).

1.  Consult with Original Equipment Manufacturer (OEM) on security options available to this firmware / motherboard. Not all security options will be available on some firmware / motherboard.

2.  Backup ALL data from entire primary boot disk (that you plan on saving)

    1.  Creating an image or having OEM recovery media is recommended

3.  Create USB bootable x64 WinPE thumb stick or CD/DVD

4.  Reboot to Firmware User Interface(UI) and switch settings to boot to UEFI (if you need to boot back into Win7, you will need CSM enabled for now)

5.  Boot to WinPE on USB/CD/DVD device (**Secure Boot** must be disabled to boot to the alternative boot device).

6.  Use Diskpart.exe to wipe clean primary boot disk. 

**Note** If more than one disk is present, verify that disk 0 is the primary boot device before cleaning the disk, as this will wipe all data on the disk.

7.  There are several options at this point, and the IT Person may need to contact System OEM for specific instructions/configuration options.

    1.  Pop in clean installation media and run setup.exe. There is a chance that installation process will detect CSM and re-install in Legacy boot/BIOS mode.

    2.  From step 5, still within Diskpart.exe with primary boot disk selected, run "Convert GPT"

        1.  Insert the installation media, reboot, and go through setup. If you encounter an error message with similar text to "cannot install to selected device" or "disk format not supported" then boot device is detecting CSM and attempting to boot to Legacy boot MBR method.

        2.  Alternatively, follow steps to manually configure GPT disk for UEFI Boot method. Looking at [Recommended UEFI-Based Disk-Partition Configurations](https://technet.microsoft.com/en-us/library/dd744301(v=ws.10).aspx) then run through setup.exe targeting 3rd partition.

8.  Once Windows 7 is installed on System and up and running (you may need to patch to latest version(s)) then upgrade to Windows 10

9.  Once Windows 10 is installed and patched, test with disabling CSM and work with manufacture to enable security options available on this system.

    **Note** In some scenarios, firmware has UEFI specific boot options. For example, select; a) boot option or b) UEFI boot option.

## Related resources

| [Recommended UEFI-Based Disk-Partition Configurations](https://technet.microsoft.com/en-us/library/dd744301(v=ws.10).aspx) |
|----------------------------------------------------------------------------------------------------------------------------|


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


