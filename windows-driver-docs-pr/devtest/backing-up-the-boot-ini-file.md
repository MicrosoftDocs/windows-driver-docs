---
title: Backing Up the Boot.ini File
description: When you install or upgrade an NT-based Windows operating system prior to Windows Vista, the Windows installer creates a new Boot.ini file for the computer. The new file retains some, but not all, of the changes you might have made to the file.
ms.assetid: c4881f5d-3404-4e87-b130-33bc57b45ec9
keywords:
- Boot.ini files WDK , backing up
- back ups WDK boot options
- back ups WDK boot options , Boot.ini files
- copying boot options
- saving boot options
- boot options WDK , backing up
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Backing Up the Boot.ini File


\[This topic describes the boot options supported in Windows XP and Windows Server 2003. If you are changing boot options for Windows 8, Windows Server 2012, Windows 7, Windows Server 2008, or Windows Vista, see [Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md).\]

When you install or upgrade an NT-based Windows operating system prior to Windows Vista, the Windows installer creates a new *Boot.ini* file for the computer. The new file retains some, but not all, of the changes you might have made to the file.

To preserve an edited *Boot.ini* file, make a backup copy before upgrading or installing an operating system.

## <span id="ddk_backing_up_the_boot_ini_file_tools"></span><span id="DDK_BACKING_UP_THE_BOOT_INI_FILE_TOOLS"></span>


After an update completes, you can replace the new file with your backup copy. If you have installed a new operating system, you can copy customized entries from your backup copy and then paste them into the new *Boot.ini* file.

An update or installation restores the default security attributes on the *Boot.ini* file, including the read-only attribute. To edit the file, use the Bootcfg command or change the file attributes. For more information, see [Editing the Boot.ini File](editing-the-boot-ini-file.md).

 

 





