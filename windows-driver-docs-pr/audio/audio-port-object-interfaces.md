---
title: Audio Port Object Interfaces
description: Audio Port Object Interfaces
ms.date: 11/28/2017
---

# Audio Port Object Interfaces

## <span id="ddk_audio_port_object_interfaces_ks"></span><span id="DDK_AUDIO_PORT_OBJECT_INTERFACES_KS"></span>


This section describes the audio port object interfaces. These include the following:

- **IPort**, which is the base type from which all other audio port object interfaces are derived

- The audio port object provides an interface for the DMus, MIDI, Topology, WaveCyclic, WavePci and WaveRT port drivers (see [Supporting a Device](./supporting-a-device.md)), which are derived from **IPort**

The audio port object interface is the primary interface that a port driver presents to a miniport driver. An adapter driver forms a KS filter for an audio device by binding together the port and miniport drivers for that device. The binding is accomplished by calling the audio port object's [**IPort::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iport-init) method and passing a reference to the audio miniport object as a call parameter. The code example in [Subdevice Creation](./subdevice-creation.md) illustrates this process.

This section describes the following audio port object interfaces:

[IPort](/windows-hardware/drivers/ddi/portcls/nn-portcls-iport)

[IPortClsPower](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportclspower)

[IPortDMus](/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iportdmus)

[IPortMidi](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportmidi)

[IPortTopology](/windows-hardware/drivers/ddi/portcls/nn-portcls-iporttopology)

[IPortWaveCyclic](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavecyclic)

[IPortWavePci](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavepci)

[IPortWaveRT](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavert)

[IPortWMIRegistration](/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwmiregistration)
