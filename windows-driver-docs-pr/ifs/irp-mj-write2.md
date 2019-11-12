---
title: Checking the Oplock State of an IRP_MJ_WRITE operation
description: Checking the Oplock State of an IRP_MJ_WRITE operation
ms.assetid: 04d09810-f157-4140-8bfb-c780a65cdf77
ms.date: 11/12/2019
ms.localizationpriority: medium
---

# Checking the Oplock State of an IRP_MJ_WRITE operation

The following conditions only apply when a *stream* is being written and the write is not a paging I/O.

- For a **Level 2** oplock type, always break to None. No acknowledgment is required; the operation proceeds immediately.

- All other oplock types are broken on IRP_MJ_WRITE only when the write operation occurs on a FILE_OBJECT with a different oplock key from the FILE_OBJECT that owns the oplock. If the oplock is broken, break to None. Acknowledgment requirements are as follows:

  - **Read** oplock: No acknowledgment is required; the operation proceeds immediately.
  
  - **Read-Handle** oplock: Although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).
  
  - **Level 1**, **Batch**, **Filter**, **Read-Write**, and **Read-Write-Handle** oplocks: An acknowledgment must be received before the operation continues.
