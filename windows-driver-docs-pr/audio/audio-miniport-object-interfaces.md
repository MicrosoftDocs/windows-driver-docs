---
title: Audio Miniport Object Interfaces
description: Audio Miniport Object Interfaces
ms.assetid: 2e79ad90-fecc-47a7-b487-809325a16239
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Audio Miniport Object Interfaces


## <span id="ddk_audio_miniport_object_interfaces_ks"></span><span id="DDK_AUDIO_MINIPORT_OBJECT_INTERFACES_KS"></span>


This section describes the audio miniport object interfaces. These include the following:

-   **IMiniport**, which is the base type from which all other audio miniport object interfaces are derived

-   The audio miniport object provides an interface for the DMus, MIDI, Topology, WaveCyclic, WavePci and WaveRT miniport drivers (see [Supporting a Device](https://msdn.microsoft.com/library/windows/hardware/ff538398)), which are derived from **IMiniport**

The audio miniport object interface is the primary interface that a miniport driver presents to a port driver. An adapter driver forms a KS filter for an audio device by binding together the port and miniport drivers for that device. The binding is accomplished by calling the audio port object's [**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943) method and passing a reference to the audio miniport object as a call parameter. The code example in [Subdevice Creation](https://msdn.microsoft.com/library/windows/hardware/ff538390) illustrates this process.

This section discusses the following audio miniport object interfaces:

[IMiniport](https://msdn.microsoft.com/library/windows/hardware/ff536698)

[IMiniportDMus](https://msdn.microsoft.com/library/windows/hardware/ff536699)

[IMiniportMidi](https://msdn.microsoft.com/library/windows/hardware/ff536703)

[IMiniportTopology](https://msdn.microsoft.com/library/windows/hardware/ff536712)

[IMiniportWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536714)

[IMiniportWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536724)

[IMiniportWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536737)

 

 





