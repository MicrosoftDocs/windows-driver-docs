---
title: PROPSETID\_VIDCAP\_EXTENSION\_UNIT
description: PROPSETID\_VIDCAP\_EXTENSION\_UNIT
ms.assetid: 7aa4742f-e64f-4798-a9e0-8c1f02aa15b3
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PROPSETID\_VIDCAP\_EXTENSION\_UNIT


## <span id="ddk_propsetid_vidcap_extension_unit_ks"></span><span id="DDK_PROPSETID_VIDCAP_EXTENSION_UNIT_KS"></span>


The PROPSETID\_VIDCAP\_EXTENSION\_UNIT property set is new for use with the [USB Video Class Driver](https://msdn.microsoft.com/library/windows/hardware/ff568649).

This property set is supported for devices that implement a vendor-specific extension unit. Vendor-supplied property pages and applications access this property set through the generic [IKsControl](https://msdn.microsoft.com/library/windows/hardware/ff559766) COM interface.

The KSPROPERTY\_EXTENSION\_UNIT enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by devices that provide vendor-defined hardware controls.

Clients of the USB video class driver can make the following requests of filters or nodes:

[**KSPROPERTY\_EXTENSION\_UNIT\_INFO**](ksproperty-extension-unit-info.md)

### <span id="directshow_interfaces"></span><span id="DIRECTSHOW_INTERFACES"></span>DirectShow Interfaces

Use the following user-mode interfaces to access the properties of this set: **IKsTopologyInfo**, **ISelector**, and **IKsNodeControl**. See the DirectShow documentation in the Microsoft Windows SDK for information about these interfaces.

 

 





