---
title: File System and Filter Driver Samples
description: The driver samples in this directory provide a starting point for writing custom file system drivers and file system filter drivers.
ms.date: 05/01/2025
---

# File system and filter driver samples

The driver samples in this directory provide a starting point for writing a custom file system driver or file system filter driver (*minifilter*).

## File system driver samples

| Sample | Description |
|--|--|
| [CDFS File System Driver](/samples/microsoft/windows-driver-samples/cdfs-file-system-driver) | The CD-ROM file system driver (cdfs) sample is a file system driver for removable media. |
| [fastfat File System Driver](/samples/microsoft/windows-driver-samples/fastfat-file-system-driver) | A file system driver based on the Windows inbox FastFAT file system used as a model for new file systems. |

## File system filter driver samples

| Sample | Description |
|--|--|
| [AvScan File System Minifilter Driver](/samples/microsoft/windows-driver-samples/avscan-file-system-minifilter-driver) | This filter is a transaction-aware file scanner that examines data in files. Anti-virus might operate in this fashion. |
| [CancelSafe File System Minifilter Driver](/samples/microsoft/windows-driver-samples/cancelsafe-file-system-minifilter-driver) | A minifilter demonstrating the use of cancel-safe queues. |
| [CDO File System Minifilter Driver](/samples/microsoft/windows-driver-samples/cdo-file-system-minifilter-driver) | An example of using a control device object (CDO) with a minifilter. |
| [Change File System Minifilter Driver](/samples/microsoft/windows-driver-samples/change-file-system-minifilter-driver) | A transaction-aware filter that monitors file changes in real time. |
| [Ctx File System Minifilter Driver](/samples/microsoft/windows-driver-samples/ctx-file-system-minifilter-drive) | Demonstrates how to attach contexts to instances, files, streams, and stream handles in your minifilter. |
| [Delete File System Minifilter Driver](/samples/microsoft/windows-driver-samples/delete-file-system-minifilter-driver) | Demonstrates how to detect deletions of files or streams. |
| [Metadata Manager File System Minifilter Driver](/samples/microsoft/windows-driver-samples/metadata-manager-file-system-minifilter-driver) | Serves as an example of how to use files for storing metadata that corresponds to your minifilters. This sample depicts scenarios in which modifications to the file might have to be blocked or the minifilter might be required to close the file temporarily. |
| [Minispy File System Minifilter Driver](/samples/microsoft/windows-driver-samples/minispy-file-system-minifilter-driver) | A tool to monitor and log any I/O and transaction activity that occurs in the system. |
| [NameChanger File System Minifilter Driver](/samples/microsoft/windows-driver-samples/namechanger-file-system-minifilter-driver) | Grafts a directory from one part of a volume's namespace to another part using a mapping. The minifilter maintains this illusion by acting as a name provider, injecting entries into directory enumerations and forwarding directory change notifications. |
| [NullFilter File System Minifilter Driver](/samples/microsoft/windows-driver-samples/nullfilter-file-system-minifilter-driver) | A minifilter that simply demonstrates registration with the filter manager. |
| [PassThrough File System Minifilter Driver](/samples/microsoft/windows-driver-samples/passthrough-file-system-minifilter-driver) | Demonstrates how to specify callback functions for different types of I/O requests. |
| [Scanner File System Minifilter Driver](/samples/microsoft/windows-driver-samples/scanner-file-system-minifilter-driver) | A file data scanner example. Typically, anti-virus filters are of this type. |
| [SimRep File System Minifilter Driver](/samples/microsoft/windows-driver-samples/simrep-file-system-minifilter-driver) | Demonstrates how a file system filter can simulate file-system like reparse-point behavior to redirect a file open to an alternate path. |
| [SwapBuffer File System Minifilter Driver](/samples/microsoft/windows-driver-samples/swapbuffer-file-system-minifilter-driver) | Demonstrates how to switch buffers between reads and writes of data. This technique is useful for encryption filters. |
