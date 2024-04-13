---
title: IRPs Are Different From Fast I/O
description: IRPs Are Different From Fast I/O
keywords:
- IRPs WDK file system
- fast I/O vs. IRPs WDK file system
ms.date: 02/23/2023
---

# IRPs Are Different From Fast I/O

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

IRPs are the default mechanism for requesting I/O operations. IRPs can be used for synchronous or asynchronous I/O, and for cached or noncached I/O. IRPs are also used for paging I/O. The Memory Manager processes page faults by sending appropriate IRPs to the file system.

Fast I/O is designed for rapid synchronous I/O on cached files. In fast I/O operations, data is transferred directly between user buffers and the system cache, bypassing the file system and the storage driver stack. (Storage drivers don't use fast I/O.) If all of the data to be read from a file is resident in the system cache when a fast I/O read or write request is received, the request is satisfied immediately. Otherwise, a page fault can occur, causing one or more IRPs to be generated. When a page fault happens, the fast I/O routine either returns FALSE, or puts the caller into a wait state until the page fault is processed. If the fast I/O routine returns FALSE, the requested operation failed and the caller must create an IRP.

File systems and legacy file system filters are required to support IRPs, but they aren't required to support fast I/O. However, file systems and file system filters must implement fast I/O routines. Even if file systems and file system filters don't support fast I/O, they must define a fast I/O routine that returns FALSE (that is, the fast I/O routine doesn't implement any functionality). When the I/O Manager receives a request for synchronous file I/O (other than paging I/O), it invokes the fast I/O routine first. If the fast I/O routine returns TRUE, it serviced the operation. If the fast I/O routine returns FALSE, the I/O Manager creates and sends an IRP instead.

File system filter drivers aren't required to support I/O on control device objects. However, filter device objects that are attached to file systems or volumes are required to pass all unrecognized or unwanted IRPs to the next-lower driver on the driver stack. In addition, filter device objects that are attached to volumes must implement FastIoDetachDevice.
