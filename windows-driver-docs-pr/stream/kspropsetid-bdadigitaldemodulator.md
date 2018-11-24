---
title: KSPROPSETID\_BdaDigitalDemodulator
description: KSPROPSETID\_BdaDigitalDemodulator
ms.assetid: 536c247d-049b-4d48-96b7-f2aa01f1fa91
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_BdaDigitalDemodulator


## <span id="ddk_kspropsetid_bdadigitaldemodulator_ks"></span><span id="DDK_KSPROPSETID_BDADIGITALDEMODULATOR_KS"></span>


KSPROPSETID\_BdaDigitalDemodulator is the BDA digital demodulator property set. It is used to control signal demodulator nodes that require specific values to be set.

The following properties are available:

<span id="KSPROPERTY_BDA_MODULATION_TYPE"></span><span id="ksproperty_bda_modulation_type"></span>[**KSPROPERTY\_BDA\_MODULATION\_TYPE**](ksproperty-bda-modulation-type.md)  
Sets or retrieves the demodulator type such as QPSK or 8VSB.

<span id="KSPROPERTY_BDA_INNER_FEC_TYPE"></span><span id="ksproperty_bda_inner_fec_type"></span>[**KSPROPERTY\_BDA\_INNER\_FEC\_TYPE**](ksproperty-bda-inner-fec-type.md)  
Sets or retrieves the inner forward error correction (FEC) type.

<span id="KSPROPERTY_BDA_INNER_FEC_RATE"></span><span id="ksproperty_bda_inner_fec_rate"></span>[**KSPROPERTY\_BDA\_INNER\_FEC\_RATE**](ksproperty-bda-inner-fec-rate.md)  
Sets or retrieves the binary convolution scheme used for the inner FEC.

<span id="KSPROPERTY_BDA_OUTER_FEC_TYPE"></span><span id="ksproperty_bda_outer_fec_type"></span>[**KSPROPERTY\_BDA\_OUTER\_FEC\_TYPE**](ksproperty-bda-outer-fec-type.md)  
Sets or retrieves the outer FEC type.

<span id="KSPROPERTY_BDA_OUTER_FEC_RATE"></span><span id="ksproperty_bda_outer_fec_rate"></span>[**KSPROPERTY\_BDA\_OUTER\_FEC\_RATE**](ksproperty-bda-outer-fec-rate.md)  
Sets or retrieves the binary convolution coding scheme used for the outer FEC.

<span id="KSPROPERTY_BDA_SYMBOL_RATE"></span><span id="ksproperty_bda_symbol_rate"></span>[**KSPROPERTY\_BDA\_SYMBOL\_RATE**](ksproperty-bda-symbol-rate.md)  
Sets or retrieves the symbol rate.

<span id="KSPROPERTY_BDA_SPECTRAL_INVERSION"></span><span id="ksproperty_bda_spectral_inversion"></span>[**KSPROPERTY\_BDA\_SPECTRAL\_INVERSION**](ksproperty-bda-spectral-inversion.md)  
Sets or retrieves the setting for spectral inversion.

<span id="KSPROPERTY_BDA_GUARD_INTERVAL"></span><span id="ksproperty_bda_guard_interval"></span>[**KSPROPERTY\_BDA\_GUARD\_INTERVAL**](ksproperty-bda-guard-interval.md)  
Sets or retrieves the setting for guard interval.

<span id="KSPROPERTY_BDA_TRANSMISSION_MODE"></span><span id="ksproperty_bda_transmission_mode"></span>[**KSPROPERTY\_BDA\_TRANSMISSION\_MODE**](ksproperty-bda-transmission-mode.md)  
Sets or retrieves the setting for how broadcast signals are transmitted.

### Comments

The KSPROPSETID\_BdaDigitalDemodulator property set describes the properties of a DVB demodulator node. Use this property set instead of KSPROPSETID\_BdaAutodemodulate if the demodulator requires specific values to be set.

### See Also

[KSPROPSETID\_BdaAutodemodulate](kspropsetid-bdaautodemodulate.md)

 

 





