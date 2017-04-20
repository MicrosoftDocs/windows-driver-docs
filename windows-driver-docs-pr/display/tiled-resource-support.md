---
title: Tiled resource support
description: Tiled resources can be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.
ms.assetid: 02F3DFB8-2407-412A-B518-9AF4A3E1466A
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Tiled resource support


Tiled resources can be supported by Windows Display Driver Model (WDDM) 1.3 and later drivers. This capability is new starting with Windows 8.1.

These reference topics describe how to implement this capability in your user-mode display driver:

-   [Tiled resource functions implemented by the user-mode driver](https://msdn.microsoft.com/library/windows/hardware/dn458996)

-   [**D3DWDDM1\_3DDI\_CHECK\_MULTISAMPLE\_QUALITY\_LEVELS\_FLAG**](https://msdn.microsoft.com/library/windows/hardware/dn458987)

-   [**D3DWDDM1\_3DDI\_D3D11\_OPTIONS\_DATA1**](https://msdn.microsoft.com/library/windows/hardware/dn475744)

-   [**D3DWDDM1\_3DDI\_DEVICEFUNCS**](https://msdn.microsoft.com/library/windows/hardware/dn458988)

-   [**D3DWDDM1\_3DDI\_TILE\_COPY\_FLAG**](https://msdn.microsoft.com/library/windows/hardware/dn458989)

-   [**D3DWDDM1\_3DDI\_TILE\_MAPPING\_FLAG**](https://msdn.microsoft.com/library/windows/hardware/dn458990)

-   [**D3DWDDM1\_3DDI\_TILE\_RANGE\_FLAG**](https://msdn.microsoft.com/library/windows/hardware/dn458991)

-   [**D3DWDDM1\_3DDI\_TILE\_REGION\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/dn440997)

-   [**D3DWDDM1\_3DDI\_TILED\_RESOURCE\_COORDINATE**](https://msdn.microsoft.com/library/windows/hardware/dn440996)

-   [**D3DWDDM1\_3DDI\_TILED\_RESOURCES\_SUPPORT\_FLAG**](https://msdn.microsoft.com/library/windows/hardware/dn475745)

-   [**D3D10\_2DDICAPS\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff541894)

    (new **D3DWDDM1\_3DDICAPS\_D3D11\_OPTIONS1** constant value)

-   [**D3D10\_DDI\_FILTER**](https://msdn.microsoft.com/library/windows/hardware/ff541952)

    (new **D3DWDDM1\_3DDI\_FILTER\_XXX** constant values)

-   [**D3D10\_DDI\_RESOURCE\_MISC\_FLAG**](https://msdn.microsoft.com/library/windows/hardware/ff542004)

    (new **D3DWDDM1\_3DDI\_RESOURCE\_MISC\_TILED** and **D3DWDDM1\_3DDI\_RESOURCE\_MISC\_TILE\_POOL** constant values)

-   [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664)

    (new **pWDDM1\_3DeviceFuncs** member)

-   [**D3D11DDIARG\_CREATEDEFERREDCONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff542044)

    (new **pWDDM1\_3ContextFuncs** member)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Tiled%20resource%20support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




