---
title: Editing the Boot.ini File
description: Prior to Windows Vista, BIOS-based computers running Windows store boot options in a Boot.ini text file.
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
ms.date: 07/03/2018
---

# Editing the Boot.ini File


> [!IMPORTANT] 
> This topic describes the boot options supported in Windows XP and Windows Server 2003. If you are changing boot options for modern versions of Windows, see [Boot Options in Windows Vista and Later](./boot-options-in-windows.md).

Prior to Windows Vista, BIOS-based computers running Windows store boot options in a Boot.ini text file. You can edit Boot.ini using Bootcfg (`bootcfg.exe`), a tool included in Windows XP and Windows Server 2003, or using a text editor such as Notepad. Bootcfg is documented in Windows Help and Support. You can also view and change some boot options in Control Panel under System. In the System Properties dialog box, on the Advanced tab, select Settings under **Startup and Recovery**. Because this functionality is limited, it is not discussed in this section. For information about the **Startup and Recovery** dialog box, see Help and Support Center.

## Bootcfg

Bootcfg is a command-line tool that can edit boot options on local and remote computers. Using the same Bootcfg commands and procedures, you can edit Boot.ini, as well as the boot options in Extensible Firmware Interface Non-Volatile Random Access Memory (EFI NVRAM). Bootcfg is included in the `%Systemroot%\\System32` directory in Windows XP and Windows Server 2003. (The Bootcfg display is slightly different on systems that store boot options in EFI NVRAM, but the commands are the same.)

You can use Bootcfg to add, delete, and change all boot entry parameters and boot options; however, you cannot use it to set an indefinite boot time-out value. You can also use Bootcfg commands in a script or batch file to set boot options or to reset them after you replace or upgrade an operating system.

Unlike manual editing, Bootcfg edits boot options without changing the protective attributes on Boot.ini. It also helps you avoid typing errors that might prevent the operating system from starting.

You must be a member of the Administrators group on the computer to use Bootcfg. For detailed instructions about using Bootcfg, see Help and Support Center.

## Editing in Notepad

You can use a text editor, such as Notepad, to edit Boot.ini. However, because this method is prone to error, use it only when Bootcfg is not available.

Before editing Boot.ini, you must remove the file attributes that Windows uses to protect the file from inadvertent changes. When Boot.ini is on an NTFS volume, you must be a member of the Administrators group on the computer to change its attributes.

Use the following procedure to prepare Boot.ini for manual editing. This procedure removes the system, hidden, and read-only attributes of the file.

**To configure Boot.ini attributes for editing**

1.  Open **Windows Command Prompt**. 

2.  Navigate to the root of the system volume.

3.  Type the following text at the command line:

    ```
    attrib -s -h -r Boot.ini
    ```

    System, hidden, and read-only attributes are removed from the file.
    
4.  Open the file in Notepad for editing. Since you are in Windows Command Prompt, the following command should do the trick quickly:

    ```
    notepad.exe Boot.ini
    ```

5.  When your editing is complete, you can restore the file attributes to protect Boot.ini. However, Ntldr can use Boot.ini with any attribute set. To restore attributes, type the following in Windows Command Prompt:

    ```
    attrib +s +h +r Boot.ini
    ```

    This restores the attributes that protect the Boot.ini file.
