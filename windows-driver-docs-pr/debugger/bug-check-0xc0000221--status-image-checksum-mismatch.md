---
title: Bug Check 0xC0000221 STATUS_IMAGE_CHECKSUM_MISMATCH
description: The STATUS_IMAGE_CHECKSUM_MISMATCH bug check has a value of 0xC0000221. This indicates that a driver or a system DLL has been corrupted.
ms.assetid: d0baccb0-51a2-45c7-ae08-507217d0ac96
keywords: ["Bug Check 0xC0000221 STATUS_IMAGE_CHECKSUM_MISMATCH", "STATUS_IMAGE_CHECKSUM_MISMATCH"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- STATUS_IMAGE_CHECKSUM_MISMATCH
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xC0000221: STATUS\_IMAGE\_CHECKSUM\_MISMATCH


The STATUS\_IMAGE\_CHECKSUM\_MISMATCH bug check has a value of 0xC0000221. This indicates that a driver or a system DLL has been corrupted.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## STATUS\_IMAGE\_CHECKSUM\_MISMATCH Parameters


Cause
-----

This bug check results from a serious error in a driver or other system file. The file header checksum does not match the expected checksum.

This can also be caused by faulty hardware in the I/O path to the file (a disk error, faulty RAM, or a corrupted page file).

Resolution
----------

To remedy this error, run the Emergency Recovery Disk (ERD) and allow the system to repair or replace the missing or damaged driver file on the system partition.

You can also run an in-place upgrade over the existing copy of Windows. This preserves all registry settings and configuration information, but replaces all system files. If any Service Packs and/or hotfixes had previously been applied, you need to reinstall them afterward in the appropriate order (latest Service Pack, then any post-Service Pack hotfixes in the order in which they were originally installed, if applicable).

If a specific file was identified in the bug check message as being corrupted, you can try replacing that individual file manually. If the system partition is formatted with FAT, you can start from an MS-DOS startup disk and copy the file from the original source onto the hard disk. If you have a dual-boot machine, you can boot to your other operating system and replace the file.

If you want to replace the file on a single-boot system with an NTFS partition, you need to restart the system, press F8 at the operating system **Loader** menu, and choose **Safe Mode with Command Prompt**. From there, copy a fresh version of the file from the original source onto the hard disk. If the file is used as part of the system startup process in Safe Mode, you need to start the computer using the Recovery Console in order to access the file. If these methods fail, try reinstalling Windows and then restoring the system from a backup.

**Note**   If the original file from the product CD has a filename extension ending in an \_ (underscore), the file needs to be uncompressed before it can be used. The Recovery Console's **Copy** command automatically detects compressed files and expands them as they are copied to the target location. If you are using Safe Mode to access a drive, use the **Expand** command to uncompress and copy the file to the target folder. You can use the **Expand** command in the command line environment of Safe Mode.

 

**Resolving a disk error problem:** Disk errors can be a source of file corruption. Run **Chkdsk /f /r** to detect and resolve any file system structural corruption. You must restart the system before the disk scan begins on a system partition.

**Resolving a RAM problem:** If the error occurred immediately after RAM was added to the system, the paging file might be corrupted or the new RAM itself might be either faulty or incompatible.

**To determine if newly added RAM is causing a bug check**

1.  Return the system to the original RAM configuration.

2.  Use the Recovery Console to access the partition containing the paging file and delete the file pagefile.sys.

3.  While still in the Recovery Console, run **Chkdsk /r** on the partition that contained the paging file.

4.  Restart the system.

5.  Set the paging file to an optimal level for the amount of RAM added.

6.  Shutdown the system and add your RAM.

    The new RAM must meet the system manufacturer's specifications for speed, parity, and type (that is, fast page-mode (FPM) versus extended data out (EDO) versus synchronous dynamic random access memory (SDRAM)). Try to match the new RAM to the existing installed RAM as closely as possible. RAM can come in many different capacities, and more importantly, in different formats (single inline memory modules -- SIMM -- or dual inline memory modules -- DIMM). The electrical contacts can be either gold or tin and it is not wise to mix these contact types.

If you experience the same error message after reinstalling the new RAM, run hardware diagnostics supplied by the system manufacturer, especially the memory scanner. For details on these procedures, see the owner's manual for your computer.

When you can log on to the system again, check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error.

Disabling memory caching of the BIOS might also resolve this error.

 

 




