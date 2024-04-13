---
title: Disabling Frame Pointer Omission (FPO) Optimization
description: In Windows 7, Windows Display Driver Model (WDDM) 1.1 kernel-mode drivers are required to disable Frame Pointer Omission (FPO) optimizations to improve the ability to diagnose performance problems.
ms.date: 04/20/2017
---

# Disabling Frame Pointer Omission (FPO) optimization


In Windows 7, Windows Display Driver Model (WDDM) 1.1 kernel-mode drivers are required to disable Frame Pointer Omission (FPO) optimizations to improve the ability to diagnose performance problems. Starting with Windows 8, the same requirement is applicable for all WDDM 1.2 and later drivers (user-mode and kernel-mode), thereby making it easier to debug performance issues related to FPO in the field.

**Minimum WDDM version**: 1.2

**Minimum Windows version**: 8

**Driver implementation—Full graphics, Render only, and Display only**: Mandatory

**[WHCK](/windows-hardware/test/hlk/windows-hardware-lab-kit) requirements and tests**: [WHQL FPO optimization check for kernel video driver](/windows-hardware/test/hlk/testref/2ad364ea-73db-47b6-a627-dea13e7c17d2)


 

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) on [WHQL FPO optimization check for kernel video driver](/windows-hardware/test/hlk/testref/2ad364ea-73db-47b6-a627-dea13e7c17d2).

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

