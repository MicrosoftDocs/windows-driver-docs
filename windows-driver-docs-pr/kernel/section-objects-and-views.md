---
title: Section Objects and Views
description: Section Objects and Views
ms.assetid: 9c60b761-6326-4d1a-b884-cc2acee4bedd
keywords: ["memory management WDK kernel , section objects", "memory management WDK kernel , shared memory", "shared memory WDK kernel", "section objects WDK kernel", "memory sections WDK kernel", "sharing memory address space", "views WDK memory section"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Section Objects and Views





A *section object* represents a section of memory that can be shared. A process can use a section object to share parts of its memory address space (memory sections) with other processes. Section objects also provide the mechanism by which a process can map a file into its memory address space.

Each memory section has one or more corresponding *views*. A view of a section is a part of the section that is actually visible to a process. The act of creating a view for a section is known as *mapping* a view of the section. Each process that is manipulating the contents of a section has its own view; a process can also have multiple views (to the same or different sections).

This section contains the following topics:

[File-Backed and Page-File-Backed Sections](file-backed-and-page-file-backed-sections.md)

[Managing Memory Sections](managing-memory-sections.md)

[Security Issues for Section Objects and Views](security-issues-for-section-objects-and-views.md)

 

 




