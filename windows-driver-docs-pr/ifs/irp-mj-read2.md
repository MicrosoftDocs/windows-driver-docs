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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP_MJ_READ%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


