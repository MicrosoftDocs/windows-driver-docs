---
title: PROPSETID\_VIDCAP\_EXTENSION\_UNIT
description: PROPSETID\_VIDCAP\_EXTENSION\_UNIT
ms.assetid: 7aa4742f-e64f-4798-a9e0-8c1f02aa15b3
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_VIDCAP_EXTENSION_UNIT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




