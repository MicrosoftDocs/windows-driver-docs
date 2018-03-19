---
title: Editing the Boot.ini File
description: Prior to Windows Vista, BIOS-based computers running Windows store boot options in a Boot.ini text file.
ms.assetid: 9edbbd5e-36b5-4a80-925d-a007a4469984
keywords:
- Bootcfg tool
- Boot.ini files WDK , editing
- editing boot options
- Notepad WDK boot options
- text editors WDK boot options
- manual editing WDK boot options
- boot entry parameters WDK
- boot parameters WDK
- indefinite boot time-out values WDK
- boot time-out values WDK
- time-outs WDK boot options
- Boot.ini files WDK , attribute removal
- removing Boot.ini attributes
- viewing boot options
- Boot.ini files WDK , viewing
- editors WDK boot options
- boot options WDK , editing
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 





