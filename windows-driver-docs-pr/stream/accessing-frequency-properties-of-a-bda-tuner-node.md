---
title: Accessing Frequency Properties of a BDA Tuner Node
description: Accessing Frequency Properties of a BDA Tuner Node
ms.assetid: 47c24e99-c82c-4bc8-af36-bd7f728634ba
keywords:
- method sets WDK BDA , RF tuner node
- property sets WDK BDA , RF tuner node
- KSPROPSETID_BdaFrequencyFilter
- RF tuners WDK BDA
- frequency properties WDK BDA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Frequency Properties of a BDA Tuner Node





A network provider uses the [KSPROPSETID\_BdaFrequencyFilter](https://msdn.microsoft.com/library/windows/hardware/ff566542) property set to control an RF tuner node in a BDA filter topology. For example, the network provider uses this property set to inform the tuner node how to tune the RF signal.

In the following code snippet, the controlling pin of the tuner node in the BDA minidriver intercepts and supplies methods for properties of the KSPROPSETID\_BdaFrequencyFilter property set. Note that some KSPROPSETID\_BdaFrequencyFilter properties are only applicable to specific types of tuners.

```cpp
//
//  BDA RF Tune Frequency Filter
//
//  Defines the dispatch routines for the Properties
//  on the RF Tuner Node
//
DEFINE_KSPROPERTY_TABLE(RFNodeFrequencyProperties)
{
    DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_FREQUENCY(
        CAntennaPin::GetCenterFrequency,
        CAntennaPin::PutCenterFrequency
        ),
    DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_FREQUENCY_MULTIPLIER(
        NULL,
        CAntennaPin::PutFrequencyMultiplier // If this set handler 
        // is not called, the minidriver must determine that the 
        // frequency is in kHz. That is, the default multiplier is 
        // 1000 (1Hz x 1000).
        ),
#ifdef SATELLITE_TUNER // Only applicable to satellite tuners.
    DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_POLARITY(
        NULL, NULL
        ),
    DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_RANGE(
        NULL, NULL
        ),
#endif // SATELLITE_TUNER
#ifdef CHANNEL_BASED_TUNER // Only applicable to channel-based tuners.
    DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_TRANSPONDER(
        NULL, NULL
        ),
#endif // CHANNEL_BASED_TUNER
#ifdef DVBT_TUNER // Only applicable to tuners that tune Digital Video Broadcast (DVB) signals.
    DEFINE_KSPROPERTY_ITEM_BDA_RF_TUNER_BANDWIDTH(
        NULL, NULL
        ),
#endif // DVBT_TUNER
};
```

 

 




