---
title: Writing Restart Records to a CLFS Stream
author: windows-driver-content
description: Writing Restart Records to a CLFS Stream
MS-HAID:
- 'Clfs\_guide\_05deb015-42bf-437e-9afd-dd8bdd703c39.xml'
- 'kernel.writing\_restart\_records\_to\_a\_clfs\_stream'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ae341d7e-37b2-4880-948c-e78e29278c64
keywords: ["Common Log File System WDK kernel , restart records", "CLFS WDK kernel , restart records", "restart records WDK CLFS", "checkpoints WDK CLFS"]
---

# Writing Restart Records to a CLFS Stream


## <a href="" id="ddk-introduction-to-wmi-kg"></a>


There are two types of records in a Common Log File System (CLFS)stream: data records and restart records. This topic explains how to write restart records to a CLFS stream. For information about how to write data records, see [Writing Data Records to a CLFS Stream](writing-data-records-to-a-clfs-stream.md).

Typically, restart records are written to a stream periodically to create checkpoints that help make recovery more efficient in the event of a system failure. Assume that you have already created a marshalling area and written several data records. You can then write a restart record by calling [**ClfsWriteRestartArea**](https://msdn.microsoft.com/library/windows/hardware/ff541770). By setting the *fFlags* parameter, you can specify whether the restart record is placed in the marshalling area's reserved space or in newly allocated space.When CLFS writes a restart record to a stream, it automatically sets the previous LSN of the record to the LSN of the previously written restart record for that stream. That forms a chain of restart records that can be traversed in reverse order. For information about reading the chain of restart records, see [Reading Restart Records from a CLFS Stream](reading-restart-records-from-a-clfs-stream.md).

If you want to write a restart record to a stream and change the base LSN of the stream at the same time, set the *plsnBase* parameter of **ClfsWriteRestartArea** to the new base LSN.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20Restart%20Records%20to%20a%20CLFS%20Stream%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


