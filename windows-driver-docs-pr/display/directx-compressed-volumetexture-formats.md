---
title: DirectX Compressed VolumeTexture Formats
description: DirectX Compressed VolumeTexture Formats
ms.assetid: 5a655a30-e489-4691-873a-58bece059877
keywords:
- drawing compressed textures WDK DirectDraw , compressed volume texture formats
- DirectDraw compressed textures WDK Windows 2000 display , compressed volume texture formats
- compressed texture surfaces WDK DirectDraw , compressed volume texture formats
- surfaces WDK DirectDraw , compressed textures
- textures WDK DirectDraw , compressed
- DXVN WDK DirectDraw
- DXTN WDK DirectDraw
- slicing WDK DirectDraw
- volume textures WDK DirectDraw
- volumetric rendering WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectX Compressed VolumeTexture Formats


## <span id="ddk_directx_compressed_volumetexture_formats_gg"></span><span id="DDK_DIRECTX_COMPRESSED_VOLUMETEXTURE_FORMATS_GG"></span>


Volume textures maps are digitized images that are generated periodically through a true 3D region of space. For example, a ball of fire may be sampled and the "amount" of flame within a slice can be accounted for. In this sense, the amount of flame represents a set of values for the alpha, red, green and blue components at each pixel in the image. The entire flame is represented by a series of these slices.

Before going into details of DirectX volume rendering, it is important to clarify some terminology. There are two common methods used in computer graphics to represent volume data sets. One is to sample the image at each location and store the appropriate ARGB values. For example, data for the flame could be stored as a 256 X 256 X 256 three-dimensional array. This requires about 64MB to store a 32-bit value at each location in the array. (Some applications, such as medical imaging, may require this amount of data.) However, "slicing" the flame into 4 or 8 slabs can make a very good approximation. Each slab stores 256 X 256 elements, where each element represents a region of data within the slab.

If we assume an array of size 256 X 256 X 4 is reasonable, then storing a 32-bit value at each location requires only 1MB of storage (less if the data is compressed). The reason to talk about these two different methods is that if you want anything in your image that is behind the flame to be hidden, then the data value stored at each location is different. In the full 256 X 256 X 256 data set, any one element may contribute about 1/256 of the final alpha and color. In the slicing method, an element could contribute anywhere from 0 up to the final alpha and color used for that pixel. The problem is that sometimes the term "voxel" is used to describe both types of sampling. Starting with DirectX 8, the slicing method (often called "Volume Texturing") is the only method supported. The idea is to reduce the volume data set to a reasonable size. With some minor modifications to the texturing hardware, the DirectX graphics API can expose high-performance volumetric rendering.

Up to this point, most of this section has focused on DXT*N* compressed surface formats. These formats work well for 2D textures. They are inefficient, however, when you are working with a volume data set because volume data sets are stored in separate surfaces that require extra hardware cycles to access. To address this issue, DirectX 8 supports a set of volume surface formats.

The idea is to take the volume slices and compress them using DXT*N*. Then, instead of storing the completed surfaces sequentially in memory, the DXT*N* data blocks are reordered. The reordering is done so that the small 4X4 texel blocks form data cubes. They can be 4X4X1, 4X4X2, 4X4X3, or 4X4X4. Note that the 4X4X1 ordering is exactly the same as that used in DXT1 through DXT5. The important point is:

Volume surfaces are slices of data that are compressed using DXT*N* and then reordered to account for the 3D locality of data. These reordered data structures are referred to by the FOURCCs of DXV1,..., DXV5 (or just DXV*N* to describe the general case). Note that a DXV1 data structure would hold a set of reordered DXT1 surfaces, DXV2 would hold a set of DXT2 surfaces, and so on.

### <span id="dxvn_details"></span><span id="DXVN_DETAILS"></span>DXV*N* Details

A DXV*N* surface stored in the 1-deep arrangement contains one set of 4x4 DXT*N* subblocks (in effect it is just a DXT*N* surface). The DXV*N* 4x4x2 block format structure contains two 4x4 DXT*N* subblocks, one taken from each of two adjacent data slices. Using this method, a DXV*N* 4x4x4 block format structure contains four 4x4 DXT*N* subblocks taken from 4 data slices. In all cases the *N* in DXV*N* is used to match it to the corresponding DXT*N* type used for compression. DXT*N* blocks can be stored as 64 bits (color and 1-bit alpha, or 128 bits with additional alpha information). So the DXV*N* subblocks have the same possible sizes based on the type *N*. That is, DXT1 and DXV1 use 64 bit subblocks, while DXT2,..,DXT5 and DXV2,..,DXV5 use 128 bit subblocks.

Given a texel coordinate *(u, v, p)* where *u* {0,1,...,*width*-1}, *v* {0, 1, ..., *height*-1}, and *p* {0, 1, ..., *depth*-1}, the following can be used to compute the corresponding address of the compressed block and subblock in memory containing that texel. As mentioned above, the subblock format matches the existing DXT*N* format:

```cpp
subblock_size = 8 (for DXT1)
subblock_size = 16 (for DXT2,...,DXT5)
block_size = MIN(p, 4) * subblock_size
horiz_stride = (width + 3) >> 2
planar_stride = ( (height + 3) >> 2) * horiz_stride
block_byte_address = block_size *
    ( (p >> 2) * planar_stride + (v >> 2) * horiz_stride + (u >> 2) )
subblock_byte_address = block_byte_address + ((p & 3) * subblock_size)
```

 

 





