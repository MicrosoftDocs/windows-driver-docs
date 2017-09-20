---
title: WaveCyclic Port Driver
description: WaveCyclic Port Driver
ms.assetid: c5572ae3-0d91-43a6-a49c-c6c005263f5b
keywords:
- WaveCyclic port driver WDK audio
- PortCls WDK audio , port drivers
- audio miniport drivers WDK , port drivers
- miniport drivers WDK audio , port drivers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WaveCyclic Port Driver


## <span id="wavecyclic_port_driver"></span><span id="WAVECYCLIC_PORT_DRIVER"></span>


**Important**  The use of WaveCyclic is no longer recommended, instead use WaverRT.

 

The WaveCyclic port driver manages the playback or recording of a wave stream by a DMA-based audio device that processes audio data in a cyclic buffer. This device is a hardware function on an audio adapter. Typically, the adapter is part of an integrated chipset on the motherboard or is mounted on an audio card that plugs into a PCI or ISA slot on the motherboard. The adapter driver provides a corresponding [WaveCyclic miniport driver](wavecyclic-miniport-driver.md) driver object that binds to the WaveCyclic port driver object to form a [wave filter](wave-filters.md) that can capture or render a wave stream.

The WaveCyclic port driver exposes an [IPortWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536899) interface to the miniport driver. IPortWaveCyclic inherits the methods in base interface [IPort](https://msdn.microsoft.com/library/windows/hardware/ff536842). IPortWaveCyclic provides the following additional methods:

[**IPortWaveCyclic::NewMasterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff536900)

Creates a new master DMA channel object for an audio device with a built-in DMA controller.

[**IPortWaveCyclic::NewSlaveDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff536902)

Creates a new subordinate DMA channel object for an audio device without a built-in DMA controller.

[**IPortWaveCyclic::Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536903)

Notifies the port driver that the DMA controller has advanced to a new position in the audio stream.

The WaveCyclic port and miniport driver objects communicate with each other through their respective [IPortWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536899) and [IMiniportWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536714) interfaces. In addition, the port driver communicates with the miniport driver's stream objects through their [IMiniportWaveCyclicStream](https://msdn.microsoft.com/library/windows/hardware/ff536715) interfaces.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20WaveCyclic%20Port%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


