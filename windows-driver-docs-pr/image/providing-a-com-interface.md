---
title: Providing a COM Interface
description: Providing a COM Interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Providing a COM Interface





A WIA minidriver must support the **IWiaMiniDrv**, **IStiUSD**, and **IUnknown** interfaces to be recognized and loaded by the WIA service. The following interface identifiers should be added to the WIA driver's **QueryInterface** method:

-   **IID\_IWiaMiniDrv** - the interface identifier for the [IWiaMiniDrv interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv), a standard WIA interface used to access WIA-specific functionality.

-   **IID\_IStiUSD** - the interface identifier for the [IStiUSD interface](/windows-hardware/drivers/ddi/_image/index), a standard STI interface used to access the STI functionality of the WIA driver

-   **IID\_IUnknown** - the interface identifier for the **IUnknown** interface, a standard COM interface defined in the Microsoft Windows SDK documentation.

The minidriver exports these interface identifiers in response to the WIA service calling the minidriver's **QueryInterface** method.

For examples of how these interfaces are implemented, see the *wiascanr* scanner sample minidriver files *wiascanr.h*, *iwiaminidrv.cpp* and *istiusd.cpp or s*ee the *wiacam* camera sample minidriver files *IWiaMiniDrv.cpp* and *IStiUSD.cpp*.

 

