---
title: Bug Check 0xC0000221 STATUS_IMAGE_CHECKSUM_MISMATCH
description: The STATUS_IMAGE_CHECKSUM_MISMATCH bug check has a value of 0xC0000221 and indicates that a driver or a system DLL is corrupted.
keywords: ["Bug check 0xC0000221 STATUS_IMAGE_CHECKSUM_MISMATCH", "STATUS_IMAGE_CHECKSUM_MISMATCH"]
ms.date: 12/08/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- STATUS_IMAGE_CHECKSUM_MISMATCH
api_type:
- NA
---

# Bug check 0xC0000221: STATUS_IMAGE_CHECKSUM_MISMATCH

The STATUS_IMAGE_CHECKSUM_MISMATCH bug check has a value of 0xC0000221. The bug check indicates that a driver or a system DLL is corrupted.

> [!IMPORTANT]
> This article is for programmers. If you're a Microsoft customer and your computer displays a blue screen error code, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## STATUS_IMAGE_CHECKSUM_MISMATCH parameters

None.

## Cause

This bug check results from a serious error in a driver or other system file. The file header checksum doesn't match the expected checksum.

This bug check also might be caused by faulty hardware in the I/O path to the file, such as a disk error, faulty RAM, or a corrupted page file.

## Resolution

To resolve this bug check, try the following options:

- If you can sign in to the system, check System Log in Event Viewer for more error messages that might help you identify the device or driver that's causing the error.

- Use the System File Checker tool to repair missing or corrupted system files. System File Checker (SFC.exe) is a Windows utility you can use to scan for and restore corrupted Windows system files.

   Use the following command to run System File Checker:

   ```console
   SFC /scannow
   ```

   For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system).

- Use the Windows disk scan utility to check for file system errors. In File Explorer, select and hold or right-click the drive you want to scan and select **Properties**. Select the **Tools** tab. Under **Error checking**, select **Check**.

- Check for sufficient free space on the hard drive. The operating system and some applications require enough free space to create swap files and to complete other functions. The exact requirement varies depending on the system configuration, but it's typically a good idea to have 10% to 15% free space available.

- Disk errors might cause file corruption. Run `Chkdsk /f /r` to detect and resolve any structural corruption in the file system. You must restart the system before the disk scan begins on a system partition.

- Check with the manufacturer to see if an updated system BIOS or firmware is available. Disabling memory caching of the BIOS or other firmware settings also might resolve this error.

- You can run an in-place installation or recovery over the existing copy of Windows. An in-place installation or recovery preserves all registry settings and configuration information, but all system files are replaced.

- Run a virus detection program. Viruses can infect all types of hard disks that are formatted for Windows. Resulting disk corruption can generate system bug check codes. Make sure that the virus detection program checks the Master Boot Record for infections.

- If these methods fail, reinstall Windows, and then restore the system from a backup.

## See also

[Bug check code reference](bug-check-code-reference2.md)
