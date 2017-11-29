---
title: PROPSETID\_EXT\_TRANSPORT
description: PROPSETID\_EXT\_TRANSPORT
ms.assetid: 2e96dec7-43a9-44a4-9636-4ccb5244d5bd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_EXT_TRANSPORT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




