---
title: PROPSETID\_VIDCAP\_SELECTOR
description: PROPSETID\_VIDCAP\_SELECTOR
ms.assetid: a7328f22-be49-48ac-b923-15f66dc38ccb
---

# PROPSETID\_VIDCAP\_SELECTOR


## <span id="ddk_propsetid_vidcap_selector_ks"></span><span id="DDK_PROPSETID_VIDCAP_SELECTOR_KS"></span>


The PROPSETID\_VIDCAP\_SELECTOR property set is new for use with the [USB Video Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff568649). This property set contains properties that are needed to implement the **ISelector** interface (see the DirectShow documentation in the Microsoft Windows SDK).

The KSPROPERTY\_VIDCAP\_SELECTOR enumeration in *ksmedia.h* specifies the properties of this set.

This property set controls the node that is currently providing lens input. Support for this property set is optional and should be implemented only by devices that provide these controls.

Clients of the USB video class driver can make the following requests of filters or nodes:

[**KSPROPERTY\_SELECTOR\_SOURCE\_NODE\_ID**](ksproperty-selector-source-node-id.md)

[**KSPROPERTY\_NUM\_SOURCES**](ksproperty-num-sources.md)

### <span id="directshow_interfaces"></span><span id="DIRECTSHOW_INTERFACES"></span>DirectShow Interfaces

Properties in the PROPSETID\_VIDCAP\_SELECTOR property set are accessed through the DirectShow **ISelector** interface (see the DirectShow documentation in the Microsoft Windows SDK).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_VIDCAP_SELECTOR%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




