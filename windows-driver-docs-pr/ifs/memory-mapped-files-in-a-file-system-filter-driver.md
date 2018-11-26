---
title: Memory Mapped Files in a File System Filter Driver
description: Memory Mapped Files in a File System Filter Driver
ms.assetid: 0915167a-f8ac-4222-bece-76d7fc8a3823
keywords:
- security WDK file systems , memory mapped files
- memory mapped files WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Memory Mapped Files in a File System Filter Driver


## <span id="ddk_memory_mapped_files_in_a_file_system_filter_driver_if"></span><span id="DDK_MEMORY_MAPPED_FILES_IN_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


A file system filter driver must be cognizant of the fact that files may be accessed via virtual memory mappings of the files, rather than via the read and write paths. A file system filter driver monitoring changes in the file will miss changes to such files. In general a file system filter driver that wants to deal with memory-mapped I/O has to filter paging I/O. A number of techniques for dealing with this are discussed in the Windows File System Developers List [(NTFSD)](http://www.osronline.com/cf.cfm?PageURL=showlists.cfm?list=NTFSD) newsgroup hosted by OSR.

 

 




