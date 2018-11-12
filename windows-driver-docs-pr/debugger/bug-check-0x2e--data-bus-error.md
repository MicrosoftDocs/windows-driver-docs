---
title: Bug Check 0x2E DATA_BUS_ERROR
description: The DATA_BUS_ERROR bug check has a value of 0x0000002E. This typically indicates that a parity error in system memory has been detected.
ms.assetid: 117adb1b-49aa-4c4e-ae01-730d1d653c02
keywords: ["Bug Check 0x2E DATA_BUS_ERROR", "DATA_BUS_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DATA_BUS_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x2E: DATA\_BUS\_ERROR


The DATA\_BUS\_ERROR bug check has a value of 0x0000002E. This typically indicates that a parity error in system memory has been detected.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DATA\_BUS\_ERROR Parameters


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
<td align="left"><p>Virtual address that caused the fault</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Physical address that caused the fault</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Processor status register (PSR)</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Faulting instruction register (FIR)</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This error is almost always caused by a hardware problem -- a configuration issue, defective hardware, or incompatible hardware.

The most common hardware problems that can cause this error are defective RAM, Level 2 (L2) RAM cache errors, or video RAM errors. Hard disk corruption can also cause this error.

This bug check can also be caused when a device driver attempts to access an address in the 0x8*xxxxxxx* range that does not exist (in other words, that does not have a physical address mapping).

Resolution
----------

**Resolving a hardware problem:** If hardware has recently been added to the system, remove it to see if the error recurs.

If existing hardware has failed, remove or replace the faulty component. You should run hardware diagnostics supplied by the system manufacturer to determine which hardware component has failed. For details on these procedures, see the owner's manual for your computer. Check that all adapter cards in the computer are properly seated. Use an ink eraser or an electrical contact treatment, available at electronics supply stores, to ensure that adapter card contacts are clean.

If the problem occurs on a newly installed system, check the availability of updates for the BIOS, the SCSI controller or network cards. Updates of this kind are typically available on the Web site or the bulletin board system (BBS) of the hardware manufacturer.

If the error occurs after installing a new or updated device driver, the driver should be removed or replaced. If, under this circumstance, the error occurs during startup and the system partition is formatted with NTFS, you might be able to use Safe Mode to rename or delete the faulty driver.

If the driver is used as part of the system startup process in Safe Mode, you need to start the computer using the Recovery Console in order to access the file.

For additional error messages that might help pinpoint the device or driver that is causing the error, check the System Log in Event Viewer. Disabling memory caching or shadowing in the BIOS might also resolve this error. In addition, check the system for viruses, using any up-to-date commercial virus scanning software that examines the Master Boot Record of the hard disk. All Windows file systems can be infected by viruses.

**Resolving a hard disk corruption problem:** Run **Chkdsk /f /r** on the system partition. You must restart the system before the disk scan begins. If you cannot start the system due to the error, use the Recovery Console and run **Chkdsk /r**.

**Warning**   If your system partition is formatted with the file allocation table (FAT) file system, the long filenames used by Windows can be damaged if Scandisk or another Microsoft MS-DOS-based hard disk tool is used to verify the integrity of your hard disk from MS-DOS. Always use the version of Chkdsk that matches your Windows version.

 

 

 




