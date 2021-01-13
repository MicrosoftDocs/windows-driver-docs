---
title: Framework Request Objects
description: Framework Request Objects
keywords:
- I/O requests WDK KMDF , request objects
- request objects WDK KMDF
- request processing WDK KMDF , request objects
- framework objects WDK KMDF , I/O request objects
- request objects WDK KMDF , about request objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Request Objects





Framework request objects represent I/O requests that the I/O manager has sent to a driver. Framework-based drivers process each I/O request by calling [framework request object methods](/windows-hardware/drivers/ddi/wdfrequest/).

Each I/O request contains a WDM *I/O request packet* ([**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp) structure), but framework-based drivers typically do not need to access the IRP structure.

## In this section


-   [Creating Framework Request Objects](creating-framework-request-objects.md)
-   [Using Request Object Context](using-request-object-context.md)
-   [Request Ownership](request-ownership.md)
-   [Processing I/O Requests](processing-i-o-requests.md)
-   [Obtaining Information About an I/O Request](obtaining-information-about-an-i-o-request.md)
-   [Accessing Data Buffers in WDF Drivers (KMDF or UMDF)](accessing-data-buffers-in-wdf-drivers.md)
-   [Managing Buffer Access Methods in UMDF Drivers](managing-buffer-access-methods-in-umdf-drivers.md)
-   [Reusing Framework Request Objects](reusing-framework-request-objects.md)

 

