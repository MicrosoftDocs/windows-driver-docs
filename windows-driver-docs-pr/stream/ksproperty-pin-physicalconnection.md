---
title: KSPROPERTY_PIN_PHYSICALCONNECTION
description: Audio adapter drivers use the KSPROPERTY_PIN_PHYSICALCONNECTION property to denote physical connections between miniports.
keywords: ["KSPROPERTY_PIN_PHYSICALCONNECTION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_PHYSICALCONNECTION
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/03/2021
ms.localizationpriority: medium
---

# KSPROPERTY_PIN_PHYSICALCONNECTION

Audio adapter drivers use the **KSPROPERTY_PIN_PHYSICALCONNECTION** property to denote physical connections between miniports.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Pin | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | [**KSPIN_PHYSICALCONNECTION**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_physicalconnection) |

## Remarks

Specify this property using KSP_PIN, where the member specifies the relevant pin factory.

**KSPROPERTY_PIN_PHYSICALCONNECTION** returns a structure of type [**KSPIN_PHYSICALCONNECTION**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_physicalconnection), specifying the connected **PinId** and the symbolic link name of the connected filter.

The class driver does not handle this property; the stream minidriver must provide handling on its own.

Audio adapter drivers register connections with [**PcRegisterPhysicalConnection**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisterphysicalconnection).

Subsequently, the SysAudio system driver (*sysaudio.sys*) queries this property and builds the graph accordingly. SysAudio uses this property to determine which wave filter pin is connected to which topology filter pin.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSPIN_PHYSICALCONNECTION**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_physicalconnection)

[**PcRegisterPhysicalConnection**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcregisterphysicalconnection)
