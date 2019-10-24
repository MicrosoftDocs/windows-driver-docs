---
title: Audio Port Object Interfaces
description: Audio Port Object Interfaces
ms.assetid: 16026a03-4859-4fe8-a106-0d8a2b2a7f14
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Audio Port Object Interfaces


## <span id="ddk_audio_port_object_interfaces_ks"></span><span id="DDK_AUDIO_PORT_OBJECT_INTERFACES_KS"></span>


This section describes the audio port object interfaces. These include the following:

-   **IPort**, which is the base type from which all other audio port object interfaces are derived

-   The audio port object provides an interface for the DMus, MIDI, Topology, WaveCyclic, WavePci and WaveRT port drivers (see [Supporting a Device](https://docs.microsoft.com/windows-hardware/drivers/audio/supporting-a-device)), which are derived from **IPort**

The audio port object interface is the primary interface that a port driver presents to a miniport driver. An adapter driver forms a KS filter for an audio device by binding together the port and miniport drivers for that device. The binding is accomplished by calling the audio port object's [**IPort::Init**](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nf-portcls-iport-init) method and passing a reference to the audio miniport object as a call parameter. The code example in [Subdevice Creation](https://docs.microsoft.com/windows-hardware/drivers/audio/subdevice-creation) illustrates this process.

This section describes the following audio port object interfaces:

[IPort](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nn-portcls-iport)

[IPortClsPower](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nn-portcls-iportclspower)

[IPortDMus](https://docs.microsoft.com/windows-hardware/drivers/ddi/dmusicks/nn-dmusicks-iportdmus)

[IPortMidi](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nn-portcls-iportmidi)

[IPortTopology](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nn-portcls-iporttopology)

[IPortWaveCyclic](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavecyclic)

[IPortWavePci](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff536905(v=vs.85))

[IPortWaveRT](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwavert)

[IPortWMIRegistration](https://docs.microsoft.com/windows-hardware/drivers/ddi/portcls/nn-portcls-iportwmiregistration)

 

 





