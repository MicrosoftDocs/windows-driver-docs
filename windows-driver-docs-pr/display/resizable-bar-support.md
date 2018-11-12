---
title: Resizable BAR support
description: It is typical today for a discrete graphics processing unit (GPU) to have only a small portion of its frame buffer exposed over the PCI bus.
ms.assetid: 9CBB8D2E-D3E3-4F52-BCAC-F17446D74991
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Resizable BAR support


It is typical today for a discrete graphics processing unit (GPU) to have only a small portion of its frame buffer exposed over the PCI bus. For compatibility with 32bit OSes, discrete GPUs typically claim a 256MB I/O region for their frame buffers and this is how typical firmware configures them.

For Windows Display Driver Model (WDDM) v2, Windows will renegotiate the size of a GPU BAR post firmware initialization on GPUs supporting resizable BAR, see [Resizable BAR Capability](http://go.microsoft.com/fwlink/p/?LinkId=525610) in the [PCI SIG Specifications Library](http://go.microsoft.com/fwlink/p/?LinkId=690603).

A GPU, supporting resizable BAR, must ensure that it can keep the display up and showing a static image during the reprogramming of the BAR. In particular, we don't want to see the display go blank and back up during this process. It is important to have smooth transition between the firmware displayed image, the boot loader image and the first kernel mode driver generated image. It is guaranteed that no PCI transaction will occur toward the GPU while the renegotiation is taking place.

For the most part this renegotiation will be invisible to the kernel mode driver. When the renegotiation is successful, the kernel mode driver will observe that the GPU BAR has been resized to its maximum size to expose the entire VRAM of the discrete GPU.

Upon successful resizing, the kernel mode driver should expose a single, *CPUVisible*, memory segment to the video memory manager. The video memory manager will map CPU virtual addresses directly to this range when the CPU need to access the content of the memory segment.

 

 





