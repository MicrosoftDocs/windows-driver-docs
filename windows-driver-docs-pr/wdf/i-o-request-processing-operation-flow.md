---
title: I/O Request Processing Operation Flow
description: I/O Request Processing Operation Flow
ms.assetid: 3a7162d2-0a8c-4748-b320-bfe64ec93c9d
keywords:
- operation flow WDK UMDF
- I/O requests WDK UMDF , operation flow
- request processing WDK UMDF , operation flow
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# I/O Request Processing Operation Flow


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

All I/O operations occur in the context of a file object (that is, all I/O operations occur between calls that an application makes to the Microsoft Win32 [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) and **CloseHandle** functions). I/O operations are calls that an application makes to, for example, the Win32 **ReadFileEx**, **WriteFileEx**, and [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) functions.

The following topics show the flow of operations that occur to and from UMDF drivers as a user I/O transaction begins, processes, and ends in a single device stack and in a double device stack:

-   [Operation Flow with Single Device Stack](operation-flow-with-single-device-stack.md)

-   [Operation Flow with Double Device Stack](operation-flow-with-double-device-stack.md)

**Note**   All I/O that is initiated by applications is routed through kernel mode as shown in the figures in the [Architecture of the UMDF](https://msdn.microsoft.com/library/windows/hardware/ff554461) section, even though the figures in the I/O Request Processing Operation Flow section do not show this situation.

 

 

 





