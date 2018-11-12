---
title: Bug Check 0x7A KERNEL_DATA_INPAGE_ERROR
description: The KERNEL_DATA_INPAGE_ERROR bug check has a value of 0x0000007A. This bug check indicates that the requested page of kernel data from the paging file could not be read into memory.
ms.assetid: 466d4864-8840-47b2-9a9a-302a125bf095
keywords: ["Bug Check 0x7A KERNEL_DATA_INPAGE_ERROR", "KERNEL_DATA_INPAGE_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KERNEL_DATA_INPAGE_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x7A: KERNEL\_DATA\_INPAGE\_ERROR


The KERNEL\_DATA\_INPAGE\_ERROR bug check has a value of 0x0000007A. This bug check indicates that the requested page of kernel data from the paging file could not be read into memory.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KERNEL\_DATA\_INPAGE\_ERROR Parameters


The four parameters that are listed in the message can have three possible meanings. If the first parameter is 1 or 2, or 3 and the third parameter is 0, the parameters have the following definitions.

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
<td align="left"><p>The lock type that was held (1, 2, or 3)</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The error status (usually an I/O status code)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p><strong>If Lock Type is 1:</strong> the current process</p>
<p><strong>If Lock Type is 2 or 3:</strong> 0</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The virtual address that could not be paged into memory</p></td>
</tr>
</tbody>
</table>

 

If the first parameter is 3 (and the third parameter is nonzero) or 4, the parameters have the following definitions.

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
<td align="left"><p>The lock type that was held (3 or 4)</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The error status (typically an I/O status code)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The address of the InPageSupport structure</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The faulting address</p></td>
</tr>
</tbody>
</table>

 

Otherwise, the parameters have the following definitions.

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
<td align="left"><p>The address of the page table entry (PTE)</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The error status (usually an I/O status code)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The PTE contents</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The faulting address</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

Frequently, you can determine the cause of the KERNEL\_DATA\_INPAGE\_ERROR bug check from the error status (Parameter 2). Some common status codes include the following:

-   0xC000009A, or STATUS\_INSUFFICIENT\_RESOURCES, indicates a lack of nonpaged pool resources.

-   0xC000009C, or STATUS\_DEVICE\_DATA\_ERROR, typically indicates bad blocks (sectors) on the hard disk.

-   0xC000009D, or STATUS\_DEVICE\_NOT\_CONNECTED, indicates defective or loose cabling, termination, or that the controller does not see the hard disk.

-   0xC000016A, or STATUS\_DISK\_OPERATION\_FAILED, indicates bad blocks (sectors) on the hard disk.

-   0xC0000185, or STATUS\_IO\_DEVICE\_ERROR, indicates improper termination or defective cabling on SCSI devices or that two devices are trying to use the same IRQ.

-   0xC000000E, or STATUS\_NO\_SUCH\_DEVICE, indicates a hardware failure or an incorrect drive configuration. Check your cables and check the drive with the diagnostic utility available from your drive manufacturer. If you are using older PATA (IDE) drives, this status code can indicate an incorrect master/subordinate drive configuration.

These status codes are the most common ones that have specific causes. For more information about other possible status codes that can be returned, see the Ntstatus.h file in the Microsoft Windows Driver Kit (WDK).

Another common cause of this error message is defective hardware or failing RAM.

A virus infection can also cause this bug check.

Resolution
----------

**Resolving a bad block problem:** An I/O status code of 0xC000009C or 0xC000016A typically indicates that the data could not be read from the disk because of a bad block (sector). If you can restart the computer after the error, Autochk runs automatically and attempts to map the bad sector to prevent it from being used anymore.

If Autochk does not scan the hard disk for errors, you can manually start the disk scanner. Run **Chkdsk /f /r** on the system partition. You must restart the computer before the disk scan begins. If you cannot start the computer because of the error, use the Recovery Console and run **Chkdsk /r**.

**Warning**   If your system partition is formatted with the FAT file system, the long file names that the Windows operating system uses might be damaged if you use Scandisk or another MS-DOS-based hard disk tool to verify the integrity of your hard disk from MS-DOS. Always use the version of Chkdsk that matches your version of Windows.

 

**Resolving a defective hardware problem:** If the I/O status is C0000185 and the paging file is on an SCSI disk, check the disk cabling and SCSI termination for problems.

**Resolving a failing RAM problem:** Run the hardware diagnostics that the system manufacturer supplies, especially the memory scanner. For more information about these procedures, see the owner's manual for your computer.

Check that all the adapter cards in the computer are properly seated. Use an ink eraser or an electrical contact treatment, available at electronics supply stores, to ensure adapter card contacts are clean.

Check the System Log in Event Viewer for additional error messages that might help identify the device that is causing the error. You can also disable memory caching of the BIOS to try to resolve this error.

Make sure that the latest Windows Service Pack is installed.

If the preceding steps do not resolve the error, take the system motherboard to a repair facility for diagnostic testing. A crack, a scratched trace, or a defective component on the motherboard can cause this error.

**Resolving a virus infection:** Check your computer for viruses by using any up-to-date, commercial virus scanning software that examines the Master Boot Record of the hard disk. All Windows file systems can be infected by viruses.

## <span id="see_also"></span>See also


[**Bug Check 0x77 (KERNEL\_STACK\_INPAGE\_ERROR)**](bug-check-0x77--kernel-stack-inpage-error.md)

 

 




