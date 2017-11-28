---
title: PROPSETID\_TIMECODE\_READER
description: PROPSETID\_TIMECODE\_READER
ms.assetid: 7f115ba5-a6b7-4bae-a562-7e84a98ef420
---

# PROPSETID\_TIMECODE\_READER


## <span id="ddk_propsetid_timecode_reader_ks"></span><span id="DDK_PROPSETID_TIMECODE_READER_KS"></span>


The PROPSETID\_TIMECODE\_READER property set retrieves timecode information from an external device.

The KSPROPERTY\_TIMECODE enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by minidrivers that support external video capture devices.

[**KSPROPERTY\_TIMECODE\_READER**](ksproperty-timecode-reader.md)

[**KSPROPERTY\_ATN\_READER**](ksproperty-atn-reader.md)

[**KSPROPERTY\_RTC\_READER**](ksproperty-rtc-reader.md)

### <span id="directshow_interface"></span><span id="DIRECTSHOW_INTERFACE"></span>DirectShow Interface

The DirectShow **IAMTimecodeReader** interface (see the DirectShow documentation in the Microsoft Windows SDK) provides access to the properties of this set.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_TIMECODE_READER%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




