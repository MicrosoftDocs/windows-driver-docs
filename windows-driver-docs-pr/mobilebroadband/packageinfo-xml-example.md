---
title: PackageInfo XML Example
description: PackageInfo XML Example
ms.assetid: 4e514e79-d450-4cae-a40d-16ce86f95e43
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PackageInfo XML Example

[!include[MBAE deprecation warning](mbae-deprecation-warning.md)]

The following XML document uses the [PackageInfo XML schema](packageinfo-xml-schema.md) to specify the components of a vendor’s metadata package.

The package is for a service that has the following hardware ID:

MBAE:0:L9@E}}DT2.\*F65MQA57Y+L

**Note**  
Hardware IDs that are included in PackageInfo.xml must have the “DOID:” prefix added to them.

 

The package is also for the EN-US locale, which the document sets as the default locale for the components of the metadata package.

``` syntax
<?xml version="1.0" encoding ="UTF-8" ?>

  <PackageInfo xmlns=http://schemas.microsoft.com/windows/DeviceMetadata/PackageInfo/2007/11/
               xmlns:v2=” http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/PackageInfov2”>

  <MetadataKey>
      <HardwareIDList>
        <HardwareID>DOID:MBAE:0:L9@E}}DT2.*F65MQA57Y+L</HardwareID>
      </HardwareIDList>
      <Locale default="true">EN-US</Locale>
      <LastModifiedDate>2008-01-24T00:00:00Z</LastModifiedDate>
      <v2:MultipleLocale>true</v2:MultipleLocale>
  </MetadataKey>

  <PackageStructure>
      <Metadata MetadataID="http://schemas.microsoft.com/windows/DeviceMetadata/PackageInfo/2007/11">PackageInfo.xml</Metadata>
      <Metadata MetadataID="http://schemas.microsoft.com/windows/DeviceMetadata/ServiceInfo/2007/11/">ServiceInformation</Metadata>
      <Metadata MetadataID=”http://schemas.microsoft.com/windows/DeviceMetadata/WindowsInfo/2007/11/”>WindowsInformation</Metadata>
    </PackageStructure>
</PackageInfo>
```

 

 





