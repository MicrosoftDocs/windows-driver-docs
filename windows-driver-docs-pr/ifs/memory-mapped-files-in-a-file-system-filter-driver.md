---
title: Memory Mapped Files in a File System Filter Driver
description: Memory Mapped Files in a File System Filter Driver
keywords:
- security WDK file systems , memory mapped files
- memory mapped files WDK file systems
ms.date: 06/14/2023
---

# Memory Mapped Files in a File System Filter Driver

A file system filter driver might need to access files via virtual memory mappings of those files rather than via the read and write paths. A file system filter driver that monitors file changes will miss changes to such files if it doesn't handle this condition. In general, a filter that needs to deal with memory-mapped I/O has to filter paging I/O.

Some resources to reference for this article are:

* See various articles in [Memory Management for Windows Drivers](../kernel/managing-memory-for-drivers.md).
* The [SwapBuffer FS Minifilter Driver sample](https://github.com/microsoft/Windows-driver-samples/tree/main/filesys/miniFilter/swapBuffers) shows how to handle memory-mapped files.
* Various techniques and considerations are discussed in the [Windows File System and Minifilters Devs Interest List](https://community.osr.com/) newsgroup hosted by OSR. Useful search terms include:
  * "memory mapped files"
  * "minifilter memory mapped files"
  * "paging io"
  * "paging io memory mapped files"
  * "paging io minifilter"
