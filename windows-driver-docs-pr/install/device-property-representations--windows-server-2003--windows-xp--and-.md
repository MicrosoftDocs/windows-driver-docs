---
title: Device Property Representations (Windows Server 2003, Windows XP, and Windows 2000)
description: Device Property Representations (Windows Server 2003, Windows XP, and Windows 2000)
ms.assetid: 124172d7-52a4-423c-a1fd-eec554f328d6
keywords: ["device properties WDK device installations , representations"]
---

# Device Property Representations (Windows Server 2003, Windows XP, and Windows 2000)


Windows Server 2003, Windows XP, and Windows 2000 do not support the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) that Windows Vista and later versions of Windows support. However, most of the [system-defined device properties](https://msdn.microsoft.com/library/windows/hardware/ff553413) that are included in the unified device property model have corresponding representations that are supported by these earlier versions of Windows. On these earlier versions of Windows, the way a device property is represented, and the mechanism to access a property, depends on the component type and property type. These representations and mechanisms include the following:

-   A device property is represented by a system-defined identifier that is supplied as an input parameter to a [SetupAPI function](setupapi.md) to access the device property.

-   A device property does not have an explicit representation. However, the information that is associated with a device property can be retrieved by calls to SetupAPI functions or Plug and Play (PnP) configuration manager functions.

-   A device property is represented by a registry entry value that can be accessed by using the Windows registry functions.

-   INF file entry values modify device properties.

The following topics provide information about how to access device properties on Windows Server 2003, Windows XP, and Windows 2000:

[INF File Entry Values that Modify Device Properties](inf-file-entry-values-that-modify-device-properties.md)

[Using SetupAPI and Configuration Manager to Access Device Properties](using-setupapi-and-configuration-manager-to-access-device-properties.md)

**Note**   To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support these mechanisms. However, you should use the unified device property model to access device properties on Windows Vista and later versions.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Property%20Representations%20%28Windows%20Server%202003,%20Windows%20XP,%20and%20Windows%202000%29%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




