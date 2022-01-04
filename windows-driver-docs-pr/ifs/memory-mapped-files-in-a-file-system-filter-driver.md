---
title: Memory Mapped Files in a File System Filter Driver
description: Memory Mapped Files in a File System Filter Driver
keywords:
- security WDK file systems , memory mapped files
- memory mapped files WDK file systems
ms.date: 04/20/2017
---

# Memory Mapped Files in a File System Filter Driver

A file system filter driver must be cognizant of the fact that files may be accessed via virtual memory mappings of the files, rather than via the read and write paths. A file system filter driver monitoring changes in the file will miss changes to such files. In general a file system filter driver that wants to deal with memory-mapped I/O has to filter paging I/O. A number of techniques for dealing with this are discussed in the [Windows File System and Minifilters Devs Interest List](https://community.osr.com/) newsgroup hosted by OSR.
