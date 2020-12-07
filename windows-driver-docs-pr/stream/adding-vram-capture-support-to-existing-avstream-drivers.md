---
title: Adding VRAM Capture Support to Existing AVStream Drivers
description: Adding VRAM capture support to existing AVStream drivers
keywords:
- VRAM capture WDK AVStream , existing driver support
ms.date: 06/15/2020
ms.localizationpriority: medium
---

# Adding VRAM capture support to existing AVStream drivers

To add VRAM capture support to an existing pin-centric AVStream driver that uses DMA, follow these steps.

1. Add VRAM capture support to your [*AVStrMiniPinProcess*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspin) callback routine. The **CCapturePin::Process** method in *Capture.cpp* of the [AVStream Simulated Hardware Sample Driver (AVSHwS)](/samples/microsoft/windows-driver-samples/avstream-simulated-hardware-sample-driver-avshws/) shows one way to do this.

1. Handle VRAM capture property requests as described earlier in this section.

1. Add support in either the child capture driver or the parent display miniport driver to map DX kernel handles to VRAM addresses.

1. Implement StopCapture functionality. When the KMD sends a stop capture notification, the capture driver must stop all capture. To register for notification, the capture driver provides a [*DxgkDdiStopCapture*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_stopcapture) callback routine. The capture driver should fail any capture requests coming from user mode after receiving this notification.
