---
title: Deinterlace DDI
description: Deinterlace DDI
ms.date: 01/05/2018
---

# Deinterlace DDI

So that the Video Mixing Renderer (VMR) can deinterlace and perform frame-rate conversion on video content, the display driver must implement the [motion compensation callback functions](./motion-compensation-callbacks.md).

To simplify driver development, use motion-compensation code templates and implement the deinterlacing functions in this section. The functions are member functions of either the deinterlace container device or the deinterlace mode device classes. For more information, see [Defining the Deinterlace Container Device Class](./defining-the-deinterlace-container-device-class.md) and [Defining the Deinterlace Bob Device Class](./defining-the-deinterlace-bob-device-class.md).
