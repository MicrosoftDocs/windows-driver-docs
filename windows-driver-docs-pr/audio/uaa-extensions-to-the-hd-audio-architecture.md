---
title: UAA Extensions to the HD Audio Architecture
description: UAA Extensions to the HD Audio Architecture
ms.assetid: 895dc7b6-f484-4be2-8f43-112254d6ef4b
keywords: ["HD Audio, Universal Audio Architecture", "High Definition Audio (HD Audio), Universal Audio Architecture", "UAA WDK", "Universal Audio Architecture WDK"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20UAA%20Extensions%20to%20the%20HD%20Audio%20Architecture%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


