---
title: DirectSound Node-Ordering Requirements
description: DirectSound Node-Ordering Requirements
ms.assetid: baca55f5-c669-4bd2-82b5-3985030864f2
keywords:
- hardware acceleration WDK DirectSound , node-ordering requirements
- node-ordering requirements WDK DirectSound
- node chains WDK DirectSound
- SUM nodes WDK DirectSound
- 3D mixing WDK audio
- 2D mixing WDK audio
- software-emulated 3D processing WDK audio
- supermixer nodes WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectSound Node-Ordering Requirements


## <span id="directsound_node_ordering_requirements"></span><span id="DIRECTSOUND_NODE_ORDERING_REQUIREMENTS"></span>


A DirectSound 2D or 3D mixer pin should have a node chain that contains the following sequence of nodes:

-   Volume node (See [**KSNODETYPE\_VOLUME**](https://msdn.microsoft.com/library/windows/hardware/ff537208).)

-   3D node (This node is optional. See [**KSNODETYPE\_3D\_EFFECTS**](https://msdn.microsoft.com/library/windows/hardware/ff537148).)

-   Supermixer node (See [**KSNODETYPE\_SUPERMIX**](https://msdn.microsoft.com/library/windows/hardware/ff537198).)

-   Volume node (for panning effects)

-   SRC node (See [**KSNODETYPE\_SRC**](https://msdn.microsoft.com/library/windows/hardware/ff537190).)

-   SUM node (See [**KSNODETYPE\_SUM**](https://msdn.microsoft.com/library/windows/hardware/ff537196).)

The nodes in this list appear in the order in which they are encountered by data streaming into the pin. Other nodes can be interleaved between these nodes without causing problems, provided that the above ordering is preserved.

A 2D pin requires all the nodes in the previous list, except for the 3D node, which is optional. A 3D pin requires all the nodes in the list, including the 3D node.

The SRC (sample-rate conversion) node should precede the SUM node. The SRC and SUM nodes are typically adjacent, although this is not a requirement. The **IDirectSoundBuffer::SetFrequency** method (see Microsoft Windows SDK documentation) perturbs the SRC node's resampling rate.

A mixer that contains only SRC and SUM nodes is sufficient for mixing streams that are managed by system drivers such as SWMidi and Redbook (see [SWMidi System Driver](kernel-mode-wdm-audio-components.md#swmidi_system_driver) and [Redbook System Driver](kernel-mode-wdm-audio-components.md#redbook_system_driver)), but DirectSound additionally requires that two volume nodes and a supermixer node precede the SUM node. DirectSound sends volume changes resulting from **IDirectSoundBuffer::SetVolume** calls to the first volume node and sends panning effects from **IDirectSoundBuffer::SetPan** calls to the second volume node.

DirectSound can produce 3D effects on a 2D pin by using the **SetVolume**, **SetPan**, and **SetFrequency** calls to control the volume and SRC nodes:

-   **SetVolume** calls can simulate changes in the distance of a sound source from the listener.

-   **SetPan** calls can simulate changes in orientation of a sound source relative to the listener.

-   **SetFrequency** calls can simulate Doppler effects and HRTFs (head-related transfer functions).

The supermixer node is a crossbar matrix that connects M input channels to N output channels, where N should be equal to the number of channels in your device's final output stream.

The optional 3D node is required to manage hardware-accelerated 3D effects (see [Supporting 3D DirectSound Acceleration in WDM Audio](supporting-3d-directsound-acceleration-in-wdm-audio.md)), but is not needed for software-emulated 3D processing. Most existing implementations place the 3D node before the SRC node and between the first volume node and the supermixer node, but other configurations are possible.

The input stream to the 3D node typically contains a single channel. In DirectSound 8.0 and later, only mono PCM buffers can be created with 3D effects. Earlier versions of DirectSound, however, support 3D nodes with both mono and stereo input streams, and drivers should support both to ensure compatibility with older applications.

 

 




