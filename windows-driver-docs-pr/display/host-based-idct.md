---
title: Host-Based IDCT
description: Host-Based IDCT
ms.assetid: 9f44e734-8cbc-4317-bd72-66d4ac7cd4de
keywords:
- macroblocks WDK DirectX VA , IDCT
- low-level IDCT WDK DirectX VA
- host-based IDCT WDK DirectX VA
- inverse discrete-cosine transform WDK DirectX VA
- IDCT WDK DirectX VA
- 16-bit host-based IDCT WDK DirectX VA
- 8-8 overflow host-based IDCT WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Host-Based IDCT


## <span id="_host_based_idct"></span><span id="_HOST_BASED_IDCT"></span>


IDCT may be performed on the host, with the result passed through the DirectX VA API in the spatial domain. There are two supported methods for sending the results from the host to the accelerator: 16-bit and 8-8 overflow. The **bConfigSpatialResid8** member of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133)structure indicates which method is used.

### <span id="16-bit_Host-Based_IDCT_Processing"></span><span id="16-bit_host-based_idct_processing"></span><span id="16-BIT_HOST-BASED_IDCT_PROCESSING"></span>16-bit Host-Based IDCT Processing

The macroblock control structures used with 16-bit host-based residual difference decoding are [**DXVA\_MBctrl\_I\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563983) and [**DXVA\_MBctrl\_P\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563993).

When sending spatial-domain residual difference data using the 16-bit method, blocks of 16-bit data are sent sequentially. Each block of spatial-domain data consists of 64 16-bit integers.

If *BPP*, as derived from the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure, is greater than 8, only the 16-bit method can be used. If the **bPicIntra** member of the DXVA\_PictureParameters structure is 1 and *BPP* is 8, the 8-8 overflow method is used. If *IntraMacroblock* is zero, the 16-bit residual difference samples are sent as signed quantities to be added to the motion-compensated prediction values. If *IntraMacroblock* is 1, the 16-bit samples are sent as follows:

-   If the **bConfigIntraResidUnsigned** member of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure is 1, the samples are sent as unsigned quantities relative to the constant reference value of zero. For example, mid-level gray would be represented as Y=2<sup>(BPP-1)</sup>, Cb=2<sup>(BPP-1)</sup>, Cr=2<sup>(BPP-1)</sup>.

-   If the **bConfigIntraResidUnsigned** member of the DXVA\_ConfigPictureDecode structure is zero, the samples are sent as signed quantities relative to the constant reference value of 2<sup>(BPP-1)</sup>. For example, mid-level gray would be represented as Y=0, Cb=0, Cr=0.

Blocks of data are sent sequentially, in the order specified by scanning the **wPatternCode** member of the macroblock control structure for bits with values of 1 from the most significant bit to least significant bit.

No clipping of the residual difference values can be assumed to have been performed on the host, unless the **bConfigSpatialHost8or9Clipping** member of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure is 1. Although only a *BPP*+1 bit range is needed to adequately represent the spatial-domain difference data, the output of some [IDCT](low-level-idct-processing-elements.md) implementations will produce numbers beyond this range unless they are clipped.

**Note**   The accelerator must work with at least a 15-bit range of values. Although video-coding standards typically specify clipping of a difference value prior to adding it to a prediction value (that is, 9-bit clipping in 8-bit-per-sample video), this clipping stage is actually unnecessary because it has no effect on the resulting decoded output picture. It is not assumed that this clipping occurs unless necessary for the accelerator hardware as indicated by the **bConfigSpatialHost8or9Clipping** member of the DXVA\_ConfigPictureDecode structure being set to 1.

 

### <span id="8-8_Overflow_Host-Based_IDCT_Processing_"></span><span id="8-8_overflow_host-based_idct_processing_"></span><span id="8-8_OVERFLOW_HOST-BASED_IDCT_PROCESSING_"></span>8-8 Overflow Host-Based IDCT Processing

