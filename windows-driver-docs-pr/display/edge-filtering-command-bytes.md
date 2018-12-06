---
title: Edge Filtering Command Bytes
description: Edge Filtering Command Bytes
ms.assetid: eefb580a-133d-4c9e-a8d2-2d114107e2ea
keywords:
- macroblocks WDK DirectX VA , deblocking filter control
- deblocking filter control WDK DirectX VA
- edge filtering WDK DirectX VA
- read-back buffers WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Edge Filtering Command Bytes


## <span id="ddk_edge_filtering_command_bytes_gg"></span><span id="DDK_EDGE_FILTERING_COMMAND_BYTES_GG"></span>


Each edge filtering control command consists of a single byte. The *DXVA\_DeblockingEdgeControl* constant defined in *dxva.h* defines how deblocking edges are processed. The 7 most significant bits of the byte contain the *EdgeFilterStrength* variable, and the least significant bit is the *EdgeFilterOn* flag.

Edge filtering is performed as specified in H.263 Annex J. The *EdgeFilterStrength* variable specifies the strength of the filtering to be performed. The *EdgeFilterOn* flag specifies whether filtering is to be done. *EdgeFilterOn* is 1 if the edge is to be filtered, and zero if not.

Edge filtering (for the edges with *EdgeFilterOn* equal to 1) is performed with the strength value specified by *EdgeFilterStrength* and with clipping the output to the range of 0 to 2<sup>(BPP)</sup> - 1. Top-edge filtering for all blocks is performed before left-edge filtering for any blocks because the values of the samples used for top-edge filtering must be those reconstructed values prior to any deblocking filtering for left-edge filtering.

If the **bPicDeblockConfined** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure indicates that sample values of macroblocks outside of the current deblocking filter command buffer are not affected, the *EdgeFilterOn* flag is zero for all edges at the left and top of the region covered by the macroblocks with deblocking filter commands in the buffer.

### <span id="Read-Back_Buffers"></span><span id="read-back_buffers"></span><span id="READ-BACK_BUFFERS"></span>Read-Back Buffers

One read-back command buffer is passed to the accelerator when the **bPicReadbackRequests** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure is 1. The data in this buffer commands the accelerator to return the resulting final picture macroblock data (after deblocking, if applicable) to the host. If an encryption protocol is in use, the accelerator may respond to read-back requests by returning an error indication, erroneous data, or encrypted data (as may be specified by the encryption protocol).

The read-back command buffer passed to the accelerator must contain read-back commands consisting of a single **wMBaddress** member of the macroblock control command for the macroblock to be read. The **wMBaddress** member is a 16-bit value that specifies the macroblock address of the current macroblock in raster-scan order. Raster-scan order (based on the **wPicWidthInMBminus1** and **wPicHeightInMBminus1** members of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure) is defined as follows:

-   Zero is the address of the top-left macroblock.

-   **wPicWidthInMBminus1** is the address of the top-right macroblock.

-   **wPicHeightInMBminus1** x (**wPicWidthInMBminus1**+1) is the address of the lower-left macroblock.

-   (**wPicHeightInMBminus1**+1) x (**wPicWidthInMBminus1**+1)-1 is the address of the lower-right macroblock.

If *BPP* as specified in the **bBPPminus1** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure is 8, the macroblock data is returned in the form of 8-bit unsigned values (thus, black is nominally Y=16, Cb=Cr=128, and white is nominally Y=235, Cb=Cr=128). If *BPP* is greater than 8, the data is returned in the form of 16-bit unsigned values.

The macroblock data is returned from the accelerator to the host in the form of a copy of the read-back command buffer itself, followed by padding to the next 32-byte alignment boundary. Then, the macroblock data values for luminance and chrominance data are returned in the order sent in the read-back command buffer, in the form of 64 samples per block for each block in each macroblock.

Residual difference blocks within a macroblock are returned in the order specified in MPEG-2 Figures 6-10, 6-11, and 6-12 (raster-scan order for Y blocks of the macroblock, followed by the 4:2:0 block of Cb, followed by the 4:2:0 block of Cr. If in a 4:2:2 or a 4:4:4 sampling operation, the 4:2:0 blocks are followed by the 4:2:2 block of Cb, followed by the 4:2:2 block of Cr. If in 4:4:4 sampling operation, the 4:2:2 blocks are followed by the 4:4:4 blocks of Cb, followed by the 4:4:4 blocks of Cr).

 

 





