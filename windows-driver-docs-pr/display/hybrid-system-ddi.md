---
title: Hybrid system DDI and dList DLL support
description: Lists hybrid system DDIs related to handling cross-adapter resources; Describes how to set up and register a dList DLL
ms.date: 11/01/2021
prerelease: false
---

# Hybrid system DDI and dList DLL support

Support for [cross-adapter resources](using-cross-adapter-resources-in-a-hybrid-system.md) on a [hybrid system](using-cross-adapter-resources-in-a-hybrid-system.md) was introduced starting with Windows 8.1 (WDDM 1.3). The following user-mode and kernel-mode functions, structures, and enumerations are available:

* [**D3D10_DDI_RESOURCE_MISC_FLAG**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3d10_ddi_resource_misc_flag) enumeration
* [**D3DDDI_RESOURCEFLAGS2**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_resourceflags2) structure
* [**D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_synchronizationobject_flags) structure
* [**D3DKMDT_GDISURFACEDATA**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_gdisurfacedata) structure
* [**D3DKMDT_GDISURFACETYPE**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_gdisurfacetype) enumeration
* [**DXGK_DRIVERCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps) structure
* [**DXGK_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) structure
* [*pfnQueryDListForApplication1*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_querydlistforapplication1) function

The [cross-adapter resource scan-out](supporting-caso.md) (CASO) feature was introduced starting with Windows Server 2022 (WDDM 2.9). The following additional support was added for CASO:

* [**pfnQueryDListForApplication2**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_querydlistforapplication2) function (added)
* [**D3DDDI_DLIST_QUERY_RESULT**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-d3dddi_dlist_query_result) enumeration (added)
* [**D3DDDI_DLIST_QUERY_DECISION_FACTOR**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-d3dddi_dlist_query_decision_factor) enumeration (added)
* **NoHybridDiscreteDListDllSupport** was added to the [**DXGK_DRIVERCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps) structure
* **CrossAdapterResourceTexture** and **CrossAdapterResourceScanout** were added to the [**DXGK_VIDMMCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidmmcaps) structure

> [!NOTE]
> On Windows Server 2022 (WDDM 2.9) and later OS versions, a user-mode display driver (UMD) on a hybrid system must support the [**pfnQueryDListForApplication2**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_querydlistforapplication2) DDI, which replaces [*pfnQueryDListForApplication1*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_querydlistforapplication1), regardless of whether it implements support for CASO.

## Setting up the dList DLL

A *dList* is a list of applications that need [cross-adapter shared surfaces](using-cross-adapter-resources-in-a-hybrid-system.md) for high-performance rendering on the discrete GPU.

The discrete GPU's UMD installs a separate, small **dList** DLL that exports its [**pfnQueryDListForApplication2**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_querydlistforapplication2) function. The operating system itself doesn't determine which GPU an application should run on. Instead, the Direct3D runtime calls **pfnQueryDListForApplication2** at most once during Direct3D initialization.

The driver must query an up-to-date list of process information to determine whether or not the process needs the enhanced performance of a discrete GPU instead of the integrated GPU.

For best performance, the DLL should:

* Be under 200 KB in size
* Keep allocations to a minimum
* Be able to return from [**pfnQueryDListForApplication2**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_querydlistforapplication2) in under 4 ms.

## Registering the dList DLL

The UMD provides the name of the small **dList** DLL in its INF file under the registry keys **UserModeDListDriverName** and **UserModeDListDriverNameWow,** the latter under the **Wow64** registry entry. Here's example INF code:

```inf
[Xxx_SoftwareDeviceSettings]
...
HKR,, UserModeDListDriverName,    %REG_MULTI_SZ%, dlistumd.dll
HKR,, UserModeDListDriverNameWow, %REG_MULTI_SZ%, dlistumdwow.dll
```
