---
title: Bug Check 0x85 SETUP_FAILURE
description: The SETUP_FAILURE bug check has a value of 0x00000085. This bug check indicates that a fatal error occurred during setup.
ms.assetid: 52c93485-7c20-4a7e-8fc7-d520753973ed
keywords: ["Bug Check 0x85 SETUP_FAILURE", "SETUP_FAILURE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SETUP_FAILURE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x85: SETUP\_FAILURE


The SETUP\_FAILURE bug check has a value of 0x00000085. This bug check indicates that a fatal error occurred during setup.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SETUP\_FAILURE Parameters


Parameter 1 indicates the type of violation. Parameter 4 is not used. The meaning of the other parameters depends on the value of Parameter 1.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The OEM HAL font is not a valid .fon format file, so setup cannot display text.</p>
<p>This cause indicates that Vga<em>xxx</em>.fon on the boot floppy or CD is damaged.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1</p></td>
<td align="left"><p>The precise video initialization failure:</p>
<p><strong>0:NtCreateFile</strong> of \device\video0</p>
<p><strong>1:</strong> IOCTL_VIDEO_QUERY_NUM_AVAIL_MODES</p>
<p><strong>2:</strong> IOCTL_VIDEO_QUERY_AVAIL_MODES</p>
<p><strong>3:</strong> The desired video mode is not supported. This value indicates an internal setup error.</p>
<p><strong>4:</strong> IOCTL_VIDEO_SET_CURRENT_MODE (unable to set video mode)</p>
<p><strong>5:</strong> IOCTL_VIDEO_MAP_VIDEO_MEMORY</p>
<p><strong>6:</strong> IOCTL_VIDEO_LOAD_AND_SET_FONT</p></td>
<td align="left"><p>The status code from the NT API call, if appropriate</p></td>
<td align="left"><p>Video initialization failed.</p>
<p>This failure might indicate that the disk that contains Vga.sys (or another video driver that is appropriate to the computer) is damaged or that the computer has video hardware that the Microsoft Windows operating system cannot communicate with.</p>
<p></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Out of memory.</p>
<p></p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3</p></td>
<td align="left"><p>The precise keyboard initialization failure:</p>
<p><strong>0:NtCreateFile</strong> of \device\KeyboardClass0 failed. (Setup did not find a keyboard connected to the computer.)</p>
<p><strong>1:</strong> Unable to load keyboard layout DLL. (Setup could not load the keyboard layout file. This failure indicates that the CD or floppy disk is missing a file, such as Kbdus.dll for the U.S. release or another layout DLL for localized releases.)</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Keyboard initialization failed.</p>
<p>This failure might indicate that the disk that contains the keyboard driver (I8042prt.sys or Kbdclass.sys) is damaged or that the computer has keyboard hardware that Windows cannot communicate with. This failure might also mean that the keyboard layout DLL could not be loaded.</p>
<p></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x4</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>Setup could not resolve the ARC device path name of the device that setup was started from.</p>
<p>This error is an internal setup error.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x5</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Reserved</p></td>
<td align="left"><p>Partitioning sanity check failed.</p>
<p>This error indicates a bug in a disk driver.</p>
<p></p></td>
</tr>
</tbody>
</table>

 

 

 