The macroblock control structures used with 8-8 overflow host-based residual difference decoding are [**DXVA\_MBctrl\_I\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563983) and [**DXVA\_MBctrl\_P\_HostResidDiff\_1**](https://msdn.microsoft.com/library/windows/hardware/ff563993).

If the *BPP* variable derived from the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure is 8, the 8-8 overflow spatial-domain residual difference method may be used. Its use is required if the **bPicIntra** member of this structure is 1 and *BPP* is 8. In this case, each spatial-domain difference value is represented using only 8 bits. When sending data using the 8-8 overflow method, blocks of 8-bit data are sent sequentially. Each block of 8-bit spatial-domain residual difference data consists of 64 bytes containing the values of the data in conventional raster scan order (the elements of the first row in order, followed by the elements of the second row, and so on).

If *IntraMacroblock* in the macroblock control command is zero, the 8-bit spatial-domain residual difference samples are signed differences to be added or subtracted (as determined from the **bConfigResid8Subtraction** member of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure and whether the sample is in a first pass block or an overflow block) relative to the motion compensation prediction value.

If *IntraMacroblock* (bit 0 in the **wMBtype** member of the macroblock structure) is zero, and the difference to be represented for some pixel in a block is too large to represent using only 8 bits, a second overflow block of 8-bit spatial-domain residual difference samples is sent.

If *IntraMacroblock* (bit 0 in the **wMBtype** member of the macroblock structure) is 1, the 8-bit spatial-domain residual difference samples are set as follows:

-   If the **bConfigIntraResidUnsigned** member of the DXVA\_ConfigPictureDecode structure is 1, the 8-bit samples are sent as unsigned quantities relative to the constant reference value of zero. For example, mid-level gray would be represented as Y=2<sup>(BPP-1)</sup>, Cb=2<sup>(BPP-1)</sup>, Cr=2<sup>(BPP-1)</sup>.

-   If the **bConfigIntraResidUnsigned** member of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure is zero, the 8-bit samples are sent as signed quantities relative to the constant reference value of 2<sup>(BPP-1)</sup>. For example, mid-level gray would be represented as Y=0, Cb=0, Cr=0.

If IntraMacroblock is 1, 8-bit overflow blocks are not sent.

Blocks of data are sent sequentially, in the order specified by scanning the **wPatternCode** member of the macroblock control command for bits with values of 1, from most significant to least significant. All necessary 8-bit overflow blocks are then sent as specified by the **wPC\_Overflow** member of the macroblock control command. Such overflow blocks are subtracted rather than added if the **bConfigResid8Subtraction** member of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure is 1. The first pass of 8-bit differences for each nonintra macroblock is added. If the **bPicOverflowBlocks** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure is zero or the *IntraMacroblock* member of the macroblock control command is 1, there is no second pass. If **bPicOverflowBlocks** is 1, *IntraMacroblock* is zero, and **bConfigResid8Subtraction** is 1, the second pass of 8-bit differences for each nonintra macroblock is subtracted. If **bPicOverflowBlocks** is 1, *IntraMacroblock* is zero, and **bConfigResid8Subtraction** is zero, the second pass of 8-bit differences for each nonintra macroblock is added.

If any sample is nonzero in both an original 8-bit block and in a corresponding 8-bit overflow block, the following rules apply:

-   If **bConfigResid8Subtraction** is zero, the sign of the sample must be the same in both blocks.

-   If **bConfigResid8Subtraction** is 1, the sign of the sample in the original 8-bit block must be the same as the sign of negative 1 times the value of the sample in the corresponding overflow block.

These rules allow the sample to be added to the prediction picture with 8-bit clipping of the result after each of the two passes.

**Note**   Using 8-bit differences with overflow blocks with **bConfigResid8Subtraction** equal to zero (which results in adding two 8-bit differences for each overflow block) cannot represent a residual difference value of +255 if *IntraMacroblock* is zero. (The largest difference value that can be represented this way is 127+127=254.) This makes the 8-8 overflow host-based IDCT method not strictly compliant with video-coding standards when **bConfigResid8Subtraction** is zero. However, this format is supported because it is used in some existing implementations, is more efficient than 16-bit sample use in terms of the amount of data needed to represent a picture, and does not generally result in any meaningful degradation of video quality.

 

 

 





