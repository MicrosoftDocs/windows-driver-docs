---
title: Making PortDMus the Default DirectMusic Port Driver
description: Making PortDMus the Default DirectMusic Port Driver
ms.assetid: 1e498eb1-8a48-4240-8557-2fd2bba02abb
keywords: ["port drivers WDK audio , default DMus port driver", "default DMus port driver"]
---

# Making PortDMus the Default DirectMusic Port Driver


## <span id="making_portdmus_the_default_directmusic_port_driver"></span><span id="MAKING_PORTDMUS_THE_DEFAULT_DIRECTMUSIC_PORT_DRIVER"></span>


To make the DMus port driver the default for all DirectMusic applications, generate a GUID (using uuidgen.exe or guidgen.exe, which are included in the Microsoft Windows SDK) to uniquely identify your synth. Your [**KSPROPERTY\_SYNTH\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff537389) property handler should copy this GUID into the **Guid** member of the [**SYNTHCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff538424) structure. Also, modify your driver's INF file to set up the following registry entry:

```
Key:    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\DirectMusic\Defaults
String Value:    DefaultOutputPort
 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Making%20PortDMus%20the%20Default%20DirectMusic%20Port%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




