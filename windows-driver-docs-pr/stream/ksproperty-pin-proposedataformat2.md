---
title: KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2
description: The OS uses the KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2 property to determine if pins instantiated by the pin factory support specific data formats.
ms.assetid: 64F6E8CA-8E48-43B3-9A60-DAB53516AD45
keywords: ["KSPROPERTY_PIN_PROPOSEDATAFORMAT2 Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_PROPOSEDATAFORMAT2
api_location:
- ks.h
api_type:
- HeaderDef
---

# KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2


The OS uses the **KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2** property to determine if pins instantiated by the pin factory support specific data formats.

## <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table


<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Filter</p></td>
<td><p>See remarks</p></td>
<td><p>[<strong>KSDATAFORMAT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561656)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The property descriptor is a [**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722) followed by a [**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441) specifying a count of variable size attributes that follow the **KSMULTIPLE\_ITEM**. Each attribute starts with a [**KSATTRIBUTE**](https://msdn.microsoft.com/library/windows/hardware/ff560987) header followed by data specific to the attribute. The attributes act as parameters for the property request, specifying the proposed data formats.

**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2** includes a structure of type [**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff561656),

Although the attributes provide a highly extensible mechanism to parameterize the property request, Windows defines only a single attribute passed with the property request- the audio signal processing mode. The attribute ID is *KSATTRIBUTEID\_AUDIOSIGNALPROCESSING\_MODE* and is specified using the [**KSATTRIBUTE\_AUDIOSIGNALPROCESSING\_MODE**](https://msdn.microsoft.com/library/windows/hardware/mt727947) structure. Note that the **KSATTRIBUTE\_AUDIOSIGNALPROCESSING\_MODE** structure starts with a [**KSATTRIBUTE**](https://msdn.microsoft.com/library/windows/hardware/ff560987) member. For more information, see [Audio Signal Processing Modes](https://msdn.microsoft.com/library/windows/hardware/mt186386).

[**KSPROPERTY\_TYPE\_GET**](https://msdn.microsoft.com/library/windows/hardware/ff564262) is only supported if the pin has proposed formats. This function allows the audio driver to provide information about the default data format on a pin given the specified attributes.

The KS filter returns STATUS\_SUCCESS, when the OS accepts the information about the pins instantiated by the pin factory supporting specific data formats, or an error code otherwise.

**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2 Input Structure**

The following table provides a description of the KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2 input structure *PinProperty* elements.

|                            |                                                                                                                                                                                    |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PinProperty.Property.Set   | The PinProperty.Property.Set should be set to the [KSPROPSETID\_Pin](kspropsetid-pin.md) for the requested mode.                                                                  |
| PinProperty.Property.Id    | The PinProperty.Property.Id always be set to **KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2**.                                                                                              |
| PinProperty.Property.Flags | The PinProperty.Property.Flags can be set to [**KSPROPERTY\_TYPE\_GET**](https://msdn.microsoft.com/library/windows/hardware/ff564262) or to KSPROPERTY\_TYPE\_BASICSUPPORT to find out basic information about the property. |
| PinProperty.PinId          | The PinProperty.PinId identifies the target pin for the **KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2** request.                                                                           |
| PinProperty.Reserved       | The PinProperty.Reserved is reserved for future use and should always be set to zero (0).                                                                                          |

 

The following table provides a description of the KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2 input structure *Attributes* elements.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Attributes.Count</td>
<td>The Attributes.Count should be set to the number of attributes, normally one (1).</td>
</tr>
<tr class="even">
<td>Attributes.Size</td>
<td>The Attributes.Size should be set to the size of the ProposeDataformat2Input. It can be calculated like this, when there is one attribute:
<p>sizeof(ProposeDataformat2Input)</p></td>
</tr>
</tbody>
</table>

 

The following table provides a description of the KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2 input structure *SignalProcessingModeAttribute* elements.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SignalProcessingModeAttribute.AttributeHeader.Attribute</td>
<td>The AttributeHeader.Attribute element should be set to desired KSATTRIBUTEID_AUDIOSIGNALPROCESSING_MODE.</td>
</tr>
<tr class="even">
<td>SignalProcessingModeAttribute.AttributeHeader.Flags</td>
<td>The Flags element is reserved for future use and should always be set to zero (0).</td>
</tr>
<tr class="odd">
<td>SignalProcessingModeAttribute.AttributeHeader.Size</td>
<td>The AttributeHeader.Size indicates the size of [<strong>KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE</strong>](https://msdn.microsoft.com/library/windows/hardware/mt727947). It can be calculated like this:
<p>sizeof(KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE)</p></td>
</tr>
<tr class="even">
<td>SignalProcessingModeAttribute.SignalProcessingMode</td>
<td>The SignalProcessingMode element should be set to the requested SIGNALPROCESSINGMODE for example, AUDIO_SIGNALPROCESSINGMODE_DEFAULT.</td>
</tr>
</tbody>
</table>

 

To use **KSPROPERTY\_PIN\_PROPOSEDATAFORMAT2** define the following structure.

```
typedef struct
{
    KSP_PIN                                 PinProperty;
    KSMULTIPLE_ITEM                         Attributes;
    KSATTRIBUTE_AUDIOSIGNALPROCESSING_MODE  SignalProcessingModeAttribute;
} ProposeDataformat2Input;
```

This code sample shows how to initialize the structure.

```
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

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available starting with Windows 8.1.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722)

[**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_PIN_PROPOSEDATAFORMAT2%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





