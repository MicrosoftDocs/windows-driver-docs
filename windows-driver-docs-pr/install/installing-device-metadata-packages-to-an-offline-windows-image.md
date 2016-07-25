---
title: Installing Device Metadata Packages to an Offline Windows Image
description: Installing Device Metadata Packages to an Offline Windows Image
ms.assetid: 53480324-951f-4c51-9b5b-051ce1a3b709
---

# Installing Device Metadata Packages to an Offline Windows Image


Computer OEMs can add device metadata packages to an offline image of Windows by copying the packages to the local device metadata store. This store is in the following location:

```
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore\<locale>
```

You must first create the *&lt;locale&gt;* subdirectory based on the target locale of the device metadata package. Then you must copy the metadata package to the appropriate *&lt;locale&gt;* subdirectory.

For example, a device metadata package that is localized for the English language of Great Britain must be copied to the following location:

```
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore\EN-GB
```

A device metadata package that is localized for the Japanese language must be copied to the following location:

```
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore\JA
```

For more information, see [Device Metadata Store](device-metadata-store.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20Device%20Metadata%20Packages%20to%20an%20Offline%20Windows%20Image%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




