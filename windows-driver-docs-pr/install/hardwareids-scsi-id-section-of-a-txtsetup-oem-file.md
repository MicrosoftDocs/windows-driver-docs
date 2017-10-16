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
---

# HardwareIds.scsi.ID Section of a TxtSetup.oem File


A **HardwareIds.scsi.***ID* section specifies the hardware IDs of the devices that a particular mass storage driver supports.

``` syntax
[HardwareIds.scsi.ID]
id = "deviceID","service"
...
```

<a href="" id="hardwareids-scsi-id"></a>**HardwareIds.scsi.***ID*  
*ID* corresponds to an *ID* entry in the *HwComponent* section.

<a href="" id="deviceid"></a>*deviceId*  
Specifies the device ID for a mass storage device.

<a href="" id="service"></a>*service*  
Specifies the service to be installed for the device. The service is specified by the file name of its executable image without a *.sys* extension.

The following example is an excerpt from a **HardwareIds.scsi.***ID* section for a disk device:

``` syntax
; ...
[HardwareIds.scsi.oemscsi]
id = "PCI\VEN_9004&DEV_8111","oemscsi"
 
; ... 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20HardwareIds.scsi.ID%20Section%20of%20a%20TxtSetup.oem%20File%20%20RELEASE:%20%2810/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




