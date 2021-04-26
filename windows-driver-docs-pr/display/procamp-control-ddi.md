---
title: ProcAmp Control DDI
description: ProcAmp Control DDI
ms.date: 01/05/2018
ms.localizationpriority: medium
---

# ProcAmp Control DDI

So that the Video Mixing Renderer (VMR) can access ProcAmp-control functionality, the display driver must implement the [motion compensation callback functions](motion-compensation-callbacks.md).

To simplify driver development, use motion-compensation code templates and implement the ProcAmp control functions in this section. The functions are member functions of either the deinterlace container device or ProcAmp control device classes. For more information, see [Defining the Deinterlace Container Device Class](./defining-the-deinterlace-container-device-class.md) and [Defining the ProcAmp Control Device Class](./defining-the-procamp-control-device-class.md).
