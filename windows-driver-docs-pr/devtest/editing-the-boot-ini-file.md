---
title: Editing the Boot.ini File
description: Prior to Windows Vista, BIOS-based computers running Windows store boot options in a Boot.ini text file.
ms.assetid: 9edbbd5e-36b5-4a80-925d-a007a4469984
keywords: ["Bootcfg tool", "Boot.ini files WDK , editing", "editing boot options", "Notepad WDK boot options", "text editors WDK boot options", "manual editing WDK boot options", "boot entry parameters WDK", "boot parameters WDK", "indefinite boot time-out values WDK", "boot time-out values WDK", "time-outs WDK boot options", "Boot.ini files WDK , attribute removal", "removing Boot.ini attributes", "viewing boot options", "Boot.ini files WDK , viewing", "editors WDK boot options", "boot options WDK , editing"]
---

# Editing the Boot.ini File


\[This topic describes the boot options supported in Windows XP and Windows Server 2003. If you are changing boot options for Windows 8, Windows Server 2012, Windows 7, Windows Server 2008, or Windows Vista, see [Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md).\]

Prior to Windows Vista, BIOS-based computers running Windows store boot options in a Boot.ini text file. You can edit the Boot.ini file by using Bootcfg (bootcfg.exe), a tool included in Windows XP and Windows Server 2003, or by using a text editor such as Notepad. Bootcfg is documented in Windows Help and Support.

## <span id="ddk_editing_the_boot_ini_file_tools"></span><span id="DDK_EDITING_THE_BOOT_INI_FILE_TOOLS"></span>


You can also view and change some boot options in Control Panel under System. In the System Properties dialog box, on the Advanced tab, click Settings under **Startup and Recovery**. Because this functionality is limited, it is not discussed in this section. For information about the **Startup and Recovery** dialog box, see Help and Support Center.

### <span id="bootcfg"></span><span id="BOOTCFG"></span>Bootcfg

Bootcfg is a command-line tool that edits boot options on local and remote computers. Using the same Bootcfg commands and procedures, you can edit a Boot.ini file or the boot options in Extensible Firmware Interface, Non-Volatile Random Access Memory (EFI NVRAM). Bootcfg is included in the %Systemroot%\\System32 directory in Windows XP and Windows Server 2003. (The Bootcfg display is slightly different on systems that store boot options in EFI NVRAM, but the commands are the same.)

You can use Bootcfg to add, delete, and change all boot entry parameters and boot options; however, you cannot use it to set an indefinite boot time-out value. You can also use Bootcfg commands in a script or batch file to set boot options or to reset them after you replace or upgrade an operating system.

Unlike manual editing, Bootcfg edits boot options without changing the protective attributes on the Boot.ini file. It also helps you avoid typing errors that might prevent the operating system from starting.

You must be a member of the Administrators group on the computer to use Bootcfg. For detailed instructions about using Bootcfg, see Help and Support Center.

### <span id="editing_in_notepad"></span><span id="EDITING_IN_NOTEPAD"></span>Editing in Notepad

You can edit use a text editor, such as Notepad, to edit the Boot.ini file. However, because this method is prone to error, use it only when Bootcfg is not available.

Before editing the Boot.ini file, you must remove the file attributes that Windows uses to protect the file from inadvertent changes. When the Boot.ini file is on an NTFS drive, you must be a member of the Administrators group on the computer to change its attributes.

Use the following procedure to prepare the Boot.ini file for manual editing. This procedure removes the system, hidden, and read-only attributes of the file.

**To configure the Boot.ini file attributes for editing**

1.  At a command prompt, navigate to the root of the boot directory.

2.  Type the following text at the command line:

    ```
    attrib -s -h -r Boot.ini
    ```

    System, hidden, and read-only attributes are removed from the file.

3.  When your editing is complete, you can restore the file attributes to protect the Boot.ini file. However, Ntldr can use the Boot.ini file with any attribute set. At a command prompt, type the following text:

    ```
    attrib +s +h +r Boot.ini
    ```

    This restores the attributes that protect the Boot.ini file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Editing%20the%20Boot.ini%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




