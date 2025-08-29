---
title: About File System Drivers
description: About file system drivers
keywords:
- file systems , WDK , Windows
- file system driver , WDK , Windows
- file system driver development , WDK , Windows
- file system development , WDK , Windows
ms.date: 04/30/2025
ms.topic: concept-article
---

# About file system drivers

Windows file systems are implemented as *file system drivers* working above the storage system. Every system-supplied Windows file system is designed to provide reliable data storage with varying features to meet the user's requirements. The four main file systems available for Windows are:

* NTFS
* ExFAT
* UDF
* FAT32

A comparison of features for each of these file systems is shown in [File System Functionality Comparison](/windows/desktop/FileIO/filesystem-functionality-comparison).

The [Resilient File System](/windows-server/storage/refs/refs-overview) (ReFS) is available on Windows Server 2012 and later versions. ReFS offers scalable large volume support and the ability to detect and correct data corruption on disk.

## Developing a file system

Developing a new file system is almost always unnecessary, and requirements/specifications for new file system drivers aren't predictable. For these reasons, the WDK documentation doesn't cover file system development.

If you do need to develop a new file system driver beyond the file systems available in Windows, see the [sample code](file-system-sample-code.md).
