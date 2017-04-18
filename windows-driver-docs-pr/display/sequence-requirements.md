---
title: Sequence Requirements
description: Sequence Requirements
ms.assetid: ee716286-f455-463d-906d-6f1b9fb8f227
keywords: ["video decoding WDK DirectX VA , sequence requirements", "decoding video WDK DirectX VA , sequence requirements", "picture decoding WDK DirectX VA , sequence requirements", "sequence requirements WDK DirectX VA", "compressed buffers WDK DirectX VA", "buffers WDK DirectX VA", "succession requirements WDK DirectX VA"]
---

# Sequence Requirements


## <span id="ddk_sequence_requirements_gg"></span><span id="DDK_SEQUENCE_REQUIREMENTS_GG"></span>


Sequence requirements for the accelerator and for the decoder must be observed to avoid race conditions and improper operation of the decoder and accelerator during the decoding process.

### <span id="Accelerator"></span><span id="accelerator"></span><span id="ACCELERATOR"></span>Accelerator

When queried, the hardware accelerator reports whether the display of an uncompressed surface is pending or in progress, and if requested operations have been completed. However, it is the responsibility of the host software decoder (not the accelerator) to ensure that race conditions do not cause undesirable behavior during the decoding process.

### <span id="Decoder"></span><span id="decoder"></span><span id="DECODER"></span>Decoder

The decoder must observe two rules to properly decode and display uncompressed surfaces:

1.  Do not overwrite any picture that has been submitted for display unless it has already been shown on the display and also removed from the display.

2.  Do not overwrite any picture that is needed as a reference for the creation of other pictures that have not yet been created.

Following these rules ensures proper operation of sequential operations in the decoding process and avoids tearing artifacts on the display. The guiding rule is: *Do not write over what you need for referencing or display, and avoid race conditions.*

To avoid race conditions, the software decoder must query the status of the accelerator. The decoder must also use a sufficient number of uncompressed picture surfaces to ensure that space is available for all necessary operations. This results in a need for at least four uncompressed picture surfaces for decoding video streams consisting of I, B, and P pictures. Using more than four surfaces is generally encouraged and is necessary for some operations, such as front-end alpha blending. (Using extra surfaces can significantly reduce the need to wait for operational dependencies to be resolved.)

Examples that show the decoding of conventional I, B, and P-structured video frames (without using a deblocking filter) are provided in [Using Four Uncompressed Surfaces for Decoding](using-four-uncompressed-surfaces-for-decoding.md) and [Using Five or More Uncompressed Surfaces for Decoding](using-five-or-more-uncompressed-surfaces-for-decoding.md).

**Note**   For compressed buffers, as well as for uncompressed surfaces, it is generally better to cycle through the allocated and available buffers rather than to keep reusing the same buffer, or the same subset of allocated buffers. This can reduce the possibility of added delays caused by waiting on unnecessary dependencies. The allocation of multiple buffers by a driver should be taken as an indication that cycling through these buffers for double or triple buffering is the proper way to operate and to avoid artifacts, such as temporary picture freezes. This applies to alpha-blend data loading in particular.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Sequence%20Requirements%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




