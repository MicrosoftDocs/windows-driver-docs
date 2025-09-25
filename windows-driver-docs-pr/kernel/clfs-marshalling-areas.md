---
title: CLFS Marshalling Areas
description: CLFS marshalling areas
keywords: ["Common Log File System WDK kernel , marshalling areas", "CLFS WDK kernel , marshalling areas", "marshalling areas WDK CLFS", "log I/O buffers WDK CLFS", "maximum number of log I/O buffers WDK CLFS", "memory allocations WDK CLFS", "buffers WDK CLFS", "appending records WDK CLFS", "stable storage WDK CLFS", "volatile memory WDK CLFS", "storage WDK CLFS"]
ms.date: 09/19/2025
ms.topic: concept-article
---

# CLFS marshalling areas

A Common Log File System (CLFS) client appends log records to a [*marshalling area*](clfs-terminology.md) in volatile memory, and CLFS periodically writes those records to stable storage. A marshalling area is a collection of log I/O buffers, each of which can hold several log records. Log I/O buffers hold records recently written to a stream (but possibly not flushed to stable storage) and records recently read from the stream.

You create a marshalling area by calling [**ClfsCreateMarshallingArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatemarshallingarea), at which time you must specify the size of the log I/O buffers that the marshalling area uses and whether those buffers are in the paged or non-paged pool. All log I/O buffers in a marshalling area are the same size, and CLFS ensures that the size is a multiple of the sector size on the underlying stable storage medium. That is, CLFS takes your requested size and rounds it up as necessary to make your I/O buffers compatible with the stable storage medium.

CLFS allocates and frees log I/O buffers as needed, but you have the option of setting the maximum number of I/O buffers that can be allocated at one time. You also have the option of providing your own buffer allocation and deallocation functions.

To specify the maximum number of log I/O buffers that can be allocated at one time for writing log records, set the *cMaxWriteBuffers* parameter of the **ClfsCreateMarshallingArea** function. Limiting the number of buffers affects the frequency of flushes to stable storage; with fewer buffers, log records must be written to stable storage more often. If you don't need to control the flush frequency, set *cMaxWriteBuffers* to INFINITE (defined in Winbase.h).

To specify the maximum number of log I/O buffers that can be allocated at one time for reading log records, set the *cMaxReadBuffers* parameter of the **ClfsCreateMarshallingArea** function. If you don't need to control the number of allocated read buffers, set *cMaxReadBuffers* to INFINITE.

If you want to do your own memory allocation for log I/O buffers, set the *pfnAllocBuffer* and *pfnFreeBuffer* parameters of the **ClfsCreateMarshallingArea** function to point to your own allocation and deallocation functions. Then CLFS calls your functions to perform the actual memory allocation and deallocation whenever it needs to create or free log I/O buffers.

In some cases, you might want to reserve space in a marshalling area ahead of time. For example, you might know that you're about to write a set of 10 log records, and you want to be sure that there's enough space in the marshalling area for the entire set. To reserve space for the 10 records, create a 10-element array that holds the sizes of the records, and then pass the array to the [**ClfsReserveAndAppendLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlog) function in the *rgcbReservation* parameter. **ClfsReserveAndAppendLog** is a multi-purpose function that reserves space in a marshalling area or appends log records to a stream or does both of those things atomically. By setting the parameters appropriately, you can call **ClfsReserveAndAppendLog** to reserve space for future use without actually appending any records to the stream.

## See also

[**ClfsCreateMarshallingArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatemarshallingarea)

[**ClfsReserveAndAppendLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlog)

[*marshalling area*](clfs-terminology.md)
