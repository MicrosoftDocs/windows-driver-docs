---
title: Bug Check 0x24 NTFS_FILE_SYSTEM
description: The NTFS_FILE_SYSTEM bug check has a value of 0x00000024. This indicates a problem occurred in ntfs.sys, the driver file that allows the system to read and write to NTFS drives.
ms.assetid: 9d2dd8a8-b550-4392-b663-6902a015ef7b
keywords: ["Bug Check 0x24 NTFS_FILE_SYSTEM", "NTFS_FILE_SYSTEM"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- NTFS_FILE_SYSTEM
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x24: NTFS\_FILE\_SYSTEM


The NTFS\_FILE\_SYSTEM bug check has a value of 0x00000024. This indicates a problem occurred in ntfs.sys, the driver file that allows the system to read and write to NTFS drives.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## NTFS\_FILE\_SYSTEM Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1</p></td>
<td align="left"><p>Specifies source file and line number information. The high 16 bits (the first four hexadecimal digits after the &quot;0x&quot;) identify the source file by its identifier number. The low 16 bits identify the source line in the file where the bug check occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>If <strong>NtfsExceptionFilter</strong> is on the stack, this parameter specifies the address of the exception record.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>If <strong>NtfsExceptionFilter</strong> is on the stack, this parameter specifies the address of the context record.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

One possible cause of this bug check is disk corruption. Corruption in the NTFS file system or bad blocks (sectors) on the hard disk can induce this error. Corrupted hard drive (SATA/IDE) drivers can also adversely affect the system's ability to read and write to disk, thus causing the error.

Resolution
----------

**To debug this problem:** Use the [**.cxr (Display Context Record)**](-cxr--display-context-record-.md) command with Parameter 3, and then use [**kb (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md).

**To resolve a disk corruption problem:**

-   Check Event Viewer for error messages related to the hard drive appearing in the System Log that might help pinpoint the device or driver that is causing the error.

-   Try disabling any virus scanners, backup programs, or disk defragmenter tools that continually monitor the system.

-   You should also run hardware diagnostics supplied by the system manufacturer related to the storage sub system.

-   Use the scan disk utility to confirm that there are no file system errors. Right click on the drive you want to scan and select **Properties**. Click on **Tools**. Click the **Check now** button.
-   Confirm that there is sufficient free space on the hard drive. The operating system and some applications require sufficient free space to create swap files and for other functions. Based on the system configuration, the exact requirement varies, but it is normally a good idea to have 10% to 15% free space available.

-   Use the System File Checker tool to repair missing or corrupted system files. The System File Checker is a utility in Windows that allows users to scan for corruptions in Windows system files and restore corrupted files. Use the following command to run the System File Checker tool (SFC.exe).

    ```console
    SFC /scannow
    ```

    For more information, see [Use the System File Checker tool to repair missing or corrupted system files](https://support.microsoft.com/kb/929833).

-   **Driver Verifier**

    Driver Verifier is a tool that runs in real time to examine the behavior of drivers. If it see errors in the execution of driver code, it proactively creates an exception to allow that part of the driver code to be further scrutinized. The driver verifier manager is built into Windows and is available on all Windows PCs. To start the driver verifier manager, type *Verifer* at a command prompt. You can configure which drivers you would like to verify. The code that verifies drivers adds overhead as it runs, so try and verify the smallest number of drivers as possible. For more information, see [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448).

In the past, another possible cause of this stop code is depletion of nonpaged pool memory. If the nonpaged pool memory is completely depleted, this error can stop the system. However, during the indexing process, if the amount of available nonpaged pool memory is very low, another kernel-mode driver requiring nonpaged pool memory can also trigger this error.

 

 




