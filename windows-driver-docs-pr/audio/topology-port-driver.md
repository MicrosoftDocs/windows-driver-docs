---
title: Topology Port Driver
description: Topology Port Driver
ms.assetid: f671f557-552e-4575-babf-869c8c0b8f08
keywords:
- Topology port driver WDK audio
- PortCls WDK audio , port drivers
- audio miniport drivers WDK , port drivers
- miniport drivers WDK audio , port drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Topology Port Driver


## <span id="topology_port_driver"></span><span id="TOPOLOGY_PORT_DRIVER"></span>


The Topology port driver exposes the topology of the audio adapter's mixing hardware. For example, the hardware that mixes the playback streams from the wave renderer and MIDI synthesizer in a typical adapter can be modeled as a set of control nodes (volume, mute, and sum) plus the data paths that connect the nodes. This topology is exposed as a set of controls and mixer lines by the Windows multimedia mixer API (see [Kernel Streaming Topology to Audio Mixer API Translation](kernel-streaming-topology-to-audio-mixer-api-translation.md)). The adapter driver provides a corresponding [Topology miniport driver](topology-miniport-driver.md) that binds to the Topology port driver to form a [topology filter](topology-filters.md).

The Topology port driver exposes an [IPortTopology](https://msdn.microsoft.com/library/windows/hardware/ff536896) interface to the miniport driver. IPortTopology inherits the methods from base interface [IPort](https://msdn.microsoft.com/library/windows/hardware/ff536842); it provides no additional methods.

The Topology port and miniport driver objects communicate with each other through their respective [IPortTopology](https://msdn.microsoft.com/library/windows/hardware/ff536896) and [IMiniportTopology](https://msdn.microsoft.com/library/windows/hardware/ff536712) interfaces.

 

 




