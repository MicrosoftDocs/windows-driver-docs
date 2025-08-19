---
title: File System Sample Code
description: File system sample code
keywords:
- drivers WDK file system
- file system drivers WDK
ms.date: 04/30/2025
ms.topic: concept-article
---

# File system sample code

In almost all situations, developing a full file system for Windows isn't necessary. If you do decide to develop a new file system driver beyond the file systems available in Windows, see the following sample code:

* [FastFAT file system driver](/samples/microsoft/windows-driver-samples/fastfat-file-system-driver/). This sample is a complete file system. It addresses issues such as storing data on disk, interacting with the cache manager, and handling various I/O operations such as file creation, deletion, and reading/writing data. It also demonstrates how to set information on a file and perform control operations on the file system.

* [CDFS driver](/samples/microsoft/windows-driver-samples/cdfs-file-system-driver/). The CD-ROM file system driver is for removable media.
