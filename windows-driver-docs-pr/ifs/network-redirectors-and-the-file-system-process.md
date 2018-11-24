---
title: Network Redirectors and the File System Process
description: Network Redirectors and the File System Process
ms.assetid: 01bdd0d4-d03e-4b3c-ab34-1d5909cde284
keywords:
- kernel network redirectors WDK , file system process
- asynchronous requests WDK network redirectors
- IRP_MJ_WRITE
- File System Dispatch WDK network redirectors
- FSD WDK network redirectors
- buffers WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Network Redirectors and the File System Process


Most of the file operations performed by a file system driver are usually completed in the user's thread context. These operations include all of the synchronous file I/O calls to the file system. In these cases, all of the work is done inline. The operation might block in the kernel, but the work is performed on the same thread. File systems on Windows often call this work using the user's thread context as the File System Dispatch (FSD). Most of the time, a file system will try to complete its work in the FSD.

There are some cases where an application does not want to block (asynchronous reads or asynchronous writes, for example). In these cases, the file I/O operation needs to be dispatched to a system worker thread for completion. File systems on Windows often call this work using a system worker thread context as the File System Process (FSP). The following example of an asynchronous IRP\_MJ\_WRITE request sent to a network mini-redirector illustrates a case where the FSP needs to be used.

To execute an asynchronous IRP\_MJ\_WRITE request, RDBSS or a network mini-redirector needs to acquire the file object's FCB resource (a synchronization object used for changing the file object). When the FCB resource is already held by another thread and RDBSS or the network mini-redirector try to acquire the FCB resource in the user's thread context (the FSD), this operation will block. Asynchronous requests to a file system are not supposed to block. For asynchronous requests (IRP\_MJ\_WRITE request, for example), a file system driver will first check if the needed resource is available (the FCB resource for a network mini-redirector, for example). If the resource is not available, then the file system driver posts the request to a work queue for later completion by a system worker thread (the FSP) and the file system returns STATUS\_PENDING from the FSD thread. To the user application, the FSD will return STATUS\_PENDING immediately, while the actual work will be handled by a system worker thread in the FSP.

Several tasks must be completed before a file system driver posts work to the FSP. The file system driver needs to capture the security context from the user's thread in the FSD since the work will be completed by a system worker thread. RDBSS does this automatically in the [**RxFsdPostRequest**](https://msdn.microsoft.com/library/windows/hardware/ff554472) routine for network mini-redirectors. This routine is called by RDBSS whenever a network mini-redirector returns STATUS\_PENDING with the **PostRequest** member of the RX\_CONTEXT structure set to **TRUE**. If work is posted to a work queue, the file system driver must also make sure that the user buffers will be available for later use by the system worker thread. There are two methods to accomplish this task:

1.  A file system driver can map the user buffers into kernel memory space before posting to the FSP so the buffers can be accessed later by a system worker thread (FSP). The method commonly used by file system drivers is to lock the user buffers in the FSP because the memory pages can always be mapped later by the system worker thread.

2.  A file system can save the thread of the calling process from the FSP and the system worker thread can attach to this calling process while in the FSP. Using the [**KeStackAttachProcess**](https://msdn.microsoft.com/library/windows/hardware/ff549659), the system worker thread would attach to the user's calling process and access the user buffers and then detach from the user's calling process using [**KeUnstackDetachProcess**](https://msdn.microsoft.com/library/windows/hardware/ff549677) when the work is done.

RDBSS will automatically lock user buffers using method 1 in the [**RxFsdPostRequest**](https://msdn.microsoft.com/library/windows/hardware/ff554472) routine for a number of IRP requests as long as the RX\_CONTEXT\_FLAG\_NO\_PREPOSTING\_NEEDED bit is not set in the **Flags** member of the RX\_CONTEXT structure. User buffers will be locked for the following requests:

-   IRP\_MJ\_DIRECTORY\_CONTROL with a minor function of IRP\_MN\_QUERY\_DIRECTORY

-   IRP\_MJ\_QUERY\_EA

-   IRP\_MJ\_READ as long as the minor function does not include IRP\_MN\_MDL

-   IRP\_MJ\_SET\_EA

-   IRP\_MJ\_WRITE as long as the minor function does not include IRP\_MN\_MDL

Method 2 is commonly used for processing IRPs that use METHOD\_NEITHER when only a small amount of information is normally passed and returned. These IRPs would include the following:

-   IRP\_MJ\_DEVICE\_CONTROL

-   IRP\_MJ\_FILE\_SYSTEM\_CONTROL

-   IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL

RDBSS only supports asynchronous calls for the **MrxLowIoSubmit** array of operations. If a network mini-redirector wants to implement other operations ([**MRxQueryFileInfo**](https://msdn.microsoft.com/library/windows/hardware/ff550770), for example) as an asynchronous call, the network mini-redirector needs to post the request to the FSP. If a network mini-redirector receives a request for **MrxQueryFileInfo** with the RX\_CONTEXT\_ASYNC\_OPERATION bit set in the **Flags** member of the RX\_CONTEXT structure, the network mini-redirector would need to post this request to the FSP for asynchronous operation. In the operation of the **MrxQueryFileInfo** routine, the network mini-redirector would first need to capture the security context of the user's thread and map the user buffers into kernel space (or set the system worker thread to attach to the user's calling process while executing in the FSP). Then the network mini-redirector would set the **PostRequest** member of the RX\_CONTEXT structure to **TRUE** and return STATUS\_PENDING from the FSD. The work would be dispatched by RDBSS to a work queue for operation by a system worker thread (the FSP).

 

 




