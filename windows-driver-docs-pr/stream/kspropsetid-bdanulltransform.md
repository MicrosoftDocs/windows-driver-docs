---
title: KSPROPSETID\_BdaNullTransform
description: KSPROPSETID\_BdaNullTransform
ms.assetid: 08277c76-4fa5-46d0-8c86-4bc0e060fa9c
---

# KSPROPSETID\_BdaNullTransform


## <span id="ddk_kspropsetid_bdanulltransform_ks"></span><span id="DDK_KSPROPSETID_BDANULLTRANSFORM_KS"></span>


KSPROPSETID\_BdaNullTransform is the BDA **null** transform property set. It is used to instruct a node to pass a signal through without change. Starting a **NULL** transform on a node effectively changes the node into direct connection from its input to its output with no other function.

The following properties are available:

<span id="KSPROPERTY_BDA_NULL_TRANSFORM_START"></span><span id="ksproperty_bda_null_transform_start"></span>[**KSPROPERTY\_BDA\_NULL\_TRANSFORM\_START**](ksproperty-bda-null-transform-start.md)  
Disables any transform that the node previously applied to a signal and allows the signal to pass through the node unchanged.

<span id="KSPROPERTY_BDA_NULL_TRANSFORM_STOP"></span><span id="ksproperty_bda_null_transform_stop"></span>[**KSPROPERTY\_BDA\_NULL\_TRANSFORM\_STOP**](ksproperty-bda-null-transform-stop.md)  
Restarts the transform that the node performed on the signal before that transform was disabled with the KSPROPERTY\_BDA\_NULL\_TRANSFORM\_START property.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The network provider filter can use this property set if a node supports it and the network provider needs the signal to pass through that particular node unchanged.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_BdaNullTransform%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




