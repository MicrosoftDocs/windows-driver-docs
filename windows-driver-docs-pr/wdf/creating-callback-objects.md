---
title: Creating Callback Objects
description: Creating Callback Objects
ms.assetid: bbae1458-911f-4a48-8bf2-0997e8f98826
keywords:
- callback objects WDK UMDF
- callback objects WDK UMDF , creating
- User-Mode Driver Framework WDK , objects
- user-mode drivers WDK UMDF , objects
- UMDF objects WDK , callback objects
- framework objects WDK UMDF , callback objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Callback Objects


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

A UMDF driver can create *callback objects*, which consist of context data and interface methods. The framework accesses the driver's callback objects through the driver's callback interface methods.

The following figure shows how driver-implemented callback objects correspond to [framework objects](framework-objects.md).

![framework objects and vendor-supplied callback objects](images/correspond.gif)

A UMDF driver can create several types of callback objects, including the following:

-   Driver callback object

    The framework uses the driver callback object to initialize the driver and notify the driver of the arrival of a new device.

-   Device callback object

    The driver uses the device callback object to store device context and to handle the cleanup and closing of file objects and Plug and Play (PnP) and power management (PM) events.

-   Queue callback object

    The driver uses the queue callback object to process I/O.

The following figure shows how a UMDF driver creates a device callback object.

![call sequence for creating a umdf device callback object](images/callback.gif)

The following topics contain code examples that show how to create a callback object:

-   [Creating Callback Objects Example](creating-callback-objects-example.md)

-   [Defining Callback Objects Example](defining-callback-objects-example.md)

-   [Associating Callback Interfaces Example](associating-callback-interfaces-example.md)

 

 





