---
title: Supporting Multiple-Head Hardware
description: Supporting Multiple-Head Hardware
ms.assetid: ea618586-3649-405c-b1fd-78a11f14c742
keywords:
- multiple-head hardware WDK DirectX 9.0
- hardware multiple-head support WDK DirectX 9.0
- multiple-head hardware WDK DirectX 9.0 , about multiple-head hardware
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Multiple-Head Hardware


## <span id="ddk_supporting_multiple_head_hardware_gg"></span><span id="DDK_SUPPORTING_MULTIPLE_HEAD_HARDWARE_GG"></span>


A DirectX 9.0 version driver can implement multiple-head support for multiple-head cards, which have the following features:

-   Common frame buffer and accelerator for all display devices (heads) on the card.

-   Independent digital to analog converters (DAC) and monitor outputs for each display device (head).

-   More usable multiple-monitor support than a similar number of heterogeneous display cards.

-   One head control or independent operation. A single device can be exposed to an application and that device can drive several fullscreen swap chains. Consequently, all resources are shared by the many heads, and each head has exactly the same capabilities. Each head can be set to independent display modes; the application can then call the **Present** method on each head at different times. Each swap chain for a head must be fullscreen. Once the device enters multiple-head mode, it must remain fullscreen. The transition back to windowed mode requires the destruction of the device (except for the minimize operation).

Note that for DirectX 8.1 and earlier applications, a DirectX 9.0 driver should still use the former mechanism of dividing video memory between heads and treating each head as a fully independent accelerator. Only if an application is coded to function in the DirectX 9.0 multiple-head mode does the driver use these new multiple-head features. The driver is notified when to switch between the two modes of operation.

The following sections describe how drivers support multiple-head hardware.

[Identifying Adapter Group and Providing Capabilities](identifying-adapter-group-and-providing-capabilities.md)

[Creating Heads](creating-heads.md)

[Example of Handle Assignments](example-of-handle-assignments.md)

[Managing Multiple-Head Memory](managing-multiple-head-memory.md)

[Reporting Multiple-Head Video Memory](reporting-multiple-head-video-memory.md)

[Presentation with Multiple Heads](presentation-with-multiple-heads.md)

[Using Multiple Multiple-Head Adapters](using-multiple-multiple-head-adapters.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Multiple-Head%20Hardware%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




