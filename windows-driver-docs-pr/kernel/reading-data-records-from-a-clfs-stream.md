---
title: Reading Data Records from a CLFS Stream
description: Reading data records from a CLFS stream
keywords: ["Common Log File System WDK kernel , data records", "CLFS WDK kernel , data records", "data records WDK CLFS", "reading data records", "read forward WDK CLFS", "forward reading WDK CLFS", "read backward WDK CLFS", "backward reading WDK CLFS", "previous LSNs WDK CLFS", "undo-next LSNs WDK CLFS"]
ms.date: 04/02/2025
ms.topic: how-to
---

# Reading data records from a CLFS stream

There are two types of records in a Common Log File System (CLFS) stream: data records and restart records. This topic explains how to read a sequence of data records from a stream. For information about how to read restart records, see [Reading restart records from a CLFS stream](reading-restart-records-from-a-clfs-stream.md).

There are several variations on reading a sequence of data records from a stream. You can read forward in the stream from a specified record or you can read backward along a chain of linked records.

For all variations on reading a sequence of data records, complete the following steps.

1. Call [**ClfsReadLogRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadlogrecord) to obtain a read context and the first data record in the sequence.

1. Pass the read context you obtained in step 1 to [**ClfsReadNextLogRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadnextlogrecord) repeatedly to obtain the remaining data records in the sequence.

> [!CAUTION]
> Read contexts are not thread-safe. Clients are responsible for serializing access to read contexts.

The following subtopics discuss the details of reading the different types of record sequences and chains.

## Reading forward from a specified data record

To read forward in a CLFS stream (starting at the data record of your choice), you must create a read context that has its mode set to **ClfsContextForward**. To create a read context and read the first record (in the set that you have chosen to read), call **ClfsReadLogRecord** as shown in the following table.

| Parameter name | Value |
|--|--|
| *pvMarshalContext* | Supply a pointer to a marshalling area. |
| *plsnFirst* | Supply the LSN of the first record you want to read. This must be the LSN of a data record, not a restart record. |
| *peContextMode* | Supply the value **ClfsContextForward**. |
| *ppvReadBuffer* | Receive your record data. |
| *pcbReadBuffer* | Receive the size of your record data. |
| *peRecordType* | Receive the record type. This value is a set of flags that indicate various features of the record. The record is a data record, so the value you receive should have the ClfsDataRecord flag set and the ClfsRestartRecord flag clear. |
| *plsnUndoNext* | Receive the undo-next LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it. |
| *plsnPrevious* | Receive the previous LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it. |
| *ppvReadContext* | Receive a pointer to an opaque read context. Use the read context to read subsequent records. |

After you have obtained the read context and the first record, you can obtain subsequent records in the stream by calling **ClfsReadNextLogRecord** repeatedly. When there are no more data records in the stream, **ClfsReadNextLogRecord** returns STATUS_END_OF_FILE. The following table shows how to set and interpret the parameters.

| Parameter name | Value |
|--|--|
| *pvReadContext* | Supply a pointer to the read context you received from **ClfsReadLogRecord**. |
| *ppvBuffer* | Receive your record data. |
| *pcbBuffer* | Receive the size of your record data. |
| *peRecordType* | Supply the value of **ClfsDataRecord**. |
| *plsnUndoNext* | Receive the undo-next LSN field of the data record. You do not need this value to continue reading the chain, so you can ignore it. |
| *plsnPrevious* | Receive the previous-LSN field of the data record. You do not need this value to continue reading the chain, so you can ignore it. |
| *plsnRecord* | Receive the LSN of the data record that was read. |

## Reading a chain of data records linked by the previous LSN

When you write a data record to a CLFS stream, you can set the previous LSN of the data record to the LSN of any record that you previously wrote to the stream. By setting the previous LSN, you can create a chain of related records that can later be traversed in reverse order. For example, suppose you are performing a database transaction and you must write several CLFS log records to describe the updates made by the transaction. Each time you write a log record that describes a transaction update, you could set the previous LSN of the record to the LSN of the previous log record that describes an update made by the same transaction.

