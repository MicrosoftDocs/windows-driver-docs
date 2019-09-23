---
title: ProcAmp Control DDI
description: ProcAmp Control DDI
ms.assetid: 102e21eb-bad4-4ab5-8630-9ac37c33f20a
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# ProcAmp Control DDI


## <span id="ddk_procamp_control_ddi_gg"></span><span id="DDK_PROCAMP_CONTROL_DDI_GG"></span>


So that the Video Mixing Renderer (VMR) can access ProcAmp-control functionality, the display driver must implement the [motion compensation callback functions](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index).

To simplify driver development, use motion-compensation code templates and implement the ProcAmp control functions in this section. The functions are member functions of either the deinterlace container device or ProcAmp control device classes. For more information, see [Defining the Deinterlace Container Device Class](https://docs.microsoft.com/windows-hardware/drivers/display/defining-the-deinterlace-container-device-class) and [Defining the ProcAmp Control Device Class](https://docs.microsoft.com/windows-hardware/drivers/display/defining-the-procamp-control-device-class).

 

 





