---
title: KSPROPERTYSETID\_NetworkCameraControl
description: Defines the network camera property set ID. 
ms.date: 04/14/2020
ms.localizationpriority: medium
---

# KSPROPERTYSETID\_NetworkCameraControl

The *ksmedia.h* header file defines the **KSPROPERTYSETID\_NetworkCameraControl** property set ID as follows:

```cpp
#define STATIC_KSPROPERTYSETID_NetworkCameraControl \
    0xe780f09, 0x5745, 0x4e3a,  0xbc, 0x9f, 0xf2, 0x26, 0xea, 0x43, 0xa6, 0xec
DEFINE_GUIDSTRUCT("0E780F09-5745-4E3A-BC9F-F226EA43A6EC", KSPROPERTYSETID_NetworkCameraControl);
#define KSPROPERTYSETID_NetworkCameraControl DEFINE_GUIDNAMED(KSPROPERTYSETID_NetworkCameraControl)
```

The **KSPROPERTYSETID\_NetworkCameraControl** property set contains the following properties:

[**KSPROPERTY_NETWORKCAMERACONTROL_NTP**](https://docs.microsoft.com/windows-hardware/drivers/stream/)

[**KSPROPERTY_NETWORKCAMERACONTROL_URI**](https://docs.microsoft.com/windows-hardware/drivers/stream/)

These property names are defined in the [KSPROPERTY_NETWORKCAMERACONTROL_PROPERTY](https://docs.microsoft.com/windows-hardware/drivers/stream/ne-ksmedia-ksproperty_networkcameracontrol_property) enumeration.
