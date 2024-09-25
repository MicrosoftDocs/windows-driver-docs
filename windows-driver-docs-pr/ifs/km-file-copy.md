---
title: Kernel-mode File Copy and Detecting Copy File Scenarios
description: How to copy files in kernel mode and detect copy file scenarios
keywords:
- NtCopyFileChunk
- Copying files in kernel mode
- Kernel-mode file copy
- Kernel-mode file copy detection scenarios
ms.date: 09/25/2024
---

# Kernel-mode file copy and detecting copy file scenarios

This article describes the trusted kernel-mode file copy functionality introduced in Windows 11, version 22H2. This functionality enables filters to easily detect copy scenarios. It's useful for antivirus filters (AVs), allowing them to determine whether they can defer or entirely skip scanning both the source and destination files during copy.

To ensure that kernel-mode read and write operations are safely marked as part of a copy operation, the following updates were made:

* The **FILE_CONTAINS_EXTENDED_CREATE_INFORMATION** flag and [**EXTENDED_CREATE_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-extended_create_information) structure were added. This flag and structure are used to signal copy intent at create time via [**NtCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile). The **EXTENDED_CREATE_INFORMATION** structure acts as a wrapper around **NtCreateFile**'s existing **EaBuffer** parameter.

  When the **FILE_CONTAINS_EXTENDED_CREATE_INFORMATION** flag is specified, the I/O manager interprets the **EaBuffer** and **EaLength** parameters as an **EXTENDED_CREATE_INFORMATION** structure. The I/O manager then parses that structure's fields as if they were provided directly to **NtCreateFile**. Underlying filters experience no change in behavior of extended attributes.

* [**IoCheckFileObjectOpenedAsCopySource**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckfileobjectopenedascopysource) and [**IoCheckFileObjectOpenedAsCopyDestination**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iocheckfileobjectopenedascopydestination) were added for filters to check whether a file was opened for copy intent.

* [**NtCopyFileChunk**](nf-ntifs-ntcopyfilechunk.md) was added to do the kernel-mode copy.

All read and write operations from **NtCopyFileChunk** have:

* The IRP's requestor mode set to **KernelMode**
* An IRP extension of type **IopCopyInformationType**.

Filters don't have access to the IRP extensions directly but can check the presence of this extension and get copy information from the callback data by calling [**FltGetCopyInformationFromCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetcopyinformationfromcallbackdata).
