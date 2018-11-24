---
title: Using Compressed Texture Surfaces
description: Using Compressed Texture Surfaces
ms.assetid: efa7efff-a1ad-49f3-b6e8-f08b520e77ae
keywords:
- drawing compressed textures WDK DirectDraw , about compressed texture surfaces
- DirectDraw compressed textures WDK Windows 2000 display , about compressed texture surfaces
- compressed texture surfaces WDK DirectDraw , about compressed texture surfaces
- surfaces WDK DirectDraw , compressed textures
- textures WDK DirectDraw , compressed
- reference rasterizers WDK DirectDraw
- rasterizers WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Compressed Texture Surfaces


## <span id="ddk_using_compressed_texture_surfaces_gg"></span><span id="DDK_USING_COMPRESSED_TEXTURE_SURFACES_GG"></span>


DirectDraw only calls the driver to do a blt between two surfaces of the same DXT type if the DDCAPS2\_COPYFOURCC flag is set in the **dwCaps2** member of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure. If this flag is not set, the DirectDraw HEL performs the blt. This is important for backing surface-to-display copy blts, because this is the mechanism whereby textures are downloaded from backing (system memory) surfaces to display memory. Thus, exposing DXT texture surfaces effectively requires your driver to support the DDCAPS2\_COPYFOURCC flag.

The DDCAPS2\_COPYFOURCC flag has some additional implications. Your driver must be able to execute a blt between FOURCC formats having at least these attributes:

-   The source and destination formats are the same FOURCC format.

-   The source and destination surfaces are different.

-   The source and destination rectangles both make up the entire surface (that is, there is no stretching and there are no subrectangles).

-   Both surfaces are in display memory.

-   The driver must be able to perform these blts for every FOURCC format it supports in display memory.

**Note**   Microsoft DirectShow uses the DDCAPS2\_COPYFOURCC flag to accelerate some video functionality; the requirement for this flag implies that all FOURCC formats can be copied.

 

If a blt operation requires compression to a DXT format, the DirectDraw HEL always performs the blt. This means that DirectDraw never requests the driver to perform a blt for which:

-   The destination surface has a DXT format.

-   The formats for the source and destination surfaces are not the same.

The semantics of the DirectDraw DDCAPS\_CANBLTSYSMEM capability bit imply that the display driver is called for all blts from system memory to display memory. Consequently, the driver may be called for such blts from DXT surfaces to non-DXT surfaces. The only requirement in this case is that the driver return DDHAL\_DRIVER\_NOTHANDLED if it cannot perform the decompression. This causes DirectDraw to propagate a DDERR\_UNSUPPORTED error code to the application. It is acceptable to implement decompression for blts from system memory to display memory in your driver, but this is not required for DirectX 6.0 and later versions.

