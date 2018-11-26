---
title: Providing a COM Interface
description: Providing a COM Interface
ms.assetid: c3e1578e-26f1-4fe3-b56d-a2baacb8e4c0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing a COM Interface





A WIA minidriver must support the **IWiaMiniDrv**, **IStiUSD**, and **IUnknown** interfaces to be recognized and loaded by the WIA service. The following interface identifiers should be added to the WIA driver's **QueryInterface** method:

-   **IID\_IWiaMiniDrv** - the interface identifier for the [IWiaMiniDrv interface](https://msdn.microsoft.com/library/windows/hardware/ff545027), a standard WIA interface used to access WIA-specific functionality.

-   **IID\_IStiUSD** - the interface identifier for the [IStiUSD interface](https://msdn.microsoft.com/library/windows/hardware/ff543827), a standard STI interface used to access the STI functionality of the WIA driver

-   **IID\_IUnknown** - the interface identifier for the **IUnknown** interface, a standard COM interface defined in the Microsoft Windows SDK documentation.

The minidriver exports these interface identifiers in response to the WIA service calling the minidriver's **QueryInterface** method.

For examples of how these interfaces are implemented, see the *wiascanr* scanner sample minidriver files *wiascanr.h*, *iwiaminidrv.cpp* and *istiusd.cpp or s*ee the *wiacam* camera sample minidriver files *IWiaMiniDrv.cpp* and *IStiUSD.cpp*.

 

 




