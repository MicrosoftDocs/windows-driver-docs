---
title: Kernel-mode file copy and detecting copy file scenarios
description: How to copy files in kernel mode and detect copy file scenarios
keywords:
- NtCopyFileChunk
- Copying files in kernel mode
- Kernel-mode file copy
- Kernel-mode file copy detection scenarios
ms.date: 05/24/2022
---

# Kernel-mode file copy and detecting copy file scenarios

The ability to do trusted file copy in kernel mode was introduced in Windows 11, version 22H2, including the ability for filters to easily detect copy scenarios. This functionality is particularly useful for antivirus filters (AVs), allowing them to determine whether they can defer or entirely skip scanning both the source and destination files during copy.

To ensure that kernel-mode read and write operations are safely marked as part of a copy operation:

* The **FILE_CONTAINS_EXTENDED_CREATE_INFORMATION** flag and [**EXTENDED_CREATE_INFORMATION**](ns-ntifs-extended_create_information.md) structure were added to signal copy intent at create time via [**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile). The **EXTENDED_CREATE_INFORMATION** structure acts as a wrapper around **NtCreateFile**'s existing **EaBuffer** parameter.

  When the **FILE_CONTAINS_EXTENDED_CREATE_INFORMATION** flag is specified, the I/O manager interprets the **EaBuffer** and **EaLength** parameters as an **EXTENDED_CREATE_INFORMATION** structure, and will parse that structure's fields as if they were provided directly to **NtCreateFile**. Underlying filters will experience no change in behavior of extended attributes.

* [**IoCheckFileObjectOpenedAsCopySource**](nf-ntifs-iocheckfileobjectopenedascopysource.md) and [**IoCheckFileObjectOpenedAsCopyDestination**](nf-ntifs-iocheckfileobjectopenedascopydestination.md) were added for filters to check whether a file was opened for copy intent.

* [**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md) was added to do the kernel-mode copy.

All read and write operations from **NtCopyFileChunk** will have:

* The IRP's requestor mode set to **KernelMode**
* An IRP extension of type **IopCopyInformationType**.

Filters do not have access to the IRP extensions directly but can check the presence of this extension and get copy information from the callback data by calling [**FltGetCopyInformationFromCallbackData**](nf-fltkernel-fltgetcopyinformationfromcallbackdata.md).
