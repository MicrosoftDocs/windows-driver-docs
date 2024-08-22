---
title: WDDM Overview
description: The Windows Display Driver Model (WDDM) is available starting with Windows Vista and is required starting with Windows 8.
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
ms.date: 08/21/2024
---

# WDDM overview

The Windows Display Driver Model (WDDM) is the graphics display driver architecture for Windows. It was introduced in Windows Vista (WDDM 1.0) and continues to evolve with every Windows release.

WDDM is required starting with Windows 8 (WDDM 1.2).

Key features of WDDM include:

* WDDM supports GPU scheduling. Preemptive scheduling allows for better management of GPU resources since multiple applications can share the GPU more efficiently.  

* WDDM supports virtual memory management for the GPU, allowing for more complex and larger graphics workloads without running out of physical memory.  

* A WDDM driver consists of both a user-mode and kernel-mode component, reducing the likelihood of system crashes due to driver failures.  

* WDDM is tightly integrated with DirectX. This integration ensures that applications can use the full capabilities of modern GPUs and more complex and efficient rendering techniques.

* WDDM supports TDR (timeout detection and recovery), thus increasing system stability.  

* WDDM supports multiple monitors, allowing for seamless configuration and management of multi-display setups.
