---
title: WavePci Port Driver
description: WavePci Port Driver
ms.assetid: 3b4a89d0-f07a-40e1-8c67-62d9cfd96ddd
keywords:
- WavePci port driver WDK audio
- PortCls WDK audio , port drivers
- audio miniport drivers WDK , port drivers
- miniport drivers WDK audio , port drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




