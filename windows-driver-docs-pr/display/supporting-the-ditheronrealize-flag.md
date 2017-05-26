---
title: Supporting the DitherOnRealize Flag
description: Supporting the DitherOnRealize Flag
ms.assetid: 2a480045-ed2e-4650-80a4-a374f0388591
keywords:
- display drivers WDK Windows 2000 , dithering
- DrvDitherColor
- dithering WDK Windows 2000 display
- color dithering WDK Windows 2000 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting the DitherOnRealize Flag


## <span id="ddk_supporting_the_ditheronrealize_flag_gg"></span><span id="DDK_SUPPORTING_THE_DITHERONREALIZE_FLAG_GG"></span>


In earlier versions of GDI and the graphics DDI, two calls by GDI to display driver functions were required to dither a specified color and then realize a brush for that color. For example, when an application requests that a rectangle be filled with a dithered color, GDI typically calls [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180), passing the extents of the rectangle and the brush object to use. The display driver then checks the brush, finds that it has not been realized, and calls back to GDI with [**BRUSHOBJ\_pvGetRbrush**](https://msdn.microsoft.com/library/windows/hardware/ff538264) for GDI's realization of the brush. Because the display driver, not GDI, performs the dithering of a brush, GDI passes the RGB that the application originally supplied for dithering in a [**DrvDitherColor**](https://msdn.microsoft.com/library/windows/hardware/ff556202) callback to the display driver.

*DrvDitherColor* returns a pointer to an array of color indexes that describe the dither information for the supplied color back to GDI. GDI immediately passes this dither information back to the display driver in a call to [**DrvRealizeBrush**](https://msdn.microsoft.com/library/windows/hardware/ff556273). With the [**BRUSHOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff538261) realized, control returns back to GDI and subsequently back to the original *DrvBitBlt* function.

To accomplish dithering using the above technique, GDI must call *DrvDitherColor*, followed immediately by a call to *DrvRealizeBrush* -- two separate function calls. Setting a GCAPS\_DITHERONREALIZE flag in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure and modifying *DrvRealizeBrush* to effectively combine these two functions eliminates the need for the separate call to *DrvDitherColor* and also saves some memory allocation. Under this scheme, if the display driver sets GCAPS\_DITHERONREALIZE, GDI calls *DrvRealizeBrush* with the RGB to be dithered and with the RB\_DITHERCOLOR flag set in *iHatch*. The RB\_DITHERCOLOR flag is set in the high byte of *iHatch*, while the RGB color to be dithered is contained in the three low-order bytes. The need to call *DrvDitherColor* is eliminated in this situation because the functionality of both calls is put into one.

For example code, refer to the *Permedia* sample display drivers.

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia2 (*3dlabs.htm*) and 3Dlabs Permedia3 (*Perm3.htm*) sample display drivers. You can get these sample drivers from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the [DDK - Windows Driver Development Kit](http://go.microsoft.com/fwlink/p/?linkid=21859) page of the WDHC website.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20the%20DitherOnRealize%20Flag%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




