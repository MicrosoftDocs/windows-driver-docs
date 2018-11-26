---
title: Writing Data Records to a CLFS Stream
description: Writing Data Records to a CLFS Stream
ms.assetid: 22bd6d39-b777-4a62-85b1-3d03a7144f7a
keywords: ["Common Log File System WDK kernel , data records", "CLFS WDK kernel , data records", "data records WDK CLFS", "reserved space WDK CLFS", "aligned entries WDK CLFS", "writing data records", "buffers WDK CLFS"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Writing Data Records to a CLFS Stream





There are two types of records in a Common Log File System (CLFS) stream: data records and restart records. This topic explains how to write data records to a stream. For information about how to write restart records, see [Writing Restart Records to a CLFS Stream](writing-restart-records-to-a-clfs-stream.md).

Before you can write data records to a CLFS stream, you must create a marshalling area by calling [**ClfsCreateMarshallingArea**](https://msdn.microsoft.com/library/windows/hardware/ff541520). Then you can append records to the marshalling area (which is in volatile memory), and CLFS will periodically flush the records to stable storage.

There are several variations on writing data records to a stream. For example, you can reserve space ahead of time and then write several records, or you can write records without reserving space. You can request that records you write to the marshalling area be immediately queued to stable storage, or you can let CLFS queue the records according to its policy.

For all variations on writing data records, complete the following steps.

1.  Create an array of one or more [**CLFS\_WRITE\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff541891) structures. Each write entry structure points to a buffer that you have filled with record data.

2.  Call [**ClfsReserveAndAppendLog**](https://msdn.microsoft.com/library/windows/hardware/ff541723) or [**ClfsReserveAndAppendLogAligned**](https://msdn.microsoft.com/library/windows/hardware/ff541726).

The tables in the following subsections show how to set the parameters of **ClfsReserveAndAppendLog** for several variations on writing a record to a stream.

### Writing a single data buffer to a stream

Suppose you have a single data buffer that you want to write to a marshalling area. You are willing to let the record be flushed to stable storage according to CLFS policy, and you do not want the record to be part of any chain of records. The following table shows how to set the parameters when you call **ClfsReserveAndAppendLog**.

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
<td><p>A pointer to a marshalling area.</p></td>
</tr>
<tr class="even">
<td><p><em>rgWriteEntries</em></p></td>
<td><p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541891" data-raw-source="[&lt;strong&gt;CLFS_WRITE_ENTRY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541891)"><strong>CLFS_WRITE_ENTRY</strong></a> structure.</p></td>
</tr>
<tr class="odd">
<td><p><em>cWriteEntries</em></p></td>
<td><p>1</p></td>
</tr>
<tr class="even">
<td><p><em>plsnUndoNext</em></p></td>
<td><p>CLFS_LSN_INVALID</p></td>
</tr>
<tr class="odd">
<td><p><em>plsnPrevious</em></p></td>
<td><p>CLFS_LSN_INVALID</p></td>
</tr>
<tr class="even">
<td><p><em>cReserveRecords</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>rgcbReservation</em></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="even">
<td><p><em>fFlags</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>plsn</em></p></td>
<td><p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff541824" data-raw-source="[&lt;strong&gt;CLFS_LSN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541824)"><strong>CLFS_LSN</strong></a> structure. (This is an output parameter that receives the LSN of the record that is written.)</p></td>
</tr>
</tbody>
</table>

 

### Reserving space for a set of CLFS log records

You can use **ClfsReserveAndAppendLog** to reserve space in a marshalling area for a set of log records without actually writing any of the records. The following table shows how to set the parameters to reserve record space.

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
<td><p>A pointer to a marshalling area.</p></td>
</tr>
<tr class="even">
<td><p><em>rgWriteEntries</em></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="odd">
<td><p><em>cWriteEntries</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>plsnUndoNext</em></p></td>
<td><p>CLFS_LSN_INVALID</p></td>
</tr>
<tr class="odd">
<td><p><em>plsnPrevious</em></p></td>
<td><p>CLFS_LSN_INVALID</p></td>
</tr>
<tr class="even">
<td><p><em>cReserveRecords</em></p></td>
<td><p>The number of elements in the array pointed to by <em>rgcbReservation</em>.</p></td>
</tr>
<tr class="odd">
<td><p><em>rgcbReservation</em></p></td>
<td><p>A pointer to an array of LONGLONG-typed variables. Each element in the array is the size, in bytes, of a record for which space will be reserved. Note that this is this size of the data portion of the record; you do not have to include the size of headers or padding.</p></td>
</tr>
<tr class="even">
<td><p><em>fFlags</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>plsn</em></p></td>
<td><p>NULL</p></td>
</tr>
</tbody>
</table>

 

**Note**   Another way to reserve space in a marshalling area is to call [**ClfsAlignReservedLog**](https://msdn.microsoft.com/library/windows/hardware/ff540779) followed by [**ClfsAllocReservedLog**](https://msdn.microsoft.com/library/windows/hardware/ff540782).

 

### Writing a record to reserved space

Suppose you have already reserved space for three records whose sizes, in bytes, are 100, 200, and 300. The marshalling area has a reserved-record count of 3 and enough reserved space to hold the 600 bytes of record data, the record headers, and any padding required for alignment.

Now suppose you want to write one of those records into the reserved space in the marshalling area. The available reserved space will be reduced, and the reserved-record count will be decremented from 3 to 2. The following table shows how to set the parameters when you call **ClfsReserveAndAppendLog**.

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
<td><p>A pointer to a marshalling area.</p></td>
</tr>
<tr class="even">
<td><p><em>rgWriteEntries</em></p></td>
<td><p>A pointer to an array of <strong>CLFS_WRITE_ENTRY</strong> structures.</p></td>
</tr>
<tr class="odd">
<td><p><em>cWriteEntries</em></p></td>
<td><p>The number of elements in the array pointed to by <em>rgWriteEntries</em>.</p></td>
</tr>
<tr class="even">
<td><p><em>plsnUndoNext</em></p></td>
<td><p>CLFS_LSN_INVALID or the LSN of the previous record in the undo chain. For more information about the undo chain, see <a href="clfs-log-sequence-numbers.md" data-raw-source="[CLFS Log Sequence Numbers](clfs-log-sequence-numbers.md)">CLFS Log Sequence Numbers</a>.</p></td>
</tr>
<tr class="odd">
<td><p><em>plsnPrevious</em></p></td>
<td><p>CLFS_LSN_INVALID or the LSN of the previous log record in the previous-LSN chain. For more information about the previous-LSN chain, see <a href="clfs-log-sequence-numbers.md" data-raw-source="[CLFS Log Sequence Numbers](clfs-log-sequence-numbers.md)">CLFS Log Sequence Numbers</a>.</p></td>
</tr>
<tr class="even">
<td><p><em>cReserveRecords</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><em>rgcbReservation</em></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="even">
<td><p><em>fFlags</em></p></td>
<td><p>CLFS_FLAG_USE_RESERVATION</p></td>
</tr>
<tr class="odd">
<td><p><em>plsn</em></p></td>
<td><p>A pointer to a <strong>CLFS_LSN</strong> structure. (This is an output parameter that receives the LSN of the record that is written.)</p></td>
</tr>
</tbody>
</table>

 

### Writing records with aligned entries

Suppose you want to write a record that has three write entries. The write entries vary in size between 300 and 500 bytes, but you require that each write entry begins on a 512-byte boundary. The following table shows how to set the parameters of the **ClfsReserveAndAppendLogAligned** function.

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
<td><p>A pointer to a marshalling area.</p></td>
</tr>
<tr class="even">
<td><p><em>rgWriteEntries</em></p></td>
<td><p>A pointer to an array of three CLFS_WRITE_ENTRY structures.</p></td>
</tr>
<tr class="odd">
<td><p><em>cWriteEntries</em></p></td>
<td><p>3</p></td>
</tr>
<tr class="even">
<td><p><em>cbEntryAlignment</em></p></td>
<td><p>512</p></td>
</tr>
<tr class="odd">
<td><p><em>plsnUndoNext</em></p></td>
<td><p>CLFS_LSN_INVALID or the LSN of the previous record in the undo chain. For more information about the undo chain, see <a href="clfs-log-sequence-numbers.md" data-raw-source="[CLFS Log Sequence Numbers](clfs-log-sequence-numbers.md)">CLFS Log Sequence Numbers</a>.</p></td>
</tr>
<tr class="even">
<td><p><em>plsnPrevious</em></p></td>
<td><p>CLFS_LSN_INVALID or the LSN of the previous log record in the previous-LSN chain. For more information about the previous-LSN chain, see <a href="clfs-log-sequence-numbers.md" data-raw-source="[CLFS Log Sequence Numbers](clfs-log-sequence-numbers.md)">CLFS Log Sequence Numbers</a>.</p></td>
</tr>
<tr class="odd">
<td><p><em>cReserveRecords</em></p></td>
<td><p>0</p></td>
</tr>
<tr class="even">
<td><p><em>rgcbReservation</em></p></td>
<td><p>NULL</p></td>
</tr>
<tr class="odd">
<td><p><em>fFlags</em></p></td>
<td><p>Zero or some combination of flags that specify flush and reservation preferences.</p></td>
</tr>
<tr class="even">
<td><p><em>plsn</em></p></td>
<td><p>A pointer to a CLFS_LSN structure. (This is an output parameter that receives the LSN of the record that is written.)</p></td>
</tr>
</tbody>
</table>

 

The preceding tables show only a few of the many variations on reserving record space and writing records to CLFS streams. As you think of other variations, keep the following point in mind: The actions performed by **ClfsReserveAndAppendLog** (or **ClfsReserveAndAppendLogAligned**) are atomic. For example, you can make a single call to **ClfsReserveAndAppendLog** that will reserve space for a record and write the record to the stream. The pair of actions (reserve, write) will either succeed as a whole or fail as a whole.

 

 




