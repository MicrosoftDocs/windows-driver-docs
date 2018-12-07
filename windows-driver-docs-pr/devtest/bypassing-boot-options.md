---
title: Bypassing Boot Options
description: Bypassing Boot Options
ms.assetid: 7991fed3-943e-4d43-acba-e2462f7e9d03
keywords:
- boot options WDK , bypassing
- F8 key (bypassing boot options) WDK
- bypassing boot options
- kernel debugging support WDK boot options
- Debugging Mode WDK boot options
- skipping boot options
ms.date: 07/02/2018
ms.localizationpriority: medium
---

# Bypassing Boot Options

Under normal circumstances, to debug a program or driver on an operating system prior to Windows Vista, you would create a boot option for debugging, reboot the computer, and then select the debugging option from the boot menu. However, sometimes you are unable to edit the boot options on a computer that needs to be debugged.

For example, you may have a computer that encounters a bug check before the login screen is reached, preventing you from editing the Boot.ini file through Windows. You can start Microsoft MS-DOS from a floppy disk, but if the boot partition of your hard disk is in NTFS format, you will not be able to edit the Boot.ini file from MS-DOS.

If you are unable to edit the boot options directly, restart the computer and wait until the initial BIOS procedures are complete. At this point, if you have multiple operating systems installed, you will see the boot menu. When this menu appears, press the F8 key. If you do not have multiple boot options, you will not see the boot menu, but you can still press the F8 key during the first two seconds of the loading of Windows. You may find it easiest to just begin pressing F8 repeatedly when the BIOS procedures are nearly complete and keep pressing it until the menu appears.

Pressing F8 will cause the Troubleshooting and Advanced Startup Options menu to appear. One of the choices on this menu is **Debugging Mode**. If you select this option, you will be able to start Windows with kernel debugging support. The kernel debugger connection will be active at a baud rate of 19200 through the highest enumerated COM port (for example, COM2 if you have two ports).

Starting with Windows 8 and Windows Server 2012, the boot loader no longer responds to F8. Instead, when the boot loader detects that the operating system is in trouble, e.g. the login screen cannot be reached, it automatically presents you with the relevant diagnostics options, among which the **Debugging Mode** could be found. If the login screen can be reached, however, one can trigger the display of diagnostics option during the next startup by holding down Shift key while issuing a Restart command.

 





