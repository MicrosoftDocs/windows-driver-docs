---
title: Timeout Detection and Recovery (TDR)
description: Timeout Detection and Recovery (TDR)
ms.assetid: f410eec7-026f-41e0-8c60-72f651659ead
keywords:
- TDR (timeout detection and recovery) WDK display , described
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Timeout Detection and Recovery (TDR)


One of the most common stability problems in graphics occurs when a computer "hangs" or appears completely "frozen" while, in reality, it is processing an end-user command or operation. The end-user typically waits a few seconds and then decides to reboot the computer. The frozen appearance of the computer typically occurs because the GPU is busy processing intensive graphical operations, typically during game play. The GPU does not update the display screen, and the computer appears frozen.

In Windows Vista and later, the operating system attempts to detect situations in which computers appear to be completely "frozen". The operating system then attempts to dynamically recover from the frozen situations so that desktops are responsive again. This process of detection and recovery is known as *timeout detection and recovery* (TDR). In the TDR process, the operating system's GPU scheduler calls the display miniport driver's [*DxgkDdiResetFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559815) function to reinitialize the driver and reset the GPU. Therefore, end users are not required to reboot the operating system, which greatly enhances their experience.

The only visible artifact from the hang detection to the recovery is a screen flicker. This screen flicker results when the operating system resets some portions of the graphics stack, which causes a screen redraw. This flicker is eliminated if the display miniport driver complies with Windows Display Driver Model (WDDM) 1.2 and later (see [Providing seamless state transitions in WDDM 1.2 and later](seamless-state-transitions-in-wddm-1-2-and-later.md)). Some legacy Microsoft DirectX applications (for example, those DirectX applications that conform to DirectX versions earlier than 9.0) might render to a black screen at the end of this recovery. The end user would have to restart these applications.

This sequence briefly describes the TDR process:

## <span id="Timeout_detection_in_the_Windows_Display_Driver_Model__WDDM_"></span><span id="timeout_detection_in_the_windows_display_driver_model__wddm_"></span><span id="TIMEOUT_DETECTION_IN_THE_WINDOWS_DISPLAY_DRIVER_MODEL__WDDM_"></span>Timeout detection in the Windows Display Driver Model (WDDM)


The GPU scheduler, which is part of the DirectX graphics kernel subsystem (Dxgkrnl.sys), detects that the GPU is taking more than the permitted amount of time to execute a particular task. The GPU scheduler then tries to preempt this particular task. The preempt operation has a "wait" timeout, which is the actual TDR timeout. This step is thus the timeout detection phase of the process. The default timeout period in Windows Vista and later operating systems is 2 seconds. If the GPU cannot complete or preempt the current task within the TDR timeout period, the operating system diagnoses that the GPU is frozen.

To prevent timeout detection from occurring, hardware vendors should ensure that graphics operations (that is, direct memory access (DMA) buffer completion) take no more than 2 seconds in end-user scenarios such as productivity and game play.

## <span id="Preparation_for_recovery"></span><span id="preparation_for_recovery"></span><span id="PREPARATION_FOR_RECOVERY"></span>Preparation for recovery


The operating system's GPU scheduler calls the display miniport driver's [*DxgkDdiResetFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559815) function to inform the driver that the operating system detected a timeout. The driver must then reinitialize itself and reset the GPU. In addition, the driver must stop accessing memory and should not access hardware. The operating system and the driver collect hardware and other state information that could be useful for post-mortem diagnosis.

## <span id="Desktop_recovery"></span><span id="desktop_recovery"></span><span id="DESKTOP_RECOVERY"></span>Desktop recovery


The operating system resets the appropriate state of the graphics stack. The video memory manager, which is also part of Dxgkrnl.sys, purges all allocations from video memory. The display miniport driver resets the GPU hardware state. The graphics stack takes the final actions and restores the desktop to the responsive state. As previously mentioned, some legacy DirectX applications might render just black at the end of this recovery, which requires the end user to restart these applications. Well-written DirectX 9Ex and DirectX 10 and later applications that handle Device Remove technology continue to work correctly. An application must release and then re-create its Microsoft Direct3D device and all of the device's objects. For more information about how DirectX applications recover, see the Windows SDK.

## <span id="Related_TDR_topics"></span><span id="related_tdr_topics"></span><span id="RELATED_TDR_TOPICS"></span>Related TDR topics


These topics describe the TDR process and registry keys that enable TDR debugging:

[Limiting Repetitive GPU Hangs and Recoveries](limiting-repetitive-gpu-hangs-and-recoveries.md)

[TDR Error Messaging](tdr-error-messaging.md)

[TDR Registry Keys](tdr-registry-keys.md)

[TDR changes in Windows 8](tdr-changes-in-windows-8.md)

 

 





