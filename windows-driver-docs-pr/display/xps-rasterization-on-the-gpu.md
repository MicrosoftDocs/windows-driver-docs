---
title: XPS rasterization on the GPU
description: XML Paper Specification (XPS) rasterization on the GPU does not require any independent hardware vendor (IHV) code or behavioral changes in drivers.
ms.assetid: 3C43552A-7D2B-4C10-9AD3-66755171D997
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# XPS rasterization on the GPU


XML Paper Specification (XPS) rasterization on the GPU does not require any independent hardware vendor (IHV) code or behavioral changes in drivers. However, XPS rasterization is a usage pattern that can potentially expose bugs or improper assumptions in driver code. Windows Display Driver Model (WDDM) 1.2 and later drivers must be able to pass XPS rasterization display conformance tests in order to ensure high-quality Windows printing.

|                                                                                   |                                                   |
|-----------------------------------------------------------------------------------|---------------------------------------------------|
| Minimum WDDM version                                                              | 1.2                                               |
| Minimum Windows version                                                           | 8                                                 |
| Driver implementation—Full graphics and Display only                              | Mandatory                                         |
| [WHCK](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests | **Device.Graphics¦XPSRasterizationConformance** |

 

## <span id="xps"></span><span id="XPS"></span>XPS rasterization conformance


The XPS rasterization display conformance requirement determines whether a WDDM GPU driver produces correct rasterization results when it's used by Direct2D in the context of the XPS rasterizer.

The XPS rasterizer is a system component used heavily by Windows print drivers to rasterize an XPS Print Descriptor Language (PDL). To determine the correctness of rasterization results, a comparison is performed between the results that are obtained from the XPS rasterizer when executed on a system with the subject WDDM GPU driver, and the results obtained from baseline use of the XPS rasterizer.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics ¦ XPSRasterizationConformance**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 





