---
title: Bug Check 0x77 KERNEL_STACK_INPAGE_ERROR
description: The KERNEL_STACK_INPAGE_ERROR bug check has a value of 0x00000077. This bug check indicates that the requested page of kernel data from the paging file could not be read into memory.
ms.assetid: 203a6d0f-0caa-46ed-9bab-61bbde1c8016
keywords: ["Bug Check 0x77 KERNEL_STACK_INPAGE_ERROR", "KERNEL_STACK_INPAGE_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KERNEL_STACK_INPAGE_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x77: KERNEL\_STACK\_INPAGE\_ERROR


The KERNEL\_STACK\_INPAGE\_ERROR bug check has a value of 0x00000077. This bug check indicates that the requested page of kernel data from the paging file could not be read into memory.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KERNEL\_STACK\_INPAGE\_ERROR Parameters


The four parameters that listed in the message have two possible meanings.

If the first parameter is 0, 1, or 2, the parameters have the following meaning.

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
<td align="left"><p><strong>0:</strong> The page of kernel data was retrieved from page cache.</p>
<p><strong>1:</strong> The page was retrieved from a disk.</p>
<p><strong>2:</strong> The page was retrieved from a disk, the storage stack returned SUCCESS, but <strong>Status.Information</strong> is not equal to PAGE_SIZE.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The value that appears in the stack where the signature should be.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The address of the signature on the kernel stack</p></td>
</tr>
</tbody>
</table>

 

If the first parameter is any value other than 0, 1, or 2, the parameters have the following meaning.

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
<td align="left"><p>The status code</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The I/O status code</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The page file number</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The offset into page file</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

If the first parameter is 0 or 1, the stack signature in the kernel stack was not found. This error is probably caused by defective hardware, such as a RAM error.

If the first parameter is 2, the driver stack returned an inconsistent status for the read of the page. For example, the driver stack returned a success status even though it did not read the whole page.

If the first parameter is any value other than 0, 1, or 2, the value of the first parameter is an NTSTATUS error code that the driver stack returns after it tries to retrieve the page of kernel data. You can determine the exact cause of this error from the I/O status code (the second parameter). Some common status codes include the following:

-   0xC000009A, or STATUS\_INSUFFICIENT\_RESOURCES, indicates a lack of nonpaged pool resources. This status code indicates a driver error in the storage stack. (The storage stack should always be able to retrieve this data, regardless of software resource availability.)

-   0xC000009C, or STATUS\_DEVICE\_DATA\_ERROR, indicates bad blocks (sectors) on the hard disk.

-   0xC000009D, or STATUS\_DEVICE\_NOT\_CONNECTED, indicates defective or loose cabling, termination, or that the controller does not see the hard disk drive.

-   0xC000016A, or STATUS\_DISK\_OPERATION\_FAILED, indicates bad blocks (sectors) on the hard disk.

-   0xC0000185, or STATUS\_IO\_DEVICE\_ERROR, indicates improper termination or defective cabling on SCSI devices or that two devices are trying to use the same IRQ.

These status codes are the most common ones that have specific causes. For more information about other possible status codes that might be returned, see the Ntstatus.h file in the Microsoft Windows Driver Kit (WDK).

A virus infection can also cause this bug check.

Resolution
----------

**Resolving a bad block problem:** If you can restart the computer after the error, Autochk runs automatically and attempts to map the bad sector to prevent it from being used anymore.

If Autochk does not scan the hard disk for errors, you can manually start the disk scanner. Run **Chkdsk /f /r** on the system partition. You must restart the computer before the disk scan begins. If you cannot start the system because the error, use the Recovery Console and run **Chkdsk /r**.

**Warning**   If your system partition is formatted with the FAT file system, the long file names that the Windows operating system uses might be damaged if you use Scandisk or another MS-DOS-based hard disk tool to verify the integrity of your hard disk drive from MS-DOS. Always use the version of Chkdsk that matches your version of the Windows operating system.

 

**Resolving a defective hardware problem:** If the I/O status is 0xC0000185 and the paging file is on an SCSI disk, check the disk cabling and SCSI termination for problems.

**Resolving a failing RAM problem:** Run the hardware diagnostics that the system manufacturer supplies, especially the memory scanner. For more information about these procedures, see the owner's manual for your computer.

Check that all the adapter cards in the computer are properly seated. Use an ink eraser or an electrical contact treatment, available at electronics supply stores, to ensure adapter card contacts are clean.

Check the System Log in Event Viewer for additional error messages that might help identify the device that is causing the error. You can also disable memory caching of the BIOS to try to resolve this error.

Make sure that the latest Windows Service Pack is installed.

If the preceding steps fail to resolve the error, take the system motherboard to a repair facility for diagnostic testing. A crack, a scratched trace, or a defective component on the motherboard can cause this error.

**Resolving a virus infection:** Check your computer for viruses by using any up-to-date, commercial virus scanning software that examines the Master Boot Record of the hard disk. All Windows file systems can be infected by viruses.

## <span id="see_also"></span>See also


[**Bug Check 0x7A (KERNEL\_DATA\_INPAGE\_ERROR)**](bug-check-0x7a--kernel-data-inpage-error.md)

 

 




