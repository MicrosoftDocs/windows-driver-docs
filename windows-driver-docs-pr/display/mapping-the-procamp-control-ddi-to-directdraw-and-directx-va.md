---
title: Mapping the ProcAmp Control DDI to DirectDraw and DirectX VA
description: Mapping the ProcAmp Control DDI to DirectDraw and DirectX VA
ms.assetid: ca2b92d9-7f3d-45b9-8841-43915dd4237d
keywords:
- ProcAmp WDK DirectX VA , mapping ProcAmp control DDI
- mapping ProcAmp control DDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mapping the ProcAmp Control DDI to DirectDraw and DirectX VA


## <span id="ddk_mapping_the_procamp_control_ddi_to_directdraw_and_directx_va_gg"></span><span id="DDK_MAPPING_THE_PROCAMP_CONTROL_DDI_TO_DIRECTDRAW_AND_DIRECTX_VA_GG"></span>


ProcAmp control functionality must be accessed through DirectDraw's [motion compensation callback functions](motion-compensation-callbacks.md) to which the [ProcAmp control DDI](https://msdn.microsoft.com/library/windows/hardware/ff569186) can be mapped. For more information about mapping a DirectX VA DDI to DirectDraw's motion compensation callbacks, see [Mapping the Deinterlace DDI to DirectDraw and DirectX VA](mapping-the-deinterlace-ddi-to-directdraw-and-directx-va.md).

The following topics describe how the ProcAmp control DDI is mapped to the motion compensation callbacks:

[Deinterlace Container Device for ProcAmp Control](deinterlace-container-device-for-procamp-control.md)

[Calling the ProcAmp Control DDI from a User-Mode Component](calling-the-procamp-control-ddi-from-a-user-mode-component.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Mapping%20the%20ProcAmp%20Control%20DDI%20to%20DirectDraw%20and%20DirectX%20VA%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




