---
title: Editing Boot Options in EFI
description: Editing Boot Options in EFI
ms.assetid: 0fdd01b3-7475-4959-87d8-5ec8ae65fea0
keywords: ["NVRAM boot options WDK , editing", "EFI NVRAM boot options WDK , editing", "editing boot options", "Bootcfg tool", "Nvrboot tool", "editors WDK boot options", "viewing boot options", "NVRAM boot options WDK , viewing", "EFI NVRAM boot options WDK , viewing", "boot options WDK , editing"]
---

# Editing Boot Options in EFI


## <span id="ddk_editing_boot_options_in_efi_tools"></span><span id="DDK_EDITING_BOOT_OPTIONS_IN_EFI_TOOLS"></span>


To edit boot options on computers with EFI NVRAM that are running Windows Server 2003 or earlier versions of NT-based Windows, use Bootcfg (bootcfg.exe), a tool that runs on Windows, or Nvrboot (nvrboot.efi), a tool that runs in the EFI environment. Both tools are included in the Windows XP 64-Bit Edition and the 64-bit version of Windows Server 2003.

You can also view and change some boot options in Control Panel under System. In the System Properties dialog box, on the Advanced tab, click Settings under **Startup and Recovery**. Because this functionality is limited, it is not discussed in this section. For information about the **Startup and Recovery** dialog box, see Help and Support Center.

### <span id="bootcfg"></span><span id="BOOTCFG"></span>Bootcfg

Bootcfg (bootcfg.exe) is a command-line tool that edits boot options on a local or remote computer Using the same Bootcfg commands and procedures, you can edit a Boot.ini file or the boot options in EFI NVRAM. Bootcfg is included in the %Systemroot%\\System32 directory in Windows XP and Windows Server 2003. (The Bootcfg display is slightly different on systems that store boot options in EFI NVRAM, but the commands are the same.)

You can use Bootcfg to add, delete, and change the values of all valid boot options; however, you cannot set an indefinite time-out value. You can also use Bootcfg commands in a script or batch file to set boot options or to reset them after you replace or upgrade an operating system.

On systems that store boot options in EFI NVRAM, Bootcfg can also display the boot partition table, add boot entries for mirrored drives, and update the GUIDs for a system partition.

You must be a member of the Administrators group on the computer to use Bootcfg. For detailed instructions about using Bootcfg, see Help and Support Center.

### <span id="nvrboot"></span><span id="NVRBOOT"></span>Nvrboot

Nvrboot (nvrboot.efi) is an EFI-based boot entry editor included in Windows XP 64-Bit Edition and the 64-bit version of Windows Server 2003. Nvrboot runs in the EFI environment. You cannot run Nvrboot while an operating system is running.

Nvrboot edits only boot entries. You cannot use it to display or change the time-out value for the boot menu, although, you can use the **push** command (**nvrboot p**) to change the default boot entry.

Nvrboot also includes commands to export backup copies of boot entries and to import backup copies of boot entries into NVRAM. This procedure is discussed in the [Backing up Boot Options in EFI](backing-up-boot-options-in-efi.md) section.

Nvrboot displays boot options in a user-friendly format. For example, it displays the operating system file path and the boot loader file path as a partition GUID followed by a Windows directory path.

The following procedure explains how to start Nvrboot from the EFI shell, a tool provided with many Itanium-based systems. Because the EFI shell tools vary among manufacturers, the description in this section might not accurately describe the EFI shell interface on a particular computer.

**To run Nvrboot**

1.  Reboot the computer.

2.  From the **boot** menu, choose **EFI Shell**.

3.  At the shell prompt, type the drive letter or file system number of the system partition, such as C: or **FS**n, where n is the file system number of the system partition.

4.  Type **cd msutil** to navigate to the Msutil directory where nvrboot.efi is located.

5.  To start Nvrboot, type **nvrboot**.

To find instructions for Nvrboot, type **h**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Editing%20Boot%20Options%20in%20EFI%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




