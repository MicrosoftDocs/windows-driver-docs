---
title: Sample Extension Unit Descriptor
author: windows-driver-content
description: Sample Extension Unit Descriptor
ms.assetid: 283a28e6-9f73-4131-bcfb-b4983a92cecd
keywords:
- Extension Unit descriptor WDK USB Video Class
- descriptors WDK USB Video Class
- descriptors WDK USB Video Class , sample code
- sample code WDK USB Video Class , extension unit descriptors
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sample Extension Unit Descriptor


This code demonstrates how to provide an Extension Unit descriptor at the hardware level.

```
BYTE  Length:            0x1a    
BYTE  DescriptorType:    0x24               
BYTE  DescriptorSubtype: 0x06             
BYTE  bUnitID:           0x05
GUID  guidExtensionCode: xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxxxxxx
BYTE  bNumControls:      0x03
BYTE  bNrInPins:         0x01
BYTE  baSourceID[0]:     0x01
```

For more detailed information on hardware requirements for USB Video Class, see the *Universal Serial Bus Device Class Definition for Video DevicesSpecification*. This specification is available at the [USB Implementers Forum](http://go.microsoft.com/fwlink/p/?linkid=8780) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Sample%20Extension%20Unit%20Descriptor%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


