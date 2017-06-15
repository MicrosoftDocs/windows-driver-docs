---
title: File-Backed and Page-File-Backed Sections
author: windows-driver-content
description: File-Backed and Page-File-Backed Sections
MS-HAID:
- 'MemMgmt\_87e8805d-06df-443b-b678-ae36fe30d511.xml'
- 'kernel.file\_backed\_and\_page\_file\_backed\_sections'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5967678a-cbc3-4db0-86d8-14ffc79f610e
keywords: ["file-backed sections WDK kernel", "page-file-backed sections WDK kernel", "backed memory sections WDK kernel", "paged file backups WDK kernel", "temporarily shared data WDK kernel", "permanently shared data WDK kernel", "memory sections WDK kernel", "section objects WDK kernel"]
---

# File-Backed and Page-File-Backed Sections


## <a href="" id="ddk-file-backed-and-page-file-backed-sections-kg"></a>


All memory sections are supported ("backed") by disk files that can contain, either temporarily or permanently, the data to be shared. When you create a section, you can identify a specific data file to which the section will be backed. Such sections are called *file-backed* sections. If you do not identify a backing file, the section is backed by the system's paging file and the section is called a *page-file-backed* section. The data in file-backed sections can be permanently written to disk. Data in page-file-backed sections is never permanently written to disk.

A *file-backed* section reflects the contents of an actual file on disk; in other words, it is a memory-mapped file. Any access to memory locations within a given file-backed section corresponds to accesses to locations in the associated file. If a process maps the view as read-only, any data that is read from the view is transparently read from the file. Similarly, if the process maps the view as read/write, any data that is read from the view or written to the view is transparently read from or written to the file. In either case, the view's virtual memory does not use any space in the page files. A file-backed section can also be mapped as copy-on-write. In that case, the view's data is read from the file, but any data written to the view is not written to the file; instead it is discarded after the final view is unmapped and the last handle to the section is closed.

A page-file-backed section is backed by the page files instead of by any explicit file on the disk. Any changes that are made to a page-file-backed section are automatically discarded after the section object is destroyed. Page-file-backed sections can be used as shared memory segments between two processes.

Any section, file-backed or not, can be shared between two processes. The same physical memory address range is mapped to a virtual memory address range within each process (though not necessarily to the same virtual address).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20File-Backed%20and%20Page-File-Backed%20Sections%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


