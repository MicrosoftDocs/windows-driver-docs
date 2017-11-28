---
title: KSPROPSETID\_BdaDigitalDemodulator
description: KSPROPSETID\_BdaDigitalDemodulator
ms.assetid: 536c247d-049b-4d48-96b7-f2aa01f1fa91
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

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The KSPROPSETID\_BdaDigitalDemodulator property set describes the properties of a DVB demodulator node. Use this property set instead of KSPROPSETID\_BdaAutodemodulate if the demodulator requires specific values to be set.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[KSPROPSETID\_BdaAutodemodulate](kspropsetid-bdaautodemodulate.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_BdaDigitalDemodulator%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




