---
title: Writing Data Records to a CLFS Stream
description: Writing data records to a CLFS stream
keywords: ["Common Log File System WDK kernel , data records", "CLFS WDK kernel , data records", "data records WDK CLFS", "reserved space WDK CLFS", "aligned entries WDK CLFS", "writing data records", "buffers WDK CLFS"]
ms.date: 04/04/2025
ms.topic: how-to
---

# Writing data records to a CLFS stream

There are two types of records in a Common Log File System (CLFS) stream: data records and restart records. This article explains how to write data records to a stream. For information about how to write restart records, see [Writing restart records to a CLFS stream](writing-restart-records-to-a-clfs-stream.md).

Before you can write data records to a CLFS stream, you must create a marshalling area by calling [**ClfsCreateMarshallingArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatemarshallingarea). Then you can append records to the marshalling area (which is in volatile memory), and CLFS  periodically flushes the records to stable storage.

There are several variations on writing data records to a stream. For example, you can reserve space ahead of time and then write several records, or you can write records without reserving space. You can request that records you write to the marshalling area are immediately queued to stable storage, or you can let CLFS queue the records according to its policy.

For all variations on writing data records, complete the following steps.

1. Create an array of one or more [**CLFS_WRITE_ENTRY**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_cls_write_entry) structures. Each write entry structure points to a buffer that you filled with record data.

1. Call [**ClfsReserveAndAppendLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlog) or [**ClfsReserveAndAppendLogAligned**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlogaligned).

The tables in the following subsections show how to set the parameters of **ClfsReserveAndAppendLog** for several variations on writing a record to a stream.

## Writing a single data buffer to a stream

Suppose you have a single data buffer that you want to write to a marshalling area. You're willing to let the record be flushed to stable storage according to CLFS policy, and you don't want the record to be part of any chain of records. The following table shows how to set the parameters when you call **ClfsReserveAndAppendLog**.

| Parameter name | Value |
|--|--|
| *pvMarshalContext* | A pointer to a marshalling area. |
| *rgWriteEntries* | A pointer to a [**CLFS_WRITE_ENTRY**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_cls_write_entry) structure. |
| *cWriteEntries* | 1 |
| *plsnUndoNext* | CLFS_LSN_INVALID |
| *plsnPrevious* | CLFS_LSN_INVALID |
| *cReserveRecords* | 0 |
| *rgcbReservation* | NULL |
| *fFlags* | 0 |
| *plsn* | A pointer to a [**CLFS_LSN**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_cls_lsn) structure. This is an output parameter that receives the log sequence number (LSN) of the record that is written. |

## Reserving space for a set of CLFS log records

You can use **ClfsReserveAndAppendLog** to reserve space in a marshalling area for a set of log records without actually writing any of the records. The following table shows how to set the parameters to reserve record space.

| Parameter name | Value |
|--|--|
| *pvMarshalContext* | A pointer to a marshalling area. |
| *rgWriteEntries* | NULL |
| *cWriteEntries* | 0 |
| *plsnUndoNext* | CLFS_LSN_INVALID |
| *plsnPrevious* | CLFS_LSN_INVALID |
| *cReserveRecords* | The number of elements in the array pointed to by *rgcbReservation*. |
| *rgcbReservation* | A pointer to an array of LONGLONG-typed variables. Each element in the array is the size, in bytes, of a record for which space is reserved. This is the size of the data portion of the record. You don't have to include the size of headers or padding. |
| *fFlags* | 0 |
| *plsn* | NULL |

Another way to reserve space in a marshalling area is to call [**ClfsAlignReservedLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsalignreservedlog) followed by [**ClfsAllocReservedLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsallocreservedlog).

## Writing a record to reserved space

Suppose you already reserved space for three records whose sizes, in bytes, are 100, 200, and 300. The marshalling area has a reserved-record count of 3 and enough reserved space to hold the 600 bytes of record data, the record headers, and any padding required for alignment.

Now suppose you want to write one of those records into the reserved space in the marshalling area. The available reserved space is reduced, and the reserved-record count is decremented from 3 to 2. The following table shows how to set the parameters when you call **ClfsReserveAndAppendLog**.

| Parameter name | Value |
|--|--|
| *pvMarshalContext* | A pointer to a marshalling area. |
| *rgWriteEntries* | A pointer to an array of **CLFS_WRITE_ENTRY** structures. |
| *cWriteEntries* | The number of elements in the array pointed to by *rgWriteEntries*. |
| *plsnUndoNext* | CLFS_LSN_INVALID or the log sequence number (LSN) of the previous record in the undo chain. For more information about the undo chain, see [CLFS log sequence numbers](clfs-log-sequence-numbers.md). |
| *plsnPrevious* | CLFS_LSN_INVALID or the LSN of the previous log record in the previous-LSN chain. For more information about the previous-LSN chain, see [CLFS log sequence numbers](clfs-log-sequence-numbers.md) |
| *cReserveRecords* | 0 |
| *rgcbReservation* | NULL |
| *fFlags* | CLFS_FLAG_USE_RESERVATION |
| *plsn* | A pointer to a **CLFS_LSN** structure. This is an output parameter that receives the LSN of the record that is written. |

## Writing records with aligned entries

Suppose you want to write a record that has three write entries. The write entries vary in size between 300 bytes and 500 bytes, but you require that each write entry begins on a 512-byte boundary. The following table shows how to set the parameters of the **ClfsReserveAndAppendLogAligned** function.

| Parameter name | Value |
|--|--|
| *pvMarshalContext* | A pointer to a marshalling area. |
| *rgWriteEntries* | A pointer to an array of three CLFS_WRITE_ENTRY structures. |
| *cWriteEntries* | 3 |
| *cbEntryAlignment* | 512 |
| *plsnUndoNext* | CLFS_LSN_INVALID or the log sequence number (LSN) of the previous record in the undo chain. For more information about the undo chain, see [CLFS log sequence numbers](clfs-log-sequence-numbers.md). |
| *plsnPrevious* | CLFS_LSN_INVALID or the LSN of the previous log record in the previous-LSN chain. For more information about the previous-LSN chain, see [CLFS log sequence numbers](clfs-log-sequence-numbers.md) |
| *cReserveRecords* | 0 |
| *rgcbReservation* | NULL |
| *fFlags* | Zero or some combination of flags that specify flush and reservation preferences. |
| *plsn* | A pointer to a **CLFS_LSN** structure. This is an output parameter that receives the LSN of the record that is written. |

The preceding tables show only a few of the many variations on reserving record space and writing records to CLFS streams. As you think of other variations, keep the following point in mind: The actions performed by **ClfsReserveAndAppendLog** (or **ClfsReserveAndAppendLogAligned**) are atomic. For example, you can make a single call to **ClfsReserveAndAppendLog** that reserves space for a record and write the record to the stream. The pair of actions (reserve, write) succeeds as a whole or fail as a whole.

## See also

[CLFS log sequence numbers](clfs-log-sequence-numbers.md)

[**ClfsAlignReservedLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsalignreservedlog)

[**ClfsAllocReservedLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsallocreservedlog)

[**ClfsCreateMarshallingArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatemarshallingarea)

[**ClfsReserveAndAppendLog**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlog)

[**ClfsReserveAndAppendLogAligned**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreserveandappendlogaligned)

[**CLFS_LSN**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_cls_lsn)

[**CLFS_WRITE_ENTRY**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_cls_write_entry)

[Writing restart records to a CLFS stream](writing-restart-records-to-a-clfs-stream.md)
