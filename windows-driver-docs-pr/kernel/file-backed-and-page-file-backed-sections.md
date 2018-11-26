---
title: File-Backed and Page-File-Backed Sections
description: File-Backed and Page-File-Backed Sections
ms.assetid: 5967678a-cbc3-4db0-86d8-14ffc79f610e
keywords: ["file-backed sections WDK kernel", "page-file-backed sections WDK kernel", "backed memory sections WDK kernel", "paged file backups WDK kernel", "temporarily shared data WDK kernel", "permanently shared data WDK kernel", "memory sections WDK kernel", "section objects WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# File-Backed and Page-File-Backed Sections





All memory sections are supported ("backed") by disk files that can contain, either temporarily or permanently, the data to be shared. When you create a section, you can identify a specific data file to which the section will be backed. Such sections are called *file-backed* sections. If you do not identify a backing file, the section is backed by the system's paging file and the section is called a *page-file-backed* section. The data in file-backed sections can be permanently written to disk. Data in page-file-backed sections is never permanently written to disk.

A *file-backed* section reflects the contents of an actual file on disk; in other words, it is a memory-mapped file. Any access to memory locations within a given file-backed section corresponds to accesses to locations in the associated file. If a process maps the view as read-only, any data that is read from the view is transparently read from the file. Similarly, if the process maps the view as read/write, any data that is read from the view or written to the view is transparently read from or written to the file. In either case, the view's virtual memory does not use any space in the page files. A file-backed section can also be mapped as copy-on-write. In that case, the view's data is read from the file, but any data written to the view is not written to the file; instead it is discarded after the final view is unmapped and the last handle to the section is closed.

A page-file-backed section is backed by the page files instead of by any explicit file on the disk. Any changes that are made to a page-file-backed section are automatically discarded after the section object is destroyed. Page-file-backed sections can be used as shared memory segments between two processes.

Any section, file-backed or not, can be shared between two processes. The same physical memory address range is mapped to a virtual memory address range within each process (though not necessarily to the same virtual address).

 

 




