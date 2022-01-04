---
title: Checking the Oplock State of IRP_MJ_FILE_SYSTEM_CONTROL
description: Checking the Oplock State of an IRP_MJ_FILE_SYSTEM_CONTROL operation
ms.date: 11/25/2019
---

# Checking the Oplock State of IRP_MJ_FILE_SYSTEM_CONTROL

The following IRP_MJ_FILE_SYSTEM_CONTROL operations check oplock state:

- **FSCTL_SET_ZERO_DATA**

This information applies when a caller wants to zero the current contents of the given stream.

### Conditions for a Level 2 request type:

- Always break to None.

- No acknowledgment is required; the operation proceeds immediately.

### Conditions for all other request types:

- Break on IRP_MJ_FILE_SYSTEM_CONTROL (for FSCTL_SET_ZERO_DATA) when the operation occurs on a FILE_OBJECT with an oplock key that differs from the key of the FILE_OBJECT that owns the oplock. If the oplock is broken, break to None.

- Acknowledgment requirements vary as follows:

  - Read request: No acknowledgment is required; the operation proceeds immediately.
  
  - Read-Handle request: Although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).
  
  - Level 1, Batch, Filter, Read-Write, and Read-Write-Handle requests: An acknowledgment must be received before the operation continues.
