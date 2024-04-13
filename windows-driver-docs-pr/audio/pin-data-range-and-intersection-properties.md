---
title: Pin Data-Range and Intersection Properties
description: Pin Data-Range and Intersection Properties
keywords:
- audio properties WDK , pins
- WDM audio properties WDK , pins
- pins WDK audio , data formats
- data-range formats WDK audio
- formats WDK audio , pins
- intersections WDK audio
ms.date: 04/20/2017
---

# Pin Data-Range and Intersection Properties


## <span id="pin_data_range_and_intersection_properties"></span><span id="PIN_DATA_RANGE_AND_INTERSECTION_PROPERTIES"></span>


Several property requests provide information about the data formats for the audio streams that an audio device is capable of handling at its input and output pins.

The audio-stream data formats that a pin is capable of supporting are expressed in a [**KSMULTIPLE\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) array of [**KSDATARANGE**](/previous-versions/ff561658(v=vs.85))-derived structures. Pin data-range support is exposed through the following three [KSPROPSETID\_Pin](../stream/kspropsetid-pin.md) properties on the filter:

[**KSPROPERTY\_PIN\_DATARANGES**](../stream/ksproperty-pin-dataranges.md)
This property reports data ranges that are static and represent all possible formats supported. Typically, data ranges are contained in a static array in the adapter driver.
[**KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES**](../stream/ksproperty-pin-constraineddataranges.md)
This property reports data ranges that are dynamic and represent the subset of formats supported at the time of the property request. The property handler should contain the logic to decide which formats the pin is capable of supporting at run time. For example, a hardware implementation could have DMA constraints that do not allow support for full-duplex in certain format combinations.
[**KSPROPERTY\_PIN\_DATAINTERSECTION**](../stream/ksproperty-pin-dataintersection.md)
This property selects a data format from a list of data ranges. Selection is based on dynamic capabilities and the format is taken from the subset of formats that the driver can support at the time of the property request. To use this property, the caller supplies an array of data ranges. Beginning at the first element, the property handler searches the array until it finds a data range that it is currently capable of supporting. If successful, the handler outputs a data format that is taken from that data range and returns STATUS\_SUCCESS. Otherwise, the handler returns STATUS\_NO\_MATCH.
The audio-system components use the KSPROPERTY\_PIN\_DATARANGES and KSPROPERTY\_PIN\_DATAINTERSECTION properties. Miniport drivers should support these properties. Support for KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES is optional.

For more information, see [Audio Data Formats and Data Ranges](audio-data-formats-and-data-ranges.md).

**Note**  
The KSPROPERTY\_PIN\_DATARANGES and KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES each begin on an 8-byte-aligned address.

 

 

