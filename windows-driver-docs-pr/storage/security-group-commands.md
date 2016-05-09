---
title: Security Group Commands
author: windows-driver-content
description: The following sections describe special requirements for sending certain security commands.
ms.assetid: 956C26D7-A434-4055-892B-E6E2D5B70CFA
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Security%20Group%20Commands%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


