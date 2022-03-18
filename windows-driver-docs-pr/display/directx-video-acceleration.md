---
title: About DXVA Version 1.0
description: DirectX Video Acceleration
keywords:
- DirectX Video Acceleration version 1.0 WDK Windows 2000 display
- Video Acceleration WDK DirectX
- motion compensation WDK
- VA WDK DirectX
- accelerators WDK DirectX
- display driver model WDK Windows 2000 , DirectX Video Acceleration
- Windows 2000 display driver model WDK , DirectX Video Acceleration
ms.date: 03/18/2022
---

# About DXVA Version 1.0

This section contains information about DirectX Video Acceleration Version 1.0 (DirectX VA or DXVA), which is supported in Windows 2000 or later versions. DXVA Version 2.0 is available starting in Windows Vista.

DXVA is an application programming interface (API) and a corresponding [motion compensation](motion-compensation.md) device driver interface (DDI) for acceleration of digital video decoding. The following additional DDIs are also provided as part of DirectX VA:

- A [deinterlacing DDI](./deinterlace-ddi.md) for deinterlacing and frame-rate conversion of video content.

- A [ProcAmp DDI](./procamp-control-ddi.md) to support ProcAmp control and postprocessing of video content.

- A [COPP DDI](sample-functions-for-copp.md) for protecting video content.

The *dxva.h* header file contains the structures and enumerations used for video acceleration and deinterlacing, and frame-rate conversion.
