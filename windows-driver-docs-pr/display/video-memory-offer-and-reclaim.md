---
title: Video memory offer and reclaim
description: Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers must use the memory offer and reclaim feature, available starting with Windows 8, to reduce memory overhead needed for temporary surfaces in local and system memory.
ms.assetid: 8BB6A7A3-E102-4069-BFC2-9605DDE9F020
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video memory offer and reclaim


Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers must use the memory offer and reclaim feature, available starting with Windows 8, to reduce memory overhead needed for temporary surfaces in local and system memory.

|                                                                                   |                                  |
|-----------------------------------------------------------------------------------|----------------------------------|
| Minimum WDDM version                                                              | 1.2                              |
| Minimum Windows version                                                           | 8                                |
| Driver implementation—Full graphics and Render only                               | Mandatory                        |
| [WHCK]( http://go.microsoft.com/fwlink/p/?linkid=258342) requirements and tests | **Device.Graphics…OfferReclaim** |

 

Especially in mobile scenarios, graphics-intensive apps that need hardware acceleration can make heavy use of GPU resources. Also, in many mobile devices the GPU is integrated into the CPU chipset and the GPU uses portions of system memory as video memory. To ensure reasonable system performance when multiple apps make heavy use of a GPU that in turn makes heavy demand on system memory, the memory footprint of display drivers should be minimized. The offer/reclaim device driver interfaces (DDIs) provide a mechanism to do this.

An API is available for apps to offer unneeded memory that the system can later reclaim for other uses, as well as to reclaim memory that was recently discarded. See the Microsoft DirectX Graphics Infrastructure (DXGI) app programming topic, [DXGI 1.2 Improvements](https://msdn.microsoft.com/library/windows/desktop/hh404490).

## <span id="Offer_and_reclaim_DDI"></span><span id="offer_and_reclaim_ddi"></span><span id="OFFER_AND_RECLAIM_DDI"></span>Offer and reclaim DDI


New functions are available starting with Windows 8 for the user-mode driver to offer or reclaim memory.

The driver calls these system-provided functions to offer or reclaim memory allocations:

-   [**pfnOfferAllocationsCb**](https://msdn.microsoft.com/library/windows/hardware/hh451693)
-   [**pfnReclaimAllocationsCb**](https://msdn.microsoft.com/library/windows/hardware/hh451695)

The driver implements these functions if it supports Microsoft Direct3D 10 hardware:

-   [*pfnOfferResources*](https://msdn.microsoft.com/library/windows/hardware/jj128409)
-   [*pfnReclaimResources*](https://msdn.microsoft.com/library/windows/hardware/hh439828)

The driver implements the following functions if it supports Microsoft Direct3D 9 hardware. Also, if apps offer or reclaim their allocations while using the Direct3D 11 API running on Direct3D 9 hardware, the Direct3D runtime calls these functions:

-   [*OfferResources*](https://msdn.microsoft.com/library/windows/hardware/hh451576)
-   [*ReclaimResources*](https://msdn.microsoft.com/library/windows/hardware/hh439826)

Use these associated structures and enumerations:

-   [**D3DDDI\_OFFER\_PRIORITY**](https://msdn.microsoft.com/library/windows/hardware/hh439275)
-   [**D3DDDIARG\_OFFERRESOURCES**](https://msdn.microsoft.com/library/windows/hardware/hh451078)
-   [**D3DDDIARG\_RECLAIMRESOURCES**](https://msdn.microsoft.com/library/windows/hardware/hh451080)
-   [**D3DDDICB\_OFFERALLOCATIONS**](https://msdn.microsoft.com/library/windows/hardware/hh451158)
-   [**D3DDDICB\_RECLAIMALLOCATIONS**](https://msdn.microsoft.com/library/windows/hardware/hh451159)
-   [**DXGI\_DDI\_ARG\_OFFERRESOURCES**](https://msdn.microsoft.com/library/windows/hardware/hh451228)
-   [**DXGI\_DDI\_ARG\_RECLAIMRESOURCES**](https://msdn.microsoft.com/library/windows/hardware/hh451235)
-   [**DXGI1\_2\_DDI\_BASE\_FUNCTIONS**](https://msdn.microsoft.com/library/windows/hardware/hh451215)

To support the offer/reclaim feature, starting with Windows 8 this structure has two new members:

-   [**D3DDDI\_ALLOCATIONLIST**](https://msdn.microsoft.com/library/windows/hardware/ff544375)

You should carefully test that your driver handles this feature correctly because after an allocation is discarded, all data in it is lost.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation]( http://go.microsoft.com/fwlink/p/?linkid=258342) on **Device.Graphics…OfferReclaim**. Note that these requirements list the scenarios in which the driver must offer allocations.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Video%20memory%20offer%20and%20reclaim%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




