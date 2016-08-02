---
title: IRP\_MJ\_FILE\_SYSTEM\_CONTROL
author: windows-driver-content
description: IRP\_MJ\_FILE\_SYSTEM\_CONTROL
ms.assetid: 3651d9ed-6b6f-4b60-9dfa-1c5c0c78b1a1
---

# IRP\_MJ\_FILE\_SYSTEM\_CONTROL


The FSCTL\_SET\_ZERO\_DATA file system control code operation checks oplock state:

**FSCTL\_SET\_ZERO\_DATA**

This information applies when a caller wants to zero the current contents of the given stream.

Request Type
Conditions
Level 1

Batch

Filter

Read-Handle

Read-Write

Read-Write-Handle

Broken on IRP\_MJ\_FILE\_SYSTEM\_CONTROL (for FSCTL\_SET\_ZERO\_DATA) when:

-   The operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to None.

-   For the Read-Handle request: Although acknowledgment of the break is required, the operation continues immediately (for example, without waiting for the acknowledgment).

-   For all other request types: An acknowledgment must be received before the operation continues.

Read

Broken on IRP\_MJ\_FILE\_SYSTEM\_CONTROL (for FSCTL\_SET\_ZERO\_DATA) when:

-   The operation occurs on a FILE\_OBJECT with a different oplock key from the FILE\_OBJECT which owns the oplock.

If the oplock is broken:

-   Break to None.

-   No acknowledgment is required, the operation proceeds immediately.

Level 2

-   Always break to None.

-   No acknowledgment is required, the operation proceeds immediately.

 

 

 


--------------------


