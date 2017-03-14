---
title: XPS rasterization on the GPU
description: XML Paper Specification (XPS) rasterization on the GPU does not require any independent hardware vendor (IHV) code or behavioral changes in drivers.
ms.assetid: 3C43552A-7D2B-4C10-9AD3-66755171D997
---

# XPS rasterization on the GPU


XML Paper Specification (XPS) rasterization on the GPU does not require any independent hardware vendor (IHV) code or behavioral changes in drivers. However, XPS rasterization is a usage pattern that can potentially expose bugs or improper assumptions in driver code. Windows Display Driver Model (WDDM) 1.2 and later drivers must be able to pass XPS rasterization display conformance tests in order to ensure high-quality Windows printing.

|                                                                                   |                                                   |
|-----------------------------------------------------------------------------------|---------------------------------------------------|
| Minimum WDDM version                                                              | 1.2                                               |
| Minimum Windows version                                                           | 8                                                 |
| Driver implementation—Full graphics and Display only                              | Mandatory                                         |
| [WHCK]( http://go.microsoft.com/fwlink/p/?linkid=258342) requirements and tests | **Device.Graphicsâ€¦XPSRasterizationConformance** |

 

## <span id="xps"></span><span id="XPS"></span>XPS rasterization conformance


The XPS rasterization display conformance requirement determines whether a WDDM GPU driver produces correct rasterization results when it's used by Direct2D in the context of the XPS rasterizer.

The XPS rasterizer is a system component used heavily by Windows print drivers to rasterize an XPS Print Descriptor Language (PDL). To determine the correctness of rasterization results, a comparison is performed between the results that are obtained from the XPS rasterizer when executed on a system with the subject WDDM GPU driver, and the results obtained from baseline use of the XPS rasterizer.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation]( http://go.microsoft.com/fwlink/p/?linkid=258342) on **Device.Graphicsâ€¦XPSRasterizationConformance**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20XPS%20rasterization%20on%20the%20GPU%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




