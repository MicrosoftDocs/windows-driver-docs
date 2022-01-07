---
title: KSPROPERTY_PIN_PROPOSEDATAFORMAT
description: Clients use the KSPROPERTY_PIN_PROPOSEDATAFORMAT property to determine if pins instantiated by the pin factory support a specific data format.
keywords: ["KSPROPERTY_PIN_PROPOSEDATAFORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_PROPOSEDATAFORMAT
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 07/13/2021
---

# KSPROPERTY_PIN_PROPOSEDATAFORMAT

Clients use the **KSPROPERTY_PIN_PROPOSEDATAFORMAT** property to determine if pins instantiated by the pin factory support a specific data format.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) | [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) |

## Remarks

**KSPROPERTY_PIN_PROPOSEDATAFORMAT** includes a structure of type [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat), specifying the proposed data format. Specify this property using [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin), where the member specifies the relevant pin factory.

Using KSPROPERTY_TYPE_GET with this property allows the audio driver to provide information about the default data format on a pin. KSPROPERTY_TYPE_GET is optional to implement for this property unless the driver supports [**KSEVENT_PINCAPS_FORMATCHANGE**](../audio/ksevent-pincaps-formatchange.md).

The KS filter returns STATUS_SUCCESS when using this property with KSPROPERTY_TYPE_SET if pins can be set to or opened with the proposed data format. If the pin cannot be set to the proposed data format, then it returns STATUS_NO_MATCH. For any other failures, an appropriate error is returned. If the driver supports [**KSPROPERTY_AUDIOSIGNALPROCESSING_MODES**](../audio/ksproperty-audiosignalprocessing-modes.md), this property should return STATUS_SUCCESS if the format is supported by any of the audio signal processing modes.

Using KSPROPERTY_TYPE_SET with this property does not actually change the data format. Clients use [**KSPROPERTY_CONNECTION_DATAFORMAT**](ksproperty-connection-dataformat.md) to change the data format. KSPROPERTY_TYPE_SET is optional to implement for this property.

## Requirements

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat)

[**KSEVENT_PINCAPS_FORMATCHANGE**](../audio/ksevent-pincaps-formatchange.md)

[**KS Properties**](ks-properties.md)

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_AUDIOSIGNALPROCESSING_MODES**](../audio/ksproperty-audiosignalprocessing-modes.md)
