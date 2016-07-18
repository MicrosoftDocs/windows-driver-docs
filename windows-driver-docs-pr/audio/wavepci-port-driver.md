---
title: WavePci Port Driver
description: WavePci Port Driver
ms.assetid: 3b4a89d0-f07a-40e1-8c67-62d9cfd96ddd
keywords: ["WavePci port driver WDK audio", "PortCls WDK audio , port drivers", "audio miniport drivers WDK , port drivers", "miniport drivers WDK audio , port drivers"]
---

# WavePci Port Driver


## <span id="wavepci_port_driver"></span><span id="WAVEPCI_PORT_DRIVER"></span>


**Important**  The use of WavePci is no longer recommended, instead use WaverRT.

 

The WavePci port driver manages the playback or recording of a wave stream by an audio device that can perform scatter/gather DMA transfers to or from any location in physical memory. With scatter/gather DMA, the device can process audio data in a buffer consisting of a series of mappings. Each mapping is a block of physically contiguous memory, but successive mappings are not necessarily contiguous to each other. The WavePci-compatible device is a hardware function on an audio adapter. Typically, the adapter is part of an integrated chipset on the motherboard or is mounted on an audio card that plugs into a PCI slot on the motherboard. The adapter driver provides a corresponding [WavePci miniport driver](wavepci-miniport-driver.md) that binds to the WavePci port driver object to form a [wave filter](wave-filters.md) that can capture or render a wave stream.

The WavePci port driver exposes an [IPortWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536905) interface to the miniport driver. IPortWavePci inherits the methods in base interface [IPort](https://msdn.microsoft.com/library/windows/hardware/ff536842). In addition, IPortWavePci provides the following methods:

[**IPortWavePci::NewMasterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff536916)

Creates a new master DMA channel object.
[**IPortWavePci::Notify**](https://msdn.microsoft.com/library/windows/hardware/ff536918)

Notifies the port driver that the DMA controller has advanced to a new position in the audio stream.
The WavePci port driver also exposes an [IPortWavePciStream](https://msdn.microsoft.com/library/windows/hardware/ff536907) interface to each of the miniport driver's stream objects. IPortWavePciStream inherits the methods in base interface [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509). IPortWavePciStream provides the following additional methods:

[**IPortWavePciStream::GetMapping**](https://msdn.microsoft.com/library/windows/hardware/ff536909)

Gets the next mapping from the port driver.
[**IPortWavePciStream::ReleaseMapping**](https://msdn.microsoft.com/library/windows/hardware/ff536911)

Releases a mapping that was previously obtained by a **GetMapping** call.
[**IPortWavePciStream::TerminatePacket**](https://msdn.microsoft.com/library/windows/hardware/ff536913)

Terminates an I/O packet even if it is only partially filled with capture data.
An I/O packet is a portion of the audio buffer consisting of all the mappings that are associated with a particular mapping IRP.

The WavePci port and miniport objects communicate with each other through their respective [IPortWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536905) and [IMiniportWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536724) interfaces. In addition, the WavePci port and miniport stream objects communicate with each other through their respective [IPortWavePciStream](https://msdn.microsoft.com/library/windows/hardware/ff536907) and [IMiniportWavePciStream](https://msdn.microsoft.com/library/windows/hardware/ff536725) interfaces.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20WavePci%20Port%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




