---
title: Submit a Multiple-locale device manifest package
description: Submit a Multiple-locale device manifest package
ms.assetid: b6748bff-d730-434e-9316-dc7b7222b727
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Submit a Multiple-locale device manifest package


## <span id="Submitting_a_multiple-locale_device_manifest_package"></span><span id="submitting_a_multiple-locale_device_manifest_package"></span><span id="SUBMITTING_A_MULTIPLE-LOCALE_DEVICE_MANIFEST_PACKAGE"></span>Submitting a multiple-locale device manifest package


You can use the same method to submit packages for preview or release.

**To submit a device manifest package**

1.  Sign the devicemanifest-ms package with the [SignTool](http://go.microsoft.com/fwlink/p/?LinkId=238330) tool.

2.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account.

3.  Under **Device metadata**, click **Create experience** if you want to submit a new experience, or click **Manage experience** if you want to modify an existing experience.

4.  Browse for and select your new devicemanifest-ms package, and then click **Submit**.

## <span id="Creating_a_Device_Manifest_Submission_Package"></span><span id="creating_a_device_manifest_submission_package"></span><span id="CREATING_A_DEVICE_MANIFEST_SUBMISSION_PACKAGE"></span>Creating a Device Manifest Submission Package


A device manifest submission package is the package format in which all multi-locale device metadata must be submitted to the Hardware Dev Center Dashboard.

The device manifest submission package contains a file that declares locale support. The device manifest package also includes a device metadata package.

Device manifest submission packages can be uploaded to the Hardware Dev Center Dashboard in the same way as device metadata packages. Using the same user interface and upload boxes, you enter the name of your \*.devicemanifest-ms file for upload.

All file upload boxes other than bulk upload on the Dashboard’s user interface will accept device manifest submission packages.

### <span id="Device_Manifest_Submission_Package_Contents"></span><span id="device_manifest_submission_package_contents"></span><span id="DEVICE_MANIFEST_SUBMISSION_PACKAGE_CONTENTS"></span>Device Manifest Submission Package Contents

Each device manifest submission package consists of the following components:

-   Device metadata package

    This package contains information and graphics to display device icons, set actions, and utilize device experience features in Windows.

    The device metadata package is always required.

-   LocaleInfo XML document

    This document contains data about the locales included in the accompanying device metadata package. The Hardware Dev Center uses this data to properly validate the device metadata package for one or more locales.

    The LocaleInfo XML document is always required, even if the device metadata package only contains a single locale.

### <span id="Structure_of_a_Device_Manifest_Submission_Package"></span><span id="structure_of_a_device_manifest_submission_package"></span><span id="STRUCTURE_OF_A_DEVICE_MANIFEST_SUBMISSION_PACKAGE"></span>Structure of a Device Manifest Submission Package

The structure of a device manifest package depends on whether the included device metadata is for a PC, for mobile broadband, or contains support for multiple locales.

If the device metadata does not fall into any of the three categories, a device manifest package is not necessary. However, a device manifest package can still be used to indicate the device metadata package is for a single locale.

### <span id="Structure_of_Multi-locale_Device_Manifest_Submission_Packages"></span><span id="structure_of_multi-locale_device_manifest_submission_packages"></span><span id="STRUCTURE_OF_MULTI-LOCALE_DEVICE_MANIFEST_SUBMISSION_PACKAGES"></span>Structure of Multi-locale Device Manifest Submission Packages

If your device metadata package contains information for supporting multiple locales, it must still be submitted in a device manifest package.

The components of a device manifest submission package are stored in a compressed cabinet file. The file name must have a suffix of .devicemanifest-ms.

Each device manifest submission package must have the following structure:

``` syntax
GUID1.devicemanifest-ms
\GUID1.devicemetadata-ms
\LocaleInfo.xml
```

“GUID1” must be a GUID.

Instructions on creating LocaleInfo.xml are below.

To learn how to develop the device metadata package, \*.devicemetadata-ms, see [Device Metadata Package Schema Reference for Windows 8](http://go.microsoft.com/fwlink/p/?LinkId=226753).

You can use the Cabarc tool to create these CAB packages. For more information about this tool, see [Cabarc overview](http://go.microsoft.com/fwlink/p/?LinkId=248843).

When you create a \*.devicemanifest-ms file by using the Cabarc tool, you must create a local directory in which the device metadata package (\*.devicemetadata-ms) and the LocaleInfo XML document are at the root of the directory.

**Remarks**

-   The .devicemanifest -ms and .devicemetadata-ms filenames must specify the GUID without the curly brace ({}) delimiters.

-   The GUID for each device manifest submission and device metadata package must be unique. When you create a new or revised package, you must create a new GUID.

-   For more details about how to create cabinet files, see the [Microsoft Cabinet Software Development Kit](http://go.microsoft.com/fwlink/p/?LinkId=248844).

**Example**

The following is an example of how to use the Cabarc tool to create a .devicemanifest-ms file. In this example, the components of the device manifest file are located in a local directory that is named DeviceManifestPackages:

``` syntax
.\DeviceManifestPackages\
.\DeviceManifestPackages\LocaleInfo.xml
.\DeviceManifestPackages\GUID.devicemetadata-ms
```

The GUID.devicemanifest-ms file was created in a local directory that is named ManifestFiles:

``` syntax
Cabarc.exe -r -p -P  .\DeviceManifestPackages\ 
N .\ManifestFiles\ GUID.devicemanifest-ms 
.\DeviceManifestPackages\LocaleInfo.xml
.\DeviceManifestPackages\GUID.devicemetadata-ms
```

## <span id="creating_localeinfo.xml"></span><span id="CREATING_LOCALEINFO.XML"></span>Creating LocaleInfo.xml


For information about creating the Localeinfo.xml file for submission, see [Create the LocaleInfo.xml Submission File](https://msdn.microsoft.com/library/windows/hardware/hh801885.aspx).

 

 





