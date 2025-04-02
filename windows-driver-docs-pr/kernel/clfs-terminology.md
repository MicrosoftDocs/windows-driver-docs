---
title: CLFS Terminology
description: This article gives definitions of key terms used in the Common Log File System (CLFS) documentation.
Robots: noindex, nofollow
keywords: ["Common Log File System WDK kernel , terminology", "CLFS WDK kernel , terminology"]
ms.date: 04/02/2025
---

# CLFS terminology

The following table gives definitions of key terms used in the Common Log File System (CLFS) documentation. These definitions apply during a discussion of CLFS, but might not apply otherwise. Many of these terms have general meanings or meanings in the context of other technologies that differ from the definitions given here.

| Term | Definition |
|--|--|
| **container** | A contiguous extent on a physical disk or other stable storage medium. For example, a container could be a contiguous disk file. |
| **sector** | The unit of atomic I/O on a physical storage medium. The size of a sector is a property of a particular storage device. For example, a hard disk might have a sector size of 512 bytes. |
| **client** | An application, driver, thread, or other unit of software that uses a CLFS log. |
| **record** | The unit of data that a client can append to or read from a log. |
| **stream** | An ordered subset of the records in a log. A log can have one or more streams. A client appends records to and reads records from a particular stream. You can compare the records in a given stream to determine the order in which they were written. You cannot compare records in different streams. A given stream can have several clients. For example, several threads could append records to a single stream. To a client, a stream appears as if it were the entire log. |
| **dedicated log** | A log that can have only one stream. |
| **multiplexed log** | A log that can have several streams. |
| **log I/O block** | A buffer where CLFS collects a set of records that are atomically written to stable storage. |
| **marshalling area** | A set of log I/O blocks, created, maintained, and scheduled by a CLFS client for gathering log records and writing them to stable storage. The log I/O blocks allocated in volatile memory for a particular marshalling area are all the same size.<br><br>Even though all the log I/O blocks (in volatile memory) for a particular marshalling area are the same size, the log I/O blocks that are written to stable storage (from that marshalling area) vary in size. For example, if a log I/O block is forced to stable storage before it is full, only the used portion of the block will be written to stable storage. |
| **log sequence number (LSN)** | An opaque structure that holds a value that uniquely identifies a log record in a given stream. When a client writes a record to a stream, it gets back an LSN that it can use to identify the record in the future. The LSNs that CLFS assigns to the records in a stream form an increasing sequence. That is, the LSN assigned to a record in a stream is always greater than the LSN assigned to the record previously written to that same stream.<br><br>Records across streams are not comparable. That is, you cannot compare the LSNs of two records in different streams to determine which record was written first. |
| **base LSN** | The LSN of the oldest record in a stream that is still needed by the stream's clients. The clients are responsible for updating the base LSN. |
| **last LSN** | The LSN of the youngest record in a stream that is still needed by the stream's clients. Typically this is the record that was most recently written to the stream, but clients have the option of manually setting the last LSN to point to some earlier record in the stream. Manually setting the last LSN to an earlier record is called *truncating* the stream. |
| **archive tail** | The LSN of the oldest record in a log for which archiving has not taken place. Not every log has an archive tail. A log that does not have an archive tail is called *ephemeral*, and a log that has an archive tail is called *non-ephemeral*. When a client specifies that a log has an archive tail, the client is responsible for updating the archive tail. |
| **active portion of a stream** | The portion of a stream that is currently in use by its clients. The active portion begins with the record pointed to by the base LSN or the archive tail, whichever is smaller. The active portion ends with the record pointed to by the last LSN. |
| **authentication codes** | Hash-bashed hash authentication codes (HMAC) that are used to ensure CLFS is the author and writer of CLFS files. |
