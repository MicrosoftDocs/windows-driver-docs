---
title: Deinterlace DDI
description: Deinterlace DDI
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# Deinterlace DDI


## <span id="ddk_deinterlace_ddi_gg"></span><span id="DDK_DEINTERLACE_DDI_GG"></span>


So that the Video Mixing Renderer (VMR) can deinterlace and perform frame-rate conversion on video content, the display driver must implement the [motion compensation callback functions](/windows-hardware/drivers/ddi/index).

To simplify driver development, use motion-compensation code templates and implement the deinterlacing functions in this section. The functions are member functions of either the deinterlace container device or the deinterlace mode device classes. For more information, see [Defining the Deinterlace Container Device Class](./defining-the-deinterlace-container-device-class.md) and [Defining the Deinterlace Bob Device Class](./defining-the-deinterlace-bob-device-class.md).

 

