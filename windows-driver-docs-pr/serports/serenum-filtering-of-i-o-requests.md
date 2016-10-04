---
title: Serenum Filtering of I/O Requests
author: windows-driver-content
description: Serenum Filtering of I/O Requests
MS-HAID:
- 'sseovr\_2ab60ed7-248a-457d-a03d-43650056b99c.xml'
- 'serports.serenum\_filtering\_of\_i\_o\_requests'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 773688b8-3d5a-48ed-8f20-368cf35fa6e2
keywords: ["Serenum driver WDK , I/O request filtering", "I/O request filtering WDK Serenum", "filtering I/O requests WDK serial devices"]
---

# Serenum Filtering of I/O Requests


## <a href="" id="ddk-serenum-filtering-of-i-o-requests-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Serenum%20Filtering%20of%20I/O%20Requests%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


