---
title: DVD Decoder Minidriver Property Sets
description: DVD Decoder Minidriver Property Sets
MS-HAID:
- 'dvdref\_6f64d8a2-1c99-4f93-b283-09d130f810bc.xml'
- 'stream.dvd\_decoder\_minidriver\_property\_sets'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c24685bd-ea20-4cc2-b419-feb1fa2ea03e
---

# DVD Decoder Minidriver Property Sets


## <span id="ddk_dvd_decoder_minidriver_property_sets_ks"></span><span id="DDK_DVD_DECODER_MINIDRIVER_PROPERTY_SETS_KS"></span>


This section describes DVD decoder-specific property sets that are available for DVD decoder minidrivers that use WDM kernel-streaming services in Microsoft Windows 98/Me, Windows 2000 and Windows XP and later.

The reference page for each property contains a table with the column headings that are shown below.

| Get | Set | Target | Property descriptor type | Property value type |
|-----|-----|--------|--------------------------|---------------------|

 

These headings have the following meanings:

-   **Get**

    Does the target KS object support the KSPROPERTY\_TYPE\_GET property request?

-   **Set**

    Does the target KS object support the KSPROPERTY\_TYPE\_SET property request?

-   **Target**

    This is the KS object to which property request is sent. The target for an DVD decoder property is either a filter or a pin. (The property request specifies the target object by its kernel handle.)

-   **Property descriptor type**

    The property descriptor specifies the property and the operation to perform on that property. The descriptor always begins with a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure.

-   **Property value type**

    A property has a value and the type of this value depends on the property. For example, a property that can be in one of only two states--on or off--typically has a Boolean value. A property that can assume integer values from 0 to 0xFFFFFFFF might have a ULONG value. More complex properties might have values that are arrays or structures.

The property descriptor and property value above are the property-specific versions of the instance-specification and operation-data buffers that are discussed in [KS Properties, Events, and Methods](https://msdn.microsoft.com/library/windows/hardware/ff567673).

A property request uses one of the following flags to specify the operation that is to be performed on the property:

-   KSPROPERTY\_TYPE\_BASICSUPPORT

-   KSPROPERTY\_TYPE\_GET

-   KSPROPERTY\_TYPE\_SET

All filter and pin objects support the basic-support operation on their properties. Whether they support the *get* and *Set* operations depends on the property. A property that represents an inherent capability of the filter or pin object is likely to require only a get operation. A property that represents a configurable setting might require only a set operation, although a get operation might also be useful for reading the current setting. For more information about using the get, set, and basic-support operations with DVD decoder properties, see [KS Properties](https://msdn.microsoft.com/library/windows/hardware/ff567671).

Properties query or change stream aspects. Several property sets are used for DVD decoders. All DVD decoder input streams support the DVD copyright protection property set in addition to the property sets outlined in this topic

Every property description contains a table that indicates whether DVD decoder minidrivers are required to support reading or writing the property. DVD decoder minidrivers should return STATUS\_NOT\_SUPPORTED in response to get or set requests for properties that are not supported by the minidriver.

The following property sets are defined for DVD decoder minidrivers:

[KSPROPSETID\_AudioDecoderOut](kspropsetid-audiodecoderout.md)

[KSPROPSETID\_DvdSubPic](kspropsetid-dvdsubpic.md)

[KSPROPSETID\_CopyProt](kspropsetid-copyprot.md)

[KSPROPSETID\_TSRateChange](kspropsetid-tsratechange.md)

[KSPROPSETID\_VPConfig and KSPROPSETID\_VPVBIConfig](kspropsetid-vpconfig-and-kspropsetid-vpvbiconfig.md)

[KSPROPSETID\_Wave](kspropsetid-wave.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20DVD%20Decoder%20Minidriver%20Property%20Sets%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




