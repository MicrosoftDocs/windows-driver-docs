---
title: WDDM 2.0 Features
description: Lists the features and enhancements introduced in WDDM 2.0, which is designed to improve the performance and capabilities of the Windows Display Driver Model.
keywords:
- WDDM 2.0 , virtual memory , driver residency , context monitoring
- WDDM 2.0 , Windows 10
ms.date: 12/16/2024
---

# WDDM 2.0 features

WDDM 2.0 was introduced starting with Windows 10. It includes several new features and enhancements that are designed to improve the performance and capabilities of the Windows Display Driver Model (WDDM), such as:

* [GPU virtual addressing](gpu-virtual-memory-in-wddm-2-0.md), where each process is assigned a unique GPU virtual address (GPUVA) space that every GPU context can execute in.

* [Driver residency](driver-residency-in-wddm-2-0.md), where residency is moved to an explicit list on the device instead of the per-command buffer list. The video memory manager (*VidMm*) ensures that all allocations on a particular device residency requirement list are resident before any contexts belonging to that device are scheduled for execution.

* [Context monitoring](context-monitoring.md), which allows for flexible synchronization between GPU engines, or across CPU cores and GPU engines. A monitored fence object, which is an advanced form of fence synchronization, allows either a CPU core or a GPU engine to signal or wait on a particular fence object.
