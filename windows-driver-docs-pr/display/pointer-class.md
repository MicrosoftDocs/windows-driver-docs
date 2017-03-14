---
title: Pointer Class
description: Pointer Class
ms.assetid: c988535a-d218-48de-bdc2-56a620bbe4a2
keywords: ["pointer class WDK display"]
---

# Pointer Class


The Windows Display Driver Model (WDDM) does not permit a call into one of the pointer class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions at a given time:

-   [*DxgkDdiSetPointerPosition*](https://msdn.microsoft.com/library/windows/hardware/ff560757)

-   [*DxgkDdiSetPointerShape*](https://msdn.microsoft.com/library/windows/hardware/ff560762)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Pointer%20Class%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




