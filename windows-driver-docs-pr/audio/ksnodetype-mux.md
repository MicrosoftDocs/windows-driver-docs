---
title: KSNODETYPE\_MUX
description: KSNODETYPE\_MUX
ms.assetid: c22054fe-7ede-4694-8ae1-6e18e1270185
keywords: ["KSNODETYPE_MUX Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_MUX
api_type:
- NA
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSNODETYPE\_MUX


## <span id="ddk_ksnodetype_mux_ks"></span><span id="DDK_KSNODETYPE_MUX_KS"></span>


The KSNODETYPE\_MUX node represents a multiplexer (MUX). The MUX has multiple input streams and one output stream, all with the same data format. Only one input stream at a time is routed to the output stream.

A KSNODETYPE\_MUX node should support the following required property:

[**KSPROPERTY\_AUDIO\_MUX\_SOURCE**](ksproperty-audio-mux-source.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_MUX%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




