---
title: WDDM driver and feature caps
description: This topic describes Windows Display Driver Model (WDDM) driver feature capabilities (caps).
ms.assetid: 452ADF64-A5CC-4694-BE31-FBED29B32DC1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDDM driver and feature caps


This topic describes Windows Display Driver Model (WDDM) driver feature capabilities (caps).

This table lists the requirements for a driver to specify to Windows the WDDM driver type and version.

**WDDM 1.2 driver requirements**

| WDDM driver type | DDI requirements                                                                                                                                                                                                                                           |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Full Graphics    | Implement all the Render-specific and Display-specific required device driver interfaces (DDIs)                                                                                                                                                            |
| Display-Only     | Implement all the Display-specific DDIs and return a null pointer for all the Render-specific DDIs                                                                                                                                                         |
| Render-Only      | Implement all the Render-specific DDIs and return a null pointer for all the Display-specific DDIs, or implement all the DDIs for a full WDDM driver but report DISPLAY\_ADAPTER\_INFO.NumVidPnSources = 0 and DISPLAY\_ADAPTER\_INFO.NumVidPnTargets = 0. |

 

This table lists all the feature capabilities visible to the Microsoft DirectX graphics kernel subsystem (Dxgkrnl.sys) that WDDM 1.2 drivers are required to set. "M" indicates a mandatory feature, "O" indicates optional, and "NA" indicates not applicable. To read details about each feature, follow the link in the left column.

**WDDM 1.2 feature caps**

| Feature                                                                                                                                          | Full graphics driver | Render-only driver | Display-only driver | Feature caps                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|--------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WDDM version                                                                                                                                     | M                    | M                  | M                   | [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062).**WDDMVersion**                                                                                                                                                                |
| [Plug and Play (PnP) start and stop](plug-and-play--pnp--start-and-stop-cases.md): Bug check and PnP Stop support for Non-VGA                   | M                    | NA                 | M                   | [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062).**SupportNonVGA**                                                                                                                                                              |
| [Optimized screen rotation support](optimized-screen-rotation-support.md)                                                                       | M                    | NA                 | M                   | [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062).**SupportSmoothRotation**                                                                                                                                                      |
| [GPU preemption](gpu-preemption.md)                                                                                                             | M                    | M                  | NA                  | [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062).**PreemptionCaps**                                                                                                                                                             |
| [**DXGK\_FLIPCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561069).**FlipOnVSyncMmIo**                                                                                  | M                    | M                  | NA                  | [**DXGK\_FLIPCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561069).**FlipOnVSyncMmIoFlipOnVSyncMmIo** was available starting with Windows Vista; the requirement starting with Windows 8 is to set the **FlipOnVSyncMmIo** cap.                       |
| [TDR changes in Windows 8](tdr-changes-in-windows-8.md)                                                                                         | M                    | M                  | NA                  | [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062).**SupportPerEngineTDR**                                                                                                                                                        |
| [Standby hibernate optimizations](standby-hibernate-optimizations.md): Optimizing the graphics stack to improve performance on sleep and resume | O                    | O                  | NA                  | [**DXGK\_SEGMENTDESCRIPTOR3**](https://msdn.microsoft.com/library/windows/hardware/hh464086).**Flags**                                                                                                                                                      |
| [Stereoscopic 3D](stereoscopic-3d.md): New infrastructure to process and present stereoscopic content                                           | O                    | NA                 | NA                  | [**D3DKMDT\_VIDPN\_SOURCE\_MODE\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff546727)                                                                                                                                               |
| [Direct flip of video memory](direct-flip-of-video-memory.md)                                                                                   | M                    | NA                 | NA                  | [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062).**SupportDirectFlip**                                                                                                                                                          |
| [GDI Hardware Acceleration](gdi-hardware-acceleration.md): A required feature starting with WDDM 1.1                                            | M                    | M                  | NA                  | [**DXGK\_PRESENTATIONCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562004).**SupportKernelModeCommandBuffer**                                                                                                                                 |
| [GPU power management of idle states and active power](gpu-power-management-of-idle-and-active-power.md)                                        | O                    | O                  | O                   | If this feature is supported, the [*DxgkDdiSetPowerComponentFState*](https://msdn.microsoft.com/library/windows/hardware/hh451422) and [*DxgkDdiPowerRuntimeControlRequest*](https://msdn.microsoft.com/library/windows/hardware/hh451396) functions must be supported. |

 

 

 





