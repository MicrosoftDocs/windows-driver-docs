---
title: Checking the Oplock State of an IRP_MJ_WRITE operation
description: Checking the Oplock State of an IRP_MJ_WRITE operation
ms.date: 11/25/2019
---

# Checking the Oplock State of an IRP_MJ_WRITE operation

The following [oplock break](./breaking-oplocks.md) conditions apply when a *stream* is being written and the write is not a paging I/O.

### Conditions for a Level 2 request type:

- Always break to None.

- No acknowledgment is required; the operation proceeds immediately.

### Conditions for all other request types:

- Break on IRP_MJ_WRITE when the write operation occurs on a FILE_OBJECT with an oplock key that differs from the key of the FILE_OBJECT that owns the oplock. If the oplock is broken, break to None.

- Acknowledgment requirements vary as follows:

  - Read request: No acknowledgment is required; the operation proceeds immediately.
  
  - Read-Handle request: Although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).
  
  - Level 1, Batch, Filter, Read-Write, and Read-Write-Handle requests: An acknowledgment must be received before the operation continues.
