---
title: KSPROPERTY_PIN_MODEDATAFORMATS
description: Clients use the KSPROPERTY_PIN_MODEDATAFORMATS property to retrieve a list of the supported formats for each supported mode for pins instantiated by the pin factory.
keywords: ["KSPROPERTY_PIN_MODEDATAFORMATS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_MODEDATAFORMATS
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 04/12/2021
---

# KSPROPERTY_PIN_MODEDATAFORMATS

Clients use the  **KSPROPERTY_PIN_MODEDATAFORMATS** property to retrieve a list of the supported formats for each supported audio signal processing mode for pins instantiated by the pin factory.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | No | Filter | **KSP_PIN**, followed by a Mode GUID | **KSMULTIPLE_ITEM** structure, followed by a sequence of [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) structures |

## Remarks

Clients use this property to retrieve a list of formats supported for a specific audio signal processing mode by pins instantiated by the pin factory.

Specify this property using [**KSP_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) followed by the Mode GUID, where the **KSP_PIN** member and the Mode GUID specify the pin factory and Mode for which to return the list of formats.

**KSPROPERTY_PIN_MODEDATAFORMATS** returns the supported formats as a [**KSMULTIPLE_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) structure where each item in the structure is a ULONGLONG with the offset to a specific [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) structure in the value from the beginning of the **KSMULTIPLE_ITEM**.

- The **KSMULTIPLE_ITEM::Size** value includes the size of the **KSMULTIPLE_ITEM** and the sizes of each **KSDATAFORMAT**.

- The **KSMULTIPLE_ITEM::Count** value includes the count of indexes to each **KSDATAFORMAT**.

In almost all cases, the **KSDATAFORMAT** structures being returned will actually be **KSDATAFORMAT_WAVEFORMATEXTENSIBLE** or [**KSDATAFORMAT_WAVEFORMATEX**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_waveformatex) structures with a Size that matches.

As an example, a value for a pin factory that supports two formats would look like the following.

```cpp
{
    // Example Property Value Result, with 2 formats
    // Size of the KSMULTIPLE_ITEM structure + Size of two ULONGLONG offset values + Size of first format + Size of second format
    sizeof(KSMULTIPLE_ITEM) + sizeof(ULONGLONG)*2 + (First KSDATAFORMAT::Size) + (Second KSDATAFORMAT::Size),
    // Number of formats being returned
    2,
    // Offset of the first format from the beginning of the Property Value
    (sizeof(KSMULTIPLE_ITEM) + 2 * sizeof(ULONGLONG)),
    // Offset of the second format from the beginning of the Property Value
    (sizeof(KSMULTIPLE_ITEM) + 2 * sizeof(ULONGLONG) + (First KSDATAFORMAT::Size),
    // First format structure
    {(First KSDATAFORMAT)},
    // Second format structure
    {(Second KSDATAFORMAT)}
}
```

For more information, see [Extensible Wave-Format Descriptors](../audio/extensible-wave-format-descriptors.md).

## Supported Mode Format and Buffer Recommendations

Starting with Windows 10, version 2004 the use of **KSPROPERTY_PIN_MODEDATAFORMATS** and [**KSAUDIO_PACKETSIZE_CONSTRAINTS2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints2) is the preferred approach for drivers to report the supported audio signal processing mode formats and buffer size constraints. Using this approach allows the Windows audio system to efficiently retrieve the endpoint streaming capabilities without having to create numerous streams to discover the formats and buffer sizes supported by the endpoint.

## Requirements

**Version:** Available starting with Windows 10, version 2004

**Header:** ks.h (include Ks.h)

## See also

[**KSP\_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat)

[**KSAUDIO_PACKETSIZE_CONSTRAINTS2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksaudio_packetsize_constraints2)

[**KSDATAFORMAT_WAVEFORMATEX**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksdataformat_waveformatex)
