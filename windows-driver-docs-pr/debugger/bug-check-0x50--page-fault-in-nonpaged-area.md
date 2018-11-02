---
title: Bug Check 0x50 PAGE_FAULT_IN_NONPAGED_AREA
description: The PAGE_FAULT_IN_NONPAGED_AREA bug check has a value of 0x00000050. This indicates that invalid system memory has been referenced. 
ms.assetid: 63b4ab82-f7a9-4e14-bf7c-707a22d7e251
keywords: ["Bug Check 0x50 PAGE_FAULT_IN_NONPAGED_AREA", "PAGE_FAULT_IN_NONPAGED_AREA"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PAGE_FAULT_IN_NONPAGED_AREA
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x50: PAGE\_FAULT\_IN\_NONPAGED\_AREA


The PAGE\_FAULT\_IN\_NONPAGED\_AREA bug check has a value of 0x00000050. This indicates that invalid system memory has been referenced. Typically the memory address is wrong or the memory address is pointing at freed memory.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PAGE\_FAULT\_IN\_NONPAGED\_AREA Parameters


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
<td align="left"><p>Memory address referenced</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p><strong>0:</strong> Read operation</p>
<p><strong>1:</strong> Write operation</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Address that referenced memory (if known)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

If the driver responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**.

Cause
-----

Bug check 0x50 can occur after the installation of faulty hardware or in the event of failure of installed hardware (usually related to defective RAM, be it main memory, L2 RAM cache, or video RAM).

Another possible cause is the installation of a faulty system service or faulty driver code.

Antivirus software can also trigger this error, as can a corrupted NTFS volume.

Resolution
----------

**Gather Information**

Examine the name of the driver if that was listed on the blue screen.

Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://windows.microsoft.com/windows/what-information-event-logs-event-viewer#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

**Windows Memory Diagnostics**

Run the Windows Memory Diagnostics tool, to test the memory. Click the Start button, and then clicking Control Panel. In the search box, type Memory, and then click **Diagnose your computer's memory problems**.‌ After the test is run, use Event viewer to view the results under the System log. Look for the *MemoryDiagnostics-Results* entry to view the results.

**Resolving a faulty hardware problem:** If hardware has been added to the system recently, remove it to see if the error recurs. If existing hardware has failed, remove or replace the faulty component. You should run hardware diagnostics supplied by the system manufacturer. For details on these procedures, see the owner's manual for your computer.

**Resolving a faulty system service problem:** Disable the service and confirm that this resolves the error. If so, contact the manufacturer of the system service about a possible update. If the error occurs during system startup, investigate the Windows repair options. For more information, see [Recovery options in Windows 10](https://windows.microsoft.com/windows-10/windows-10-recovery-options).

**Resolving an antivirus software problem:** Disable the program and confirm that this resolves the error. If it does, contact the manufacturer of the program about a possible update.

**Resolving a corrupted NTFS volume problem:** Run **Chkdsk /f /r** to detect and repair disk errors. You must restart the system before the disk scan begins on a system partition. Contact the manufacture of the hard driver system to locate any diagnostic tools that they provide for the hard drive sub system.

For general blue screen troubleshooting information, see [**Blue Screen Data**](blue-screen-data.md).

Remarks
-------

Typically, this address is in freed memory or is simply invalid.

This cannot be protected by a **try - except** handler -- it can only be protected by a probe.

 

 




