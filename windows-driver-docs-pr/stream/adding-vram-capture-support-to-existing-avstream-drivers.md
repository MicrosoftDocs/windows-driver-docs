---
title: Adding VRAM Capture Support to Existing AVStream Drivers
author: windows-driver-content
description: Adding VRAM Capture Support to Existing AVStream Drivers
ms.assetid: 10736533-3873-4f1d-91c5-d2e55163daaa
keywords:
- VRAM capture WDK AVStream , existing driver support
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adding VRAM Capture Support to Existing AVStream Drivers


To add VRAM capture support to an existing pin-centric AVStream driver that uses DMA, follow these steps.

1.  Add VRAM capture support to your [*AVStrMiniPinProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556351) callback routine. The **CCapturePin::Process** method in *Capture.cpp* of the [AVStream Simulated Hardware Sample Driver (AVSHwS)](http://go.microsoft.com/fwlink/p/?linkid=256083) in the MSDN Code Gallery shows one way to do this.

2.  Handle VRAM capture property requests as described earlier in this section.

3.  Add support in either the child capture driver or the parent display miniport driver to map DX kernel handles to VRAM addresses.

4.  Implement StopCapture functionality. When the KMD sends a stop capture notification, the capture driver must stop all capture. To register for notification, the capture driver provides a [*DxgkDdiStopCapture*](https://msdn.microsoft.com/library/windows/hardware/ff560776) callback routine. The capture driver should fail any capture requests coming from user mode after receiving this notification.

 

 




