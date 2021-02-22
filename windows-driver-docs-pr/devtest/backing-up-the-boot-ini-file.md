---
title: Backing Up the Boot.ini File
description: When you install or upgrade an NT-based Windows operating system prior to Windows Vista, the Windows installer creates a new Boot.ini file for the computer. The new file retains some, but not all, of the changes you might have made to the file.
keywords:
- Boot.ini files WDK , backing up
- back ups WDK boot options
- back ups WDK boot options , Boot.ini files
- copying boot options
- saving boot options
- boot options WDK , backing up
ms.date: 07/03/2018
ms.localizationpriority: medium
---

# Backing Up the Boot.ini File


> [!IMPORTANT] 
> This topic describes the boot options supported in Windows XP and Windows Server 2003. If you are changing boot options for modern versions of Windows, see [Boot Options in Windows(boot-options-in-windows.md).

When you install or upgrade to Windows XP, Windows Server 2003 or one their predecessors, the Windows installer creates a new *Boot.ini* file for the computer. The new file retains some, but not all, of the changes you might have made to the file. Thus, to preserve an edited *Boot.ini* file, make a backup copy before upgrading or installing an operating system. After an update completes, you can replace the new file with your backup copy. If you have installed a new operating system, you can copy customized entries from your backup copy and then paste them into the new *Boot.ini* file.

An update or installation restores the default security attributes on Boot.ini, including the read-only attribute. To edit the file, use the Bootcfg command or change the file attributes. For more information, see [Editing the Boot.ini File](editing-the-boot-ini-file.md).


