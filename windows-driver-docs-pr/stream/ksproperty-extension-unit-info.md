---
title: KSPROPERTY_EXTENSION_UNIT_INFO
description: The KSPROPERTY_EXTENSION_UNIT_INFO property retrieves the guidExtensionCode, bNumControls, bNrInPins, and baSourceID members of the Extension Unit Descriptor.
keywords: ["KSPROPERTY_EXTENSION_UNIT_INFO Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_EXTENSION_UNIT_INFO
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
---

# KSPROPERTY_EXTENSION_UNIT_INFO

The **KSPROPERTY_EXTENSION_UNIT_INFO** property retrieves the guidExtensionCode, bNumControls, bNrInPins, and baSourceID members of the Extension Unit Descriptor.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter node | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | PVOID |

## Remarks

This property is available in the SDK for Microsoft DirectX 9.2 or later versions.

During device startup, the system-supplied USB Video Class driver (*Usbvideo.sys*) caches information from the device's extension unit descriptor. *Usbvideo.sys* then uses this cached information to respond to **KSPROPERTY_EXTENSION_UNIT_INFO**.

Therefore, the fields returned by this property are identical to those provided by the device in the extension unit descriptor. For an example of such a descriptor, see [Sample Extension Unit Descriptor](sample-extension-unit-descriptor.md).

Specifically, KSPROPERTY_EXTENSION_UNIT_INFO returns the extension unit GUID followed by the data fields from the descriptor as shown in the following table.

| Data field | Description |
|--|--|
| bNumControls | Number of controls in this extension unit. |
| bNrInPins | Number of input pins in the extension unit. |
| baSourceID(n) | Identifier of the unit or terminal to which pin *n* of this extension unit is connected. This is a hardware identifier and not a DirectShow identifier. |

The following code example shows how to submit KSPROPERTY_EXTENSION_UNIT_INFO, taken from the complete sample shown in [Sample Extension Unit Plug-in DLL](sample-extension-unit-plug-in-dll.md):

```cpp
ExtensionProp.Property.Set = PROPSETID_VIDCAP_EXTENSION_UNIT;
    ExtensionProp.Property.Id = KSPROPERTY_EXTENSION_UNIT_INFO;
    ExtensionProp.Property.Flags = KSPROPERTY_TYPE_GET | 
                                   KSPROPERTY_TYPE_TOPOLOGY;
    ExtensionProp.NodeId = m_dwNodeId;

    hr = m_pKsControl->KsProperty(
        (PKSPROPERTY) &ExtensionProp,
        sizeof(ExtensionProp),
        NULL,
        0,
        &ulBytesReturned);
```

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[Sample Extension Unit Plug-in DLL](sample-extension-unit-plug-in-dll.md)

[Sample Extension Unit Descriptor](sample-extension-unit-descriptor.md).
