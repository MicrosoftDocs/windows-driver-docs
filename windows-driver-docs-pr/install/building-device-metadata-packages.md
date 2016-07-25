---
title: Building Device Metadata Packages
description: Building Device Metadata Packages
ms.assetid: 8b95a88e-430c-4250-959f-43536fdc1824
keywords: ["device metadata packages WDK , building"]
---

# Building Device Metadata Packages


This topic provides guidelines on how to build device metadata packages.

### <a href="" id="device-metadata-package-file-names"></a> Device metadata package file names

Before you create the device metadata package file, you must first create a globally unique identifier (GUID) for the metadata package. To do this, use the Guidgen tool *(Guidgen.exe*) that is described in the [GUID Generation](http://go.microsoft.com/fwlink/p/?linkid=145426) website.

The file name of the device metadata package must use the following naming convention:

```
<GUID>.devicemetadata-ms
```

For example, if you create a GUID that has the value of {20f001a99-4675-8707-248ca-187dfd9}, you use that GUID to create the following device metadata package file:

```
20f001a99-4675-8707-248ca-187dfd9.devicemetadata-ms
```

**Note**  The operating system recognizes device metadata packages only if it has a suffix of .*devicemetadata-ms*.

 

The following rules apply to device metadata package files:

-   The GUID for each metadata package file name must be unique. When you create a new or revised metadata package, you must create a new GUID, even if the changes are minor.

-   Each metadata package can support only one locale. If you support more than one locale for your device, you must create separate metadata packages for each locale, with each metadata package having its own GUID. For more information, see [**Locale XML element**](https://msdn.microsoft.com/library/windows/hardware/ff548647).

    **Note**  If you require multiple locale-specific device metadata package files for your device, you can group all the files by creating a language-neutral identifier. This identifier is a GUID, and the same GUID can be specified in the [**LanguageNeutralIdentifier**](https://msdn.microsoft.com/library/windows/hardware/ff548617) XML element within all metadata packages for the same device.

     

-   The *&lt;GUID&gt;* prefix of the device metadata package file name must specify the GUID without the '{' or '}' delimiters.

### Creating a device metadata package file

The [components of a device metadata package](device-metadata-package-components.md) are stored in a file compressed by using the Cabarc (*Cabarc.exe*) tool. For more information about this tool, refer to the [Cabarc Overview](http://go.microsoft.com/fwlink/p/?linkid=145395) website.

The following code example shows how to use the Cabarc tool to create a device metadata package file. In this example, the components of the metadata package are located in a local directory named *MyMetadataPackage*. The following list shows the subdirectories and files within the *MyMetadataPackage* directory:

```
.\MyMetadataPackages
.\MyMetadataPackage\PackageInfo.xml
.\MyMetadataPackage\DeviceInformation\DeviceInfo.xml
.\MyMetadataPackage\DeviceInformation\MyIcon.ico
.\MyMetadataPackage\WindowsInformation\WindowsInfo.xml
```

First, a GUID with the value of {f4ea2b40-77ff-443d-8212-be7e74a344ae} is created for the device metadata package. The following figure shows how to use the Guidgen tool to create the GUID:

![screen shot of the guidgen create guid dialog box](images/dmrc.png)

Then, the following command uses the Cabarc tool to create a new device metadata package file in a local directory named *MyDeviceMetadataPackage*:

```
Cabarc.exe -r -p -P .\MyMetadataPackage\ 
    N .\MyDeviceMetadataPackage\f4ea2b40-77ff-443d-8212-be7e74a344ae.devicemetadata-ms 
    .\MyMetadataPackage\PackageInfo.xml 
    .\MyMetadataPackage\DeviceInformation\DeviceInfo.xml 
    .\MyMetadataPackage\DeviceInformation\MyIcon.ico 
    .\MyMetadataPackage\WindowsInformation\WindowsInfo.xml
```

**Note**  Each metadata package can support only one locale. If you support more than one locale for your device, you must create separate metadata packages for each locale, with each metadata package having its own GUID.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Building%20Device%20Metadata%20Packages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




