---
title: Callback Objects
description: Callback Objects
ms.assetid: d6ccb064-5936-4996-a5cd-795803958b5d
keywords: ["synchronization WDK kernel , callback objects", "callback objects WDK kernel", "objects WDK callback objects", "kernel callback mechanism WDK"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Callback Objects





The kernel's callback mechanism provides a general way for drivers to request and provide notification when certain conditions are satisfied.

A driver can create a callback object, and other drivers can request notification for conditions associated with this driver-defined callback. In addition, the system defines two callback objects for driver use.

Every callback object has a name and a set of attributes, defined when the object is created. The system-defined callback objects are named **\\Callback\\SetSystemTime**, **\\Callback\\PowerState**, and **\\Callback\\ProcessorAdd**; driver-defined callbacks must not duplicate these names.

To request notification from a system- or driver-defined callback, a driver opens the callback object and registers a callback routine. When the conditions defined for the callback become true, its creator triggers notification. In turn, the system calls all the callback routines registered for the callback.

This section contains the following topics:

[Defining a Callback Object](defining-a-callback-object.md)

[Using a Driver-Defined Callback Object](using-a-driver-defined-callback-object.md)

[Using a System-Defined Callback Object](using-a-system-defined-callback-object.md)

 

 




