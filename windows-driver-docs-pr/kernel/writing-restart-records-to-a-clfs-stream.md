---
title: Writing Restart Records to a CLFS Stream
description: Writing Restart Records to a CLFS Stream
ms.assetid: ae341d7e-37b2-4880-948c-e78e29278c64
keywords: ["Common Log File System WDK kernel , restart records", "CLFS WDK kernel , restart records", "restart records WDK CLFS", "checkpoints WDK CLFS"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Writing Restart Records to a CLFS Stream





There are two types of records in a Common Log File System (CLFS)stream: data records and restart records. This topic explains how to write restart records to a CLFS stream. For information about how to write data records, see [Writing Data Records to a CLFS Stream](writing-data-records-to-a-clfs-stream.md).

Typically, restart records are written to a stream periodically to create checkpoints that help make recovery more efficient in the event of a system failure. Assume that you have already created a marshalling area and written several data records. You can then write a restart record by calling [**ClfsWriteRestartArea**](https://msdn.microsoft.com/library/windows/hardware/ff541770). By setting the *fFlags* parameter, you can specify whether the restart record is placed in the marshalling area's reserved space or in newly allocated space.When CLFS writes a restart record to a stream, it automatically sets the previous LSN of the record to the LSN of the previously written restart record for that stream. That forms a chain of restart records that can be traversed in reverse order. For information about reading the chain of restart records, see [Reading Restart Records from a CLFS Stream](reading-restart-records-from-a-clfs-stream.md).

If you want to write a restart record to a stream and change the base LSN of the stream at the same time, set the *plsnBase* parameter of **ClfsWriteRestartArea** to the new base LSN.

 

 




