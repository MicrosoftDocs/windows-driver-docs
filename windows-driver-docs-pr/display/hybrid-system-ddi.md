---
title: Hybrid system DDI
description: Starting with Windows 8.1, these user-mode and kernel-mode structures and enumerations of the display device driver interface (DDI) are updated to handle cross-adapter resources on a hybrid system D3D10_DDI_RESOURCE_MISC_FLAGD3DDDI_RESOURCEFLAGS2D3DDDI_SYNCHRONIZATIONOBJECT_FLAGSD3DKMDT_GDISURFACEDATAD3DKMDT_GDISURFACETYPEDXGK_DRIVERCAPSDXGK_VIDMMCAPSThis function, new for Windows 8.1, is implemented by the user-mode display driver QueryDListForApplication1.
ms.assetid: 8AABE677-2C2D-4CFD-AF22-06D65524A158
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Hybrid system DDI


Starting with Windows 8.1, these user-mode and kernel-mode structures and enumerations of the display device driver interface (DDI) are updated to handle [cross-adapter resources](using-cross-adapter-resources-in-a-hybrid-system.md) on a [hybrid system](using-cross-adapter-resources-in-a-hybrid-system.md):

-   [**D3D10\_DDI\_RESOURCE\_MISC\_FLAG**](https://msdn.microsoft.com/library/windows/hardware/ff542004)
-   [**D3DDDI\_RESOURCEFLAGS2**](https://msdn.microsoft.com/library/windows/hardware/hh439286)
-   [**D3DDDI\_SYNCHRONIZATIONOBJECT\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544662)
-   [**D3DKMDT\_GDISURFACEDATA**](https://msdn.microsoft.com/library/windows/hardware/ff546021)
-   [**D3DKMDT\_GDISURFACETYPE**](https://msdn.microsoft.com/library/windows/hardware/ff546039)
-   [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062)
-   [**DXGK\_VIDMMCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562072)

This function, new for Windows 8.1, is implemented by the user-mode display driver:

-   [*QueryDListForApplication1*](https://msdn.microsoft.com/library/windows/hardware/dn270597)

Here's how to set up and register a DLL that exports this function.
## <span id="Setting_up_the_dList_DLL"></span><span id="setting_up_the_dlist_dll"></span><span id="SETTING_UP_THE_DLIST_DLL"></span>Setting up the dList DLL


A *dList* is a list of applications that need cross-adapter shared surfaces for high-performance rendering on the discrete GPU. The discrete GPU installs a separate small **dList** DLL that exports the [**QueryDListForApplication1**](https://msdn.microsoft.com/library/windows/hardware/dn270597) function. The operating system itself doesn't determine which GPU an application should run on. Instead, the Microsoft Direct3D runtime calls **QueryDListForApplication1** at most once during Direct3D initialization.

The driver must query an up-to-date list of process information to determine whether or not the process needs the enhanced performance of a discrete GPU instead of the integrated GPU.

For best performance, the DLL should be under 200 KB in size, should keep allocations to a minimum, and should be able to return from the [**QueryDListForApplication1**](https://msdn.microsoft.com/library/windows/hardware/dn270597) function in under 4 ms.

## <span id="Registering_the_dList_DLL"></span><span id="registering_the_dlist_dll"></span><span id="REGISTERING_THE_DLIST_DLL"></span>Registering the dList DLL


The user-mode display driver provides the name of the small **dList** DLL in its INF file under the registry keys **UserModeDListDriverName** and **UserModeDListDriverNameWow,** the latter under the **Wow64** registry entry. Here's example INF code:

```cpp
[Xxx_SoftwareDeviceSettings]
...
HKR,, UserModeDListDriverName,    %REG_MULTI_SZ%, dlistumd.dll
HKR,, UserModeDListDriverNameWow, %REG_MULTI_SZ%, dlistumdwow.dll
```

 

 





