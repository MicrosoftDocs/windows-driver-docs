---
title: Using Request Object Context
author: windows-driver-content
description: Using Request Object Context
ms.assetid: befb4a22-0640-45e3-890e-6ff17969b017
keywords:
- request objects WDK KMDF , context space
- context space WDK KMDF
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Request Object Context


## <a href="" id="ddk-using-request-object-context-df"></a>


Every framework request object, whether created by the framework or by a driver, can contain driver-defined context space. When a framework-based driver initializes a framework device object, the driver can call [**WdfDeviceInitSetRequestAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff546786) to specify a [**WDF\_OBJECT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff552400) structure that describes context space for the device's request objects.

The framework allocates context space for request objects as follows:

-   When the framework creates request objects for your driver, it allocates context space with the size that your driver specified when it called **WdfDeviceInitSetRequestAttributes**.

-   If your driver creates additional request objects by calling [**WdfRequestCreate**](https://msdn.microsoft.com/library/windows/hardware/ff549951), you can specify a context size by providing a WDF\_OBJECT\_ATTRIBUTES structure.

For more information about allocating and accessing context space for framework objects, see [Framework Object Context Space](framework-object-context-space.md).

 

 





