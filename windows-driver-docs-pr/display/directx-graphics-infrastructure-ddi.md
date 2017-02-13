---
title: DirectX Graphics Infrastructure DDI
description: DirectX Graphics Infrastructure DDI
ms.assetid: e4f2bd03-d04b-4f67-94ff-54e023000f35
---

# DirectX Graphics Infrastructure DDI


The DirectX Graphics Infrastructure (DXGI) was developed with the realization that some parts of graphics evolve more slowly than others. DXGI provides a common framework for future graphics components. The first Direct3D runtime version that takes advantage of DXGI is Direct3D version 10. In previous versions of the Direct3D runtime, access to low-level tasks was included in the Direct3D runtime. DXGI defines a DDI that manages low-level shared tasks independently from the Direct3D runtime. The following tasks are now implemented with DXGI, and you can use the DXGI DDI to handle these tasks:

-   Presentation

-   Gamma correction control

-   Resource residency

-   Resource priority

The following sections describe how the user-mode display driver supports and uses the DXGI DDI:

[Supporting the DXGI DDI](supporting-the-dxgi-ddi.md)

[Passing DXGI Information at Resource Creation Time](passing-dxgi-information-at-resource-creation-time.md)

[DXGI Presentation Path](dxgi-presentation-path.md)

[Setting DXGI Information in the Registry](setting-dxgi-information-in-the-registry.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DirectX%20Graphics%20Infrastructure%20DDI%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




