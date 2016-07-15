---
Description: Topology Port Driver
MS-HAID: 'audio.topology\_port\_driver'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Topology Port Driver
---

# Topology Port Driver


## <span id="topology_port_driver"></span><span id="TOPOLOGY_PORT_DRIVER"></span>


The Topology port driver exposes the topology of the audio adapter's mixing hardware. For example, the hardware that mixes the playback streams from the wave renderer and MIDI synthesizer in a typical adapter can be modeled as a set of control nodes (volume, mute, and sum) plus the data paths that connect the nodes. This topology is exposed as a set of controls and mixer lines by the Windows multimedia mixer API (see [Kernel Streaming Topology to Audio Mixer API Translation](kernel-streaming-topology-to-audio-mixer-api-translation.md)). The adapter driver provides a corresponding [Topology miniport driver](topology-miniport-driver.md) that binds to the Topology port driver to form a [topology filter](topology-filters.md).

The Topology port driver exposes an [IPortTopology](audio.iporttopology) interface to the miniport driver. IPortTopology inherits the methods from base interface [IPort](audio.iport); it provides no additional methods.

The Topology port and miniport driver objects communicate with each other through their respective [IPortTopology](audio.iporttopology) and [IMiniportTopology](audio.iminiporttopology) interfaces.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Topology%20Port%20Driver%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


