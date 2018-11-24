---
title: Event Objects
description: Event Objects
ms.assetid: da9df4a2-26cf-4861-80ca-1790ca059e45
keywords: ["kernel dispatcher objects WDK , event objects", "dispatcher objects WDK kernel , event objects", "event objects WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Event Objects





A driver can use an event object to wait while the next-lower driver processes an IRP set up by the waiting driver. Drivers that have driver-created threads or driver dispatch routines that wait for the completion of a synchronous I/O request also can use an event object to synchronize operations between their threads and/or other driver routines.

This section contains the following topics:

[Defining and Using an Event Object](defining-and-using-an-event-object.md)

[Standard Event Objects](standard-event-objects.md)

 

 




