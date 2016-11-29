---
title: Overview of Boot Options in Windows Vista and Later
description: Windows Vista introduced a new boot loader architecture, a new firmware-independent boot configuration and storage system called Boot Configuration Data (BCD), and a new boot option editing tool, BCDEdit (BCDEdit.exe).
ms.assetid: 1cc5b1cc-8d0e-4b4e-93fe-272772a3e458
keywords: ["boot options WDK , Windows Vista", "editing boot options", "multiboot systems WDK boot options", "legacy boot entries WDK", "Boot Configuration Data WDK", "BCD WDK", "BCDEdit tool", "boot options WDK , editing", "ntldr tool", "Windows Boot Manager WDK", "Bootmgr tool", "system-specific boot loaders WDK", "boot loaders WDK", "firmware-independent boot options WDK"]
---

# Overview of Boot Options in Windows Vista and Later


Windows Vista introduced a new boot loader architecture, a new firmware-independent boot configuration and storage system called *Boot Configuration Data* (BCD), and a new boot option editing tool, BCDEdit (BCDEdit.exe). During development, you can use BCDEdit to configure boot options for debugging, testing, and troubleshooting your driver on computers running Windows 10, Windows 8, Windows Server 2012, Windows 7, and Windows Server 2008.

**Important**  Administrative privileges are required to use BCDEdit to modify BCD. Changing some boot entry options using BCDEdit could render your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings.

 

### <span id="boot_loading_architecture_in_windows_vista_and_later"></span><span id="BOOT_LOADING_ARCHITECTURE_IN_WINDOWS_VISTA_AND_LATER"></span>Boot Loading Architecture

Windows includes boot loader components that are designed to load Windows quickly and securely. The previous Windows NT boot loader, *ntldr*, is replaced by three components:

-   Windows Boot Manager (Bootmgr.exe)

-   Windows operating system loader (Winload.exe)

-   Windows resume loader (Winresume.exe)

In this configuration, the Windows Boot Manager is generic and unaware of the specific requirements for each operating system while the system-specific boot loaders are optimized for the system that they load.

When a computer with multiple boot entries includes at least one entry for Windows, the Windows Boot Manager, which resides in the root directory, starts the system and interacts with the user. It displays the boot menu, loads the selected system-specific boot loader, and passes the boot parameters to the boot loader.

The boot loaders reside in the root directory of each Windows partition. Once selected, the boot loaders take over the boot process and load the operating system in accordance with the selected boot parameters.

### <span id="boot_configuration_data"></span><span id="BOOT_CONFIGURATION_DATA"></span>Boot Configuration Data

Windows boot options are stored in the Boot Configuration Data (BCD) store on BIOS-based and EFI-based computers.

BCD replaces the traditional Boot.ini text file in BIOS-based systems. Storing boot parameters in a text file, however simple, was considered to be too vulnerable to malicious attacks to justify its use. On EFI-based computers, where boot options are stored in NVRAM, you use the same BCD methods to edit boot options as you would use on a BIOS-based computer, instead of accessing NVRAM directly using Windows APIs or specialized tools.

BCD provides a common, firmware-independent boot option interface for all computers running Windows 10, Windows 8, Windows Server 2012, Windows 7, and Windows Server 2008. It is more secure than previous boot option storage configurations, because it permits secure lockdown of the BCD store and lets Administrators assign rights for managing boot options. BCD is available at run time and during all phases of setup. You can even call BCD during power state transitions and use it to define the boot process for resuming after hibernation.

You can manage BCD remotely and manage BCD when the system boots from media other than the media on which the BCD store resides. This feature is extremely important for debugging and troubleshooting, especially when a BCD store must be restored while running Startup Repair from a CD, from USB-based storage media, or even remotely.

BCD is easy to use. The BCD store, with its familiar object-and-element architecture, uses GUIDs to precisely identify boot-related applications.

This new data format for BCD uses a new set of boot options. Most of the Windows boot options that were used in pre-Vista versions of Windows, such as **/debug**, **/maxmem**, and **/pae**, have been preserved; however, in some cases, the names of the options might have changed to better suite their function. For more information about these boot options, see [BCD Boot Options Reference](https://msdn.microsoft.com/library/windows/hardware/ff542205).

### <span id="multiboot_scenarios"></span><span id="MULTIBOOT_SCENARIOS"></span>Multiboot Scenarios

If multiple Windows operating systems are installed on the computer, the Windows Boot Manager works with the booting components for older ("legacy") versions of Windows to interact with the user and start the selected operating system.

When a multiboot computer is started, the following scenario occurs:

-   The Windows Boot Manager displays a menu with the boot entries for Windows and a **Legacy** option.

-   If you select a boot entry for Windows Vista or a later version of Windows, the Windows Boot Manager loads the system-specific boot loader for that operating system and passes the parameters for that boot entry to the system-specific boot loader. The system-specific boot loader loads the operating system in accordance with the boot parameters.

-   If you select **Legacy**, the Windows Boot Manager starts Ntldr, the boot manager for NT-based Windows operating systems prior to Windows Vista. From this point forward, the boot process proceeds as it did prior to Windows Vista.

    If the computer includes multiple installations of pre-Windows Vista Windows, Ntldr displays a boot menu consisting of the entries for Windows Server 2003, Windows XP, Windows 2000, and Windows NT operating systems. This boot menu is generated from the entries in the Boot.ini file on BIOS-based systems and the boot entries stored in EFI-NVRAM on EFI-based systems. When you select a boot entry, Ntldr loads the operating system in accordance with the boot parameters.

### <span id="editing_boot_options_in_windows_vista"></span><span id="EDITING_BOOT_OPTIONS_IN_WINDOWS_VISTA"></span>Editing Boot Options

To edit boot options in Windows, use BCDEdit (BCDEdit.exe), a tool included in Windows. You cannot use Bootcfg or NvrBoot to edit boot options in Windows, although you can continue to use them to edit boot options on legacy versions of Windows.

To use BCDEdit, you must be a member of the Administrators group on the computer.

You can also use the System Configuration utility (MSConfig.exe) to change boot settings.

To change boot options programmatically in Windows, use the Windows Management Instrument (WMI) interface to boot options. This BCD WMI interface is the best method to programmatically change the boot options. For information about the BCD WMI interface, see [Boot Configuration Data](http://go.microsoft.com/fwlink/p/?linkid=74322) in the Windows SDK documentation.

## <span id="related_topics"></span>Related topics


[BCD Boot Options Reference](https://msdn.microsoft.com/library/windows/hardware/ff542205)

[Editing Boot Options](editing-boot-options.md)

[Using Boot Parameters](using-boot-parameters.md)

[Boot Configuration Data](http://go.microsoft.com/fwlink/p/?linkid=74322)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Overview%20of%20Boot%20Options%20in%20Windows%20Vista%20and%20Later%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





