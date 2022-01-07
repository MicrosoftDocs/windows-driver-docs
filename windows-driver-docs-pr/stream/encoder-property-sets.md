---
title: Encoder Property Sets
description: Describes encoder and codec API-specific property sets available for encoder minidrivers that use WDM kernel-streaming services.
ms.date: 10/11/2021
---

# Encoder Property Sets

This section describes the encoder and codec API-specific property sets that are available for encoder minidrivers that use WDM kernel-streaming services in Microsoft Windows 98/Me, Windows 2000, and Windows XP and later.

The reference page for each property contains a table with the column headings that are shown below.

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
|  |  |  |  |  |

These headings have the following meanings:

- **Get**

    Does the target KS object support the KSPROPERTY_TYPE_GET property request?

- **Set**

    Does the target KS object support the KSPROPERTY_TYPE_SET property request?

- **Target**

    This is the KS object to which property request is sent. The target for a video encoder property is either a filter or a pin. (The property request specifies the target object by its kernel handle.)

- **Property descriptor type**

    The property descriptor specifies the property and the operation to perform on that property. The descriptor always begins with a [**KSPROPERTY**](ksproperty-structure.md) structure.

- **Property value type**

    A property has a value and the type of this value depends on the property. For example, a property that can be in one of only two states--on or off--typically has a BOOL value. A property that can assume integer values from 0x0 to 0xFFFFFFFF might have a ULONG value. More complex properties might have values that are arrays or structures.

The property descriptor and property value above are the property-specific versions of the instance-specification and operation-data buffers that are discussed in [KS Properties, Events, and Methods](./ks-properties--events--and-methods.md).

A property request uses one of the following flags to specify the operation that is to be performed on the property:

- KSPROPERTY_TYPE_BASICSUPPORT

- KSPROPERTY_TYPE_GET

- KSPROPERTY_TYPE_SET

All filter and pin objects support the basic-support operation on their properties. Whether they support the *get* and *Set* operations depends on the property. A property that represents an inherent capability of the filter or pin object is likely to require only a *get* operation. A property that represents a configurable setting might require only a *Set* operation, although a *get* operation might also be useful for reading the current setting. For more information about using the get, set, and basic-support operations with video encoder properties, see [KS Properties](./ks-properties.md).

A table in the description of every property indicates whether video encoder minidrivers are required to support reading or writing the property. Video encoder minidrivers should return STATUS_NOT_SUPPORTED in response to get or set requests for properties that are not supported by the minidriver.

The following property sets each contain a single property that must be implemented by video encoder minidrivers. That is, effectively each property gets its own set, so specify 0 in the **PropertyId** member of the [**KSPROPERTY_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_item) member in the [**KSPROPERTY_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_set) structure as required.

The following property sets belong to the codec API:

[CODECAPI_VIDEO_ENCODER](codecapi-video-encoder.md)

[CODECAPI_AUDIO_ENCODER](codecapi-audio-encoder.md)

[CODECAPI_SETALLDEFAULTS](codecapi-setalldefaults.md)

[CODECAPI_ALLSETTINGS](codecapi-allsettings.md)

[CODECAPI_SUPPORTSEVENTS](codecapi-supportsevents.md)

[CODECAPI_CURRENTCHANGELIST](codecapi-currentchangelist.md)

The following property sets belong to the encoder API:

[ENCAPIPARAM_BITRATE](encapiparam-bitrate.md)

[ENCAPIPARAM_BITRATE_MODE](encapiparam-bitrate-mode.md)

[ENCAPIPARAM_PEAK_BITRATE](encapiparam-peak-bitrate.md)
