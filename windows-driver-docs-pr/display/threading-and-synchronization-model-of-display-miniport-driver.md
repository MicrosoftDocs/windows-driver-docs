---
title: Threading and Sync Model of Display Miniport Driver
description: Threading and Synchronization Model of Display Miniport Driver
keywords:
- threading WDK display , miniport drivers
- synchronization WDK display , miniport drivers
- miniport drivers WDK display , synchronization
- miniport drivers WDK display , threading
ms.date: 10/03/2023
---

# Threading and Synchronization Model of Display Miniport Driver

In general, the display miniport driver (KMD) is reentrant. That is, multiple threads can be present within a KMD at the same time. However, some calls into the KMD shouldn't be reentrant because they either access graphics hardware or access global cross-thread data structures.

Although reentrancy or nonreentrancy can't be selected at a per-call level, WDDM pre-assigns, per call, synchronization levels that define precisely what the driver should expect for the call. These synchronization levels are as follows:

* [Threading and Synchronization Level Three](threading-and-synchronization-third-level.md)

* [Threading and Synchronization Level Two](threading-and-synchronization-second-level.md)

* [Threading and Synchronization Level One](threading-and-synchronization-first-level.md)

* [Threading and Synchronization Level Zero](threading-and-synchronization-zero-level.md)

* [Thread Synchronization and TDR](thread-synchronization-and-tdr.md)
