---
title: Disabling Frame Pointer Omission (FPO) Optimization
description: Windows Display Driver Model (WDDM) drivers must disable frame pointer omission (FPO) optimizations
keywords:
- Windows Display Driver Model (WDDM) , debugging
ms.date: 10/21/2024
---

# Disabling Frame Pointer Omission (FPO) optimization

WDDM 1.2 and later drivers must disable Frame Pointer Omission (FPO) optimizations to improve the ability to diagnose customer performance problems related to FPO. This requirement applies to both user-mode and kernel-mode display drivers.

* Minimum WDDM version: 1.2

* Minimum Windows version: 8

* Driver implementation—Full graphics, Render only, and Display only: Mandatory

* [WHLK](/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests: [WHQL FPO optimization check for kernel video driver](/windows-hardware/test/hlk/testref/8fa8a507-3867-4319-b7a3-c0460e47a819)

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.
