---
title: Making PortDMus the Default DirectMusic Port Driver
description: Making PortDMus the Default DirectMusic Port Driver
keywords:
- port drivers WDK audio , default DMus port driver
- default DMus port driver
ms.date: 09/30/2022
---

# Making PortDMus the Default DirectMusic Port Driver


## <span id="making_portdmus_the_default_directmusic_port_driver"></span><span id="MAKING_PORTDMUS_THE_DEFAULT_DIRECTMUSIC_PORT_DRIVER"></span>


To make the DMus port driver the default for all DirectMusic applications, generate a GUID (using uuidgen.exe or guidgen.exe, which are included in the Microsoft Windows SDK) to uniquely identify your synth. Your [**KSPROPERTY\_SYNTH\_CAPS**](/previous-versions/ff537389(v=vs.85)) property handler should copy this GUID into the **Guid** member of the [**SYNTHCAPS**](/windows-hardware/drivers/ddi/dmusprop/ns-dmusprop-_synthcaps) structure. Also, modify your driver's INF file to set up the following registry entry.


| Description  | Value                    |
|--------------|--------------------------|
| Key          | HKR\DirectMusic\Defaults |
| String Value | DefaultOutputPort        |

