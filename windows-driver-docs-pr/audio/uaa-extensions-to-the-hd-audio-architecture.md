---
title: UAA Extensions to the HD Audio Architecture
description: UAA Extensions to the HD Audio Architecture
ms.assetid: 895dc7b6-f484-4be2-8f43-112254d6ef4b
keywords:
- HD Audio, Universal Audio Architecture
- High Definition Audio (HD Audio), Universal Audio Architecture
- UAA WDK
- Universal Audio Architecture WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UAA Extensions to the HD Audio Architecture


To be UAA-compliant, a hardware controller must implement the following change to the *Intel High Definition Audio Specification*:

-   A UAA device must support 256 entries each for the command output ring buffer (CORB) and the response input ring buffer (RIRB).

In addition, the Intel HD Audio architecture includes several features that are not required to implement a UAA-compliant HD Audio device. As an option, hardware vendors can omit the following features from their HD Audio devices and remain UAA-compliant:

-   DMA position lower base address (DPLBASE) and DMA position upper base address (DPUBASE) registers (at offsets 70h and 74h).

-   Immediate command output, immediate response input, and immediate command status registers (at offsets 60h, 64h, and 68h).

-   Flush control bit in the global control register (at offset 08h).

A bus controller design can omit these features and still be fully compatible with the HD Audio bus driver. However, a hardware vendor should consider whether these features might be necessary for compatibility with other device-specific software. For example, a BIOS routine might use the immediate command, response, and status registers.

For UAA version 1.0, the HD Audio hardware version must be 1.0. (The VMAJ and VMIN registers must specify a major version number of 01h and a minor version number of 00h.)

 

 




