---
title: KSPROPERTY_PIN_PROPOSEDATAFORMAT2
description: The OS uses the KSPROPERTY_PIN_PROPOSEDATAFORMAT2 property to determine if pins instantiated by the pin factory support specific data formats.
keywords: ["KSPROPERTY_PIN_PROPOSEDATAFORMAT2 Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_PIN_PROPOSEDATAFORMAT2
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 07/13/2021
---

# KSPROPERTY_PIN_PROPOSEDATAFORMAT2

The OS uses the **KSPROPERTY_PIN_PROPOSEDATAFORMAT2** property to determine if the driver has a preferred data format on a pin given the specified attribute.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | See remarks  |  [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat)  |

## Remarks

The property descriptor is a [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) followed by a [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) specifying a count of variable size attributes that follow the **KSMULTIPLE_ITEM**. Each attribute starts with a [**KSATTRIBUTE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksattribute) header followed by data specific to the attribute. The attributes act as parameters for the property request, specifying the proposed data formats.

**KSPROPERTY_PIN_PROPOSEDATAFORMAT2** includes a structure of type [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat),

The only attribute  supported for the property is *KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE*
and it is specified using the [**KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagksattribute_audiosignalprocessing_mode) structure. Note that the **KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE** structure starts with a [**KSATTRIBUTE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksattribute) member. For more information, see [Audio Signal Processing Modes](../audio/audio-signal-processing-modes.md).

KSPROPERTY_TYPE_GET is only supported if the pin has proposed formats. This function allows the audio driver to provide information about the default data format on a pin given the specified attribute.

The KS filter returns STATUS_SUCCESS if pin has preferred data format for the specified attribute. If pin does not have a preferred data format for the specified attribute it returns STATUS_NOT_SUPPORTED. For any other failures, an appropriate error is returned. If driver supports this property, OS will always use this format for the specific signal processing mode.
KSPROPERTY_TYPE_SET is not supported for this property.

The following table provides a description of the **KSPROPERTY_PIN_PROPOSEDATAFORMAT2** input structure *PinProperty* elements.

| Element | Description |
|--|--|
| PinProperty.Property.Set | The PinProperty.Property.Set should be set to the [KSPROPSETID_Pin](kspropsetid-pin.md) for the requested mode. |
| PinProperty.Property.Id | The PinProperty.Property.Id always be set to **KSPROPERTY_PIN_PROPOSEDATAFORMAT2**. |
| PinProperty.Property.Flags | The PinProperty.Property.Flags can be set to KSPROPERTY_TYPE_GET or to KSPROPERTY_TYPE_BASICSUPPORT to find out basic information about the property. |
| PinProperty.PinId | The PinProperty.PinId identifies the target pin for the **KSPROPERTY_PIN_PROPOSEDATAFORMAT2** request. |
| PinProperty.Reserved | The PinProperty.Reserved is reserved for future use and should always be set to zero (0). |

The following table provides a description of the **KSPROPERTY_PIN_PROPOSEDATAFORMAT2** input structure *Attributes* elements.

| Element | Description |
|--|--|
| Attributes.Count | The Attributes.Count should be set to the number of attributes, normally one (1). |
| Attributes.Size | The Attributes.Size should be set to the size of the ProposeDataformat2Input. It can be calculated like this, when there is one attribute:<br><br>`sizeof(ProposeDataformat2Input)` |

The following table provides a description of the **KSPROPERTY_PIN_PROPOSEDATAFORMAT2** input structure *SignalProcessingModeAttribute* elements.

| Element | Description |
|--|--|
| SignalProcessingModeAttribute.AttributeHeader.Attribute | The AttributeHeader.Attribute element should be set to desired KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE. |
| SignalProcessingModeAttribute.AttributeHeader.Flags | The Flags element is reserved for future use and should always be set to zero (0). |
| SignalProcessingModeAttribute.AttributeHeader.Size | The AttributeHeader.Size indicates the size of [**KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagksattribute_audiosignalprocessing_mode). It can be calculated like this:<br><br>`sizeof(KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE)` |
| SignalProcessingModeAttribute.SignalProcessingMode | The SignalProcessingMode element should be set to the requested SIGNALPROCESSINGMODE for example, AUDIO_SIGNALPROCESSINGMODE_DEFAULT. |

To use **KSPROPERTY_PIN_PROPOSEDATAFORMAT2** define the following structure.

```cpp
typedef struct
{
    KSP_PIN                                 PinProperty;
    KSMULTIPLE_ITEM                         Attributes;
    KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE  SignalProcessingModeAttribute;
} ProposeDataformat2Input;
```

This code sample shows how to initialize the structure.

```cpp
ProposeDataformat2Input input = {0};

input.PinProperty.Property.Set = KSPROPSETID_Pin;  
input.PinProperty.Property.Id = KSPROPERTY_PIN_PROPOSEDATAFORMAT2;  
input.PinProperty.Property.Flags = KSPROPERTY_TYPE_GET;  
input.PinProperty.PinId = m_nPinId;  
input.PinProperty.Reserved = 0;     

input.Attributes.Count = 1;
input.Attributes.Size = sizeof(ProposeDataformat2Input) - RTL_SIZEOF_THROUGH_FIELD(ProposeDataformat2Input, PinProperty);

input.SignalProcessingModeAttribute.AttributeHeader.Attribute = KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE;
input.SignalProcessingModeAttribute.AttributeHeader.Flags = 0;
input.SignalProcessingModeAttribute.AttributeHeader.Size = sizeof(KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE);
input.SignalProcessingModeAttribute.SignalProcessingMode = gProcessingMode;
```

## Requirements

**Version:** Available starting with Windows 8.1

**Header:** ks.h (include Ks.h)

## See also

[**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat)

[**KSEVENT_PINCAPS_FORMATCHANGE**](../audio/ksevent-pincaps-formatchange.md)

[**KS Properties**](ks-properties.md)

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_AUDIOSIGNALPROCESSING_MODES**](../audio/ksproperty-audiosignalprocessing-modes.md)
