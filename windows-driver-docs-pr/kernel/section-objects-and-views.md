---
title: Section Objects and Views
author: windows-driver-content
description: Section Objects and Views
MS-HAID:
- 'MemMgmt\_866348b9-6415-46a0-8857-2d9d90a678b4.xml'
- 'kernel.section\_objects\_and\_views'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9c60b761-6326-4d1a-b884-cc2acee4bedd
keywords: ["memory management WDK kernel , section objects", "memory management WDK kernel , shared memory", "shared memory WDK kernel", "section objects WDK kernel", "memory sections WDK kernel", "sharing memory address space", "views WDK memory section"]
---

# Section Objects and Views


## <a href="" id="ddk-section-objects-and-views-kg"></a>


A *section object* represents a section of memory that can be shared. A process can use a section object to share parts of its memory address space (memory sections) with other processes. Section objects also provide the mechanism by which a process can map a file into its memory address space.

Each memory section has one or more corresponding *views*. A view of a section is a part of the section that is actually visible to a process. The act of creating a view for a section is known as *mapping* a view of the section. Each process that is manipulating the contents of a section has its own view; a process can also have multiple views (to the same or different sections).

This section contains the following topics:

[File-Backed and Page-File-Backed Sections](file-backed-and-page-file-backed-sections.md)

[Managing Memory Sections](managing-memory-sections.md)

[Security Issues for Section Objects and Views](security-issues-for-section-objects-and-views.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Section%20Objects%20and%20Views%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


