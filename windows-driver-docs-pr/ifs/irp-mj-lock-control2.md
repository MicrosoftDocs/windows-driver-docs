---
title: IRP\_MJ\_LOCK\_CONTROL
author: windows-driver-content
description: IRP\_MJ\_LOCK\_CONTROL
ms.assetid: 6e0a5287-9a22-465f-b345-c9af556e6cdb
---

# IRP\_MJ\_LOCK\_CONTROL


The following applies on every byte range lock operation on the given stream.

Request Type
Conditions
Level 1

Batch

Read-Handle

Read-Write

Read-Write-Handle

Broken on IRP\_MJ\_LOCK\_CONTROL when:

-   The lock operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to None.

-   For the Handle request: Although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).

-   For all other request types: An acknowledgment must be received before the operation continues.

Read

Broken on IIRP\_MJ\_LOCK\_CONTROL when:

-   The lock operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to None.

-   No acknowledgment is required, the operation proceeds immediately.

Filter

-   The oplock is not broken, no acknowledgment is required, and the operation proceeds immediately.

Level 2

-   Always break to None.

-   No acknowledgment is required, the operation proceeds immediately.

 

 

 


--------------------


