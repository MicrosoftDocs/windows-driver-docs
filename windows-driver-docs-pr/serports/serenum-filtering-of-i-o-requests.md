---
title: Serenum Filtering of I/O Requests
description: Serenum Filtering of I/O Requests
ms.assetid: 773688b8-3d5a-48ed-8f20-368cf35fa6e2
keywords:
- Serenum driver WDK , I/O request filtering
- I/O request filtering WDK Serenum
- filtering I/O requests WDK serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Serenum Filtering of I/O Requests





The following describes how Serenum filters I/O requests that are directed to a filter DO:

-   Handles bus-related operations that are associated with Plug and Play and power requests:
    -   Removes a PDO, if one exists, when the filter DO is removed.
    -   Enumerates the RS-232 port in response to an [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670) request of type **BusRelations**.
-   Completes Serenum-specific device control requests that return information about the RS-232 port.

The following describes how Serenum filters I/O requests that are directed to a PDO (the PDO represents a child device attached to an RS-232 port):

-   Completes all Plug and Play and power requests.

-   Reroutes device control requests to the filter DO associated with the PDO.

-   Completes a Serenum-specific internal device control request that invalidates the bus relations on an RS-232 port.

For more information, see the following:

-   [Serenum Driver Reference](https://msdn.microsoft.com/library/windows/hardware/ff547040)

-   Sample code in the \\src\\kernel\\serenum directory in the Windows Driver Kit (WDK)

 

 




