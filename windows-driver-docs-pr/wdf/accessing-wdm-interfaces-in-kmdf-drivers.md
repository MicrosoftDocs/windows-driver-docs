---
title: Accessing WDM Interfaces in KMDF Drivers
description: Most Kernel-Mode Driver Framework (KMDF) drivers do not need to access Windows Driver Model (WDM) interfaces directly.
ms.assetid: 86e35617-cb6a-4d65-b2a6-9c7bcfa73480
keywords: ["kernel-mode drivers WDK KMDF , WDM", "KMDF WDK , WDM", "Kernel-Mode Driver Framework WDK , WDM", "framework-based drivers WDK KMDF , WDM", "WDM interfaces WDK KMDF"]
---

# Accessing WDM Interfaces in KMDF Drivers


\[Applies to KMDF only\]

Most Kernel-Mode Driver Framework (KMDF) drivers do not need to access Windows Driver Model (WDM) interfaces directly. This section describes the limited cases when a KMDF driver requires direct access to WDM data structures, for example to obtain WDM information or manipulate an IRP.

## In this section


-   [Obtaining WDM Information](obtaining-wdm-information.md)
-   [Handling WDM IRPs Outside of the Framework](handling-wdm-irps-outside-of-the-framework.md)
-   [WDM Interface Restrictions](wdm-interface-restrictions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Accessing%20WDM%20Interfaces%20in%20KMDF%20Drivers%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




