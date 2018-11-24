---
title: Supporting a Device
description: Supporting a Device
ms.assetid: 5f60d3aa-6061-40f7-8108-d752534b88ed
keywords:
- audio miniport drivers WDK , device support
- miniport drivers WDK audio , device support
- port class drivers WDK audio
- PortCls WDK audio , device support
- port drivers WDK audio , miniport drivers
- port drivers WDK audio , Port Class
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting a Device


## <span id="supporting_a_device"></span><span id="SUPPORTING_A_DEVICE"></span>


The PortCls system driver (*Portcls.sys*) provides several built-in port drivers to support audio devices that render and capture wave and MIDI streams.

All port drivers expose interfaces that derive from base interface [IPort](https://msdn.microsoft.com/library/windows/hardware/ff536842). **IPort** inherits the methods from base interface **IUnknown**. **IPort** provides the following additional methods:

[**IPort::GetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff536941)

Retrieves an audio adapter's Plug and Play properties from the registry.
[**IPort::Init**](https://msdn.microsoft.com/library/windows/hardware/ff536943)

Initializes the port object.
[**IPort::NewRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff536945)

Creates a new registry key or opens an existing key.
PortCls implements the following port drivers:

[WaveCyclic Port Driver](wavecyclic-port-driver.md)

[WavePci Port Driver](wavepci-port-driver.md)

[WaveRT Port Driver](wavert-port-driver.md)

[Topology Port Driver](topology-port-driver.md)

[MIDI Port Driver](midi-port-driver.md)

[DMus Port Driver](dmus-port-driver.md)

 

 




