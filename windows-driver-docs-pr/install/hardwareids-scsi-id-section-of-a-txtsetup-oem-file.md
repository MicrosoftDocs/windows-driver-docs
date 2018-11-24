---
title: HardwareIds.scsi.ID Section of a TxtSetup.oem File
description: A HardwareIds.scsi.ID section specifies the hardware IDs of the devices that a particular mass storage driver supports.
ms.assetid: 904744d3-524d-42ea-83a8-1fd7e80d07b8
keywords: ["HardwareIds.scsi.ID Section of a TxtSetup.oem File Device and Driver Installation"]
topic_type:
- apiref
api_name:
- HardwareIds.scsi.ID Section of a TxtSetup.oem File
api_type:
- NA
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# HardwareIds.scsi.ID Section of a TxtSetup.oem File


A **HardwareIds.scsi.**<em>ID</em> section specifies the hardware IDs of the devices that a particular mass storage driver supports.

``` syntax
[HardwareIds.scsi.ID]
id = "deviceID","service"
...
```

<a href="" id="hardwareids-scsi-id"></a>**HardwareIds.scsi.**<em>ID</em>  
*ID* corresponds to an *ID* entry in the *HwComponent* section.

<a href="" id="deviceid"></a>*deviceId*  
Specifies the device ID for a mass storage device.

<a href="" id="service"></a>*service*  
Specifies the service to be installed for the device. The service is specified by the file name of its executable image without a *.sys* extension.

The following example is an excerpt from a **HardwareIds.scsi.**<em>ID</em> section for a disk device:

``` syntax
; ...
[HardwareIds.scsi.oemscsi]
id = "PCI\VEN_9004&DEV_8111","oemscsi"
 
; ... 
```

 

 





