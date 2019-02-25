---
title: Making PortDMus the Default DirectMusic Port Driver
description: Making PortDMus the Default DirectMusic Port Driver
ms.assetid: 1e498eb1-8a48-4240-8557-2fd2bba02abb
keywords:
- port drivers WDK audio , default DMus port driver
- default DMus port driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Making PortDMus the Default DirectMusic Port Driver


## <span id="making_portdmus_the_default_directmusic_port_driver"></span><span id="MAKING_PORTDMUS_THE_DEFAULT_DIRECTMUSIC_PORT_DRIVER"></span>


To make the DMus port driver the default for all DirectMusic applications, generate a GUID (using uuidgen.exe or guidgen.exe, which are included in the Microsoft Windows SDK) to uniquely identify your synth. Your [**KSPROPERTY\_SYNTH\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff537389) property handler should copy this GUID into the **Guid** member of the [**SYNTHCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff538424) structure. Also, modify your driver's INF file to set up the following registry entry:

```inf
Key:    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\DirectMusic\Defaults
String Value:    DefaultOutputPort
```








