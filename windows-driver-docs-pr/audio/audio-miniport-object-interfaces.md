---
title: Audio Miniport Object Interfaces
description: Audio Miniport Object Interfaces
ms.assetid: 2e79ad90-fecc-47a7-b487-809325a16239
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Miniport%20Object%20Interfaces%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




