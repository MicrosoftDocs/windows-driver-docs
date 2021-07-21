---
title: Checking the Oplock State of an IRP_MJ_READ operation
description: Checking the Oplock State of an IRP_MJ_READ operation
ms.date: 11/25/2019
ms.localizationpriority: medium
---

# Checking the Oplock State of an IRP_MJ_READ operation

The following [oplock break](./breaking-oplocks.md) conditions apply when a *stream* is being read. If a TxF transacted reader performs the read, this check is not made since a transacted reader excludes a writer (that is, a writer holding an oplock cannot be present at all).

### Conditions for Level 2, Filter, Read, and Read-Handle request types

- The oplock is not broken.

- No acknowledgment is required, and the operation proceeds immediately.

### Conditions for Level 1, Batch, Read-Write, and Read-Write-Handle request types

- Break on IRP_MJ_READ when the read operation occurs on a FILE_OBJECT with an oplock key that differs from the key of the FILE_OBJECT that owns the oplock. If the oplock is broken:

  - Level 1 and Batch requests break to Level 2.

  - Read-Write requests break to Read.

  - Read-Write-Handle requests break to Read-Handle.

- An acknowledgment must be received before the operation continues.
