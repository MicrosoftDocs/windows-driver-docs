---
title: KSPROPSETID\_BdaLNBInfo
description: KSPROPSETID\_BdaLNBInfo
ms.assetid: 2b385e93-2d0d-44ca-9cfc-58afea946db6
---

# KSPROPSETID\_BdaLNBInfo


## <span id="ddk_kspropsetid_bdalnbinfo_ks"></span><span id="DDK_KSPROPSETID_BDALNBINFO_KS"></span>


KSPROPSETID\_BdaLNBInfo is the BDA low-noise block (LNB) information property set. It is used to provide an RF tuner with information about a satellite dish's LNB device.

The following properties are available:

<span id="KSPROPERTY_BDA_LNB_LOF_LOW_BAND"></span><span id="ksproperty_bda_lnb_lof_low_band"></span>[**KSPROPERTY\_BDA\_LNB\_LOF\_LOW\_BAND**](ksproperty-bda-lnb-lof-low-band.md)  
Informs the RF tuner node about the local oscillator frequency (LOF) that is used by the LNB for shifting the frequency of incoming low-band RF signals.

<span id="KSPROPERTY_BDA_LNB_LOF_HIGH_BAND"></span><span id="ksproperty_bda_lnb_lof_high_band"></span>[**KSPROPERTY\_BDA\_LNB\_LOF\_HIGH\_BAND**](ksproperty-bda-lnb-lof-high-band.md)  
Informs the RF tuner node about the LOF that is used by the LNB for shifting the frequency of incoming high-band RF signals.

<span id="KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY"></span><span id="ksproperty_bda_lnb_switch_frequency"></span>[**KSPROPERTY\_BDA\_LNB\_SWITCH\_FREQUENCY**](ksproperty-bda-lnb-switch-frequency.md)  
Informs the RF tuner node about the frequency of incoming RF signals at which the tuner should inform the LNB device to switch from using low-band LOF to using high-band LOF or vice versa.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The LNB is the device at the focal point of a satellite dish. The LNB gathers the signal reflected by the dish and sends it to the RF tuner's LNB amplifier.

The KSPROPSETID\_BdaLNBInfo property set communicates information about a satellite dish's LNB device to an RF tuner. When a client sends a [**KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY**](ksproperty-bda-rf-tuner-frequency.md) request to tune an RF tuner to a specific frequency, the tuner can send, if required, control signals to the LNB device to adjust internal parameters according to the properties of the LNB.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY**](ksproperty-bda-rf-tuner-frequency.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_BdaLNBInfo%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




