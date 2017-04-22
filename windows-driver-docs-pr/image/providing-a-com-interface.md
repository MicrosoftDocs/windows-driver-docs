---
title: Providing a COM Interface
author: windows-driver-content
description: Providing a COM Interface
ms.assetid: c3e1578e-26f1-4fe3-b56d-a2baacb8e4c0
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Providing a COM Interface


## <a href="" id="ddk-providing-a-com-interface-si"></a>


A WIA minidriver must support the **IWiaMiniDrv**, **IStiUSD**, and **IUnknown** interfaces to be recognized and loaded by the WIA service. The following interface identifiers should be added to the WIA driver's **QueryInterface** method:

-   **IID\_IWiaMiniDrv** - the interface identifier for the [IWiaMiniDrv interface](https://msdn.microsoft.com/library/windows/hardware/ff545027), a standard WIA interface used to access WIA-specific functionality.

-   **IID\_IStiUSD** - the interface identifier for the [IStiUSD interface](https://msdn.microsoft.com/library/windows/hardware/ff543827), a standard STI interface used to access the STI functionality of the WIA driver

-   **IID\_IUnknown** - the interface identifier for the **IUnknown** interface, a standard COM interface defined in the Microsoft Windows SDK documentation.

The minidriver exports these interface identifiers in response to the WIA service calling the minidriver's **QueryInterface** method.

For examples of how these interfaces are implemented, see the *wiascanr* scanner sample minidriver files *wiascanr.h*, *iwiaminidrv.cpp* and *istiusd.cpp or s*ee the *wiacam* camera sample minidriver files *IWiaMiniDrv.cpp* and *IStiUSD.cpp*.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Providing%20a%20COM%20Interface%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


