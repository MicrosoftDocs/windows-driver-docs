---
title: PROPSETID\_VIDCAP\_SELECTOR
description: PROPSETID\_VIDCAP\_SELECTOR
ms.assetid: a7328f22-be49-48ac-b923-15f66dc38ccb
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





