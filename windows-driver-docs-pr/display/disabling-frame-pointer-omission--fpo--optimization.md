---
title: Disabling Frame Pointer Omission (FPO) optimization
description: In Windows 7, Windows Display Driver Model (WDDM) 1.1 kernel-mode drivers are required to disable Frame Pointer Omission (FPO) optimizations to improve the ability to diagnose performance problems.
ms.assetid: ABA1A097-D9AA-41F4-90D4-B2FBB9B08534
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Disabling Frame Pointer Omission (FPO) optimization


In Windows 7, Windows Display Driver Model (WDDM) 1.1 kernel-mode drivers are required to disable Frame Pointer Omission (FPO) optimizations to improve the ability to diagnose performance problems. Starting with Windows 8, the same requirement is applicable for all WDDM 1.2 and later drivers (user-mode and kernel-mode), thereby making it easier to debug performance issues related to FPO in the field.

|                                                                                   |                                                                                    |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Minimum WDDM version                                                              | 1.2                                                                                |
| Minimum Windows version                                                           | 8                                                                                  |
| Driver implementation—Full graphics, Render only, and Display only                | Mandatory                                                                          |
| [WHCK]( http://go.microsoft.com/fwlink/p/?linkid=258342) requirements and tests | **Device.Graphicsâ€¦WHQL FPO optimization check for kernel video driver(s) (1.1)** |

 

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation]( http://go.microsoft.com/fwlink/p/?linkid=258342) on **Device.Graphicsâ€¦WHQL FPO optimization check for kernel video driver(s) (1.1)**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 





