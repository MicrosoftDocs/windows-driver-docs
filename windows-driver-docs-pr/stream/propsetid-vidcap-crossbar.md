---
title: PROPSETID\_VIDCAP\_CROSSBAR
description: PROPSETID\_VIDCAP\_CROSSBAR
ms.assetid: a2ed126c-75ee-4346-845e-9f675ca34416
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PROPSETID\_VIDCAP\_CROSSBAR


## <span id="ddk_propsetid_vidcap_crossbar_ks"></span><span id="DDK_PROPSETID_VIDCAP_CROSSBAR_KS"></span>


The PROPSETID\_VIDCAP\_CROSSBAR property set controls devices that route video and audio signals. The crossbar is modeled on a general switching matrix with N inputs and M outputs. Any of the input signals can be routed to one or more of the outputs, although actual hardware implementations may allow only a subset of this general routing capability. The crossbar can be used to route either digital or analog signals. A single crossbar can route both video and audio signals. Video pins optionally can indicate an audio pin that is related to a video pin.

The KSPROPERTY\_VIDCAP\_CROSSBAR enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by minidrivers of crossbar devices.

Crossbar capture minidrivers are required to implement the following properties:

[**KSPROPERTY\_CROSSBAR\_CAN\_ROUTE**](ksproperty-crossbar-can-route.md)

[**KSPROPERTY\_CROSSBAR\_CAPS**](ksproperty-crossbar-caps.md)

[**KSPROPERTY\_CROSSBAR\_PININFO**](ksproperty-crossbar-pininfo.md)

[**KSPROPERTY\_CROSSBAR\_ROUTE**](ksproperty-crossbar-route.md)

### <span id="directshow_interface"></span><span id="DIRECTSHOW_INTERFACE"></span>DirectShow Interface

The DirectShow **IAMCrossbar** interface (see the DirectShow documentation in the Microsoft Windows SDK) provides access to the properties of this set.

 

 





