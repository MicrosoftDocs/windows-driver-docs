---
title: Programming Guidelines
description: Programming Guidelines
ms.assetid: 289bdf85-9138-4920-a61f-050c51077d3e
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Programming Guidelines


This section presents programming guidelines for using the HD Audio DDI versions (as defined by the [**HDAUDIO\_BUS\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536413), [**HDAUDIO\_BUS\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff536418) and [**HDAUDIO\_BUS\_INTERFACE\_BDL**](https://msdn.microsoft.com/library/windows/hardware/ff536416) structures) to control audio and modem codecs that are connected to an HD Audio bus interface controller.

The HD Audio bus driver exposes one or both versions of the HD Audio DDI to its children, which are kernel-mode function drivers for the audio and modem codecs. (One of these children might be the UAA HD Audio class driver.) These drivers call the routines in the DDIs to access the hardware capabilities of the HD Audio controller device.

This section includes:

[Differences Between the HD Audio DDI Versions](differences-between-the-hd-audio-ddi-versions.md)

[Synchronous and Asynchronous Codec Commands](synchronous-and-asynchronous-codec-commands.md)

[Wall Clock and Link Position Registers](wall-clock-and-link-position-registers.md)

[Hardware Resource Management](hardware-resource-management.md)

[Synchronizing Two or More Streams](synchronizing-two-or-more-streams.md)

[Wake Enable](wake-enable.md)

[Data Copying and Caching Policy](data-copying-and-caching-policy.md)

[Querying for an HD Audio DDI](querying-for-an-hd-audio-ddi.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Programming%20Guidelines%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


