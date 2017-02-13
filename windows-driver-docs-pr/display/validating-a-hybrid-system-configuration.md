---
title: Validating a hybrid system configuration
ms.assetid: 9DB53DAB-0A3D-48A4-84C0-8D60F56B64E8
description: 
---

# Validating a hybrid system configuration


This procedure is used starting in Windows 8.1 to validate the configuration of a [hybrid system](using-cross-adapter-resources-in-a-hybrid-system.md) of display adapters:

1.  When the system boots, one of the display adapters is marked as the current POST adapter. If this POST adapter supports Windows Display Driver Model (WDDM) 1.3 and has an integrated display panel, it's considered an *integrated hybrid* adapter.
2.  A discrete adapter in a hybrid system is considered a *hybrid discrete* adapter. It must:
    -   Set the [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062).**HybridDiscrete** member.
    -   Support WDDM 1.3.
    -   Support cross-adapter resources.
    -   Have no display outputs.

3.  Only one WDDM hybrid discrete adapter is allowed on the system.
4.  When an integrated hybrid adapter is detected:
    -   Any new WDDM 1.3 display adapter (excluding an adapter that matches (2) or (3) or is a basic display or basic render driver) will not be loaded.
    -   Any loaded WDDM 1.3 display adapter (excluding an adapter that matches (2) or (3) or is a basic display or basic render driver) that is not a hybrid discrete adapter will be stopped.

5.  Drivers that support WDDM versions prior to 1.3 are allowed to load even when an integrated hybrid adapter is present.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Validating%20a%20hybrid%20system%20configuration%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




