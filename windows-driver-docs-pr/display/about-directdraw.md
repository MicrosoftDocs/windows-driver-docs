---
title: About DirectDraw
description: About DirectDraw
ms.assetid: f2ab4863-8ec8-4eaf-b59f-635570aef470
keywords: ["drawing WDK DirectDraw , about DirectDraw", "DirectDraw WDK Windows 2000 display , about DirectDraw", "tears WDK DirectDraw", "screen flicker WDK DirectDraw", "GDI WDK DirectDraw"]
---

# About DirectDraw


## <span id="ddk_about_directdraw_gg"></span><span id="DDK_ABOUT_DIRECTDRAW_GG"></span>


Microsoft DirectDraw is the display component of Microsoft DirectX that allows software designers to directly manipulate display memory, hardware blitters, hardware overlays, and flipping surfaces. DirectDraw provides a device-independent way for games and Windows subsystem software, such as 3D graphics packages and digital video codecs, to gain access to the features of specific display devices.

DirectDraw provides device-independent access to the device-specific display functionality in a direct 32-bit path. DirectDraw calls important functions in a driver that accesses the display card directly, without the intervention of the Windows graphics device interface (GDI) or the device-independent bitmap (DIB) engine.

By taking advantage of this direct path, games and other display-intensive applications run faster and avoid tearing. A *tear* is a screen flicker caused by an image displayed and written to at the same time. Direct access often allows game performance to be limited solely by display card performance. DirectDraw also uses page flipping to provide smooth animation.

The rapid motion and ever-changing screens of many games and multimedia applications put a heavy burden on the display process and tend to exacerbate tearing. Although GDI is very fast at drawing spreadsheets, graphs, TrueType font rendering, and so on, it is not meant to be a real-time graphics API. DirectDraw augments GDI by handling the device-dependent hardware accelerator functions in a 32-bit driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20About%20DirectDraw%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




