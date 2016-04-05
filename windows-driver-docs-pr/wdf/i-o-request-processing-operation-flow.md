---
title: I/O Request Processing Operation Flow
description: I/O Request Processing Operation Flow
ms.assetid: 3a7162d2-0a8c-4748-b320-bfe64ec93c9d
keywords: ["operation flow WDK UMDF", "I/O requests WDK UMDF , operation flow", "request processing WDK UMDF , operation flow"]
---

# I/O Request Processing Operation Flow


\[This topic applies to UMDF 1.*x*.\]

All I/O operations occur in the context of a file object (that is, all I/O operations occur between calls that an application makes to the Microsoft Win32 [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) and **CloseHandle** functions). I/O operations are calls that an application makes to, for example, the Win32 **ReadFileEx**, **WriteFileEx**, and [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) functions.

The following topics show the flow of operations that occur to and from UMDF drivers as a user I/O transaction begins, processes, and ends in a single device stack and in a double device stack:

-   [Operation Flow with Single Device Stack](operation-flow-with-single-device-stack.md)

-   [Operation Flow with Double Device Stack](operation-flow-with-double-device-stack.md)

**Note**   All I/O that is initiated by applications is routed through kernel mode as shown in the figures in the [Architecture of the UMDF](https://msdn.microsoft.com/library/windows/hardware/ff554461) section, even though the figures in the I/O Request Processing Operation Flow section do not show this situation.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20I/O%20Request%20Processing%20Operation%20Flow%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




