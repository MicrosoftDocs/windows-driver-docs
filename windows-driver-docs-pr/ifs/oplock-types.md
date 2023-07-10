---
title: Types of oplocks
description: Describes the different types of oplocks
ms.date: 07/07/2023
---

# Types of oplocks

This article describes the types of [oplocks](oplock-overview.md).

* Four oplock types are current.
* Four oplock types are considered legacy.

## Legacy oplocks

The following four oplocks were implemented in Windows NT 3.1 (Level 1, Level 2, Batch) and Windows 2000 (Filter), and are considered "legacy oplocks":

* A **Level 1** (exclusive) oplock allows a client to open a stream for exclusive access and to perform arbitrary buffering. This oplock supports client read caching and write caching.

* A **Level 2** (shared) oplock indicates that there are multiple readers of a stream and no writers. This oplock supports client read caching.

* A **Batch** oplock (exclusive) allows a client to keep a stream open on the server even though the local accessor on the client machine has closed the stream. This oplock supports scenarios where the client needs to repeatedly open and close the same file, such as during batch script execution. It supports client read caching, write caching, and handle caching.

* A **Filter** oplock (exclusive) allows applications and file system filter drivers that open and read stream data a way to "back out" when other applications, clients, or both try to access the same stream. This oplock supports client read caching and write caching.

## Current "Windows 7" oplocks

The following oplocks were added in Windows 7, and so are collectively known as "Windows 7 oplocks":

* A **Read** (R) oplock (shared) indicates that there are multiple readers of a stream and no writers. This oplock supports client read caching.

* A **Read-Handle** (RH) oplock (shared) indicates that there are multiple readers of a stream, no writers, and that a client can keep a stream open on the server even though the local accessor on the client machine has closed the stream. This oplock supports client read caching and handle caching.

* A **Read-Write** (RW) oplock (exclusive) allows a client to open a stream for exclusive access and allows the client to perform arbitrary buffering. This oplock supports client read caching and write caching.

* A **Read-Write-Handle** (RWH) oplock (exclusive) allows a client to keep a stream open on the server even though the local accessor on the client machine has closed the stream. This oplock supports client read caching, write caching, and handle caching.

Some legacy oplocks might seem similar to Windows 7 oplocks. In particular, R seems similar to Level 2, RW seems similar to Level 1, and RWH seems similar to Batch. But they're indeed different. The Windows 7 oplocks were added to:

* Provide greater flexibility for the caller to express caching intentions.
* Allow oplock breaks and upgrades; that is, to allow modification of the oplock state from one level to a level of greater caching (for example, upgrading a Read oplock to a Read-Write oplock).

This flexibility isn't achievable with the legacy oplocks.
