---
title: Debugging Tips for WDDM Drivers
description: Describes debugging techniques for Windows Display Driver Model (WDDM) drivers
keywords:
- Windows Display Driver Model (WDDM) , debugging
ms.date: 10/21/2024
---

# Debugging tips for WDDM drivers

This article describes a few debugging tips and tools that you can use to debug WDDM drivers.

The DirectX graphics kernel subsystem (*Dxgkrnl.sys*) records display driver-related errors, assertions, warnings, and events to an internal-use log (*Watchdog.sys*).

For tips on debugging indirect display drivers, see [Debugging Indirect Displays](indirect-display-debugging.md).

For general information about debugging drivers, see [Getting Started with Windows Debugging](../debugger/getting-started-with-windows-debugging.md).

## Change the behavior of the GPU scheduler for debugging

To help debug the driver, you can modify the behavior of the GPU scheduler by configuring the registry. The following setting allows you to enable or disable preemption requests from the GPU scheduler. For more information, see [Timeout Detection and Recovery](timeout-detection-and-recovery.md).

```registry  
Registry Key Path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler  
Key Value: EnablePreemption  
Value Type: REG_DWORD  
Value Data: 0 to disable preemption, 1 to enable preemption (default).  
```  

## Enable Direct3d to emulate state blocks  

To enable the Direct3D runtime to emulate state blocks, configure the registry in the following way:

```registry  
Registry Key Path: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Direct3D  
Key Value: EmulateStateBlocks  
Value Type: REG_DWORD  
Value Data: 1 for D3D runtime emulation of state blocks, 0 for driver implementation (default).  
```  

When emulation is enabled, the Direct3D runtime doesn't call the user-mode display driver's [**StateSet**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_stateset) function to set any state-block information.  

## Disable frame pointer omission optimization

WDDM 1.2 and later drivers must disable frame pointer omission (FPO) optimizations to improve the ability to diagnose performance problems. For more information, see [Disabling Frame Pointer Omission (FPO) Optimization](disabling-frame-pointer-omission--fpo--optimization.md).

## User-mode driver logging

A [user-mode driver logging](user-mode-driver-logging.md) interface was introduced in Windows 8 to enhance Event Tracing for Windows (ETW). This DDI offers insights into video memory usage from the API perspective, aiding in the analysis of memory-related performance issues.

## XPS rasterization on the GPU

WDDM 1.2 and later drivers must be able to pass XPS rasterization display conformance tests in order to ensure high-quality Windows printing. For more information, see [XPS Rasterization on the GPU](xps-rasterization-on-the-gpu.md).

## GPUView

[GPUView](using-gpuview.md) is a tool that you can use to analyze GPU and CPU activity on Windows systems. It can help you identify performance bottlenecks and other issues.

## Timeout Detection and Recovery (TDR)

Timeout Detection and Recovery (TDR) is a feature in Windows that is designed to detect and recover from issues that cause the GPU to stop responding. For more information, see [Timeout Detection and Recovery (TDR)](timeout-detection-and-recovery.md).
