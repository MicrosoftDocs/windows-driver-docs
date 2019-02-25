---
title: Handling the Creation of Multisampled Surfaces
description: Handling the Creation of Multisampled Surfaces
ms.assetid: 78557c9d-b741-4eb9-b8e2-56387cad80c4
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multisample rendering, creating
- multisample rendering WDK DirectX 8.0 , creating
- rendering multisamples WDK DirectX 8.0 , creating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling the Creation of Multisampled Surfaces


## <span id="ddk_handling_the_creation_of_multisampled_surfaces_gg"></span><span id="DDK_HANDLING_THE_CREATION_OF_MULTISAMPLED_SURFACES_GG"></span>


When a multisampled surface is being created, the number of samples can be found in the **ddsCapsEx.dwCaps3** of the [**DD\_SURFACE\_MORE**](https://msdn.microsoft.com/library/windows/hardware/ff551737) structure. This field holds one of the values of the enumerated type D3DMULTISAMPLE\_TYPE. It is not a bitfield like **wFlipMSTypes** or **wBltMSTypes**. If a surface is not multisampled, **dwCaps3** has the value D3DMULTISAMPLE\_NONE (0).

When determining whether a creation request for a multisample surface can be satisfied or not, the driver should not take into account the current value of the D3DRS\_MULTISAMPLEANTIALIAS render state. It is not permissible for a driver to fail a request to set D3DRS\_MULTISAMPLEANTIALIAS **FALSE**. Therefore, any restriction that affects the ability to perform multisample rendering should be enforced at context create time even if D3DRS\_MULTISAMPLEANTIALIAS is **FALSE** at that time.

 

 





