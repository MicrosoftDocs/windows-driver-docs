---
title: CLFS Terminology
description: The following list gives definitions of key terms used in the Common Log File System (CLFS) documentation.
Robots: noindex, nofollow
ms.assetid: d8511c5a-0181-4c54-acdc-e8a5892bb620
keywords: ["Common Log File System WDK kernel , terminology", "CLFS WDK kernel , terminology"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# CLFS Terminology


The following list gives definitions of key terms used in the Common Log File System (CLFS) documentation. These definitions apply during a discussion of CLFS, but might not apply otherwise. Many of these terms have general meanings or meanings in the context of other technologies that differ from the definitions given here.

<a href="" id="kernel-clfs-term-container"></a>**container**  
A contiguous extent on a physical disk or other stable storage medium. For example, a container could be a contiguous disk file.

<a href="" id="kernel-clfs-term-sector"></a>**sector**  
The unit of atomic I/O on a physical storage medium. The size of a sector is a property of a particular storage device. For example, a hard disk might have a sector size of 512 bytes.

<a href="" id="kernel-clfs-term-log"></a>**log**  
A base file and a set of logically ordered containers. The base file holds metadata for the log, and the containers hold log records. All the containers are the same size.

<a href="" id="kernel-clfs-term-client"></a>**client**  
An application, driver, thread, or other unit of software that uses a CLFS log.

<a href="" id="kernel-clfs-term-record"></a>**record**  
The unit of data that a client can append to or read from a log.

<a href="" id="kernel-clfs-term-stream"></a>**stream**  
An ordered subset of the records in a log. A log can have one or more streams. A client appends records to and reads records from a particular stream. You can compare the records in a given stream to determine the order in which they were written. You cannot compare records in different streams. A given stream can have several clients. For example, several threads could append records to a single stream. To a client, a stream appears as if it were the entire log.

<a href="" id="kernel-clfs-term-dedicated-log"></a>**dedicated log**  
A log that can have only one stream.

<a href="" id="kernel-clfs-term-multiplexed-log"></a>**multiplexed log**  
A log that can have several streams.

<a href="" id="kernel-clfs-term-log-i-o-block"></a>**log I/O block**  
A buffer where CLFS collects a set of records that are atomically written to stable storage.

<a href="" id="kernel-clfs-term-marshalling-area"></a>**marshalling area**  
A set of log I/O blocks, created, maintained, and scheduled by a CLFS client for gathering log records and writing them to stable storage. The log I/O blocks allocated in volatile memory for a particular marshalling area are all the same size.

**Note**   Even though all the log I/O blocks (in volatile memory) for a particular marshalling area are the same size, the log I/O blocks that are written to stable storage (from that marshalling area) vary in size. For example, if a log I/O block is forced to stable storage before it is full, only the used portion of the block will be written to stable storage.

 

<a href="" id="kernel-clfs-term-log-sequence-number--lsn"></a>**log sequence number (LSN)**  
An opaque structure that holds a value that uniquely identifies a log record in a given stream. When a client writes a record to a stream, it gets back an LSN that it can use to identify the record in the future. The LSNs that CLFS assigns to the records in a stream form an increasing sequence. That is, the LSN assigned to a record in a stream is always greater than the LSN assigned to the record previously written to that same stream.

**Note**   Records across streams are not comparable. That is, you cannot compare the LSNs of two records in different streams to determine which record was written first.

 

<a href="" id="kernel-clfs-term-base-lsn"></a>**base LSN**  
The LSN of the oldest record in a stream that is still needed by the stream's clients. The clients are responsible for updating the base LSN.

<a href="" id="kernel-clfs-term-last-lsn"></a>**last LSN**  
The LSN of the youngest record in a stream that is still needed by the stream's clients. Typically this is the record that was most recently written to the stream, but clients have the option of manually setting the last LSN to point to some earlier record in the stream. Manually setting the last LSN to an earlier record is called *truncating* the stream.

<a href="" id="kernel-clfs-term-archive-tail"></a>**archive tail**  
The LSN of the oldest record in a log for which archiving has not taken place. Not every log has an archive tail. A log that does not have an archive tail is called *ephemeral*, and a log that has an archive tail is called *non-ephemeral*. When a client specifies that a log has an archive tail, the client is responsible for updating the archive tail.

<a href="" id="kernel-clfs-term-active-portion-of-a-stream"></a>**active portion of a stream**  
The portion of a stream that is currently in use by its clients. The active portion begins with the record pointed to by the base LSN or the archive tail, whichever is smaller. The active portion ends with the record pointed to by the last LSN.

 

 




