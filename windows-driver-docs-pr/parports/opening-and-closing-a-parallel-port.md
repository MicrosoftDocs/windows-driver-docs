---
title: Opening and Closing a Parallel Port
author: windows-driver-content
description: Opening and Closing a Parallel Port
MS-HAID:
- 'vspd\_30166531-5586-4e06-98be-b7e7e3f6489f.xml'
- 'parports.opening\_and\_closing\_a\_parallel\_port'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2183ffd9-8265-4848-b5d1-703643e0d0e6
keywords: ["parallel ports WDK , opening", "parallel ports WDK , closing", "parallel ports WDK , sharing"]
---

# Opening and Closing a Parallel Port


## <a href="" id="ddk-opening-and-closing-a-parallel-port-kg"></a>


Clients can share a parallel port. A client must open a file on a parallel port before the client can use other I/O requests or use the [parallel port callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544307). A client must not attempt to communicate with a parallel port after the client has closed its file on the port.

Note that in a Plug and Play environment, a device can be removed or added whenever there are no open files on it. In general, every time a parallel port is added, Plug and Play assigns a different location and resources.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Opening%20and%20Closing%20a%20Parallel%20Port%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


