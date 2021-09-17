---
title: Sample Extension Unit Descriptor
description: This code demonstrates how to provide an Extension Unit descriptor at the hardware level.
keywords:
- Extension Unit descriptor WDK USB Video Class
- descriptors WDK USB Video Class
- descriptors WDK USB Video Class , sample code
- sample code WDK USB Video Class , extension unit descriptors
ms.date: 09/17/2021
ms.localizationpriority: medium
---

# Sample extension unit descriptor

> [!IMPORTANT]
> The content and sample code in this topic is outdated and currently unsupported. It may not work with the current driver development toolchain.

This code demonstrates how to provide an Extension Unit descriptor at the hardware level.

```cpp
BYTE  Length:            0x1a
BYTE  DescriptorType:    0x24
BYTE  DescriptorSubtype: 0x06
BYTE  bUnitID:           0x05
GUID  guidExtensionCode: xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxxxxxx
BYTE  bNumControls:      0x03
BYTE  bNrInPins:         0x01
BYTE  baSourceID[0]:     0x01
```

For more detailed information on hardware requirements for USB Video Class, see the *Universal Serial Bus Device Class Definition for Video DevicesSpecification*. This specification is available at the [USB Implementers Forum](https://www.usb.org/) website.
