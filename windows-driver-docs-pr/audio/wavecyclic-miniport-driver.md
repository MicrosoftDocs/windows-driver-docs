---
Description: WaveCyclic Miniport Driver
MS-HAID: 'audio.wavecyclic\_miniport\_driver'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: WaveCyclic Miniport Driver
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

The miniport interface, [IMiniportWaveCyclic](audio.iminiportwavecyclic), inherits the methods in the [IMiniport](audio.iminiport) interface. IMiniportWaveCyclic provides the following additional methods:

[**IMiniportWaveCyclic::Init**](audio.iminiportwavecyclic_init)

Initializes the miniport object.
[**IMiniportWaveCyclic::NewStream**](audio.iminiportwavecyclic_newstream)

Creates a new stream object.
The stream interface, [IMiniportWaveCyclicStream](audio.iminiportwavecyclicstream), inherits the methods in the [**IUnknown**](com.iunknown) interface. IMiniportWaveCyclicStream provides the following additional methods:

[**IMiniportWaveCyclicStream::GetPosition**](audio.iminiportwavecyclicstream_getposition)

Gets the device's current position in the wave stream.
[**IMiniportWaveCyclicStream::NormalizePhysicalPosition**](audio.iminiportwavecyclicstream_normalizephysicalposition)

Converts a physical buffer position value into a time-based value.
[**IMiniportWaveCyclicStream::SetFormat**](audio.iminiportwavecyclicstream_setformat)

Sets the data format of the wave stream.
[**IMiniportWaveCyclicStream::SetNotificationFreq**](audio.iminiportwavecyclicstream_setnotificationfreq)

Sets the frequency at which notification interrupts occur.
[**IMiniportWaveCyclicStream::SetState**](audio.iminiportwavecyclicstream_setstate)

Sets the state of the wave stream.
[**IMiniportWaveCyclicStream::Silence**](audio.iminiportwavecyclicstream_silence)

Copies silence into a buffer.
 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20WaveCyclic%20Miniport%20Driver%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


