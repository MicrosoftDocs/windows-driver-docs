---
title: PROPSETID\_EXT\_TRANSPORT
description: PROPSETID\_EXT\_TRANSPORT
ms.assetid: 2e96dec7-43a9-44a4-9636-4ccb5244d5bd
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PROPSETID\_EXT\_TRANSPORT


## <span id="ddk_propsetid_ext_transport_ks"></span><span id="DDK_PROPSETID_EXT_TRANSPORT_KS"></span>


The PROPSETID\_EXT\_TRANSPORT property set controls the transport of data to and from an external device.

The KSPROPERTY\_EXTXPORT enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by minidrivers that support external video capture devices.

[**KSPROPERTY\_EXTXPORT\_CAPABILITIES**](ksproperty-extxport-capabilities.md)

[**KSPROPERTY\_EXTXPORT\_INPUT\_SIGNAL\_MODE**](ksproperty-extxport-input-signal-mode.md)

[**KSPROPERTY\_EXTXPORT\_OUTPUT\_SIGNAL\_MODE**](ksproperty-extxport-output-signal-mode.md)

[**KSPROPERTY\_EXTXPORT\_LOAD\_MEDIUM**](ksproperty-extxport-load-medium.md)

[**KSPROPERTY\_EXTXPORT\_MEDIUM\_INFO**](ksproperty-extxport-medium-info.md)

[**KSPROPERTY\_EXTXPORT\_STATE**](ksproperty-extxport-state.md)

[**KSPROPERTY\_EXTXPORT\_STATE\_NOTIFY**](ksproperty-extxport-state-notify.md)

[**KSPROPERTY\_EXTXPORT\_TIMECODE\_SEARCH**](ksproperty-extxport-timecode-search.md)

[**KSPROPERTY\_EXTXPORT\_ATN\_SEARCH**](ksproperty-extxport-atn-search.md)

[**KSPROPERTY\_EXTXPORT\_RTC\_SEARCH**](ksproperty-extxport-rtc-search.md)

[**KSPROPERTY\_RAW\_AVC\_CMD**](ksproperty-raw-avc-cmd.md)

### <span id="directshow_interface"></span><span id="DIRECTSHOW_INTERFACE"></span>DirectShow Interface

The DirectShow **IAMExtTransport** interface (see the DirectShow documentation in the Microsoft Windows SDK). provides access to the properties of this set. The interface defines many methods, but only a subset for external device control are implemented.

 

 





