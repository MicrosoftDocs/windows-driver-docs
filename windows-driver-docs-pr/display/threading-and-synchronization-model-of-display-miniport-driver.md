---
title: Threading and Sync Model of Display Miniport Driver
description: Threading and Synchronization Model of Display Miniport Driver
keywords:
- threading WDK display , miniport drivers
- synchronization WDK display , miniport drivers
- miniport drivers WDK display , synchronization
- miniport drivers WDK display , threading
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# Threading and Synchronization Model of Display Miniport Driver

Multiple threads can be present within the display miniport driver at the same time. That is, in general, the display miniport driver is reentrant. However, some calls into the display miniport driver should not be reentrant because they either access graphics hardware or access global cross-thread data structures. Although reentrancy or nonreentrancy cannot be selected at a per-call level, the Windows Display Driver Model (WDDM) pre-assigns, per call, the following synchronization levels that define precisely what the driver should expect for the call:

-   [Threading and Synchronization Third Level](threading-and-synchronization-third-level.md)

-   [Threading and Synchronization Second Level](threading-and-synchronization-second-level.md)

-   [Threading and Synchronization First Level](threading-and-synchronization-first-level.md)

-   [Threading and Synchronization Zero Level](threading-and-synchronization-zero-level.md)

-   [Thread Synchronization and TDR](thread-synchronization-and-tdr.md)

 

 





