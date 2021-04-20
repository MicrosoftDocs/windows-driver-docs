---
title: Hybrid system DDI
description: Starting with Windows 8.1, these user-mode and kernel-mode structures and enumerations of the display device driver interface (DDI) are updated to handle cross-adapter resources on a hybrid system D3D10_DDI_RESOURCE_MISC_FLAGD3DDDI_RESOURCEFLAGS2D3DDDI_SYNCHRONIZATIONOBJECT_FLAGSD3DKMDT_GDISURFACEDATAD3DKMDT_GDISURFACETYPEDXGK_DRIVERCAPSDXGK_VIDMMCAPSThis function, new for Windows 8.1, is implemented by the user-mode display driver QueryDListForApplication1.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hybrid system DDI


Starting with Windows 8.1, these user-mode and kernel-mode structures and enumerations of the display device driver interface (DDI) are updated to handle [cross-adapter resources](using-cross-adapter-resources-in-a-hybrid-system.md) on a [hybrid system](using-cross-adapter-resources-in-a-hybrid-system.md):

-   [**D3D10\_DDI\_RESOURCE\_MISC\_FLAG**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3d10_ddi_resource_misc_flag)
-   [**D3DDDI\_RESOURCEFLAGS2**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_resourceflags2)
-   [**D3DDDI\_SYNCHRONIZATIONOBJECT\_FLAGS**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_synchronizationobject_flags)
-   [**D3DKMDT\_GDISURFACEDATA**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_gdisurfacedata)
-   [**D3DKMDT\_GDISURFACETYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_gdisurfacetype)
-   [**DXGK\_DRIVERCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps)
-   [**DXGK\_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps)

This function, new for Windows 8.1, is implemented by the user-mode display driver:

-   [*QueryDListForApplication1*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_querydlistforapplication1)

Here's how to set up and register a DLL that exports this function.
## <span id="Setting_up_the_dList_DLL"></span><span id="setting_up_the_dlist_dll"></span><span id="SETTING_UP_THE_DLIST_DLL"></span>Setting up the dList DLL


A *dList* is a list of applications that need cross-adapter shared surfaces for high-performance rendering on the discrete GPU. The discrete GPU installs a separate small **dList** DLL that exports the [**QueryDListForApplication1**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_querydlistforapplication1) function. The operating system itself doesn't determine which GPU an application should run on. Instead, the Microsoft Direct3D runtime calls **QueryDListForApplication1** at most once during Direct3D initialization.

The driver must query an up-to-date list of process information to determine whether or not the process needs the enhanced performance of a discrete GPU instead of the integrated GPU.

For best performance, the DLL should be under 200 KB in size, should keep allocations to a minimum, and should be able to return from the [**QueryDListForApplication1**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_querydlistforapplication1) function in under 4 ms.

## <span id="Registering_the_dList_DLL"></span><span id="registering_the_dlist_dll"></span><span id="REGISTERING_THE_DLIST_DLL"></span>Registering the dList DLL


The user-mode display driver provides the name of the small **dList** DLL in its INF file under the registry keys **UserModeDListDriverName** and **UserModeDListDriverNameWow,** the latter under the **Wow64** registry entry. Here's example INF code:

```inf
[Xxx_SoftwareDeviceSettings]
...
HKR,, UserModeDListDriverName,    %REG_MULTI_SZ%, dlistumd.dll
HKR,, UserModeDListDriverNameWow, %REG_MULTI_SZ%, dlistumdwow.dll
```
