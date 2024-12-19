---
title: File System Reparse Points
description: Describes file system filter driver reparse points
keywords:
- WDK file systems filter driver , reparse points
- reparse points WDK file systems
ms.date: 12/18/2024
---

# File system reparse points

Reparse points are file system objects used to extend the attributes of a file system. Not all file systems support reparse points; for example, NTFS and ReFS support them, but the FAT file system doesn't. A reparse point consists of:

- User-defined data
- A *reparse point tag* that uniquely identifies the file system filter driver that owns the reparse point. Microsoft assigns all reparse point tags. These tags are defined in *ntifs.h*. Some tags are reserved for Microsoft. [Non-Microsoft tags can be requested](reparse-point-tag-request.md).

A filter can set or delete a reparse point on a file or directory by calling [**FltTagFileEx**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-flttagfileex) and [**FltUntagFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltuntagfile).

When a file system opens a file with a reparse point, it attempts to find the file system filter associated with the data format identified by the reparse tag. If present, the associated filter should process the file as directed by the reparse data.

For more information about reparse points, see the [Windows SDK documentation](/windows/win32/fileio/reparse-points).
