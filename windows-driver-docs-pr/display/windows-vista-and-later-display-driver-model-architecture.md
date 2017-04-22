---
title: Windows Display Driver Model (WDDM) Architecture
description: Windows Display Driver Model (WDDM) Architecture
ms.assetid: 1ae66fd3-8497-4098-9899-c2363671c2b0
keywords:
- display driver model WDK Windows Vista , architecture
- Windows Vista display driver model WDK , architecture
- architecture WDK display
- user-mode display drivers WDK Windows Vista , architecture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows Display Driver Model (WDDM) Architecture


## <span id="ddk_longhorn_display_driver_model_architecture_gg"></span><span id="DDK_LONGHORN_DISPLAY_DRIVER_MODEL_ARCHITECTURE_GG"></span>


The display driver model architecture for the Windows Display Driver Model (WDDM), available starting with Windows Vista, is composed of user-mode and kernel-mode parts. The following figure shows the architecture required to support WDDM.

![diagram illustrating the wddm architecture](images/dx10arch.png)

A graphics hardware vendor must supply the user-mode display driver and the display miniport driver. The user-mode display driver is a dynamic-link library (DLL) that is loaded by the Microsoft Direct3D runtime. The display [*miniport driver*](https://msdn.microsoft.com/library/windows/hardware/ff556308#wdkgloss-miniport-driver) communicates with the Microsoft DirectX graphics kernel subsystem. For more information about the user-mode display driver and display miniport driver, see the [Windows Display Driver Model (WDDM) Reference](https://msdn.microsoft.com/library/windows/hardware/ff570595).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windows%20Display%20Driver%20Model%20%28WDDM%29%20Architecture%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




