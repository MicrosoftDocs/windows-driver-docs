---
title: Handling the E\_INVALIDARG Return Value
description: Handling the E\_INVALIDARG Return Value
ms.assetid: 312b2452-71b3-4fbe-93fb-f4b0e6099c0f
keywords:
- user-mode display drivers WDK Windows Vista , E_INVALIDARG return value
- E_INVALIDARG return value WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling the E\_INVALIDARG Return Value


Typically, a user-mode display driver cannot fail any of its [functions](https://msdn.microsoft.com/library/windows/hardware/ff570118) by returning E\_INVALIDARG. However, if the user-mode display driver receives the E\_INVALIDARG return value when it calls one of the [Microsoft Direct3D runtime-supplied functions](https://msdn.microsoft.com/library/windows/hardware/ff552862) (because of a programming error in the driver or malicious code that runs in the operating system), the driver must return E\_INVALIDARG back to the Direct3D runtime after the runtime calls one of the driver's functions. Otherwise, the user-mode display driver should never return E\_INVALIDARG to the Direct3D runtime.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20the%20E_INVALIDARG%20Return%20Value%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




