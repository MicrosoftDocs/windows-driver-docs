---
title: 4 2 0 Video Pixel Formats
description: 4 2 0 Video Pixel Formats
keywords:
- uncompressed video pixel formats WDK DirectX VA
- pixel formats for uncompressed video WDK DirectX VA
- compressed picture decoding WDK DirectX VA , pixel formats for uncompressed video
- picture decoding WDK DirectX VA , compressed
- 4 2 0 video WDK DirectX VA
ms.date: 04/20/2017
---

# 4:2:0 Video Pixel Formats

## <span id="ddk_4_2_0_video_pixel_formats_gg"></span><span id="DDK_4_2_0_VIDEO_PIXEL_FORMATS_GG"></span>

To decode compressed 4:2:0 video, use one of the following uncompressed pixel formats.

| Pixel Format | Description |
| ------------ | ----------- |
| YUY2 | As described in [4:2:2 Video Pixel Formats](4-2-2-video-pixel-formats.md), except that two lines of output Cb and Cr samples are produced for each actual line of 4:2:0 Cb and Cr samples. The second line of each pair of output lines is generally either a duplicate of the first line or is produced by averaging the samples in the first line of the pair with the samples of the first line of the next pair. |
| UYVY | As described in [4:2:2 Video Pixel Formats](4-2-2-video-pixel-formats.md), except that two lines of output Cb and Cr samples are produced for each actual line of 4:2:0 Cb and Cr samples. The second line of each pair of output lines is generally either a duplicate of the first line or is produced by averaging the samples in the first line of the pair with the samples of the first line of the next pair. |
| YV12 | All Y samples are found first in memory as an array of unsigned char (possibly with a larger stride for memory alignment), followed immediately by all Cr samples (with half the stride of the Y lines, and half the number of lines), then followed immediately by all Cb samples in a similar fashion. |
| IYUV | The same as YV12, except for swapping the order of the Cb and Cr planes. |
| NV12 | A format in which all Y samples are found first in memory as an array of unsigned char with an even number of lines (possibly with a larger stride for memory alignment). This is followed immediately by an array of unsigned char containing interleaved Cb and Cr samples. If these samples are addressed as a little-endian WORD type, Cb would be in the least significant bits and Cr would be in the most significant bits with the same total stride as the Y samples. NV12 is the preferred 4:2:0 pixel format. |
| NV21 | The same as NV12, except that Cb and Cr samples are swapped so that the chroma array of unsigned char would have Cr followed by Cb for each sample (such that if addressed as a little-endian WORD type, Cr would be in the least significant bits and Cb would be in the most significant bits). |
| IMC1 | The same as YV12, except that the stride of the Cb and Cr planes is the same as the stride in the Y plane. Also, the Cb and Cr planes must fall on memory boundaries that are a multiple of 16 lines. The following code examples show calculations for the Cb and Cr planes.<br/>`BYTE* pCr = pY + (((Height + 15) & ~15) * Stride);`<br/>`BYTE* pCb = pY + (((((Height * 3) / 2) + 15) & ~15) * Stride);`<br/>In the preceding examples, pY is a byte pointer that points to the beginning of the memory array, and Height must be a multiple of 16. |
| IMC2 | The same as IMC1, except that Cb and Cr lines are interleaved at half-stride boundaries. In other words, each full-stride line in the chrominance area starts with a line of Cr, followed by a line of Cb that starts at the next half-stride boundary. (This is a more address-space-efficient format than IMC1, because it cuts the chrominance address space in half, and thus cuts the total address space by 25 percent.) This is an optionally preferred format in relation to NV12, but NV12 appears to be more popular. |
| IMC3 | The same as IMC1, except for swapping Cb and Cr. |
| IMC4 | The same as IMC2, except for swapping Cb and Cr. |

For more information about these formats, see [Recommended 8-Bit YUV Formats for Video Rendering](/windows/desktop/medfound/recommended-8-bit-yuv-formats-for-video-rendering) in the Microsoft Media Foundation documentation.
