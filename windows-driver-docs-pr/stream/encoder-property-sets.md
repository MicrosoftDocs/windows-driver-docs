---
title: Encoder Property Sets
description: Encoder Property Sets
ms.assetid: b273464d-0d40-488c-a848-291f949609f0
---

# Encoder Property Sets


## <span id="ddk_encoder_property_sets_ks"></span><span id="DDK_ENCODER_PROPERTY_SETS_KS"></span>


This section describes the encoder and codec API-specific property sets that are available for encoder minidrivers that use WDM kernel-streaming services in Microsoft Windows 98/Me, Windows 2000, and Windows XP and later.

The reference page for each property contains a table with the column headings that are shown below.

| Get | Set | Target | Property descriptor type | Property value type |
|-----|-----|--------|--------------------------|---------------------|

 

These headings have the following meanings:

-   **Get**

    Does the target KS object support the KSPROPERTY\_TYPE\_GET property request?

-   **Set**

    Does the target KS object support the KSPROPERTY\_TYPE\_SET property request?

-   **Target**

    This is the KS object to which property request is sent. The target for a video encoder property is either a filter or a pin. (The property request specifies the target object by its kernel handle.)

-   **Property descriptor type**

    The property descriptor specifies the property and the operation to perform on that property. The descriptor always begins with a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure.

-   **Property value type**

    A property has a value and the type of this value depends on the property. For example, a property that can be in one of only two states--on or off--typically has a BOOL value. A property that can assume integer values from 0x0 to 0xFFFFFFFF might have a ULONG value. More complex properties might have values that are arrays or structures.

The property descriptor and property value above are the property-specific versions of the instance-specification and operation-data buffers that are discussed in [KS Properties, Events, and Methods](https://msdn.microsoft.com/library/windows/hardware/ff567673).

A property request uses one of the following flags to specify the operation that is to be performed on the property:

-   KSPROPERTY\_TYPE\_BASICSUPPORT

-   KSPROPERTY\_TYPE\_GET

-   KSPROPERTY\_TYPE\_SET

All filter and pin objects support the basic-support operation on their properties. Whether they support the *get* and *Set* operations depends on the property. A property that represents an inherent capability of the filter or pin object is likely to require only a *get* operation. A property that represents a configurable setting might require only a *Set* operation, although a *get* operation might also be useful for reading the current setting. For more information about using the get, set, and basic-support operations with video encoder properties, see [KS Properties](https://msdn.microsoft.com/library/windows/hardware/ff567671).

A table in the description of every property indicates whether video encoder minidrivers are required to support reading or writing the property. Video encoder minidrivers should return STATUS\_NOT\_SUPPORTED in response to get or set requests for properties that are not supported by the minidriver.

The following property sets each contain a single property that must be implemented by video encoder minidrivers. That is, effectively each property gets its own set, so specify 0 in the **PropertyId** member of the [**KSPROPERTY\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff565176) member in the [**KSPROPERTY\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff565617) structure as required.

The following property sets belong to the codec API:

[CODECAPI\_VIDEO\_ENCODER](codecapi-video-encoder.md)

[CODECAPI\_AUDIO\_ENCODER](codecapi-audio-encoder.md)

[CODECAPI\_SETALLDEFAULTS](codecapi-setalldefaults.md)

[CODECAPI\_ALLSETTINGS](codecapi-allsettings.md)

[CODECAPI\_SUPPORTSEVENTS](codecapi-supportsevents.md)

[CODECAPI\_CURRENTCHANGELIST](codecapi-currentchangelist.md)

The following property sets belong to the encoder API:

[ENCAPIPARAM\_BITRATE](encapiparam-bitrate.md)

[ENCAPIPARAM\_BITRATE\_MODE](encapiparam-bitrate-mode.md)

[ENCAPIPARAM\_PEAK\_BITRATE](encapiparam-peak-bitrate.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Encoder%20Property%20Sets%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




