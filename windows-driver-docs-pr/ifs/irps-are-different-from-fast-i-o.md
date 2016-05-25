---
title: IRPs Are Different From Fast I/O
author: windows-driver-content
description: IRPs Are Different From Fast I/O
ms.assetid: 22b08da2-043e-4724-b8f1-90b337fa222c
keywords: ["IRPs WDK file system", "fast I/O vs. IRPs WDK file system"]
---

# IRPs Are Different From Fast I/O


## <span id="ddk_irps_are_different_from_fast_io_if"></span><span id="DDK_IRPS_ARE_DIFFERENT_FROM_FAST_IO_IF"></span>


IRPs are the default mechanism for requesting I/O operations. IRPs can be used for synchronous or asynchronous I/O, and for cached or noncached I/O. IRPs are also used for paging I/O. The Memory Manager processes page faults by sending appropriate IRPs to the file system.

Fast I/O is specifically designed for rapid synchronous I/O on cached files. In fast I/O operations, data is transferred directly between user buffers and the system cache, bypassing the file system and the storage driver stack. (Storage drivers do not use fast I/O.) If all of the data to be read from a file is resident in the system cache when a fast I/O read or write request is received, the request is satisfied immediately. Otherwise, a page fault can occur, causing one or more IRPs to be generated. When this happens, the fast I/O routine either returns **FALSE**, or puts the caller into a wait state until the page fault is processed. If the fast I/O routine returns **FALSE**, the requested operation failed and the caller must create an IRP.

File systems and file system filters are required to support IRPs, but they are not required to support fast I/O. However, file systems and file system filters must implement fast I/O routines. Even if file systems and file system filters do not support fast I/O, they must define a fast I/O routine that returns **FALSE** (that is, the fast I/O routine does not implement any functionality). When the I/O Manager receives a request for synchronous file I/O (other than paging I/O), it invokes the fast I/O routine first. If the fast I/O routine returns **TRUE**, the operation was serviced by the fast I/O routine. If the fast I/O routine returns **FALSE**, the I/O Manager creates and sends an IRP instead.

File system filter drivers are not required to support I/O on control device objects. However, filter device objects that are attached to file systems or volumes are required to pass all unrecognized or unwanted IRPs to the next-lower driver on the driver stack. In addition, filter device objects that are attached to volumes must implement FastIoDetachDevice.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRPs%20Are%20Different%20From%20Fast%20I/O%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


