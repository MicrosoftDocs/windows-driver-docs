---
title: UMDF Objects and Interfaces
description: UMDF Objects and Interfaces
keywords:
- User-Mode Driver Framework WDK , objects
- user-mode drivers WDK UMDF , objects
- objects WDK UMDF
- UMDF objects WDK
- interfaces WDK UMDF
- framework objects WDK UMDF
ms.date: 04/20/2017
---

# UMDF Objects and Interfaces


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The User-Mode Driver Framework (UMDF) is composed of a set of cooperating objects. The UMDF creates and manages a series of objects exposed to the user-mode device driver. Some of theses objects are created by the UMDF in response to application-triggered actions, such as an I/O request, while other UMDF objects are created when the driver calls UMDF interface methods. For example, to create an I/O queue object, the driver calls the [**IWDFDevice::CreateIoQueue**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createioqueue) method.

The following topics describe the core framework objects, the subset of the Component Object Model (COM) on which they are based, and the UMDF DDI programming model:

-   [Framework Objects](framework-objects.md)
-   [Framework Object Hierarchy](framework-object-hierarchy.md)
-   [UMDF Based on COM Subset](umdf-based-on-com-subset.md)
-   [UMDF DDI Programming Model](umdf-ddi-programming-model.md)
-   [Managing the Lifetime of Objects](managing-the-lifetime-of-objects.md)

 

