---
title: Connecting Between Pins of Filters for BDA Minidrivers
description: Connecting Between Pins of Filters for BDA Minidrivers
ms.assetid: 549031f3-1501-43c0-b172-bc88613d7e61
keywords:
- Broadcast Driver Architecture WDK AVStream , pin data ranges
- BDA WDK AVStream , pin data ranges
- data ranges WDK AVStream
- ranges WDK AVStream
- pin data ranges WDK
- pin connections WDK BDA
- connecting pins WDK BDA
- connections WDK BDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Connecting Between Pins of Filters for BDA Minidrivers





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

 

 

 




