---
title: UMDF Based on COM Subset
description: UMDF Based on COM Subset
ms.assetid: 918459a9-a6a2-40b8-8b97-3aabe3e49bfb
keywords: ["UMDF objects WDK , COM subset", "framework objects WDK UMDF , COM subset", "COM WDK UMDF"]
---

# UMDF Based on COM Subset


\[This topic applies to UMDF 1.*x*.\]

The framework objects and interfaces are based on the Component Object Model (COM) for the following reasons:

-   COM is familiar to many applications programmers.

-   C++ is the preferred language for programming COM applications.

-   COM interfaces enable logical groupings of functions, so that the device driver interface (DDI) is easy to understand and navigate.

-   Using COM enables the DDI to extend and evolve without requiring existing driver DLLs to be recompiled.

-   Numerous tools, including Microsoft Visual Studio and active template library (ATL), support COM-based applications and objects.

The framework uses only a small subset of COM; it does not depend on the entire COM infrastructure and runtime library. Instead, the framework uses only the query-interface and reference-counting features. Every framework interface derives from **IUnknown** and therefore supports the **QueryInterface**, **AddRef**, and **Release** methods by default. The **AddRef** and **Release** methods manage object lifetime. The **QueryInterface** method enables other components to determine which interfaces the driver supports.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20UMDF%20Based%20on%20COM%20Subset%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




