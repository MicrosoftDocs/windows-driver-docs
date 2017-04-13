---
title: Accessing Frequency Properties of a BDA Tuner Node
author: windows-driver-content
description: Accessing Frequency Properties of a BDA Tuner Node
ms.assetid: 47c24e99-c82c-4bc8-af36-bd7f728634ba
keywords: ["method sets WDK BDA , RF tuner node", "property sets WDK BDA , RF tuner node", "KSPROPSETID_BdaFrequencyFilter", "RF tuners WDK BDA", "frequency properties WDK BDA"]
---

# Accessing Frequency Properties of a BDA Tuner Node


## <a href="" id="ddk-accessing-frequency-properties-of-a-bda-tuner-node-ksg"></a>


A network provider uses the [KSPROPSETID\_BdaFrequencyFilter](https://msdn.microsoft.com/library/windows/hardware/ff566542) property set to control an RF tuner node in a BDA filter topology. For example, the network provider uses this property set to inform the tuner node how to tune the RF signal.

In the following code snippet, the controlling pin of the tuner node in the BDA minidriver intercepts and supplies methods for properties of the KSPROPSETID\_BdaFrequencyFilter property set. Note that some KSPROPSETID\_BdaFrequencyFilter properties are only applicable to specific types of tuners.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Accessing%20Frequency%20Properties%20of%20a%20BDA%20Tuner%20Node%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


