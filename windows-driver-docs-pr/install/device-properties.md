---
title: Device Properties
description: Device Properties
ms.assetid: 87a43865-74bc-412c-9ae2-3ba38589c8f8
keywords: ["device installations WDK , device properties", "device properties WDK device installations"]
---

# Device Properties


Device properties codify the attributes of device instances, [device setup classes](device-setup-classes.md), [device interface classes](device-interface-classes.md), and device interfaces. These attributes describe the function of the component and its configuration in the Windows operating system.

Windows Vista and later versions of Windows support a [unified device property model](unified-device-property-model--windows-vista-and-later-.md) that defines how these device properties are represented.

Microsoft Windows Server 2003, Windows XP, and Windows 2000 do not support this unified device property model. However these earlier Windows versions do support corresponding [device property representations](device-property-representations--windows-server-2003--windows-xp--and-.md) that depend on the component type and property type. To maintain compatibility with these earlier Windows versions, Windows Vista and later versions of Windows also support these earlier representations. However, you should use the unified device property model of Windows Vista and later to access device properties.

For reference information about the components of the unified device property model—including device property functions, system-defined device properties, data structures, and INF file directives—see [Device Property Reference](https://msdn.microsoft.com/library/windows/hardware/ff541483).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Properties%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




