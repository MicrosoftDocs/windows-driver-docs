---
title: Disabling Frame Pointer Omission (FPO) optimization
description: In Windows 7, Windows Display Driver Model (WDDM) 1.1 kernel-mode drivers are required to disable Frame Pointer Omission (FPO) optimizations to improve the ability to diagnose performance problems.
ms.assetid: ABA1A097-D9AA-41F4-90D4-B2FBB9B08534
ms.author: windows-driver-content
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Disabling%20Frame%20Pointer%20Omission%20%28FPO%29%20optimization%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




