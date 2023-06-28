---
title: Bug check 0x7A KERNEL_DATA_INPAGE_ERROR
description: Learn about bug check 0x7A KERNEL_DATA_INPAGE_ERROR, which indicates that the requested page of kernel data from the paging file couldn't be read into memory.
keywords: ["Bug check 0x7A KERNEL_DATA_INPAGE_ERROR", "KERNEL_DATA_INPAGE_ERROR"]
ms.date: 02/24/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- KERNEL_DATA_INPAGE_ERROR
api_type:
- NA
---

# Bug check 0x7A: KERNEL\_DATA\_INPAGE\_ERROR

The KERNEL\_DATA\_INPAGE\_ERROR bug check has a value of 0x0000007A. This bug check indicates that the requested page of kernel data from the paging file couldn't be read into memory.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## Parameters

The four parameters that are listed in the message can have three possible meanings.

If the first parameter is 1, 2, or 3 and the third parameter is 0, the parameters have the following definitions.

| Parameter | Description |
|-----------|-------------|
| 1         | The lock type that was held (1, 2, or 3) |
| 2         | The error status (usually an I/O status code) |
| 3         | If the lock type is 1: the current process <br><br> If the lock type is 2 or 3: 0 |
| 4         | The virtual address that couldn't be paged into memory |

If the first parameter is 3 or 4 (and the third parameter is not 0), the parameters have the following definitions.

| Parameter | Description |
|-----------|-------------|
| 1         | The lock type that was held (3 or 4)            |
| 2         | The error status (typically an I/O status code) |
| 3         | The address of the InPageSupport structure      |
| 4         | The faulting address                            |

Otherwise, the parameters have the following definitions.

| Parameter | Description |
|-----------|-------------|
| 1         | The address of the page table entry (PTE)     |
| 2         | The error status (usually an I/O status code) |
| 3         | The PTE contents                              |
| 4         | The faulting address                          |

## Cause

Frequently, you can determine the cause of the KERNEL\_DATA\_INPAGE\_ERROR bug check from the error status (parameter 2).  These are [NTSTATUS Values](/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55). 

Some common status codes include:

- 0xC000009A, or STATUS\_INSUFFICIENT\_RESOURCES, indicates a lack of non-paged pool resources.

- 0xC000009C, or STATUS\_DEVICE\_DATA\_ERROR, typically indicates bad blocks (sectors) on the hard disk.

- 0xC000009D, or STATUS\_DEVICE\_NOT\_CONNECTED, indicates defective or loose cabling, termination, or that the controller doesn't see the hard disk.

- 0xC000016A, or STATUS\_DISK\_OPERATION\_FAILED, indicates bad blocks (sectors) on the hard disk.

- 0xC0000185, or STATUS\_IO\_DEVICE\_ERROR, indicates improper termination or defective cabling on SCSI devices or that two devices are trying to use the same IRQ.

- 0xC000000E, or STATUS\_NO\_SUCH\_DEVICE, indicates a hardware failure or an incorrect drive configuration. Check your cables and check the drive with the diagnostic utility available from your drive manufacturer. If you're using older PATA (IDE) drives, this status code can indicate an incorrect master/subordinate drive configuration.

These status codes are the most common ones that have specific causes. For more information about other possible status codes that can be returned for a specific version of Windows, see the `Ntstatus.h` file in the Microsoft Windows Driver Kit (WDK). OSR a third party, offers a PDF document that maps NTSTATUS to Win32 Error codes [NTSTATUS to Win32 Error Code Mappings](https://www.osr.com/blog/2020/04/23/ntstatus-to-win32-error-code-mappings/)

Another common cause of this error message is defective storage hardware or failing RAM memory.

A virus infection can also cause this bug check.

## Resolution

**Resolve a bad block problem:** An I/O status code of 0xC000009C or 0xC000016A typically indicates that the data couldn't be read from the disk because of a bad block (sector). If you can restart the computer after the error, Autochk runs automatically and attempts to map the bad sector to prevent it from being used anymore.

If Autochk doesn't scan the hard disk for errors, you can manually start the disk scanner. Run `Chkdsk /f /r` on the system partition. You must restart the computer before the disk scan begins. If you can't start the computer because of the error, use the Recovery Console and run `Chkdsk /r`.

**Resolve a failing RAM problem:** Run the hardware diagnostics that the system manufacturer supplies, especially the memory scanner. For more information about these procedures, see the owner's manual for your computer.

**Resolve a defective hardware problem:** If the I/O status is C0000185 and the paging file is on an older SCSI disk, check the disk cabling and SCSI termination for problems.

**Resolve a virus infection:** Check your computer for viruses by using any up-to-date, commercial virus-scanning software that examines the Master Boot Record of the hard disk. Windows file systems can be infected by viruses.

Check the System Event Viewer for error messages that might help identify the device that's causing the error. In particular, errors that occur right before the bug check should be examined.

Make sure that the latest Windows updates are installed.

Locate and run any available diagnostic testing software for the PC. A crack, a scratched trace, or a defective component on the motherboard can cause this bug check.

For PCs, with card slots, check that all the adapter cards in the computer are properly seated. Use an ink eraser or an electrical contact treatment, available at electronics supply stores, to ensure adapter card contacts are clean.

## See also

[Bug check 0x77: KERNEL\_STACK\_INPAGE\_ERROR](bug-check-0x77--kernel-stack-inpage-error.md)
