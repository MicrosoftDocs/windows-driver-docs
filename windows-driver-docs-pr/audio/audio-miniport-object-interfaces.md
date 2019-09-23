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

-   The audio miniport object provides an interface for the DMus, MIDI, Topology, WaveCyclic, WavePci and WaveRT miniport drivers (see [Supporting a Device](https://docs.microsoft.com/windows-hardware/drivers/audio/supporting-a-device)), which are derived from **IMiniport**

The audio miniport object interface is the primary interface that a miniport driver presents to a port driver. An adapter driver forms a KS filter for an audio device by binding together the port and miniport drivers for that device. The binding is accomplished by calling the audio port object's [**IPort::Init**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nf-portcls-iport-init) method and passing a reference to the audio miniport object as a call parameter. The code example in [Subdevice Creation](https://docs.microsoft.com/windows-hardware/drivers/audio/subdevice-creation) illustrates this process.

This section discusses the following audio miniport object interfaces:

[IMiniport](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nn-portcls-iminiport)

[IMiniportDMus](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/dmusicks/nn-dmusicks-iminiportdmus)

[IMiniportMidi](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nn-portcls-iminiportmidi)

[IMiniportTopology](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nn-portcls-iminiporttopology)

[IMiniportWaveCyclic](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nn-portcls-iminiportwavecyclic)

[IMiniportWavePci](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nn-portcls-iminiportwavepci)

[IMiniportWaveRT](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/portcls/nn-portcls-iminiportwavert)

 

 





