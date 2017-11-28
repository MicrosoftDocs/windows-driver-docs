---
title: PROPSETID\_EXT\_DEVICE
description: PROPSETID\_EXT\_DEVICE
ms.assetid: fe1a14dc-b337-462b-ac2a-10eef036ef7f
---

# PROPSETID\_EXT\_DEVICE


## <span id="ddk_propsetid_ext_device_ks"></span><span id="DDK_PROPSETID_EXT_DEVICE_KS"></span>


The PROPSETID\_EXT\_DEVICE property set controls an external device such as a Mini-DV camcorder.

The KSPROPERTY\_EXTDEVICE enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by minidrivers that support external video capture devices.

[**KSPROPERTY\_EXTDEVICE\_ID**](ksproperty-extdevice-id.md)

[**KSPROPERTY\_EXTDEVICE\_VERSION**](ksproperty-extdevice-version.md)

[**KSPROPERTY\_EXTDEVICE\_POWER\_STATE**](ksproperty-extdevice-power-state.md)

[**KSPROPERTY\_EXTDEVICE\_PORT**](ksproperty-extdevice-port.md)

[**KSPROPERTY\_EXTDEVICE\_CAPABILITIES**](ksproperty-extdevice-capabilities.md)

### <span id="directshow_interface"></span><span id="DIRECTSHOW_INTERFACE"></span>DirectShow Interface

The DirectShow **IAMExtDevice** interface (see the DirectShow documentation in the Microsoft Windows SDK) provides access to the properties of this set.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_EXT_DEVICE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




