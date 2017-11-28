---
title: KSNODETYPE\_SUPERMIX
description: KSNODETYPE\_SUPERMIX
ms.assetid: fae4d315-b599-4226-8f1d-e1757320afb2
keywords: ["KSNODETYPE_SUPERMIX Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_SUPERMIX
api_type:
- NA
---

# KSNODETYPE\_SUPERMIX


## <span id="ddk_ksnodetype_supermix_ks"></span><span id="DDK_KSNODETYPE_SUPERMIX_KS"></span>


The KSNODETYPE\_SUPERMIX node represents a supermixer. A supermixer has one input stream with *m* channels and one output stream with *n* channels. For each output channel, the supermixer specifies a mix level for each of the input channels that adds to the mix in the output channel. The *m*-channel input stream is upmixed or down-mixed to *n* channels.

A KSNODETYPE\_SUPERMIX node should support the following required properties:

[**KSPROPERTY\_AUDIO\_MIX\_LEVEL\_TABLE**](ksproperty-audio-mix-level-table.md)

[**KSPROPERTY\_AUDIO\_MIX\_LEVEL\_CAPS**](ksproperty-audio-mix-level-caps.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_SUPERMIX%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




