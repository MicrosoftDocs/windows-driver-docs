---
title: Checking the Oplock State of an IRP_MJ_LOCK_CONTROL operation
description: Checking the Oplock State of an IRP_MJ_LOCK_CONTROL operation
ms.date: 11/25/2019
ms.localizationpriority: medium
---

# Checking the Oplock State of an IRP_MJ_LOCK_CONTROL operation

The following [oplock break](./breaking-oplocks.md) conditions apply on every byte range lock operation on the given stream.

### Conditions for a Level 2 request type

- Always break to None.

- No acknowledgment is required; the operation proceeds immediately.

### Conditions for a Filter request type

- The oplock is not broken.

- No acknowledgement is required, and the operation proceeds immediately.

### Conditions for Level 1, Batch, Read, Read-Handle, Read-Write, and Read-Write-Handle request types

- Break on IRP_MJ_LOCK_CONTROL when the lock operation occurs on a FILE_OBJECT with an oplock key that differs from the key of the FILE_OBJECT that owns the oplock. If the oplock is broken, break to None.

- Acknowledgement requirements vary as follows:

  - Read request: No acknowledgment is required; the operation proceeds immediately.

  - Read-Handle and Read-Write-Handle requests: Although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).

  - Level 1, Batch, and Read-Write requests: An acknowledgement must be received before the operations continues.
