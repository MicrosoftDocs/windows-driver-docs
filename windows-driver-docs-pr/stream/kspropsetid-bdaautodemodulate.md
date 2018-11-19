---
title: KSPROPSETID\_BdaAutodemodulate
description: KSPROPSETID\_BdaAutodemodulate
ms.assetid: b7c3c934-5b31-48da-9fb0-98007267711b
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_BdaAutodemodulate


## <span id="ddk_kspropsetid_bdaautodemodulate_ks"></span><span id="DDK_KSPROPSETID_BDAAUTODEMODULATE_KS"></span>


KSPROPSETID\_BdaAutodemodulate is the BDA autodemodulate property set. It is used to control signal demodulator nodes that can automatically determine the characteristics of the modulated signal and demodulate.

The following properties are available:

<span id="KSPROPERTY_BDA_AUTODEMODULATE_START"></span><span id="ksproperty_bda_autodemodulate_start"></span>[**KSPROPERTY\_BDA\_AUTODEMODULATE\_START**](ksproperty-bda-autodemodulate-start.md)  
Informs the demodulator node that, when it is in pause or run state, it should attempt to automatically determine the modulation parameters and demodulate the signal.

<span id="KSPROPERTY_BDA_AUTODEMODULATE_STOP"></span><span id="ksproperty_bda_autodemodulate_stop"></span>[**KSPROPERTY\_BDA\_AUTODEMODULATE\_STOP**](ksproperty-bda-autodemodulate-stop.md)  
Informs the demodulator node that it should stop trying to automatically demodulate the signal.

### Comments

KSPROPSETID\_BdaAutodemodulate is also used for demodulator nodes, such as the 8VSB demodulator node which only support one configuration of modulation parameters. For these types of nodes, the demodulator is not informed to set specific values such as Inner and Outer forward error correction (FEC) method.

 

 





