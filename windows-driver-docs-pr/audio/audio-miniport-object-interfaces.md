---
title: Audio Miniport Object Interfaces
description: Audio Miniport Object Interfaces
ms.date: 03/06/2023
ms.topic: reference
---


# Audio Miniport Object Interfaces


## <span id="ddk_audio_miniport_object_interfaces_ks"></span><span id="DDK_AUDIO_MINIPORT_OBJECT_INTERFACES_KS"></span>


This section describes the audio miniport object interfaces. These include the following:

-   **IMiniport**, which is the base type from which all other audio miniport object interfaces are derived

-   The audio miniport object provides an interface for the DMus, MIDI, Topology, WaveCyclic, WavePci and WaveRT miniport drivers (see [Supporting a Device](./supporting-a-device.md)), which are derived from **IMiniport**

The audio miniport object interface is the primary interface that a miniport driver presents to a port driver. An adapter driver forms a KS filter for an audio device by binding together the port and miniport drivers for that device. The binding is accomplished by calling the audio port object's [**IPort::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iport-init) method and passing a reference to the audio miniport object as a call parameter. The code example in [Subdevice Creation](./subdevice-creation.md) illustrates this process.

This section discusses the following audio miniport object interfaces:

[IMiniport](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiport)

[IMiniportDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iminiportdmus)

[IMiniportMidi](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportmidi)

[IMiniportTopology](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiporttopology)

[IMiniportWaveCyclic](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavecyclic)

[IMiniportWavePci](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavepci)

[IMiniportWaveRT](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavert)

 

