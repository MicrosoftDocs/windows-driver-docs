---
title: Plotter Driver Capabilities
author: windows-driver-content
description: Plotter Driver Capabilities
ms.assetid: 9fc32297-504c-453d-967b-ca4a4e56eaa2
keywords:
- Plotter Driver WDK print , capabilities
- MSPlot WDK print , capabilities
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Plotter Driver Capabilities


## <a href="" id="ddk-plotter-driver-capabilities-gg"></a>


The Microsoft Plotter Driver (MSPlot) provides the following capabilities:

-   Support for all plotters that use the HPGL/2 version of the Hewlett-Packard Graphics Language, by means of plotter model-specific [plotter driver minidrivers](plotter-driver-minidrivers.md).

-   A [plotter driver user interface](plotter-driver-user-interface.md), based on the TreeView control and property sheets, that is consistent for all plotters.

-   A [plotter driver renderer](plotter-driver-renderer.md) that, along with the GDI graphics engine, converts Win32 GDI calls from applications into printer commands that can be sent to the print spooler.

To provide support for a new HPGL/2-compliant device type, all you need to do is provide a minidriver that describes the device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Plotter%20Driver%20Capabilities%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


