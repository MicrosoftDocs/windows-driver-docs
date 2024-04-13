---
title: PTP Events
description: PTP Events
ms.date: 04/20/2017
---

# PTP Events





When an object is added or removed, including in response to the **StoreAdded** or **StoreRemoved** events (described in the PIMA 15740 standard), a WIA event is triggered. The WIA\_EVENT\_ITEM\_CREATED event is fired when an object is added, and the WIA\_EVENT\_ITEM\_DELETED event is fired when an object is removed. (See the Microsoft Windows SDK documentation for a description of these and other WIA event identifiers.) The PTP driver uses the other PTP events to update internal structures, but these events are not reported to applications. Note that the PTP driver monitors for events only while an application has the device open.

 

 




