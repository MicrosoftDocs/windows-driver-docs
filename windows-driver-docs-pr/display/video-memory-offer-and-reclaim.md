---
title: Video memory offer and reclaim
description: Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers must use the memory offer and reclaim feature, available starting with Windows 8, to reduce memory overhead needed for temporary surfaces in local and system memory.
ms.assetid: 8BB6A7A3-E102-4069-BFC2-9605DDE9F020
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video memory offer and reclaim


Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers must use the memory offer and reclaim feature, available starting with Windows 8, to reduce memory overhead needed for temporary surfaces in local and system memory.

|                                                                                   |                                  |
|-----------------------------------------------------------------------------------|----------------------------------|
| Minimum WDDM version                                                              | 1.2                              |
| Minimum Windows version                                                           | 8                                |
| Driver implementation—Full graphics and Render only                               | Mandatory                        |
| [WHCK](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests | **Device.Graphics…OfferReclaim** |

 

Especially in mobile scenarios, graphics-intensive apps that need hardware acceleration can make heavy use of GPU resources. Also, in many mobile devices the GPU is integrated into the CPU chipset and the GPU uses portions of system memory as video memory. To ensure reasonable system performance when multiple apps make heavy use of a GPU that in turn makes heavy demand on system memory, the memory footprint of display drivers should be minimized. The offer/reclaim device driver interfaces (DDIs) provide a mechanism to do this.

An API is available for apps to offer unneeded memory that the system can later reclaim for other uses, as well as to reclaim memory that was recently discarded. See the Microsoft DirectX Graphics Infrastructure (DXGI) app programming topic, [DXGI 1.2 Improvements](https://docs.microsoft.com/windows/desktop/direct3ddxgi/dxgi-1-2-improvements).

## <span id="Offer_and_reclaim_DDI"></span><span id="offer_and_reclaim_ddi"></span><span id="OFFER_AND_RECLAIM_DDI"></span>Offer and reclaim DDI


New functions are available starting with Windows 8 for the user-mode driver to offer or reclaim memory.

The driver calls these system-provided functions to offer or reclaim memory allocations:

-   [**pfnOfferAllocationsCb**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_offerallocationscb)
-   [**pfnReclaimAllocationsCb**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_reclaimallocationscb)

The driver implements these functions if it supports Microsoft Direct3D 10 hardware:

-   [*pfnOfferResources*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_offerresources)
-   [*pfnReclaimResources*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi1_2_ddi_base_functions)

The driver implements the following functions if it supports Microsoft Direct3D 9 hardware. Also, if apps offer or reclaim their allocations while using the Direct3D 11 API running on Direct3D 9 hardware, the Direct3D runtime calls these functions:

-   [*OfferResources*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_offerresources)
-   [*ReclaimResources*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_reclaimresources)

Use these associated structures and enumerations:

-   [**D3DDDI\_OFFER\_PRIORITY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dukmdt/ne-d3dukmdt-_d3dddi_offer_priority)
-   [**D3DDDIARG\_OFFERRESOURCES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddiarg_offerresources)
-   [**D3DDDIARG\_RECLAIMRESOURCES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddiarg_reclaimresources)
-   [**D3DDDICB\_OFFERALLOCATIONS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddicb_offerallocations)
-   [**D3DDDICB\_RECLAIMALLOCATIONS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/ns-d3dumddi-_d3dddicb_reclaimallocations)
-   [**DXGI\_DDI\_ARG\_OFFERRESOURCES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-_dxgi_ddi_arg_offerresources)
-   [**DXGI\_DDI\_ARG\_RECLAIMRESOURCES**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-_dxgi_ddi_arg_reclaimresources)
-   [**DXGI1\_2\_DDI\_BASE\_FUNCTIONS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dxgiddi/ns-dxgiddi-dxgi1_2_ddi_base_functions)

To support the offer/reclaim feature, starting with Windows 8 this structure has two new members:

-   [**D3DDDI\_ALLOCATIONLIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dukmdt/ns-d3dukmdt-_d3dddi_allocationlist)

You should carefully test that your driver handles this feature correctly because after an allocation is discarded, all data in it is lost.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics…OfferReclaim**. Note that these requirements list the scenarios in which the driver must offer allocations.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 





