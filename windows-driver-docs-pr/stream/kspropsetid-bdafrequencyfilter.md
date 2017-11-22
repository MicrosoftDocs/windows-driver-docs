---
title: KSPROPSETID\_BdaFrequencyFilter
description: KSPROPSETID\_BdaFrequencyFilter
MS-HAID:
- 'bdaref\_d1b3b4cd-c501-4771-a897-00e1b05c1f30.xml'
- 'stream.kspropsetid\_bdafrequencyfilter'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7650a239-3d49-4cb1-99bb-12bac55d70d2
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

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The KSPROPSETID\_BdaFrequencyFilter property set is generic across almost all tuners. It is used to inform the tuner node how to tune the RF signal.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_BdaFrequencyFilter%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




