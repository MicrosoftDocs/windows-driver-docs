---
title: Creating Device-Dependent Bitmaps
description: Creating Device-Dependent Bitmaps
keywords:
- GDI WDK Windows 2000 display , bitmaps
- graphics drivers WDK Windows 2000 display , bitmaps
- drawing WDK GDI , bitmaps
- bitmaps WDK GDI
- device-specific bitmaps WDK GDI
- DDB WDK GDI
ms.date: 04/20/2017
---

# Creating Device-Dependent Bitmaps


## <span id="ddk_creating_device_dependent_bitmaps_gg"></span><span id="DDK_CREATING_DEVICE_DEPENDENT_BITMAPS_GG"></span>

When an application requests the creation of a bitmap, a driver can create and manage a [*DDB*](/windows/desktop/gdi/device-dependent-bitmaps) by supporting the [**DrvCreateDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-drvcreatedevicebitmap) function. When such a driver creates the bitmap, it can store the bitmap in any format. The driver examines the passed parameters and provides a bitmap with at least as many bits-per-pixel as requested.

> [!NOTE]
> Graphics drivers can improve performance by supporting bitmaps in [*off-screen memory*](video-present-network-terminology.md#off_screen_memory) and by drawing bitmaps using hardware. For an example of this, see the **Permedia** display driver sample.


> [!NOTE]
> The Microsoft Windows Driver Kit (WDK) does not contain the 3Dlabs Permedia2 (*3dlabs.htm*) and 3Dlabs Permedia3 (*Perm3.htm*) sample display drivers. You can get these sample drivers from the Windows Server 2003 SP1 Driver Development Kit (DDK), which you can download from the DDK - Windows Driver Development Kit page of the WDHC website.

Within **DrvCreateDeviceBitmap**, the driver calls the GDI service [**EngCreateDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-engcreatedevicebitmap) to have GDI create a handle for the device bitmap.

If the driver supports **DrvCreateDeviceBitmap**, it creates a DDB, defines its format, and returns a handle to it. The driver controls where the bitmap is stored, and in what format. The driver should support the color format that matches its device surface most closely.

The contents of the bitmap are undefined after creation. If the driver returns **NULL**, it does not create and manage the bitmap; instead, GDI performs these tasks.

If the driver creates bitmaps, it must also be able to delete them by implementing the [**DrvDeleteDeviceBitmap**](/windows/win32/api/winddi/nf-winddi-drvdeletedevicebitmap) function.

 

