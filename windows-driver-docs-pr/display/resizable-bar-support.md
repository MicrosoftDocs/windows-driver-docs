---
title: Resizable BAR support
description: It is typical today for a discrete graphics processing unit (GPU) to have only a small portion of its frame buffer exposed over the PCI bus.
ms.assetid: 9CBB8D2E-D3E3-4F52-BCAC-F17446D74991
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Resizable BAR support


It is typical today for a discrete graphics processing unit (GPU) to have only a small portion of its frame buffer exposed over the PCI bus. For compatibility with 32bit OSes, discrete GPUs typically claim a 256MB I/O region for their frame buffers and this is how typical firmware configures them.

For Windows Display Driver Model (WDDM) v2, Windows will renegotiate the size of a GPU BAR post firmware initialization on GPUs supporting resizable BAR, see [Resizable BAR Capability](http://go.microsoft.com/fwlink/p/?LinkId=525610) in the [PCI SIG Specifications Library](http://go.microsoft.com/fwlink/p/?LinkId=690603).

A GPU, supporting resizable BAR, must ensure that it can keep the display up and showing a static image during the reprogramming of the BAR. In particular, we don't want to see the display go blank and back up during this process. It is important to have smooth transition between the firmware displayed image, the boot loader image and the first kernel mode driver generated image. It is guaranteed that no PCI transaction will occur toward the GPU while the renegotiation is taking place.

For the most part this renegotiation will be invisible to the kernel mode driver. When the renegotiation is successful, the kernel mode driver will observe that the GPU BAR has been resized to its maximum size to expose the entire VRAM of the discrete GPU.

Upon successful resizing, the kernel mode driver should expose a single, *CPUVisible*, memory segment to the video memory manager. The video memory manager will map CPU virtual addresses directly to this range when the CPU need to access the content of the memory segment.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Resizable%20BAR%20support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




