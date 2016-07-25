---
title: Accessing the Co-installers Registry Entry Value of a Device Setup Class
description: Accessing the Co-installers Registry Entry Value of a Device Setup Class
ms.assetid: 731d29df-6fdd-4f25-9758-d7306fef7ec0
---

# Accessing the Co-installers Registry Entry Value of a Device Setup Class


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes a [device setup class property](accessing-device-setup-class-properties.md) that represents the co-installers that are installed for the class. The unified device property model uses the [**DEVPKEY\_DeviceClass\_ClassCoInstallers**](https://msdn.microsoft.com/library/windows/hardware/ff542264) [property key](property-keys.md) to represent this property.

Windows Server 2003, Windows XP, and Windows 2000 also support this property. However, these earlier versions of Windows do not support the property key of the unified device property model. Instead, these versions of Windows represent this property by using a corresponding system-defined registry entry value. To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support this system-defined registry entry value. However, you should use the property key to access these properties on Windows Vista and later versions.

For information about how to use property keys to access device setup class properties on Windows Vista and later versions, see [Accessing Device Class Properties (Windows Vista and Later)](accessing-device-class-properties--windows-vista-and-later-.md).

On Windows Server 2003, Windows XP, and Windows 2000, you can set or retrieve this property by using the Windows registry functions to access the following registry entry value for a device setup class:

**HLM\\System\\CurrentControlSet\\Control\\CoDeviceInstallers\\{***device-setup-class-guid***}**.

For information about registering a class co-installer, see [Registering a Class Co-installer](registering-a-class-co-installer.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Accessing%20the%20Co-installers%20Registry%20Entry%20Value%20of%20a%20Device%20Setup%20Class%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




