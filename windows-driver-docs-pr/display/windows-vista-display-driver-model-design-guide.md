---
title: WDDM Overview
description: Explore the Windows Display Driver Model (WDDM), which is available in Windows Vista and later, and required in Windows 8 and later.
keywords:
- WDDM Design Guide WDK
- display driver model WDK Windows Vista
- Windows display driver model WDK
- display devices WDK
- display drivers WDK , Windows Vista
- display driver model WDK Windows Vista , about display driver model
- Windows display driver model WDK , about display driver model
- miniport drivers WDK display
- display miniport drivers WDK See miniport drivers WDK display
ms.date: 11/19/2025
ms.topic: concept-article
ai-usage: ai-assisted
---

# WDDM overview

The Windows Display Driver Model (WDDM) is the graphics display driver architecture for Windows. Microsoft introduced WDDM in Windows Vista (WDDM 1.0) and continues to evolve it with every Windows release. WDDM replaced the [legacy XDDM driver model](/previous-versions/windows/drivers/display/windows-2000-display-driver-model-design-guide) to enable advanced graphics features like the Desktop Window Manager (DWM), improved stability through fault tolerance and recovery, and better performance through efficient GPU scheduling and virtual memory management. This modern architecture enables Windows to support increasingly sophisticated graphics capabilities, from composited desktops to real-time raytracing and AI-powered graphics workloads.

Windows 8 (WDDM 1.2) requires WDDM.

## WDDM version history

The following table shows the WDDM versions and the Windows releases that introduced them:

| WDDM Version | Windows Version | Major Features |
|--------------|-----------------|----------------|
| WDDM 1.0 | Windows Vista | GPU scheduling, virtual memory management, TDR |
| WDDM 1.1 | Windows 7 | GDI hardware acceleration, Direct3D 11, multi-adapter support |
| WDDM 1.2 | Windows 8 | Stereoscopic 3D, preemptive multitasking, reduced memory footprint |
| WDDM 1.3 | Windows 8.1 | Miracast wireless displays, multi-plane overlays |
| WDDM 2.0 | Windows 10 (1507) | GPU virtual addressing, driver residency model, Direct3D 12 |
| WDDM 2.1 | Windows 10 (1607) | Shader Model 6.0, HDR10 support |
| WDDM 2.2 | Windows 10 (1703) | Virtual/mixed reality support |
| WDDM 2.3 | Windows 10 (1709) | HDR, display color space transforms |
| WDDM 2.4 | Windows 10 (1803) | GPU paravirtualization, IOMMU support, HDR improvements |
| WDDM 2.5 | Windows 10 (1809) | DirectX Raytracing (DXR), HDR brightness compensation |
| WDDM 2.6 | Windows 10 (1903) | Hardware-accelerated GPU scheduling, variable rate shading |
| WDDM 2.7 | Windows 10 (2004) | Mesh shaders, DXR 1.1, sampler feedback |
| WDDM 3.0 | Windows 11 (21H2) | WSL GPU support, Direct3D 12 video encoding |
| WDDM 3.1 | Windows 11 (22H2) | Shader Model 6.7, IOMMU DMA remapping |
| WDDM 3.2 | Windows 11 (24H2) | Shader Model 6.8, work graphs, generic programs |

For detailed information about features in each version, see the version-specific feature pages linked in the table of contents.

## Core WDDM 1.0 features

Key features introduced with WDDM 1.0 and enhanced in later versions include:

- **GPU scheduling**: Preemptive scheduling allows for better management of GPU resources because multiple applications can share the GPU more efficiently.  

- **Virtual memory management for the GPU**: Supports more complex and larger graphics workloads without running out of physical memory. Virtual memory management is enhanced in WDDM 2.0 with GPU virtual addressing.

- **Driver with both a user-mode and kernel-mode component**: Reduces the likelihood of system crashes due to driver failures.  

- **Tight integration with DirectX**: Ensures applications can use the full capabilities of modern GPUs and more complex and efficient rendering techniques.

- **Timeout detection and recovery (TDR) support**: Increases system stability.  

- **Multiple monitor support**: Enables seamless configuration and management of multi-display setups.

## WDDM 2.0 architectural improvements

WDDM 2.0, introduced in Windows 10, represents a significant architectural evolution of the display driver model. The major version increment from 1.x to 2.0 reflects fundamental changes to the memory model and driver architecture, particularly the introduction of GPU virtual addressing. This change allows each process to have its own GPU virtual address space, dramatically reducing kernel-mode driver complexity and enabling better performance and stability.

Key WDDM 2.0 improvements include:

- **[GPU virtual addressing](gpu-virtual-memory-in-wddm-2-0.md)**: Each process gets a unique GPU virtual address (GPUVA) space that every GPU context can execute in. This fundamental change enables more efficient memory management and better isolation between processes.

- **[Driver residency model](driver-residency-in-wddm-2-0.md)**: Applications have more control over which allocations should be resident in GPU memory, allowing for better performance optimization.

- **[Context monitoring](context-monitoring.md)**: Enhanced monitoring capabilities for GPU contexts improve stability and debugging.

## WDDM 3.0 architectural improvements

WDDM 3.0, introduced in Windows 11, marks an architectural milestone. The version bump from 2.x to 3.0 brings substantial improvements to the graphics subsystem architecture for Windows 11, including better integration with the Windows Subsystem for Linux (WSL), enhanced video capabilities, and foundational changes to support modern rendering techniques.

Key WDDM 3.0+ features include:

- **WSL GPU support**: User-mode driver support in WSL enables Linux applications to use GPU acceleration on Windows 11.

- **Direct3D 12 video encoding**: Hardware-accelerated video encoding capabilities integrated into the Direct3D 12 API.

- **Advanced rendering features**: Support for work graphs (WDDM 3.2), generic programs (WDDM 3.2), and shader model enhancements that enable new GPU-driven rendering techniques.

WDDM continues to evolve with each Windows release, adding support for cutting-edge graphics technologies. See the version-specific feature pages for details on what's new in each release.
