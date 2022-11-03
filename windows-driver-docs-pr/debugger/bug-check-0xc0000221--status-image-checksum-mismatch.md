---
title: Bug Check 0xC0000221 STATUS_IMAGE_CHECKSUM_MISMATCH
description: The STATUS_IMAGE_CHECKSUM_MISMATCH bug check has a value of 0xC0000221. This indicates that a driver or a system DLL has been corrupted.
keywords: ["Bug Check 0xC0000221 STATUS_IMAGE_CHECKSUM_MISMATCH", "STATUS_IMAGE_CHECKSUM_MISMATCH"]
ms.date: 11/03/2022
topic_type:
- apiref
api_name:
- STATUS_IMAGE_CHECKSUM_MISMATCH
api_type:
- NA
---

# Bug Check 0xC0000221: STATUS\_IMAGE\_CHECKSUM\_MISMATCH


The STATUS\_IMAGE\_CHECKSUM\_MISMATCH bug check has a value of 0xC0000221. This indicates that a driver or a system DLL has been corrupted.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## STATUS\_IMAGE\_CHECKSUM\_MISMATCH Parameters


## Cause

This bug check results from a serious error in a driver or other system file. The file header checksum does not match the expected checksum.

This can also be caused by faulty hardware in the I/O path to the file (a disk error, faulty RAM, or a corrupted page file).

## Resolution

- If you can log on to the system again, check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error.

-  Use the System File Checker tool to repair missing or corrupted system files. The System File Checker is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the following command to run the System File Checker tool (SFC.exe).

```console
SFC /scannow
```

For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system).

- Use the scan disk utility to confirm that there are no file system errors. Select and hold (or right-click) on the drive you want to scan and select **Properties**. Select **Tools**. Select the **Check now** button.

-   Confirm that there is sufficient free space on the hard drive. The operating system and some applications require sufficient free space to create swap files and for other functions. Based on the system configuration, the exact requirement varies, but it is normally a good idea to have 10% to 15% free space available.

- Disk errors can be a source of file corruption. Run **Chkdsk /f /r** to detect and resolve any file system structural corruption. You must restart the system before the disk scan begins on a system partition.

- Check with the manufacturer to see if an updated system BIOS or firmware is available. Disabling memory caching of the BIOS or other firmware settings might also resolve this error.

- You can also run an in-place install or recovery over the existing copy of Windows. This preserves all registry settings and configuration information, but replaces all system files.

- Run a virus detection program. Viruses can infect all types of hard disks formatted for Windows, and resulting disk corruption can generate system bug check codes. Make sure the virus detection program checks the Master Boot Record for infections.

- If these methods fail, try reinstalling Windows and then restoring the system from a backup.

## See also

[Bug Check Code Reference](bug-check-code-reference2.md)

