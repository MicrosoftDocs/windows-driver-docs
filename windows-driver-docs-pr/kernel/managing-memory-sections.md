---
title: Managing Memory Sections
description: Managing Memory Sections
keywords: ["memory sections WDK kernel", "section objects WDK kernel", "views WDK memory section", "mapping section views"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Managing Memory Sections





A driver can create a section object by calling [**ZwCreateSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatesection), which returns a handle to the section object. Use the *FileHandle* parameter to specify the backing file, or **NULL** if the section is not file-backed. Additional handles to the section object can be opened by using [**ZwOpenSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensection).

To make the data that belongs to a section object accessible within the current process' address space, a view of the section must be mapped. Drivers can map a view of a section into the current process' address space by using the [**ZwMapViewOfSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection) routine. The *SectionOffset* parameter specifies the byte offset where the view begins within the section, and the *ViewSize* specifies the number of bytes to be mapped.

The *Protect* parameter specifies the allowed operations on the view. Specify PAGE\_READONLY for a read-only view, PAGE\_READWRITE for a read/write view, and PAGE\_WRITECOPY for a copy-on-write view.

No physical memory is allocated for a view until the virtual memory range is accessed. The first access of the memory range causes a page fault; the system then allocates a page to hold that memory location. If the section is file-backed, the system reads the contents of the file that corresponds to that page and copies it into memory. (Note that unused section objects and views do use some paged and nonpaged pool for bookkeeping purposes.)

After a driver is no longer using a view, it unmaps it by making a call to [**ZwUnmapViewOfSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwunmapviewofsection). After the driver is no longer using the section object, it closes the section handle with [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose). Note that after the view is mapped and no other views are going to be mapped, it is safe to immediately call **ZwClose** on the section handle; the view (and section object) continue to exist until the view is unmapped. This is the recommended practice because it reduces the risk of the driver failing to close the handle.

 

