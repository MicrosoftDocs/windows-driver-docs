---
title: Transparency in Display Drivers
description: Transparency in Display Drivers
ms.assetid: 566706fb-66bd-44f5-b98c-23ed60e27970
keywords: ["display drivers WDK Windows 2000 , transparency", "transparency WDK Windows 2000 display"]
---

# Transparency in Display Drivers


## <span id="ddk_transparency_in_display_drivers_gg"></span><span id="DDK_TRANSPARENCY_IN_DISPLAY_DRIVERS_GG"></span>


If the display hardware supports transparency, the display driver should implement [**DrvTransparentBlt**](https://msdn.microsoft.com/library/windows/hardware/ff557283).

To reduce the cost of reading from video memory, drivers should implement this function when both the source and destination surfaces are in video memory. Drivers should let GDI process transparent bit-block transfers from system memory to video memory, and let GDI handle stretched bit-block transfers as well.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Transparency%20in%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




