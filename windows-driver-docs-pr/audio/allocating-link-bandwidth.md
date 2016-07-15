---
Description: Allocating Link Bandwidth
MS-HAID: 'audio.allocating\_link\_bandwidth'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Allocating Link Bandwidth
---

# Allocating Link Bandwidth


The HD Audio Link has a finite amount of bus bandwidth available for render and capture streams to use. To ensure glitchless audio, the HD Audio bus driver manages bus bandwidth as a shared resource. When a function driver allocates a DMA engine, it must also allocate a portion of the available bus bandwidth for the DMA engine's render or capture stream to use.

A fixed amount of bus bandwidth is available on the HD Audio Link's serial data in (SDI) lines and on the serial data out (SDO) lines. The HD Audio bus driver monitors bandwidth consumption separately on the SDI and SDO lines. If a request to allocate input or output bus bandwidth exceeds the available bandwidth, the bus driver fails the request.

When the function driver calls the bus driver's [**AllocateCaptureDmaEngine**](audio.allocatecapturedmaengine) and [**AllocateRenderDmaEngine**](audio.allocaterenderdmaengine) routines, it specifies a stream format. The stream format specifies the stream's sample rate, sample size, and number of channels. From this information, the Allocate*Xxx*DmaEngine routine determines the stream's bus bandwidth requirements. If sufficient bandwidth is available, the routine allocates the required bandwidth for the DMA engine to use. Otherwise, the call to Allocate*Xxx*DmaEngine fails.

A function driver can call [**ChangeBandwidthAllocation**](audio.changebandwidthallocation) to request a change in the bandwidth allocation for an existing DMA engine allocation.

The Allocate*Xxx*DmaEngine and [**ChangeBandwidthAllocation**](audio.changebandwidthallocation) routines are available in both versions of the HD Audio DDI.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Allocating%20Link%20Bandwidth%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


