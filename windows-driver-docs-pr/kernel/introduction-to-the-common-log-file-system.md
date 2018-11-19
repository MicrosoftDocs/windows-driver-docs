---
title: Introduction to the Common Log File System
description: Introduction to the Common Log File System
ms.assetid: 2185d834-81f3-4bf9-afa6-897c1515f8b5
keywords: ["Common Log File System WDK kernel , about Common Log File System", "CLFS WDK kernel , about Common Log File System", "logging service WDK CLFS", "Common Log File System WDK user-mode", "CLFS WDK user-mode", "logs WDK CLFS", "multiplexed logs WDK CLFS", "dedicated logs WDK CLFS", "log sequence numbers WDK CLFS", "LSNs WDK CLFS"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to the Common Log File System





The Common Log File System (CLFS) is a general-purpose logging service that can be used by software [*clients*](clfs-terminology.md#kernel-clfs-term-client) running in user-mode or kernel-mode. This documentation discusses the CLFS interface for kernel-mode clients. For information about the user-mode interface, see Common Log File System in the Microsoft Windows SDK.

CLFS encapsulates all the functionality of the Algorithm for Recovery and Isolation Exploiting Semantics (ARIES). However, the CLFS device driver interface (DDI) is not limited to supporting ARIES; it is well suited to a variety of logging scenarios.

The primary job of any high-performance transactional log is to allow log clients to accurately repeat history. CLFS does this by marshalling client log records into memory buffers, forcing them to stable storage, and reading records back on request. It is important to note that after a record makes it to stable storage and the storage media is intact, CLFS will be able to read the record across system failures.

CLFS supports dedicated logs and multiplexed logs. A dedicated log has a single [*stream*](clfs-terminology.md#kernel-clfs-term-stream) of log records that is used by all of the log's clients. A multiplexed log (also called a common log) has several streams. Each stream has its own clients and its own memory buffers for marshalling log records, but the records from all those buffers are multiplexed into a single queue and flushed to a single log on stable storage. Multiplexing allows the I/O operations of several streams to be consolidated.

When a client writes a record to a stream, it gets back a log sequence number (LSN) that identifies the log record for future reference. The LSNs assigned to the records that are written to a particular stream form an increasing sequence. That is, the LSN assigned to a record that is written to a stream is always greater than the LSN assigned to the previous record written to that same stream.

CLFS provides several services in addition to marshalling, flushing, and retrieving log records. The following list describes some of those additional services.

-   Space for a set of related log records can be reserved ahead of time. This means that a client can proceed with a transaction knowing that CLFS will be able to append to the log all of the records that describe the transaction.

-   CLFS maintains a header for each log record. Clients can set certain fields in the header to create chains of linked records that you can later traverse in reverse order.

-   CLFS flushes log records to stable storage according to its policy, but also allows clients to force a set of log records to stable storage.

-   CLFS maintains metadata for a log and also for each stream of a multiplexed log. Clients can view metadata and set certain portions of the metadata.

-   For each stream, CLFS maintains a base LSN and a last LSN that a client can use to delineate the active portion of the stream.

-   For dedicated logs, CLFS maintains (at the client's request) an archive tail that the client can use to keep track of the portion of the log that has been archived.

Certain features of CLFS (for example, the previous LSN and undo-next LSN fields of a record header) can be best understood by studying ARIES. For more information about ARIES, see the following papers.

-   C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh, Peter Schwarz, *ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging*.

-   C. Mohan, *Repeating History Beyond ARIES*.

 

 




