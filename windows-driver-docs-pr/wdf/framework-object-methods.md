---
title: Framework Object Methods
description: Framework Object Methods
ms.assetid: f82275c5-15f9-43f5-91bb-b83446526c28
keywords:
- framework objects WDK KMDF , methods
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Object Methods





Each framework object exports a set of methods (functions). Each method serves one of two purposes:

-   It performs an action that is associated with the object.

    For example, the [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) method creates an I/O queue for a device.

    Methods that perform an action typically return an [NTSTATUS value](https://msdn.microsoft.com/library/windows/hardware/ff557697).

-   It retrieves or modifies a [property](framework-object-properties.md) that is associated with the object.

    For example, the [**WdfRequestGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff549965) method returns information about an I/O request's completion status.

    Methods that retrieve a property typically return the property's value, while methods that modify a property typically do not return a value.

Each object method accepts an object handle as input. If a driver passes an invalid object handle to an object method, a system bug check occurs.

 

 





