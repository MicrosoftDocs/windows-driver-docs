---
title: Jack Description Property
description: Jack Description Property
ms.assetid: 6398efc9-4435-4234-bd72-1ed0f96c9f9f
ms.date: 05/08/2018
ms.localizationpriority: medium
---

# Jack Description Property


In Windows Vista and later, the [**KSPROPERTY\_JACK\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff537364) property describes an audio jack or other physical connector on an audio adapter. The property value describes the color of the jack, the physical location of the jack, the connector type, and other jack features. The purpose of this information is to help the user to find the correct jack for plugging in an audio endpoint device such as a microphone, headphones, or speakers. For more information, see [Audio Endpoint Devices](https://go.microsoft.com/fwlink/p/?linkid=130876).

If a KS filter on an audio adapter supports the KSPROPERTY\_JACK\_DESCRIPTION property, the Windows multimedia control panel, Mmsys.cpl, displays the jack information for the bridge pins on the filter. A bridge pin represents a connection (typically, a jack) to an audio endpoint device. Although the property value contains information about a pin (or rather, the jack or jacks that are associated with the pin), the property is a property of the filter, not of the pin. For more information about bridge pins, see [Audio Filter Graphs](audio-filter-graphs.md). For more information about filter properties and pin properties, see [Filter, Pin, and Node Properties](filter--pin--and-node-properties.md).

An audio application can obtain the KSPROPERTY\_JACK\_DESCRIPTION property value for an audio endpoint device by calling the **IKsJackDescription::GetJackDescription** method in the DeviceTopology API. For example, an application can use the jack information to help the user to distinguish a microphone plugged into a green XLR jack from a microphone plugged into an orange XLR jack. For more information about the DeviceTopology API, see [Device Topologies](https://go.microsoft.com/fwlink/p/?linkid=130878).

The Microsoft HD Audio class driver automatically constructs the KSPROPERTY\_JACK\_DESCRIPTION property values from the data that it reads from the pin-configuration registers in an HD Audio codec. However, any KS-based audio driver can implement support for this property in its filter automation tables. For more information about the HD Audio class driver, see [HD Audio and UAA](hd-audio-and-uaa.md). For more information about pin-configuration registers, see [Pin Configuration Guidelines for High Definition Audio Devices](https://download.microsoft.com/download/9/c/5/9c5b2167-8017-4bae-9fde-d599bac8184a/PinConfig.doc) white paper.

An audio endpoint device can connect to a bridge pin through one or more jacks. For example, a set of (two-channel) stereo speakers requires one jack, but a set of 5.1 surround-sound speakers requires three jacks (assuming that each jack handles two of the six channels).

The description for each jack is contained in a [**KSJACK\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff537136) structure. For example, the KSPROPERTY\_JACK\_DESCRIPTION property value for an audio endpoint device with one jack contains one KSJACK\_DESCRIPTION structure, but the property value for an endpoint device with three jacks contains three KSJACK\_DESCRIPTION structures. In either case, the KSJACK\_DESCRIPTION structure or structures in the property value are preceded by a [**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441) structure that specifies the size of the property value. For more information, see [**KSPROPERTY\_JACK\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff537364).

Jack information is particularly useful for helping users to distinguish among the jacks that connect to a multichannel speaker configuration. The following code example shows an array of KSJACK\_DESCRIPTION structures that an audio driver uses to describe the three jacks for a set of 5.1 surround speakers:

```cpp
KSJACK_DESCRIPTION ar_5dot1_Jacks[] =
{
    // Jack 1
    {
        (SPEAKER_FRONT_LEFT | SPEAKER_FRONT_RIGHT), // ChannelMapping (L,R)
        RGB(0,255,0),       // Color (green)
        eConnType3Point5mm, // ConnectionType
        eGeoLocRear,        // GeoLocation
        eGenLocPrimaryBox,  // GenLocation
        ePortConnJack,      // PortConnection
        TRUE                // IsConnected
    },
    // Jack 2
    {
        (SPEAKER_FRONT_CENTER | SPEAKER_LOW_FREQUENCY), // (C,Sub)
        RGB(0,0,255),       // (red)
        eConnType3Point5mm,
        eGeoLocRear,
        eGenLocPrimaryBox,
        ePortConnJack,
        TRUE
    },
    // Jack 3
    {
        (SPEAKER_SIDE_LEFT | SPEAKER_SIDE_RIGHT),  // (SL,SR)
        RGB(0,255,255),     // (yellow)
        eConnType3Point5mm,
        eGeoLocRear,
        eGenLocPrimaryBox,
        ePortConnJack,
        TRUE
    }
};
```

If the audio hardware can detect whether the device is plugged in, the driver dynamically updates the value of this member to indicate whether the device is currently plugged in (**TRUE**) or unplugged (**FALSE**)

In the preceding code example, the **IsConnected** member in each array element is set to **TRUE** to indicate that the endpoint device is plugged into the jack. However, if the hardware lacks jack presence detection, **IsConnected** must always be set to **TRUE**, whether there is a device plugged into the jack. To remove the ambiguity that results from this dual meaning of the **TRUE** return value, a client application can call [IKsJackDescription2::GetJackDescription2](https://go.microsoft.com/fwlink/p/?linkid=143698) to read the JackCapabilities flag of the [**KSJACK\_DESCRIPTION2**](https://msdn.microsoft.com/library/windows/hardware/ff537138) structure. If this flag has the JACKDESC2\_PRESENCE\_DETECT\_CAPABILITY bit set, it indicates that the endpoint does in fact support jack presence detection. In that case, the value of the **IsConnected** member can be interpreted as an accurate reflection of the insertion status of the jack.

The RGB macro that appears in the preceding structures is defined in header file Wingdi.h in the Windows SDK.

In addition, an array of jack descriptions can be used to show that two or more jacks are functionally equivalent to each other. In the following code example, the audio driver combines the jack descriptions for a yellow RCA jack and for a black digital-optical jack into one array to indicate to the user that the two jacks carry the same signal:

```cpp
KSJACK_DESCRIPTION ar_SPDIF_Jacks[] =
{
    // Jack 1
    {
        (SPEAKER_FRONT_LEFT | SPEAKER_FRONT_RIGHT), // ChannelMapping (L,R)
        RGB(0,255,255),         // Color (yellow)
        eConnTypeRCA,           // ConnectionType (RCA)
        eGeoLocRear,            // GeoLocation
 eGenLocPrimaryBox,   // GenLocation
        ePortConnJack,       // PortConnection
        TRUE                    // IsConnected
    },
    // Jack 2
    {
        (SPEAKER_FRONT_LEFT | SPEAKER_FRONT_RIGHT), // (L,R)
        RGB(0,0,0),             // (black)
        eConnTypeOptical,       // (optical)
        eGeoLocRear,
 eGenLocPrimaryBox,
        ePortConnJack,
        TRUE
    }
};
```

In the preceding code example, the values of the **ChannelMapping** members in the two KSJACK\_DESCRIPTION structures are identical.

The "Simple" MSVAD sample driver in the WDK (in sample directory Src\\Audio\\Msvad\\Simple) can be adapted to support the KSPROPERTY\_JACK\_DESCRIPTION property. This sample driver is convenient for demonstrating the use of the property because it does not require actual hardware. Thus, it can be installed on any computer running Windows. (However, only Windows Vista and later operating systems provide full support for the KSPROPERTY\_JACK\_DESCRIPTION property.) For more information about this sample, see [Windows Driver Kit Samples](https://msdn.microsoft.com/library/windows/hardware/ff554118).

The topology filter for the Simple MSVAD sample defines three bridge pins. These pins are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Pin ID</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>KSPIN_TOPO_SYNTHIN_SOURCE</p></td>
<td align="left"><p>MIDI input jack</p></td>
</tr>
<tr class="even">
<td align="left"><p>KSPIN_TOPO_MIC_SOURCE</p></td>
<td align="left"><p>Microphone input jack</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSPIN_TOPO_LINEOUT_DEST</p></td>
<td align="left"><p>Stereo speaker output jack</p></td>
</tr>
</tbody>
</table>

 

The remainder of this topic explains how to modify the Simple MSVAD sample driver to provide the jack information for the three bridge pins.

First, the jack information for these pins can be specified as follows:

```cpp
// Describe MIDI input jack (pin ID = KSPIN_TOPO_SYNTHIN_SOURCE).
static KSJACK_DESCRIPTION SynthIn_Jack[] =
{
    {
        0,                  // ChannelMapping
        RGB(255,255,0),    // Color (cyan)
 eConnType3Point5mm, // ConnectionType
        eGeoLocRear,        // GeoLocation
        eGenLocPrimaryBox,  // GenLocation
        ePortConnJack,      // PortConnection
        TRUE                // IsConnected
    }
};

// Describe microphone jack (pin ID = KSPIN_TOPO_MIC_SOURCE).
static KSJACK_DESCRIPTION MicIn_Jack[] =
{
    {
        0,
        RGB(0,128,255),   // (orange)
 eConnType3Point5mm,
        eGeoLocFront,
        eGenLocPrimaryBox,
        ePortConnJack,
        TRUE
    }
};

// Describe stereo speaker jack (pin ID = KSPIN_TOPO_LINEOUT_DEST).
static KSJACK_DESCRIPTION LineOut_Jack[] =
{
    {
        (SPEAKER_FRONT_LEFT | SPEAKER_FRONT_RIGHT), // ChannelMapping (L,R)
        RGB(0,255,0),       // (green)
 eConnType3Point5mm,
        eGeoLocRear,
        eGenLocPrimaryBox,
        ePortConnJack,
        TRUE
    }
};
```

The preceding code example sets the **ChannelMapping** members for the two capture pins to 0. Only analog rendering pins should have nonzero **ChannelMapping** values.

The primary modification to the Simple MSVAD sample is to add the following property handler to the implementation of the topology miniport in sample file Mintopo.cpp:

```cpp
#define ARRAY_LEN(a)  sizeof(a)/sizeof(a[0]);
#define MAXIMUM_VALID_PIN_ID  KSPIN_TOPO_WAVEIN_DEST

NTSTATUS
CMiniportTopology::PropertyHandlerJackDescription(
               IN PPCPROPERTY_REQUEST PropertyRequest)
{
    PAGED_CODE();

    ASSERT(PropertyRequest);

    DPF_ENTER(("[PropertyHandlerJackDescription]"));

    NTSTATUS ntStatus = STATUS_INVALID_DEVICE_REQUEST;
    ULONG nPinId = (ULONG)-1;

    if (PropertyRequest->InstanceSize >= sizeof(ULONG))
    {
        nPinId = *((PULONG)(PropertyRequest->Instance));

        if (nPinId > MAXIMUM_VALID_PIN_ID)
        {
            ntStatus = STATUS_INVALID_PARAMETER;
        }
        else if (PropertyRequest->Verb & KSPROPERTY_TYPE_BASICSUPPORT)
        {
            ntStatus = PropertyHandler_BasicSupport(
                            PropertyRequest,
                            KSPROPERTY_TYPE_BASICSUPPORT | KSPROPERTY_TYPE_GET,
                            VT_ILLEGAL);
        }
        else
        {
            PKSJACK_DESCRIPTION pJack = NULL;
            ULONG cJacks = 0;

            switch (nPinId)
            {
            case KSPIN_TOPO_SYNTHIN_SOURCE:
                pJack = SynthIn_Jack;
                cJacks = ARRAY_LEN(SynthIn_Jack);
                break;
            case KSPIN_TOPO_MIC_SOURCE:
                pJack = MicIn_Jack;
                cJacks = ARRAY_LEN(MicIn_Jack);
                break;
            case KSPIN_TOPO_LINEOUT_DEST:
                pJack = LineOut_Jack;
                cJacks = ARRAY_LEN(LineOut_Jack);
                break;
            default:
                break;
            }

            ULONG cbNeeded = sizeof(KSMULTIPLE_ITEM) +
                             sizeof(KSJACK_DESCRIPTION) * cJacks;

            if (PropertyRequest->ValueSize == 0)
            {
                PropertyRequest->ValueSize = cbNeeded;
                ntStatus = STATUS_BUFFER_OVERFLOW;
            }
            else if (PropertyRequest->ValueSize < cbNeeded)
            {
                ntStatus = STATUS_BUFFER_TOO_SMALL;
            }
            else if (PropertyRequest->Verb & KSPROPERTY_TYPE_GET)
            {
                PKSMULTIPLE_ITEM pMI = (PKSMULTIPLE_ITEM)PropertyRequest->Value;

                pMI->Size = cbNeeded;
                pMI->Count = cJacks;

                // Copy jack description structure into Value buffer.
                // RtlCopyMemory correctly handles the case Length=0.
                PKSJACK_DESCRIPTION pDesc = (PKSJACK_DESCRIPTION)(pMI + 1);

                RtlCopyMemory(pDesc, pJack, pMI->Size * pMI->Count);

                ntStatus = STATUS_SUCCESS;
            }
        }
    }

    return ntStatus;
}

NTSTATUS
PropertyHandler_TopoFilter(IN PPCPROPERTY_REQUEST PropertyRequest)
{
    PAGED_CODE();

    ASSERT(PropertyRequest);

    DPF_ENTER(("[PropertyHandler_TopoFilter]"));

    // PropertyRequest structure is filled by PortCls.
    // MajorTarget is a pointer to miniport object for miniports.
    //
    NTSTATUS ntStatus = STATUS_INVALID_DEVICE_REQUEST;
    PCMiniportTopology pMiniport = (PCMiniportTopology)PropertyRequest->MajorTarget;

    if (IsEqualGUIDAligned(*PropertyRequest->PropertyItem->Set, KSPROPSETID_Jack) &&
        (PropertyRequest->PropertyItem->Id == KSPROPERTY_JACK_DESCRIPTION))
    {
        ntStatus = pMiniport->PropertyHandlerJackDescription(PropertyRequest);
    }

    return ntStatus;
}
```

The preceding code example refers to the three KSJACK\_DESCRIPTION variables - SynthIn\_Jack, MicIn\_Jack, and LineOut\_Jack - that were defined previously. If the client queries the filter for the jack description of a valid pin, but one that is not a bridge pin (and therefore has no jack description), the query succeeds (with status code STATUS\_SUCCESS), but the property handler returns an empty jack description consisting of a KSMULTIPLE\_ITEM structure and nothing else. If the client specifies an invalid pin ID (that identifies a nonexistent pin), the handler returns status code STATUS\_INVALID\_PARAMETER.

Two additional modifications to the Simple MSVAD sample are required to support the KSPROPERTY\_JACK\_DESCRIPTION property. These are:

-   Add the declaration of the **PropertyHandlerJackDescription** method in the preceding code example to the CMiniportTopology class definition in header file Mintopo.h.

-   Implement an automation table for the topology filter and load the address of this table into the **AutomationTable** member of the [**PCFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff537694) structure in header file Toptable.h. This structure is named **MiniportFilterDescriptor**.

To implement the automation table for the filter, insert the following code into header file Toptable.h (before the definition of **MiniportFilterDescriptor**):

```cpp
static PCPROPERTY_ITEM PropertiesTopoFilter[] =
{
    {
        &KSPROPSETID_Jack,
        KSPROPERTY_JACK_DESCRIPTION,
        KSPROPERTY_TYPE_GET | KSPROPERTY_TYPE_BASICSUPPORT,
        PropertyHandler_TopoFilter
    }
};

DEFINE_PCAUTOMATION_TABLE_PROP(AutomationTopoFilter, PropertiesTopoFilter);
```

In the preceding code example, the **Handler** member of the [**PCPROPERTY\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff537722) structure contains a function pointer to the property handler that was added to Mintopo.cpp in a previous step. To make the property handler accessible from the header file, insert an **extern** function declaration for PropertyHandler\_TopoFilter at the start of the header file.

For more information about the jack description property, see [Jack Descriptions for Dynamic Audio Subdevices](jack-descriptions-for-dynamic-audio-subdevices.md).

 

 




