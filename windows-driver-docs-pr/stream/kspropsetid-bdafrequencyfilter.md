---
title: KSPROPSETID\_BdaFrequencyFilter
description: KSPROPSETID\_BdaFrequencyFilter
ms.assetid: 7650a239-3d49-4cb1-99bb-12bac55d70d2
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_BdaFrequencyFilter


## <span id="ddk_kspropsetid_bdafrequencyfilter_ks"></span><span id="DDK_KSPROPSETID_BDAFREQUENCYFILTER_KS"></span>


KSPROPSETID\_BdaFrequencyFilter is the BDA frequency filter property set. It is used to control the RF tuner node in a receiver topology.

The following properties are available:

<span id="KSPROPERTY_BDA_RF_TUNER_FREQUENCY"></span><span id="ksproperty_bda_rf_tuner_frequency"></span>[**KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY**](ksproperty-bda-rf-tuner-frequency.md)  
Informs the tuner node about the base frequency of the signal carrier. Multiply the base frequency by the value of the KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY\_MULTIPLIER property to obtain the actual frequency.

<span id="KSPROPERTY_BDA_RF_TUNER_POLARITY"></span><span id="ksproperty_bda_rf_tuner_polarity"></span>[**KSPROPERTY\_BDA\_RF\_TUNER\_POLARITY**](ksproperty-bda-rf-tuner-polarity.md)  
Informs the tuner node about the polarization that is used on the transmitted signal.

<span id="KSPROPERTY_BDA_RF_TUNER_RANGE"></span><span id="ksproperty_bda_rf_tuner_range"></span>[**KSPROPERTY\_BDA\_RF\_TUNER\_RANGE**](ksproperty-bda-rf-tuner-range.md)  
Sets the tuner range.

<span id="KSPROPERTY_BDA_RF_TUNER_TRANSPONDER"></span><span id="ksproperty_bda_rf_tuner_transponder"></span>[**KSPROPERTY\_BDA\_RF\_TUNER\_TRANSPONDER**](ksproperty-bda-rf-tuner-transponder.md)  
Informs the tuner node of the appropriate transponder number.

<span id="KSPROPERTY_BDA_RF_TUNER_BANDWIDTH"></span><span id="ksproperty_bda_rf_tuner_bandwidth"></span>[**KSPROPERTY\_BDA\_RF\_TUNER\_BANDWIDTH**](ksproperty-bda-rf-tuner-bandwidth.md)  
Informs the tuner node of the bandwidth of the transmitted signal.

<span id="KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER"></span><span id="ksproperty_bda_rf_tuner_frequency_multiplier"></span>[**KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY\_MULTIPLIER**](ksproperty-bda-rf-tuner-frequency-multiplier.md)  
Informs the tuner node about the value with which to multiply the value of the KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY property to obtain the actual frequency.

### Comments

The KSPROPSETID\_BdaFrequencyFilter property set is generic across almost all tuners. It is used to inform the tuner node how to tune the RF signal.

 

 





