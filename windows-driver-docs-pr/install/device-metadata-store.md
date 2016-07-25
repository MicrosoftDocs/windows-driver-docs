---
title: Device Metadata Store
description: Device Metadata Store
ms.assetid: 59af6173-28f3-44f5-874e-305bf570d683
keywords: ["device metadata store WDK"]
---

# Device Metadata Store


The device metadata store is the directory where device metadata packages are stored on the local computer. The device metadata store is accessed from the following directory:

```
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore\<locale>
```

The &lt;locale&gt; subdirectory represents the locale of the device metadata package. The name of this subdirectory can be in the following format:

```
<Language>[-<Region>] 
```

For example, a value of EN-US specifies the subdirectory that contains device metadata package that are localized for the English language of the United States.

If only *&lt;Language&gt;* is specified, the subdirectory that contains device metadata packages that are localized for the specified language in all locations where the language exists. For example, a value of 'EN' applies to 'EN-US and EN-BR.

A device metadata package is copied to the device metadata store in one of the following ways:

-   The OEM or developer copies the device metadata package. For more information, see [Manually Adding Device Metadata Packages](manually-adding-device-metadata-packages.md).

-   The device metadata package is copied by using an application that is provided by the OEM. For more information, see [Installing Device Metadata Packages through an Application](installing-device-metadata-packages-through-an-application.md).

**Note**   We do not recommend that end-users copy device metadata packages to the device metadata store. Instead, end-users should install device metadata packages by using either the [Windows Metadata and Internet Services (WMIS)](installing-device-metadata-packages-from-wmis.md) or an application provided by the OEM.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Metadata%20Store%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




