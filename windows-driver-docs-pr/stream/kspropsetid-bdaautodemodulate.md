---
title: KSPROPSETID\_BdaAutodemodulate
description: KSPROPSETID\_BdaAutodemodulate
ms.assetid: b7c3c934-5b31-48da-9fb0-98007267711b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPSETID\_BdaAutodemodulate


## <span id="ddk_kspropsetid_bdaautodemodulate_ks"></span><span id="DDK_KSPROPSETID_BDAAUTODEMODULATE_KS"></span>


KSPROPSETID\_BdaAutodemodulate is the BDA autodemodulate property set. It is used to control signal demodulator nodes that can automatically determine the characteristics of the modulated signal and demodulate.

The following properties are available:

<span id="KSPROPERTY_BDA_AUTODEMODULATE_START"></span><span id="ksproperty_bda_autodemodulate_start"></span>[**KSPROPERTY\_BDA\_AUTODEMODULATE\_START**](ksproperty-bda-autodemodulate-start.md)  
Informs the demodulator node that, when it is in pause or run state, it should attempt to automatically determine the modulation parameters and demodulate the signal.

<span id="KSPROPERTY_BDA_AUTODEMODULATE_STOP"></span><span id="ksproperty_bda_autodemodulate_stop"></span>[**KSPROPERTY\_BDA\_AUTODEMODULATE\_STOP**](ksproperty-bda-autodemodulate-stop.md)  
Informs the demodulator node that it should stop trying to automatically demodulate the signal.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

KSPROPSETID\_BdaAutodemodulate is also used for demodulator nodes, such as the 8VSB demodulator node which only support one configuration of modulation parameters. For these types of nodes, the demodulator is not informed to set specific values such as Inner and Outer forward error correction (FEC) method.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_BdaAutodemodulate%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