Suppose you have written a chain of data records that are linked by their previous LSNs. To read the chain of records, you must create a read context that has its mode set to **ClfsContextPrevious**. To create a read context and read the first record in the chain, call **ClfsReadLogRecord** as shown in the following table.

| Parameter name | Value |
|--|--|
| *pvMarshalContext* | Supply a pointer to a marshalling area. |
| *plsnFirst* | Supply the LSN of the first record in the chain. This must be the LSN of a data record, not a restart record. |
| *peContextMode* | Supply the value of **ClfsContextPrevious**. |
| *ppvReadBuffer* | Receive your record data. |
| *pcbReadBuffer* | Receive the size of your record data. |
| *peRecordType* | Receive the record type. This value is a set of flags that indicate various features of the record. The record is a data record, so the value you receive should have the ClfsDataRecord flag set and the ClfsRestartRecord flag clear. |
| *plsnUndoNext* | Receive the undo-next LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it. |
| *plsnPrevious* | Receive the previous LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it. |
| *ppvReadContext* | Receive a pointer to an opaque read context. Use the read context to read the previous records in the chain. |

After you have the read context and the first record, you can read the remaining records in the chain by calling **ClfsReadNextLogRecord** repeatedly. The following table shows how to set and interpret the parameters.

| Parameter name | Value |
|--|--|
| *pvReadContext* | Supply a pointer to the read context you received from **ClfsReadLogRecord**. |
| *ppvBuffer* | Receive your record data. |
| *pcbBuffer* | Receive the size of your record data. |
| *peRecordType* | Supply the value of **ClfsDataRecord**. |
| *plsnUndoNext* | Receive the undo-next LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it. |
| *plsnPrevious* | Receive the previous LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it. |
| *plsnRecord* | Receive the LSN of the data record that was read. |

As you make repeated calls to **ClfsReadNextLogRecord**, your sequence of calls will end in one of the following ways.

- Eventually you will read a data record that has its previous LSN set to CLFS_LSN_INVALID. The next time you call **ClfsReadNextLogRecord**, it will return STATUS_END_OF_FILE.

- Eventually you will read a data record that has a previous LSN that is less than both the base LSN of the stream and the [*archive tail*](clfs-terminology.md) of the stream. The next time you call **ClfsReadNextLogRecord**, it will return STATUS_LOG_START_OF_LOG.

## Reading a chain of data records linked by the undo-next LSN

When you write a data record to a CLFS stream, you can set the undo-next LSN of the data record to the LSN of any record that you previously wrote to the stream. By setting the undo-next LSN, you can create a chain of related records that can be traversed in reverse order. For more information about creating and interpreting undo-next chains, see [CLFS Log Sequence Numbers](clfs-log-sequence-numbers.md).

Suppose you have written a chain of data records that are linked by their undo-next LSNs. To read the chain of records, you must call [**ClfsReadLogRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadlogrecord) to create a read context that has its mode set to **ClfsContextUndoNext**. After that, the process is identical to reading a chain linked by previous LSNs (described previously in this topic).

## Reading a chain of data records linked by the user LSN

In addition to chains linked by previous LSNs and undo-next LSNs, you can create chains linked by your own LSNs that you embed in your record data.

Suppose you have written a chain of data records that are linked by LSNs you have stored in the record data itself. To read the chain of records, you must create a read context that has its mode set to either **ClfsContextPrevious** or **ClfsContextUndoNext**. Create your read context and obtain the most recently written record in the chain by calling [**ClfsReadLogRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadlogrecord). Then call [**ClfsReadNextLogRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfsreadnextlogrecord) repeatedly to obtain the previous records in the chain. Each time you call **ClfsReadNextLogRecord**, set the *plsnUser* parameter to the LSN of the previous record in your chain. The LSN you supply in *plsnUser* overrides any values stored in the current record's previous-LSN or undo-next LSN fields.

You can only move backward in the stream when you call **ClfsReadNextLogRecord** to read a record chain. The LSN you supply in *plsnUser* must be less than the LSN of the current record in the chain.
