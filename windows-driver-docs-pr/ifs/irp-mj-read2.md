---
title: IRP\_MJ\_READ
author: windows-driver-content
description: IRP\_MJ\_READ
ms.assetid: 9b4d1ba9-0838-44f1-8328-f60bfb3910ee
---

# IRP\_MJ\_READ


The following only applies when a *stream* is being read. If a TxF transacted reader performs the read, this check is not made since a transacted reader excludes a writer (that is, a writer holding an oplock cannot be present at all).

Request Type
Conditions
Level 1

Batch

Broken on IRP\_MJ\_READ when:

-   The read operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to Level 2.

-   An acknowledgment must be received before the operation continues.

Read-Write

Broken on IRP\_MJ\_READ when:

-   The read operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to Read.

-   An acknowledgment must be received before the operation continues.

Read-Write-Handle

Broken on IRP\_MJ\_READ when:

-   The read operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to Read-Handle.

-   An acknowledgment must be received before the operation continues.

Level 2

Filter

Read

Read-Handle

-   The oplock is not broken, no acknowledgment is required, and the operation proceeds immediately.

 

 

 


--------------------


