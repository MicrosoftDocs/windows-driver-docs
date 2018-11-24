---
title: KSPROPSETID\_VramCapture
description: KSPROPSETID\_VramCapture
ms.assetid: 369bb258-5335-42f7-bd2f-7bfc9848e7f0
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





