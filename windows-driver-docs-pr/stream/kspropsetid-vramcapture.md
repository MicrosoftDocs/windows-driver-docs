---
title: KSPROPSETID\_VramCapture
description: KSPROPSETID\_VramCapture
ms.assetid: 369bb258-5335-42f7-bd2f-7bfc9848e7f0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPSETID\_VramCapture


Video streaming pins support the **KSPROPSETID\_VramCapture** property set. All properties in this set are mandatory for VRAM surface capture and transport.

If these properties are not supported, the capture defaults to surface based capture and transport to system memory.

Property items in this set are specified by KSPROPERTY\_VIDMEM\_TRANSPORT enumeration values, as defined in the header file, *Ksmedia.h*.

The **KSPROPSETID\_VramCapture** property set includes the following properties:

[**KSPROPERTY\_DISPLAY\_ADAPTER\_GUID**](ksproperty-display-adapter-guid.md)

[**KSPROPERTY\_PREFERRED\_CAPTURE\_SURFACE**](ksproperty-preferred-capture-surface.md)

[**KSPROPERTY\_CURRENT\_CAPTURE\_SURFACE**](ksproperty-current-capture-surface.md)

[**KSPROPERTY\_MAP\_CAPTURE\_HANDLE\_TO\_VRAM\_ADDRESS**](ksproperty-map-capture-handle-to-vram-address.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_VramCapture%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




