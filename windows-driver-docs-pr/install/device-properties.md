---
title: Device Properties
description: Device Properties
ms.assetid: 87a43865-74bc-412c-9ae2-3ba38589c8f8
keywords:
- device installations WDK , device properties
- device properties WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Properties


Device properties codify the attributes of device instances, [device setup classes](device-setup-classes.md), [device interface classes](device-interface-classes.md), and device interfaces. These attributes describe the function of the component and its configuration in the Windows operating system.

Windows Vista and later versions of Windows support a [unified device property model](unified-device-property-model--windows-vista-and-later-.md) that defines how these device properties are represented.

Microsoft Windows Server 2003, Windows XP, and Windows 2000 do not support this unified device property model. However these earlier Windows versions do support corresponding [device property representations](device-property-representations--windows-server-2003--windows-xp--and-.md) that depend on the component type and property type. To maintain compatibility with these earlier Windows versions, Windows Vista and later versions of Windows also support these earlier representations. However, you should use the unified device property model of Windows Vista and later to access device properties.

For reference information about the components of the unified device property model—including device property functions, system-defined device properties, data structures, and INF file directives—see [Device Property Reference](https://msdn.microsoft.com/library/windows/hardware/ff541483).

 

 





