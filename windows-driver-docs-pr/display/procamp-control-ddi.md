---
title: ProcAmp Control DDI
description: ProcAmp Control DDI
ms.assetid: 102e21eb-bad4-4ab5-8630-9ac37c33f20a
ms.author: windowsdriverdev
ms.date: 01/05/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ProcAmp Control DDI


## <span id="ddk_procamp_control_ddi_gg"></span><span id="DDK_PROCAMP_CONTROL_DDI_GG"></span>


So that the Video Mixing Renderer (VMR) can access ProcAmp-control functionality, the display driver must implement the [motion compensation callback functions](https://msdn.microsoft.com/library/windows/hardware/ff568441).

To simplify driver development, use motion-compensation code templates and implement the ProcAmp control functions in this section. The functions are member functions of either the deinterlace container device or ProcAmp control device classes. For more information, see [Defining the Deinterlace Container Device Class](https://msdn.microsoft.com/library/windows/hardware/ff552682) and [Defining the ProcAmp Control Device Class](https://msdn.microsoft.com/library/windows/hardware/ff552686).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20ProcAmp%20Control%20DDI%20%20RELEASE:%20%281/4/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




