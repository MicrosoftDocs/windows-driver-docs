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
ms.date: 07/11/2025
ms.topic: concept-article
---

# WDDM overview

The Windows Display Driver Model (WDDM) is the graphics display driver architecture for Windows. WDDM was introduced in Windows Vista (WDDM 1.0) and continues to evolve with every Windows release.

WDDM is required starting with Windows 8 (WDDM 1.2).

Key features of WDDM include:

- **GPU scheduling**: Allows for better management of GPU resources with preemptive scheduling because multiple applications can share the GPU more efficiently.  

- **Virtual memory management for the GPU**: Supports more complex and larger graphics workloads without running out of physical memory.  

- **Driver with both user-mode and kernel-mode components**: Reduces the likelihood of system crashes due to driver failures.  

- **Tight integration with DirectX**: Ensures applications can use the full capabilities of modern GPUs and more complex and efficient rendering techniques.

- **Timeout detection and recovery (TDR)**: Increases system stability.  

- **Multiple monitor support**: Enables seamless configuration and management of multi-display setups.