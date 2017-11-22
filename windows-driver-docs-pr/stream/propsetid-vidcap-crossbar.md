---
title: PROPSETID\_VIDCAP\_CROSSBAR
description: PROPSETID\_VIDCAP\_CROSSBAR
MS-HAID:
- 'vidcapprop\_a98cf1c8-5afd-49c7-a865-86ee3cc97fff.xml'
- 'stream.propsetid\_vidcap\_crossbar'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a2ed126c-75ee-4346-845e-9f675ca34416
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_VIDCAP_CROSSBAR%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




