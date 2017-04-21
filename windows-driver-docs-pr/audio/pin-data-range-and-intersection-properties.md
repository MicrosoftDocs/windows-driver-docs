---
title: Pin Data-Range and Intersection Properties
description: Pin Data-Range and Intersection Properties
ms.assetid: 55a749b2-1f54-42f8-876c-f391112d7bab
keywords:
- audio properties WDK , pins
- WDM audio properties WDK , pins
- pins WDK audio , data formats
- data-range formats WDK audio
- formats WDK audio , pins
- intersections WDK audio
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Pin Data-Range and Intersection Properties


## <span id="pin_data_range_and_intersection_properties"></span><span id="PIN_DATA_RANGE_AND_INTERSECTION_PROPERTIES"></span>


Several property requests provide information about the data formats for the audio streams that an audio device is capable of handling at its input and output pins.

The audio-stream data formats that a pin is capable of supporting are expressed in a [**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441) array of [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658)-derived structures. Pin data-range support is exposed through the following three [KSPROPSETID\_Pin](https://msdn.microsoft.com/library/windows/hardware/ff566584) properties on the filter:

[**KSPROPERTY\_PIN\_DATARANGES**](https://msdn.microsoft.com/library/windows/hardware/ff565199)
This property reports data ranges that are static and represent all possible formats supported. Typically, data ranges are contained in a static array in the adapter driver.
[**KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES**](https://msdn.microsoft.com/library/windows/hardware/ff565195)
This property reports data ranges that are dynamic and represent the subset of formats supported at the time of the property request. The property handler should contain the logic to decide which formats the pin is capable of supporting at run time. For example, a hardware implementation could have DMA constraints that do not allow support for full-duplex in certain format combinations.
[**KSPROPERTY\_PIN\_DATAINTERSECTION**](https://msdn.microsoft.com/library/windows/hardware/ff565198)
This property selects a data format from a list of data ranges. Selection is based on dynamic capabilities and the format is taken from the subset of formats that the driver can support at the time of the property request. To use this property, the caller supplies an array of data ranges. Beginning at the first element, the property handler searches the array until it finds a data range that it is currently capable of supporting. If successful, the handler outputs a data format that is taken from that data range and returns STATUS\_SUCCESS. Otherwise, the handler returns STATUS\_NO\_MATCH.
The audio-system components use the KSPROPERTY\_PIN\_DATARANGES and KSPROPERTY\_PIN\_DATAINTERSECTION properties. Miniport drivers should support these properties. Support for KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES is optional.

For more information, see [Audio Data Formats and Data Ranges](audio-data-formats-and-data-ranges.md).

**Note**  
The KSPROPERTY\_PIN\_DATARANGES and KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES each begin on an 8-byte-aligned address.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Pin%20Data-Range%20and%20Intersection%20Properties%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


