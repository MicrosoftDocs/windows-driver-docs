---
Description: Synchronizing Two or More Streams
MS-HAID: 'audio.synchronizing\_two\_or\_more\_streams'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Synchronizing Two or More Streams
---

# Synchronizing Two or More Streams


The [**SetDmaEngineState**](audio.setdmaenginestate) routine sets the state of one or more DMA engines to one of the following: running, paused, stopped, or reset. If a call to this routine specifies more than one DMA engine, then all of the DMA engines make the state transition synchronously.

The ability to synchronize a group of streams is required for some audio applications. For example, an audio driver might use codec-combining to create a logical surround-sound audio device that joins two audio codecs: one codec drives the front speakers and a second audio codec drives the back speakers. Depending on the capabilities of the codecs, the audio driver might be required to split the original surround-sound audio stream into two streams, one for each codec. By using the [**SetDmaEngineState**](audio.setdmaenginestate) routine to start and stop the streams in unison, the two streams can remain synchronized.

Allowing the two streams to fall out of synchronization by even a few samples might cause undesirable audio artifacts.

The [**SetDmaEngineState**](audio.setdmaenginestate) routine is available in both versions of the HD Audio DDI.

The UAA HD Audio class driver does not perform codec-combining.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Synchronizing%20Two%20or%20More%20Streams%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


