---
title: About Storport miniport drivers
description: Storport Miniport Drivers
keywords:
- Storport miniport drivers WDK
- Storport miniport drivers WDK , routines listed
- storage miniport drivers WDK , Storport miniport drivers
- miniport drivers WDK storage , Storport miniport drivers
ms.date: 06/08/2023
---

# About Storport miniport drivers

A Storport miniport driver is a vendor-supplied module that works with the system-supplied [Storport driver](storport-driver-overview.md) to support that vendor's storage device on Windows. A Storport driver is more efficient and higher performing than a SCSI port driver and is the recommended model for vendors.

Storport miniport drivers are typically implemented as dynamic-link libraries (DLLs) that the Storport driver loads. The Storport driver calls routines in the miniport driver to perform operations on the storage device. The Storport miniport driver is responsible for managing the hardware and for implementing the routines that the Storport driver calls.

The following articles provide information about how to implement a Storport miniport driver:

* [Storport miniport driver routines](storport-miniport-driver-routines.md) lists the routines that a Storport miniport driver implements.

* [Storport driver support routines](storport-driver-support-routines.md) lists many of the routines that the Storport driver provides to support Storport miniport drivers.

For more Storport miniport driver implementation information, see the subtopics of this article.
