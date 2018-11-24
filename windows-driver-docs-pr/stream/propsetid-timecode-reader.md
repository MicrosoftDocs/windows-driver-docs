---
title: PROPSETID\_TIMECODE\_READER
description: PROPSETID\_TIMECODE\_READER
ms.assetid: 7f115ba5-a6b7-4bae-a562-7e84a98ef420
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





