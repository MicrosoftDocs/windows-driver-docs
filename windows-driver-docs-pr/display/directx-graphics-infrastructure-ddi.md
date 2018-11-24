---
title: DirectX Graphics Infrastructure DDI
description: DirectX Graphics Infrastructure DDI
ms.assetid: e4f2bd03-d04b-4f67-94ff-54e023000f35
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





