---
title: Attaching a Filter to a File System or Volume
description: Attaching a Filter to a File System or Volume
ms.assetid: 7c5059b3-cd9f-4a83-8f78-5a2fcc96b246
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attaching a Filter to a File System or Volume


## <span id="ddk_attaching_a_filter_to_a_file_system_or_volume_if"></span><span id="DDK_ATTACHING_A_FILTER_TO_A_FILE_SYSTEM_OR_VOLUME_IF"></span>


A file system filter driver attaches itself to one or more mounted volumes and filters all I/O operations on them. But how does it determine which volumes to attach itself to? The sample filter drivers in the Windows Driver Kit (WDK) illustrate the two most common ways in which this is done:

-   The end user can specify the volumes to filter by, for example, typing in the drive letters for the volumes. The end user's commands are relayed to the filter driver as a private [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548649) request.

-   The file system filter driver can attach to one or more file system drivers, listen for [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548670), IRP\_MN\_MOUNT\_VOLUME requests, and attach to volumes as they are mounted.

**Note**   You should generally assume that the mapping of volumes to drive letters is one-to-many, not one-to-one. This is because of advanced storage features, such as dynamic volumes and volume mount points.

 

**Note**   You should not assume that IRP\_MN\_MOUNT\_VOLUME requests are always handled synchronously by the file system. For example, a floppy drive may be mounted asynchronously if there is no floppy disk in the drive. Thus your filter driver should be prepared to propagate the **PendingReturned** flag in its mount completion routine. For more information, see "[Checking the PendingReturned Flag](checking-the-pendingreturned-flag.md)."

 

File system filter drivers can attach to, and filter I/O for, any file system volume. They cannot attach directly to storage devices, such as disk drives or partitions. Also, they cannot attach to individual directories or files.

For more information, see the following topics:

[Creating the Filter Device Object](creating-the-filter-device-object.md)

[Attaching the Filter Device Object to the Target Device Object](attaching-the-filter-device-object-to-the-target-device-object.md)

[Propagating the DO\_BUFFERED\_IO and DO\_DIRECT\_IO Flags](propagating-the-do-buffered-io-and-do-direct-io-flags.md)

[Propagating the FILE\_DEVICE\_SECURE\_OPEN Flag](propagating-the-file-device-secure-open-flag.md)

[Clearing the DO\_DEVICE\_INITIALIZING Flag](clearing-the-do-device-initializing-flag.md)

 

 




