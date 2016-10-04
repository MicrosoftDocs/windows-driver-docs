---
title: Unidrv Renderer
author: windows-driver-content
description: Unidrv Renderer
MS-HAID:
- 'nt5gpd\_a8072c6f-c3cc-452d-9b89-e02197389cf7.xml'
- 'print.unidrv\_renderer'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5c19eb9c-149b-4587-a12d-f01164231b51
keywords: ["Unidrv, renderer", "renderer WDK Unidrv", "Unidrv WDK print"]
---

# Unidrv Renderer


## <a href="" id="ddk-unidrv-renderer-gg"></a>


The Unidrv renderer is implemented as a [printer graphics DLL](printer-graphics-dll.md) and thus exports functions defined by the Microsoft Device Driver Interface (DDI) for graphics drivers. When an application calls Graphics Device Interface (GDI) functions to send images to a printer device, the kernel-mode graphics engine calls the renderer's graphics DDI functions. These graphics DDI functions assist GDI in drawing a print job's page images.

The renderer is also responsible for sending rendered image data, along with printer command sequences, to the print spooler, which then directs the images and commands to printer hardware. The printer commands that the renderer sends are specified in [Unidrv Minidrivers](unidrv-minidrivers.md).

You can modify Unidrv's rendering operations by providing a [rendering plug-in](rendering-plug-ins.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Unidrv%20Renderer%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


