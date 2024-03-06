---
title: Portcls Helper Interfaces for Offloaded Audio Processing
description: This topic presents the PortCls helper interfaces, to simplify the drivers that support offloaded-audio processing.
ms.date: 09/26/2023
ms.localizationpriority: medium
---

# Portcls Helper Interfaces for Offloaded Audio Processing

This topic presents the helper interfaces that Microsoft has added to its audio port-class driver (PortCls), to simplify the implementation of drivers that support offloaded-audio processing.

When you develop your WaveRT miniport driver that will work with an audio adapter that is capable of processing hardware-offloaded audio streams, your miniport driver works with PortCls to stream and/or process audio data.

PortCls can handle all the offload-related kernel streaming (KS) properties, and that is what makes it simple to develop a WaveRT miniport driver to expose support for processing hardware-offloaded audio streams. As a result of the updates, PortCls only calls the underlying miniport driver for hardware and/or driver-specific operations via two newly defined interfaces:

- [**IMiniportAudioEngineNode**](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportaudioenginenode)

- [**IMiniportStreamAudioEngineNode**](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportstreamaudioenginenode)

You must develop two classes to work with these interfaces, one for each interface.

## Working with IMiniportAudioEngineNode

The class that you develop to work with **IMiniportAudioEngineNode**, must also inherit from [IMiniportWaveRT](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavert). The methods defined in **IMiniportAudioEngineNode** allow your driver to use KS properties that access the audio engine via a KS filter handle. The class/interface hierarchy is as follows:

:::image type="content" source="images/offload-class-hier1.png" alt-text="Diagram showing custom WaveRT miniport class inheriting from IMiniportWaveRT and IMiniportAudioEngineNode.":::

So if, for example, you develop a class called CYourMiniportWaveRT, then as you can see from the preceding diagram, CYourMiniportWaveRT must implement all the methods (shown as Operations) defined for the two parent interfaces.

A skeletal template for such a class would contain the following code:

```cpp
class CMiniportWaveRT : 
    public IMiniportWaveRT,
    public IMiniportAudioEngineNode,
    public CUnknown
{
...

    IMP_IMiniportWaveRT;
    IMP_IMiniportAudioEngineNode;
...

};
```

The *Portcls.h* header file defines these interfaces.

## Working with IMiniportStreamAudioEngineNode

The class that you develop to work with the second interface, **IMiniportStreamAudioEngineNode**, must also inherit from [IMiniportWaveRTStreamNotification](/windows-hardware/drivers/ddi/portcls/nn-portcls-iminiportwavertstreamnotification). The methods defined in **IMiniportStreamAudioEngineNode** allow your driver to use KS properties that access the audio engine via a pin instance handle. The class/interface hierarchy is as follows:

:::image type="content" source="images/offload-class-hier2.png" alt-text="Diagram showing custom WaveRT stream miniport class inheriting from IMiniportWaveRTStreamNotification and IMiniportStreamAudioEngineNode.":::

So if, for example, you develop a class called CYourMiniportWaveRTStream, then as you can see from the preceding diagram, CYourMiniportWaveRTStream must implement all the methods defined for the two parent interfaces.

A skeletal template for such a class would contain the following code:

```cpp
class CMiniportWaveRTStream : 
    public IMiniportWaveRTStreamNotification,
    public IMiniportStreamAudioEngineNode,
    public CUnknown
{
...
    IMP_IMiniportWaveRTStream;
    IMP_IMiniportWaveRTStreamNotification;
    IMP_IMiniportStreamAudioEngineNode;
...

};
```

The *Portcls.h* header file defines these interfaces. And for more information about how to develop a driver that can handle hardware-offloaded audio streams, see [Hardware Offloaded Audio Driver Implementation](driver-implementation-details.md).
