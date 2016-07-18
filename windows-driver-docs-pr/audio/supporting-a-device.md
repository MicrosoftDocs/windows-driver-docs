---
title: Supporting a Device
description: Supporting a Device
ms.assetid: 5f60d3aa-6061-40f7-8108-d752534b88ed
keywords: ["audio miniport drivers WDK , device support", "miniport drivers WDK audio , device support", "port class drivers WDK audio", "PortCls WDK audio , device support", "port drivers WDK audio , miniport drivers", "port drivers WDK audio , Port Class"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Supporting%20a%20Device%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


