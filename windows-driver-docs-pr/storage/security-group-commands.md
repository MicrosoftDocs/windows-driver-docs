---
title: Security Group Commands
description: The following sections describe special requirements for sending certain security commands.
ms.assetid: 956C26D7-A434-4055-892B-E6E2D5B70CFA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Security Group Commands


The following sections describe special requirements for sending certain security commands.

## <span id="SECURE_ERASE"></span><span id="secure_erase"></span>SECURE ERASE


To increase data security, starting with Windows 8, the ability to send ATA security group commands (such as the commands used to perform SECURE ERASE) is restricted to the Windows Preinstallation Environment (WinPE) with the use of a specific, hard-coded password. The reason for this is to ensure that when issuing SECURE ERASE commands, the device can remain in a secure state while, at the same time, allowing a device unlock if power loss or some other unforeseen event occurs during the processing of the SECURE ERASE commands.

Since some applications still need to issue these commands, the following process of performing a SECURE ERASE on Windows 8 or newer is described.

**Note**  In Windows Vista and Windows 7 no ATA Security Group commands are permitted in the Microsoft provided ATA storage driver stack. A SECURITY FREEZE LOCK is sent at driver initialization time preventing an erase.

 

The SECURE ERASE feature is performed using this sequence of the following ATA Security Group commands:

-   SECURITY SET PASSWORD
-   SECURITY ERASE PREPARE
-   SECURITY ERASE UNIT

The requirements to perform a SECURE ERASE are:

-   A SECURITY FREEZE LOCK command is not sent from BIOS during initialization.
-   The AHCI controller is not operating in IDE/ATA mode (e.g. the Microsoft PATA driver, *atapi.sys*, must not manage the controller).
-   A system must boot into a Windows 8, or greater, based WinPE. When running under WinPE, Microsoft’s AHCI driver, *StorAHCI.sys*, does not send a SECURITY FREEZE LOCK command during initialization.
-   Issue a SECURITY SET PASSWORD command containing “AutoATAWindowsString12345678901” as the user password string.

    **Note**  This command allows setting only the user password.

     

-   Perform security command processing as necessary, including sending SECURITY ERASE PREPARE and SECURITY ERASE UNIT.

For new applications, it is recommended to use the CRYPTO SCRAMBLE EXT command from the SANITIZE feature set. This is preferred over the SECURITY ERASE UNIT command since SANITIZE is supported in both the T10 standard (SCSI) and the T13 standard (ATA), and for all derived busses.

 

 




