---
title: KSPROPSETID\_BdaNullTransform
description: KSPROPSETID\_BdaNullTransform
ms.assetid: 08277c76-4fa5-46d0-8c86-4bc0e060fa9c
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_BdaNullTransform


## <span id="ddk_kspropsetid_bdanulltransform_ks"></span><span id="DDK_KSPROPSETID_BDANULLTRANSFORM_KS"></span>


KSPROPSETID\_BdaNullTransform is the BDA **null** transform property set. It is used to instruct a node to pass a signal through without change. Starting a **NULL** transform on a node effectively changes the node into direct connection from its input to its output with no other function.

The following properties are available:

<span id="KSPROPERTY_BDA_NULL_TRANSFORM_START"></span><span id="ksproperty_bda_null_transform_start"></span>[**KSPROPERTY\_BDA\_NULL\_TRANSFORM\_START**](ksproperty-bda-null-transform-start.md)  
Disables any transform that the node previously applied to a signal and allows the signal to pass through the node unchanged.

<span id="KSPROPERTY_BDA_NULL_TRANSFORM_STOP"></span><span id="ksproperty_bda_null_transform_stop"></span>[**KSPROPERTY\_BDA\_NULL\_TRANSFORM\_STOP**](ksproperty-bda-null-transform-stop.md)  
Restarts the transform that the node performed on the signal before that transform was disabled with the KSPROPERTY\_BDA\_NULL\_TRANSFORM\_START property.

### Comments

The network provider filter can use this property set if a node supports it and the network provider needs the signal to pass through that particular node unchanged.

 

 





