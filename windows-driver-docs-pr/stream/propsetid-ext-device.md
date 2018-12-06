---
title: PROPSETID\_EXT\_DEVICE
description: PROPSETID\_EXT\_DEVICE
ms.assetid: fe1a14dc-b337-462b-ac2a-10eef036ef7f
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





