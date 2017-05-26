---
title: WaveCyclic Miniport Driver
description: WaveCyclic Miniport Driver
ms.assetid: 8a4811e9-e52b-4183-8d11-482883500f82
keywords:
- audio miniport drivers WDK , WaveCyclic
- miniport drivers WDK audio , WaveCyclic
- WaveCyclic miniport drivers WDK audio
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WaveCyclic Miniport Driver


## <span id="wavecyclic_miniport_driver"></span><span id="WAVECYCLIC_MINIPORT_DRIVER"></span>


**Important**  The use of WavePci is no longer recommended, instead use WaverRT.

 

A WaveCyclic miniport driver manages the hardware-dependent functions of a wave-rendering or wave-capture device that uses a cyclic buffer for audio data. The cyclic buffer is typically a single block of contiguous physical memory and can be located in a region of memory of the driver's choosing. A device with any of the following limitations should provide a WaveCyclic miniport driver rather than a [WavePci miniport driver](wavepci-miniport-driver.md):

-   The device lacks DMA hardware.

-   The device's DMA hardware can access data only in a buffer that occupies a single block of contiguous physical memory.

-   The device's DMA hardware is unable to access data in all regions of physical memory.

A WaveCyclic miniport driver should implement two interfaces:

-   **The miniport interface** supports miniport driver initialization and stream creation.

-   **The stream interface** manages a wave stream and exposes most of the miniport driver's functionality.

The miniport interface, [IMiniportWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536714), inherits the methods in the [IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698) interface. IMiniportWaveCyclic provides the following additional methods:

[**IMiniportWaveCyclic::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536722)

Initializes the miniport object.

[**IMiniportWaveCyclic::NewStream**](https://msdn.microsoft.com/library/windows/hardware/ff536723)

Creates a new stream object.

The stream interface, [IMiniportWaveCyclicStream](https://msdn.microsoft.com/library/windows/hardware/ff536715), inherits the methods in the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. IMiniportWaveCyclicStream provides the following additional methods:

[**IMiniportWaveCyclicStream::GetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536716)

Gets the device's current position in the wave stream.

[**IMiniportWaveCyclicStream::NormalizePhysicalPosition**](https://msdn.microsoft.com/library/windows/hardware/ff536717)

Converts a physical buffer position value into a time-based value.

[**IMiniportWaveCyclicStream::SetFormat**](https://msdn.microsoft.com/library/windows/hardware/ff536718)

Sets the data format of the wave stream.

[**IMiniportWaveCyclicStream::SetNotificationFreq**](https://msdn.microsoft.com/library/windows/hardware/ff536719)

Sets the frequency at which notification interrupts occur.

[**IMiniportWaveCyclicStream::SetState**](https://msdn.microsoft.com/library/windows/hardware/ff536720)

Sets the state of the wave stream.

[**IMiniportWaveCyclicStream::Silence**](https://msdn.microsoft.com/library/windows/hardware/ff536721)

Copies silence into a buffer.
 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20WaveCyclic%20Miniport%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


