---
title: Reading Data Records from a CLFS Stream
description: Reading Data Records from a CLFS Stream
ms.assetid: 46e583c5-9f12-4f05-8f11-683ac428313a
keywords: ["Common Log File System WDK kernel , data records", "CLFS WDK kernel , data records", "data records WDK CLFS", "reading data records", "read forward WDK CLFS", "forward reading WDK CLFS", "read backward WDK CLFS", "backward reading WDK CLFS", "previous LSNs WDK CLFS", "undo-next LSNs WDK CLFS"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Reading Data Records from a CLFS Stream


There are two types of records in a Common Log File System (CLFS) stream: data records and restart records. This topic explains how to read a sequence of data records from a stream. For information about how to read restart records, see [Reading Restart Records from a CLFS Stream](reading-restart-records-from-a-clfs-stream.md).

There are several variations on reading a sequence of data records from a stream. You can read forward in the stream from a specified record or you can read backward along a chain of linked records.

For all variations on reading a sequence of data records, complete the following steps.

1.  Call [**ClfsReadLogRecord**](https://msdn.microsoft.com/library/windows/hardware/ff541682) to obtain a read context and the first data record in the sequence.

2.  Pass the read context you obtained in step 1 to [**ClfsReadNextLogRecord**](https://msdn.microsoft.com/library/windows/hardware/ff541690) repeatedly to obtain the remaining data records in the sequence.

**Caution**  Read contexts are not thread-safe. Clients are responsible for serializing access to read contexts.

 

The following subtopics discuss the details of reading the different types of record sequences and chains.

### Reading forward from a specified data record

To read forward in a CLSF stream (starting at the data record of your choice), you must create a read context that has its mode set to **ClfsContextForward**. To create a read context and read the first record (in the set that you have chosen to read), call **ClfsReadLogRecord** as shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pvMarshalContext</em></p></td>
<td><p>Supply a pointer to a marshalling area.</p></td>
</tr>
<tr class="even">
<td><p><em>plsnFirst</em></p></td>
<td><p>Supply the LSN of the first record you want to read. This must be the LSN of a data record, not a restart record.</p></td>
</tr>
<tr class="odd">
<td><p><em>peContextMode</em></p></td>
<td><p>Supply the value <strong>ClfsContextForward</strong>.</p></td>
</tr>
<tr class="even">
<td><p><em>ppvReadBuffer</em></p></td>
<td><p>Receive your record data.</p></td>
</tr>
<tr class="odd">
<td><p><em>pcbReadBuffer</em></p></td>
<td><p>Receive the size of your record data.</p></td>
</tr>
<tr class="even">
<td><p><em>peRecordType</em></p></td>
<td><p>Receive the record type. This value is a set of flags that indicate various features of the record. The record is a data record, so the value you receive should have the ClfsDataRecord flag set and the ClfsRestartRecord flag clear.</p></td>
</tr>
<tr class="odd">
<td><p><em>plsnUndoNext</em></p></td>
<td><p>Receive the undo-next LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it.</p></td>
</tr>
<tr class="even">
<td><p><em>plsnPrevious</em></p></td>
<td><p>Receive the previous LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it.</p></td>
</tr>
<tr class="odd">
<td><p><em>ppvReadContext</em></p></td>
<td><p>Receive a pointer to an opaque read context. Use the read context to read subsequent records.</p></td>
</tr>
</tbody>
</table>

 

After you have obtained the read context and the first record, you can obtain subsequent records in the stream by calling **ClfsReadNextLogRecord** repeatedly. When there are no more data records in the stream, **ClfsReadNextLogRecord** returns STATUS\_END\_OF\_FILE. The following table shows how to set and interpret the parameters.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pvReadContext</em></p></td>
<td><p>Supply a pointer to the read context you received from <strong>ClfsReadLogRecord</strong>.</p></td>
</tr>
<tr class="even">
<td><p><em>ppvBuffer</em></p></td>
<td><p>Receive your record data.</p></td>
</tr>
<tr class="odd">
<td><p><em>pcbBuffer</em></p></td>
<td><p>Receive the size of your record data.</p></td>
</tr>
<tr class="even">
<td><p><em>peRecordType</em></p></td>
<td><p>Supply the value of <strong>ClfsDataRecord</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><em>plsnUndoNext</em></p></td>
<td><p>Receive the undo-next LSN field of the data record. You do not need this value to continue reading the chain, so you can ignore it.</p></td>
</tr>
<tr class="even">
<td><p><em>plsnPrevious</em></p></td>
<td><p>Receive the previous-LSN field of the data record. You do not need this value to continue reading the chain, so you can ignore it.</p></td>
</tr>
<tr class="odd">
<td><p><em>plsnRecord</em></p></td>
<td><p>Receive the LSN of the data record that was read.</p></td>
</tr>
</tbody>
</table>

 

### Reading a chain of data records linked by the previous LSN

When you write a data record to a CLFS stream, you can set the previous LSN of the data record to the LSN of any record that you previously wrote to the stream. By setting the previous LSN, you can create a chain of related records that can later be traversed in reverse order. For example, suppose you are performing a database transaction and you must write several CLFS log records to describe the updates made by the transaction. Each time you write a log record that describes a transaction update, you could set the previous LSN of the record to the LSN of the previous log record that describes an update made by the same transaction.

Suppose you have written a chain of data records that are linked by their previous LSNs. To read the chain of records, you must create a read context that has its mode set to **ClfsContextPrevious**. To create a read context and read the first record in the chain, call **ClfsReadLogRecord** as shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pvMarshalContext</em></p></td>
<td><p>Supply a pointer to a marshalling area.</p></td>
</tr>
<tr class="even">
<td><p><em>plsnFirst</em></p></td>
<td><p>Supply the LSN of the first record in the chain. This must be the LSN of a data record, not a restart record.</p></td>
</tr>
<tr class="odd">
<td><p><em>peContextMode</em></p></td>
<td><p>Supply the value of <strong>ClfsContextPrevious</strong>.</p></td>
</tr>
<tr class="even">
<td><p><em>ppvReadBuffer</em></p></td>
<td><p>Receive your record data.</p></td>
</tr>
<tr class="odd">
<td><p><em>pcbReadBuffer</em></p></td>
<td><p>Receive the size of your record data.</p></td>
</tr>
<tr class="even">
<td><p><em>peRecordType</em></p></td>
<td><p>Receive the record type. This value is a set of flags that indicate various features of the record. The record is a data record, so the value you receive should have the ClfsDataRecord flag set and the ClfsRestartRecord flag clear.</p></td>
</tr>
<tr class="odd">
<td><p><em>plsnUndoNext</em></p></td>
<td><p>Receive the undo-next LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it.</p></td>
</tr>
<tr class="even">
<td><p><em>plsnPrevious</em></p></td>
<td><p>Receive the previous LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it.</p></td>
</tr>
<tr class="odd">
<td><p><em>ppvReadContext</em></p></td>
<td><p>Receive a pointer to an opaque read context. Use the read context to read the previous records in the chain.</p></td>
</tr>
</tbody>
</table>

 

After you have the read context and the first record, you can read the remaining records in the chain by calling **ClfsReadNextLogRecord** repeatedly. The following table shows how to set and interpret the parameters.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>pvReadContext</em></p></td>
<td><p>Supply a pointer to the read context you received from <strong>ClfsReadLogRecord</strong>.</p></td>
</tr>
<tr class="even">
<td><p><em>ppvBuffer</em></p></td>
<td><p>Receive your record data.</p></td>
</tr>
<tr class="odd">
<td><p><em>pcbBuffer</em></p></td>
<td><p>Receive the size of your record data.</p></td>
</tr>
<tr class="even">
<td><p><em>peRecordType</em></p></td>
<td><p>Supply the value of <strong>ClfsDataRecord</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><em>plsnUndoNext</em></p></td>
<td><p>Receive the undo-next LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it.</p></td>
</tr>
<tr class="even">
<td><p><em>plsnPrevious</em></p></td>
<td><p>Receive the previous LSN of the data record. You do not need this value to continue reading the chain, so you can ignore it.</p></td>
</tr>
<tr class="odd">
<td><p><em>plsnRecord</em></p></td>
<td><p>Receive the LSN of the data record that was read.</p></td>
</tr>
</tbody>
</table>

 

As you make repeated calls to **ClfsReadNextLogRecord**, your sequence of calls will end in one of the following ways.

-   Eventually you will read a data record that has its previous LSN set to CLFS\_LSN\_INVALID. The next time you call **ClfsReadNextLogRecord**, it will return STATUS\_END\_OF\_FILE.

-   Eventually you will read a data record that has a previous LSN that is less than both the base LSN of the stream and the [*archive tail*](clfs-terminology.md#kernel-clfs-term-archive-tail) of the stream. The next time you call **ClfsReadNextLogRecord**, it will return STATUS\_LOG\_START\_OF\_LOG.

### Reading a chain of data records linked by the undo-next LSN

When you write a data record to a CLFS stream, you can set the undo-next LSN of the data record to the LSN of any record that you previously wrote to the stream. By setting the undo-next LSN, you can create a chain of related records that can be traversed in reverse order. For more information about creating and interpreting undo-next chains, see [CLFS Log Sequence Numbers](clfs-log-sequence-numbers.md).

Suppose you have written a chain of data records that are linked by their undo-next LSNs. To read the chain of records, you must call [**ClfsReadLogRecord**](https://msdn.microsoft.com/library/windows/hardware/ff541682) to create a read context that has its mode set to **ClfsContextUndoNext**. After that, the process is identical to reading a chain linked by previous LSNs (described previously in this topic).

### Reading a chain of data records linked by the user LSN

In addition to chains linked by previous LSNs and undo-next LSNs, you can create chains linked by your own LSNs that you embed in your record data.

Suppose you have written a chain of data records that are linked by LSNs you have stored in the record data itself. To read the chain of records, you must create a read context that has its mode set to either **ClfsContextPrevious** or **ClfsContextUndoNext**. Create your read context and obtain the most recently written record in the chain by calling [**ClfsReadLogRecord**](https://msdn.microsoft.com/library/windows/hardware/ff541682). Then call [**ClfsReadNextLogRecord**](https://msdn.microsoft.com/library/windows/hardware/ff541690) repeatedly to obtain the previous records in the chain. Each time you call **ClfsReadNextLogRecord**, set the *plsnUser* parameter to the LSN of the previous record in your chain. The LSN you supply in *plsnUser* overrides any values stored in the current record's previous-LSN or undo-next LSN fields.

Note that you can only move backward in the stream when you call **ClfsReadNextLogRecord** to read a record chain. The LSN you supply in *plsnUser* must be less than the LSN of the current record in the chain.

 

 