DirectDraw display memory allocation routines do not handle pixel format considerations. [**HeapVidMemAllocAligned**](https://msdn.microsoft.com/library/windows/hardware/ff567267), for example, expects a count of bytes as its input parameter. Likewise, DDHAL\_PLEASEALLOC\_BLOCKSIZE (see the **fpVidMem** member of the [**DD\_SURFACE\_GLOBAL**](https://msdn.microsoft.com/library/windows/hardware/ff551726) structure) signifies that the **dwBlockSizeX** and **dwBlockSizeY** members of the DD\_SURFACE\_GLOBAL structure are counts of bytes and lines, respectively. Consequently, if your driver uses either of these mechanisms to allocate display memory through DirectDraw allocators, your driver must be able to calculate the memory consumption, in bytes, of a DXT surface by itself. The following sample shows one way to perform this calculation:

```cpp
DWORD dx, dy;
DWORD blksize, surfsize;
LPVOID pmem;

/*
 * Determine how much memory to allocate for the FOURCC format.
 */
switch ((int)pDDPF->dwFourCC)
{
  case MAKEFOURCC(&#39;D&#39;,&#39;X&#39;,&#39;T&#39;,&#39;1&#39;):
    blksize = 8; // The size of a DXT1 4x4 pixel block. 
    break;
  case MAKEFOURCC(&#39;D&#39;,&#39;X&#39;,&#39;T&#39;,&#39;2&#39;):    // premultiplied alpha
  case MAKEFOURCC(&#39;D&#39;,&#39;X&#39;,&#39;T&#39;,&#39;3&#39;):    // non-premultiplied alpha
    blksize = 16; //The size of a DXT2,3 4x4 pixel block 
    break;
  case MAKEFOURCC(&#39;D&#39;,&#39;X&#39;,&#39;T&#39;,&#39;4&#39;):    // premultiplied alpha
  case MAKEFOURCC(&#39;D&#39;,&#39;X&#39;,&#39;T&#39;,&#39;5&#39;):    // non-premultiplied alpha
    blksize = 16; //The size of a DXT4,5 4x4 pixel block.
  break;

  default:
    DDASSERT(0);
}

/*
 * Calculate the number of blocks in the x and y dimensions.
 */
dx = (nWidth  + 3) >> 2;
dy = (nHeight + 3) >> 2;
surfsize = dx * dy * blksize;
```

When the application calls the **IDirect3DVertexBuffer7::Lock** or **IDirectDrawSurface7::GetSurfaceDesc** methods (described in the Direct3D and DirectDraw SDK documentation sets, respectively) on a compressed surface, the driver must set the DDSD\_LINEARSIZE flag in the **dwFlags** member of the [**DDSURFACEDESC2**](https://msdn.microsoft.com/library/windows/hardware/ff550340) structure. In addition, the driver must set the number of bytes allocated to contain the compressed surface data in the **dwLinearSize** member of the same structure. (The **dwLinearSize** member resides in a union with the **lPitch** member, so these members are mutually exclusive, as are the DDSD\_LINEARSIZE and DDSD\_PITCH flags.)

Your hardware or driver can convert and store the compressed texture in any format you choose (typically a reordering into a more hardware-efficient layout). However, your hardware or driver must be able to convert the compressed texture back to its original DXT code format whenever DirectDraw requires it, that is, whenever the application calls the **IDirect3DVertexBuffer7::Lock** method.

### <span id="windows_2000_note"></span><span id="WINDOWS_2000_NOTE"></span>Windows 2000 Note

Under Windows 2000, system memory DXT surfaces have had some of their fields mapped for memory allocation purposes. The mapping is:

```cpp
wWidth = lPitch = dx * blksize;
wHeight         = dy;
dwRGBBitCount   = 8;
```

When the driver encounters a system memory DXT surface, for example in [**D3dCreateSurfaceEx**](https://msdn.microsoft.com/library/windows/hardware/ff542840), it must map the fields back before making use of them. The back mapping is:

```cpp
realWidth        = (wWidth  << 2) / blksize;
realHeight       =  wHeight << 2;
realLinearSize   = dwLinearSize * wHeight;
realRGBBitCount  = 0
```

### <span id="reference_rasterizer_notes"></span><span id="REFERENCE_RASTERIZER_NOTES"></span>Reference Rasterizer Notes

The following three items should be observed when implementing reference rasterizer (RefRast) code:

1.  The section entitled *3-Bit Linear Alpha Interpolation (DXT4 and DXT5 format)* in the DirectDraw SDK documentation shows the correct order in which to ramp the Alpha values for DXT4 and DXT5 formats.

2.  Reference rasterizer code should have the following logic guarding the color comparison logic.
    ```cpp
    if ((color_0 > color_1) OR !DXT1) {
    /*  color comparison logic */
    }
    ```

3.  Because hardware implementations of reference rasterizers can perform the rounding of calculations to better approximate the original value in slightly different ways, testing should allow for slight variations in the color and alpha values obtained from the decompression logic.

 

 





