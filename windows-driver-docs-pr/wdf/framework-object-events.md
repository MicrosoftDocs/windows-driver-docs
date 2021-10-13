---
title: Framework Object Events
description: Framework Object Events
keywords:
- framework objects WDK KMDF , events
- events WDK KMDF
- events WDK KMDF , framework objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Object Events





Some framework objects can generate events. Framework-based drivers can register to receive notification of all, some, or none of an object's events. To register for an event, the driver provides an event callback function. The framework calls the callback function when the event occurs.

For example, a driver can register an [*EvtIoDefault*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_default) callback function for an I/O queue. The framework will call this callback function each time the framework is ready to remove an I/O request from the I/O queue and deliver it to the driver.

 

