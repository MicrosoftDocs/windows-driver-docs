---
title: DVD Decoder Minidriver Property Sets
description: Describes DVD decoder minidriver property sets.
ms.date: 10/08/2021
---

# DVD Decoder Minidriver Property Sets

This section describes DVD decoder-specific property sets that are available for DVD decoder minidrivers that use WDM kernel-streaming services in Microsoft Windows 98/Me, Windows 2000 and Windows XP and later.

The reference page for each property contains a table with the column headings that are shown below.

| Get | Set | Target | Property descriptor type | Property value type |
|-----|-----|--------|--------------------------|---------------------|
|     |     |        |                          |                     |

These headings have the following meanings:

- **Get**

    Does the target KS object support the KSPROPERTY_TYPE_GET property request?

- **Set**

    Does the target KS object support the KSPROPERTY_TYPE_SET property request?

- **Target**

    This is the KS object to which property request is sent. The target for an DVD decoder property is either a filter or a pin. (The property request specifies the target object by its kernel handle.)

- **Property descriptor type**

    The property descriptor specifies the property and the operation to perform on that property. The descriptor always begins with a [**KSPROPERTY**](ksproperty-structure.md) structure.

- **Property value type**

    A property has a value and the type of this value depends on the property. For example, a property that can be in one of only two states--on or off--typically has a Boolean value. A property that can assume integer values from 0 to 0xFFFFFFFF might have a ULONG value. More complex properties might have values that are arrays or structures.

The property descriptor and property value above are the property-specific versions of the instance-specification and operation-data buffers that are discussed in [KS Properties, Events, and Methods](./ks-properties--events--and-methods.md).

A property request uses one of the following flags to specify the operation that is to be performed on the property:

- KSPROPERTY_TYPE_BASICSUPPORT

- KSPROPERTY_TYPE_GET

- KSPROPERTY_TYPE_SET

All filter and pin objects support the basic-support operation on their properties. Whether they support the *get* and *Set* operations depends on the property. A property that represents an inherent capability of the filter or pin object is likely to require only a get operation. A property that represents a configurable setting might require only a set operation, although a get operation might also be useful for reading the current setting. For more information about using the get, set, and basic-support operations with DVD decoder properties, see [KS Properties](./ks-properties.md).

Properties query or change stream aspects. Several property sets are used for DVD decoders. All DVD decoder input streams support the DVD copyright protection property set in addition to the property sets outlined in this topic

Every property description contains a table that indicates whether DVD decoder minidrivers are required to support reading or writing the property. DVD decoder minidrivers should return STATUS_NOT_SUPPORTED in response to get or set requests for properties that are not supported by the minidriver.

The following property sets are defined for DVD decoder minidrivers:

[KSPROPSETID_AudioDecoderOut](kspropsetid-audiodecoderout.md)

[KSPROPSETID_DvdSubPic](kspropsetid-dvdsubpic.md)

[KSPROPSETID_CopyProt](kspropsetid-copyprot.md)

[KSPROPSETID_TSRateChange](kspropsetid-tsratechange.md)

[KSPROPSETID_VPConfig and KSPROPSETID_VPVBIConfig](kspropsetid-vpconfig-and-kspropsetid-vpvbiconfig.md)

[KSPROPSETID_Wave](kspropsetid-wave.md)
