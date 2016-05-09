---
title: IRP\_MJ\_WRITE
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP_MJ_WRITE%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




