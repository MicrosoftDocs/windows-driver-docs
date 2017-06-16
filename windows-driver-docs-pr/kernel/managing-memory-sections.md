---
title: Managing Memory Sections
author: windows-driver-content
description: Managing Memory Sections
ms.assetid: 620ba31d-596f-493a-b97f-65a27d50cc9a
keywords: ["memory sections WDK kernel", "section objects WDK kernel", "views WDK memory section", "mapping section views"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Managing Memory Sections


## <a href="" id="ddk-managing-memory-sections-kg"></a>


A driver can create a section object by calling [**ZwCreateSection**](https://msdn.microsoft.com/library/windows/hardware/ff566428), which returns a handle to the section object. Use the *FileHandle* parameter to specify the backing file, or **NULL** if the section is not file-backed. Additional handles to the section object can be opened by using [**ZwOpenSection**](https://msdn.microsoft.com/library/windows/hardware/ff567029).

To make the data that belongs to a section object accessible within the current process' address space, a view of the section must be mapped. Drivers can map a view of a section into the current process' address space by using the [**ZwMapViewOfSection**](https://msdn.microsoft.com/library/windows/hardware/ff566481) routine. The *SectionOffset* parameter specifies the byte offset where the view begins within the section, and the *ViewSize* specifies the number of bytes to be mapped.

The *Protect* parameter specifies the allowed operations on the view. Specify PAGE\_READONLY for a read-only view, PAGE\_READWRITE for a read/write view, and PAGE\_WRITECOPY for a copy-on-write view.

No physical memory is allocated for a view until the virtual memory range is accessed. The first access of the memory range causes a page fault; the system then allocates a page to hold that memory location. If the section is file-backed, the system reads the contents of the file that corresponds to that page and copies it into memory. (Note that unused section objects and views do use some paged and nonpaged pool for bookkeeping purposes.)

After a driver is no longer using a view, it unmaps it by making a call to [**ZwUnmapViewOfSection**](https://msdn.microsoft.com/library/windows/hardware/ff567119). After the driver is no longer using the section object, it closes the section handle with [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417). Note that after the view is mapped and no other views are going to be mapped, it is safe to immediately call **ZwClose** on the section handle; the view (and section object) continue to exist until the view is unmapped. This is the recommended practice because it reduces the risk of the driver failing to close the handle.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Managing%20Memory%20Sections%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


