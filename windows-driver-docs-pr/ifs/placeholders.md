---
title: About Placeholders
description: Defines file system placeholders
keywords:
- filter drivers file system , placeholders
- minifilter, file system placeholders
ms.date: 02/22/2023
prerelease: false
---

# About placeholders

A file system placeholder is a file that is a representation for the actual content of a file or a directory that resides elsewhere. This optimization allows for the real contents of a file or directory to reside elsewhere and be fetched on demand. The real contents includes metadata, file data, and directory entries.

Placeholders can be files or directories. They may contain a portion of the real file or directory metadata or a portion of the real file data or directory entries. Placeholder files are marked as sparse files with the FILE_ATTRIBUTE_SPARSE_FILE bit set.  

Typically, a placeholder is a reparse point that a file system minifilter owns and manages. The owning minifilter is the enabler of virtualization and makes it possible for a placeholder to look and behave like a regular file or directory on the file system. These virtualization drivers intercept IO requests on their placeholders and facilitate a file system-like behavior.  [ProjFs](/windows/win32/projfs/projected-file-system) and [Cloud Files](/windows/win32/cfapi/cloud-files-api-portal) are two examples of virtualization platforms in Windows that use placeholders.  

The minifilters that own the placeholders are able to appropriately handle such IO requests to satisfy the IO. For example, if an application attempts to read a dehydrated placeholder file, the minifilter furnishes the file data to satisfy the IO request.

Owning minifilters are only able to provide the virtualization for IO requests that originate above them, either from user-mode or from components that are above them in the IO stack.

Minifilters that don't own the placeholder have the ability to issue IO operations targeted to filters below them using APIs such as [**FltReadFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreadfile), [**FltWriteFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltwritefile), and so on. If a non-owning minifilter were to issue a targeted IO request to a placeholder file from below the owning minifilter, the owning minifilter wouldn't be able to appropriately satisfy the IO request.

For example, if a filter issues a targeted **FltReadFile** to a dehydrated placeholder file that the owning minifilter doesn't see, the targeting filter might get a block of zeroes (0s) rather than the actual data because the placeholder might be a sparse file. If the system caches a read that fetched a block of 0s, this read pollutes the cache which could corrupt the file data if the system flushes the polluted cache to the disk. Hence, it's imperative that minifilters [handle placeholders appropriately](placeholders_guidance.md).
