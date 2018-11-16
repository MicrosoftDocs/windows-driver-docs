---
title: IRPs Are Different From Fast I/O
description: IRPs Are Different From Fast I/O
ms.assetid: 22b08da2-043e-4724-b8f1-90b337fa222c
keywords:
- IRPs WDK file system
- fast I/O vs. IRPs WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IRPs Are Different From Fast I/O


## <span id="ddk_irps_are_different_from_fast_io_if"></span><span id="DDK_IRPS_ARE_DIFFERENT_FROM_FAST_IO_IF"></span>


IRPs are the default mechanism for requesting I/O operations. IRPs can be used for synchronous or asynchronous I/O, and for cached or noncached I/O. IRPs are also used for paging I/O. The Memory Manager processes page faults by sending appropriate IRPs to the file system.

Fast I/O is specifically designed for rapid synchronous I/O on cached files. In fast I/O operations, data is transferred directly between user buffers and the system cache, bypassing the file system and the storage driver stack. (Storage drivers do not use fast I/O.) If all of the data to be read from a file is resident in the system cache when a fast I/O read or write request is received, the request is satisfied immediately. Otherwise, a page fault can occur, causing one or more IRPs to be generated. When this happens, the fast I/O routine either returns **FALSE**, or puts the caller into a wait state until the page fault is processed. If the fast I/O routine returns **FALSE**, the requested operation failed and the caller must create an IRP.

File systems and file system filters are required to support IRPs, but they are not required to support fast I/O. However, file systems and file system filters must implement fast I/O routines. Even if file systems and file system filters do not support fast I/O, they must define a fast I/O routine that returns **FALSE** (that is, the fast I/O routine does not implement any functionality). When the I/O Manager receives a request for synchronous file I/O (other than paging I/O), it invokes the fast I/O routine first. If the fast I/O routine returns **TRUE**, the operation was serviced by the fast I/O routine. If the fast I/O routine returns **FALSE**, the I/O Manager creates and sends an IRP instead.

File system filter drivers are not required to support I/O on control device objects. However, filter device objects that are attached to file systems or volumes are required to pass all unrecognized or unwanted IRPs to the next-lower driver on the driver stack. In addition, filter device objects that are attached to volumes must implement FastIoDetachDevice.

 

 




