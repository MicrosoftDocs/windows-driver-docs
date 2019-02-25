---
title: KSPROPSETID\_BdaLNBInfo
description: KSPROPSETID\_BdaLNBInfo
ms.assetid: 2b385e93-2d0d-44ca-9cfc-58afea946db6
ms.date: 11/28/2017
ms.localizationpriority: medium
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

### Comments

The LNB is the device at the focal point of a satellite dish. The LNB gathers the signal reflected by the dish and sends it to the RF tuner's LNB amplifier.

The KSPROPSETID\_BdaLNBInfo property set communicates information about a satellite dish's LNB device to an RF tuner. When a client sends a [**KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY**](ksproperty-bda-rf-tuner-frequency.md) request to tune an RF tuner to a specific frequency, the tuner can send, if required, control signals to the LNB device to adjust internal parameters according to the properties of the LNB.

### See Also

[**KSPROPERTY\_BDA\_RF\_TUNER\_FREQUENCY**](ksproperty-bda-rf-tuner-frequency.md)

 

 





