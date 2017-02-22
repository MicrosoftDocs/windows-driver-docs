---
title: Creating Device-Dependent Bitmaps
description: Creating Device-Dependent Bitmaps
ms.assetid: da53a8bf-5991-4abb-81f1-2d3a7cb0ff90
keywords: ["GDI WDK Windows 2000 display , bitmaps", "graphics drivers WDK Windows 2000 display , bitmaps", "drawing WDK GDI , bitmaps", "bitmaps WDK GDI", "device-specific bitmaps WDK GDI", "DDB WDK GDI"]
---

# Creating Device-Dependent Bitmaps


## <span id="ddk_creating_device_dependent_bitmaps_gg"></span><span id="DDK_CREATING_DEVICE_DEPENDENT_BITMAPS_GG"></span>


When an application requests the creation of a bitmap, a driver can create and manage a [*DDB*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-ddb) by supporting the [**DrvCreateDeviceBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff556185) function. When such a driver creates the bitmap, it can store the bitmap in any format. The driver examines the passed parameters and provides a bitmap with at least as many bits-per-pixel as requested.

**Note**   Graphics drivers can improve performance by supporting bitmaps in [*off-screen memory*](https://msdn.microsoft.com/library/windows/hardware/ff556318#wdkgloss-off-screen-memory) and by drawing bitmaps using hardware. For an example of this, see the **Permedia** display driver sample.

 

**Note**   The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia2 (*3dlabs.htm*) and 3Dlabs Permedia3 (*Perm3.htm*) sample display drivers. You can get these sample drivers from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the [DDK - Windows Driver Development Kit](http://go.microsoft.com/fwlink/p/?linkid=21859) page of the WDHC website.

 

Within **DrvCreateDeviceBitmap**, the driver calls the GDI service [**EngCreateDeviceBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff564204) to have GDI create a handle for the device bitmap.

If the driver supports **DrvCreateDeviceBitmap**, it creates a DDB, defines its format, and returns a handle to it. The driver controls where the bitmap is stored, and in what format. The driver should support the color format that matches its device surface most closely.

The contents of the bitmap are undefined after creation. If the driver returns **NULL**, it does not create and manage the bitmap; instead, GDI performs these tasks.

If the driver creates bitmaps, it must also be able to delete them by implementing the [**DrvDeleteDeviceBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff556187) function.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Creating%20Device-Dependent%20Bitmaps%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




