---
title: Get driver package metadata
description: This page helps to understand the structure of the driver package metadata.
author: balapv
ms.author: balapv
ms.date: 04/18/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

#Driver package metadata

The driver metadata package is a file associated to a submission. This file contains details about each INF file in a driver package or bundle. This file can be downloaded by using the [get a submission](get-a-submission.md) method. The file will be available in the [link object](get-product-data.md#link-object) of the submission with the *rel* - **driverMetadata**. 

##Driver Metadata structure

```json
{
  "BundleInfoMap": {
    "dc3b111e-c750-4a55-96ce-0eae1d1da8a2": {
      "Locales": [
        "English"
      ],
      "InfInfoMap": {
        "foo_bar.inf": {
          "DriverPackageFamilyId": "RAID-foo_bar.inf",
          "InfClass": "SCSIAdapter",
          "DriverVersion": "1.1.1.1",
          "DriverDate": "2018-01-11T00:00:00",
          "ExtensionId": null,
          "Provider": "RAID",
          "ClassGuid": "{a43418dc-cfc9-42e1-85b0-2d644331e214}",
          "InstallationComputerHardwareIds": [
            "a9a8e6fc-4969-4336-927c-9d8f7b6c1d14",
            "a4a127cb-2c10-464e-abb5-e78fcdf0d3c3"
          ],
          "OSPnPInfoMap": {
            "WINDOWS_v100_RS3_FULL": {
              "pci\\ven_test&dev_abcd": {
                "Manufacturer": "RAID",
                "DeviceDescription": "Virtual Raid Adapter",
                "FeatureScore": null
              }
            }
          }
        }
      }
    }
  }
}
```

The file has the following values:

| Value | Type | Description |
|:--|:--|:--|
|BundleInfoMap|object|This is the parent. It is identified by a GUID and contains all details about the driver bundle.|
|Locales|array of strings|This is an array of applicable locales for the bundle|
|InfInfoMap|array of objects|This is an array which describes each INF file within the bundle. The identifier of each item is the INF file name|
|DriverPackageFamilyId|string|ID of the driver package family|
|InfClass|string|The device class or INF class of the driver|
|DriverVersion|string|The version of the driver|
|DriverDate|datetime|The date and time for this driver|
|ExtensionId|GUID|Applicable for Extension INFs. A GUID which represents the Extension ID for this INF|
|Provider|string|The provider for this driver|
|ClassGuid|string|CLass GUID of the driver|
|InstallationComputerHardwareIds|array of GUIDs|list of CHIDs to which this driver can be targeted|
|OSPnPInfoMap|array of objects|Array of objects which maps an operating system to hardware IDs. The object has a base element which is the Operating system. Inside each operating system will be a list of PNP or Hardware IDs along with details|
|Manufacturer|string|Manufacturer of the hardware ID|
|DeviceDescription|string|Description of the hardware ID |
|FeatureScore|string|Feature score for this driver|