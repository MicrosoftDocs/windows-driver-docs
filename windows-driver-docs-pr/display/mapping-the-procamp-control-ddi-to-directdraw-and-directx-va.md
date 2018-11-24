---
title: Mapping the ProcAmp Control DDI to DirectDraw and DirectX VA
description: Mapping the ProcAmp Control DDI to DirectDraw and DirectX VA
ms.assetid: ca2b92d9-7f3d-45b9-8841-43915dd4237d
keywords:
- ProcAmp WDK DirectX VA , mapping ProcAmp control DDI
- mapping ProcAmp control DDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping the ProcAmp Control DDI to DirectDraw and DirectX VA


## <span id="ddk_mapping_the_procamp_control_ddi_to_directdraw_and_directx_va_gg"></span><span id="DDK_MAPPING_THE_PROCAMP_CONTROL_DDI_TO_DIRECTDRAW_AND_DIRECTX_VA_GG"></span>


ProcAmp control functionality must be accessed through DirectDraw's [motion compensation callback functions](motion-compensation-callbacks.md) to which the [ProcAmp control DDI](https://msdn.microsoft.com/library/windows/hardware/ff569186) can be mapped. For more information about mapping a DirectX VA DDI to DirectDraw's motion compensation callbacks, see [Mapping the Deinterlace DDI to DirectDraw and DirectX VA](mapping-the-deinterlace-ddi-to-directdraw-and-directx-va.md).

The following topics describe how the ProcAmp control DDI is mapped to the motion compensation callbacks:

[Deinterlace Container Device for ProcAmp Control](deinterlace-container-device-for-procamp-control.md)

[Calling the ProcAmp Control DDI from a User-Mode Component](calling-the-procamp-control-ddi-from-a-user-mode-component.md)

 

 





