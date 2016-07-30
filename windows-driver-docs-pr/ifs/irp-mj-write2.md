---
title: IRP\_MJ\_WRITE
author: windows-driver-content
description: IRP\_MJ\_WRITE
ms.assetid: 04d09810-f157-4140-8bfb-c780a65cdf77
---

# IRP\_MJ\_WRITE


The following only applies when a *stream* is being written and the write is not a paging I/O.

Request Type
Conditions
Level 1

Batch

Filter

Read-Handle

Read-Write

Read-Write-Handle

Broken on IRP\_MJ\_WRITE when:

-   The write operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to None.

-   For the Read-Handle request: Although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).

-   For all other request types: An acknowledgment must be received before the operation continues.

Read

Broken on IRP\_MJ\_WRITE when:

-   The write operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to None.

-   No acknowledgment is required, the operation proceeds immediately.

Level 2

-   Always break to None.

-   No acknowledgment is required, the operation proceeds immediately.

 

 

 


--------------------


