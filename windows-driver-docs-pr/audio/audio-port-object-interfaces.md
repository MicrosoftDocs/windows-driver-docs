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

-   The audio port object provides an interface for the DMus, MIDI, Topology, WaveCyclic, WavePci and WaveRT port drivers (see [Supporting a Device](https://msdn.microsoft.com/library/windows/hardware/ff538398)), which are derived from **IPort**

The audio port object interface is the primary interface that a port driver presents to a miniport driver. An adapter driver forms a KS filter for an audio device by binding together the port and miniport drivers for that device. The binding is accomplished by calling the audio port object's [**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943) method and passing a reference to the audio miniport object as a call parameter. The code example in [Subdevice Creation](https://msdn.microsoft.com/library/windows/hardware/ff538390) illustrates this process.

This section describes the following audio port object interfaces:

[IPort](https://msdn.microsoft.com/library/windows/hardware/ff536842)

[IPortClsPower](https://msdn.microsoft.com/library/windows/hardware/ff536844)

[IPortDMus](https://msdn.microsoft.com/library/windows/hardware/ff536879)

[IPortMidi](https://msdn.microsoft.com/library/windows/hardware/ff536891)

[IPortTopology](https://msdn.microsoft.com/library/windows/hardware/ff536896)

[IPortWaveCyclic](https://msdn.microsoft.com/library/windows/hardware/ff536899)

[IPortWavePci](https://msdn.microsoft.com/library/windows/hardware/ff536905)

[IPortWaveRT](https://msdn.microsoft.com/library/windows/hardware/ff536920)

[IPortWMIRegistration](https://msdn.microsoft.com/library/windows/hardware/ff536935)

 

 





