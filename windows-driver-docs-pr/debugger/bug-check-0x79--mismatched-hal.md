---
title: Bug Check 0x79 MISMATCHED_HAL
description: The MISMATCHED_HAL bug check has a value of 0x00000079 that indicates that the HAL revision level or configuration does not match that of the kernel or the computer.
ms.assetid: 2d063c2a-c647-4436-b005-04f71a4d2b66
keywords: ["Bug Check 0x79 MISMATCHED_HAL", "MISMATCHED_HAL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- MISMATCHED_HAL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x79: MISMATCHED\_HAL


The MISMATCHED\_HAL bug check has a value of 0x00000079. This bug check indicates that the Hardware Abstraction Layer (HAL) revision level or configuration does not match that of the kernel or the computer.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## MISMATCHED\_HAL Parameters


Parameter 1 indicates the type of mismatch.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>The major processor control block (PRCB) level of Ntoskrnl.exe.</p></td>
<td align="left"><p>The major PRCB level of Hal.dll.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The PRCB release levels are mismatched. (Something is out of date.)</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>The build type of Ntoskrnl.exe.</p></td>
<td align="left"><p>The build type of Hal.dll.</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>The build types are mismatched.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>The size of the loader parameter extension.</p></td>
<td align="left"><p>The major version of the loader parameter extension.</p></td>
<td align="left"><p>The minor version of the loader parameter extension.</p></td>
<td align="left"><p>The loader (ntldr) and HAL versions are mismatched.</p></td>
</tr>
</tbody>
</table>

 

When Parameter 1 equals 0x2, the following build type codes are used:

-   0: Multiprocessor-enabled free build

-   1: Multiprocessor-enabled checked build

-   2: Single-processor free build

-   3: Single-processor checked build

Cause
-----

The MISMATCHED\_HAL bug check often occurs when a user manually updates Ntoskrnl.exe or Hal.dll.

The error can also indicate that one of those two files is out of date. For example, the HAL might be designed for Microsoft Windows 2000 and the kernel is designed for Windows XP. Or the computer might erroneously have a multiprocessor HAL and a single-processor kernel installed, or vice versa.

The Ntoskrnl.exe kernel file is for single-processor systems and Ntkrnlmp.exe is for multiprocessor systems. However, these file names correspond to the files on the installation media.After you have installed the Windows operating system, the file is renamed to Ntoskrnl.exe, regardless of the source file that is used. The HAL file also uses the name Hal.dll after installation, but there are several possible HAL files on the installation media. For more information, see "Installing the Checked Build" in the Windows Driver Kit (WDK).

Resolution
----------

Restart the computer by using the product CD or the Windows Setup disks. At the Welcome screen, press F10 to start the Recovery Console. Use the **Copy** command to copy the correct HAL or kernel file from the original CD into the appropriate folder on the hard disk. The **Copy** command detects whether the file that you are copying is in the Microsoft compressed file format. If so, it automatically expands the file that is copied on the target drive.

 

 




