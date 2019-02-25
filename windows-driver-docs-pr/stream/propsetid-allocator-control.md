---
title: PROPSETID\_ALLOCATOR\_CONTROL
description: PROPSETID\_ALLOCATOR\_CONTROL
ms.assetid: a3e0a5e9-4357-4bc9-ba2a-098f344ed01e
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PROPSETID\_ALLOCATOR\_CONTROL


## <span id="ddk_propsetid_allocator_control_ks"></span><span id="DDK_PROPSETID_ALLOCATOR_CONTROL_KS"></span>


The PROPSETID\_ALLOCATOR\_CONTROL property set controls the allocation of overlay surface, such as video ports and/or Microsoft DirectDraw surfaces. Devices that control the number of allocated DirectDraw surfaces, and/or that indicate to the Overlay Mixer that video scaling at the video decoder is not possible should implement the properties of this set. The Overlay Mixer uses the properties of this set to control Microsoft DirectDraw surface allocation and dimensions.

The KSPROPERTY\_ALLOCATOR\_CONTROL enumeration in *ksmedia.h* specifies the properties of this set.

Support for this property set is optional and should be implemented only by devices that use overlay surfaces.

[**KSPROPERTY\_ALLOCATOR\_CONTROL\_HONOR\_COUNT**](ksproperty-allocator-control-honor-count.md)

[**KSPROPERTY\_ALLOCATOR\_CONTROL\_SURFACE\_SIZE**](ksproperty-allocator-control-surface-size.md)

[**KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_CAPS**](ksproperty-allocator-control-capture-caps.md)

[**KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_INTERLEAVE**](ksproperty-allocator-control-capture-interleave.md)

### <span id="directshow_interface"></span><span id="DIRECTSHOW_INTERFACE"></span>DirectShow Interface

There is no DirectShow interface that provides access to this property set.

 

 





