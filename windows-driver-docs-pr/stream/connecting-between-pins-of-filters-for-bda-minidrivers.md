---
title: Connecting Between Pins of Filters for BDA Minidrivers
author: windows-driver-content
description: Connecting Between Pins of Filters for BDA Minidrivers
ms.assetid: 549031f3-1501-43c0-b172-bc88613d7e61
keywords: ["Broadcast Driver Architecture WDK AVStream , pin data ranges", "BDA WDK AVStream , pin data ranges", "data ranges WDK AVStream", "ranges WDK AVStream", "pin data ranges WDK", "pin connections WDK BDA", "connecting pins WDK BDA", "connections WDK BDA"]
---

# Connecting Between Pins of Filters for BDA Minidrivers


## <a href="" id="ddk-connecting-between-pins-of-filters-for-bda-minidrivers-ksg"></a>


To let pins of BDA filters connect to each other, BDA minidrivers for those filters must provide lists of data ranges for the pins as described in [Data Range Intersections in AVStream](data-range-intersections-in-avstream.md). In other words, pins of filters specify the data ranges they support to enable stream connections to pins of other filters that also support those data ranges.

For example, to let pins of BDA tuner and capture filters connect, the output pin of the tuner filter and the input pin of the capture filter must have the following data formats set in the [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures for the pins:

-   **MajorFormat** set to STATIC\_KSDATAFORMAT\_TYPE\_STREAM

-   **SubFormat** set to STATIC\_KSDATAFORMAT\_TYPE\_MPEG2\_TRANSPORT

-   **Specifier** set to STATIC\_KSDATAFORMAT\_SPECIFIER\_BDA\_TRANSPORT

To let pins of BDA capture and demultiplex filters connect, the output pin of the capture filter and the input pin of the demultiplex filter must have the following data formats set in the [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures for the pins:

-   **MajorFormat** set to STATIC\_KSDATAFORMAT\_TYPE\_STREAM

-   **SubFormat** set to STATIC\_KSDATAFORMAT\_SUBTYPE\_BDA\_MPEG2\_TRANSPORT

-   **Specifier** set to STATIC\_KSDATAFORMAT\_SPECIFIER\_NONE

**Note**   You can only set a demultiplex filter's input pin to the STATIC\_KSDATAFORMAT\_SUBTYPE\_BDA\_MPEG2\_TRANSPORT subformat if the AVStream minidriver for the filter is BDA compliant.
If the media type for the input pin is set to STATIC\_KSDATAFORMAT\_SUBTYPE\_BDA\_MPEG2\_TRANSPORT and the filter does not comply to BDA rules, the broadcast signal might not render properly.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Connecting%20Between%20Pins%20of%20Filters%20for%20BDA%20Minidrivers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


