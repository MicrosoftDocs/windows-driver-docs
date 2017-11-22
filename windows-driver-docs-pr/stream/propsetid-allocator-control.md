---
title: PROPSETID\_ALLOCATOR\_CONTROL
description: PROPSETID\_ALLOCATOR\_CONTROL
MS-HAID:
- 'vidcapprop\_70e6f90b-40d8-47be-814f-9cc5347feb31.xml'
- 'stream.propsetid\_allocator\_control'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a3e0a5e9-4357-4bc9-ba2a-098f344ed01e
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20PROPSETID_ALLOCATOR_CONTROL%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




