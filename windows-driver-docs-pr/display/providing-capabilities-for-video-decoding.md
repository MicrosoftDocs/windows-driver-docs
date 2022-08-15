---
title: Providing Capabilities for Video Decoding
description: Providing Capabilities for Video Decoding
keywords:
- video decoding WDK DirectX VA , capabilities provided per request type
- decoding video WDK DirectX VA , capabilities provided per request type
- D3DDDICAPS_GETDECODEGUIDCOUNT
- D3DDDICAPS_GETDECODEGUIDS
- D3DDDICAPS_GETDECODERTFORMATCOUNT
- D3DDDICAPS_GETDECODERTFORMATS
- D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFOCOUNT
- D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFO
- D3DDDICAPS_GETDECODECONFIGURATIONCOUNT
- D3DDDICAPS_GETDECODECONFIGURATIONS
ms.date: 10/22/2021
---

# Providing capabilities for video decoding

## How to query video decoding capabilities

To query the video decoding capabilities of a user-mode display driver (UMD), the D3D runtime calls the UMD's [**GetCaps**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getcaps) function with one of the following [request types](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_d3dddicaps_type) specified in the **Type** member of the [**D3DDDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) structure passed to **GetCaps**:

* D3DDDICAPS_GETDECODEGUIDCOUNT
* D3DDDICAPS_GETDECODEGUIDS
* D3DDDICAPS_GETDECODERTFORMATCOUNT
* D3DDDICAPS_GETDECODERTFORMATS
* D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFOCOUNT
* D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFO
* D3DDDICAPS_GETDECODECONFIGURATIONCOUNT
* D3DDDICAPS_GETDECODECONFIGURATIONS

[**GetCaps**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getcaps) returns the following:

* The UMD's capabilities for the request type, in the buffer that the **pData** member of [**D3DDDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) points to. The UMD must allocate a buffer large enough to hold the capabilities.
* The size (in bytes) of the buffer containing the capabilities, in **DataSize**.

The following subtopics list the possible request types and their associated video decoding capabilities.

## D3DDDICAPS_GETDECODEGUIDCOUNT and D3DDDICAPS_GETDECODEGUIDS request types

The Direct3D runtime calls [**GetCaps**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_getcaps) to request the number of GUIDs, then calls **GetCaps** again with a request for the list of supported GUIDs. The UMD returns the number and then a list of GUIDs from the following list that it supports for video acceleration (VA) decoding. The [**D3DDDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps).**pInfo** member is NULL for both of these request types.

```cpp
DEFINE_GUID(DXVADDI_ModeMPEG2_MoComp, 0xe6a9f44b, 0x61b0, 0x4563,0x9e,0xa4,0x63,0xd2,0xa3,0xc6,0xfe,0x66);
DEFINE_GUID(DXVADDI_ModeMPEG2_IDCT,   0xbf22ad00, 0x03ea, 0x4690,0x80,0x77,0x47,0x33,0x46,0x20,0x9b,0x7e);
DEFINE_GUID(DXVADDI_ModeMPEG2_VLD,    0xee27417f, 0x5e28, 0x4e65,0xbe,0xea,0x1d,0x26,0xb5,0x08,0xad,0xc9);

DEFINE_GUID(DXVADDI_ModeH264_A,  0x1b81be64, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeH264_B,  0x1b81be65, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeH264_C,  0x1b81be66, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeH264_D,  0x1b81be67, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeH264_E,  0x1b81be68, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeH264_F,  0x1b81be69, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);

DEFINE_GUID(DXVADDI_ModeWMV8_A,  0x1b81be80, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeWMV8_B,  0x1b81be81, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);

DEFINE_GUID(DXVADDI_ModeWMV9_A,  0x1b81be90, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeWMV9_B,  0x1b81be91, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeWMV9_C,  0x1b81be94, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);

DEFINE_GUID(DXVADDI_ModeVC1_A,   0x1b81beA0, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeVC1_B,   0x1b81beA1, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeVC1_C,   0x1b81beA2, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);
DEFINE_GUID(DXVADDI_ModeVC1_D,   0x1b81beA3, 0xa0c7, 0x11d3,0xb9,0x84,0x00,0xc0,0x4f,0x2e,0x73,0xc5);

#define DXVADDI_ModeMPEG2_MOCOMP  DXVADDI_ModeMPEG2_MoComp

#define DXVADDI_ModeWMV8_PostProc  DXVADDI_ModeWMV8_A
#define DXVADDI_ModeWMV8_MoComp  DXVADDI_ModeWMV8_B

#define DXVADDI_ModeWMV9_PostProc  DXVADDI_ModeWMV9_A
#define DXVADDI_ModeWMV9_MoComp  DXVADDI_ModeWMV9_B
#define DXVADDI_ModeWMV9_IDCT  DXVADDI_ModeWMV9_C

#define DXVADDI_ModeVC1_PostProc  DXVADDI_ModeVC1_A
#define DXVADDI_ModeVC1_MoComp  DXVADDI_ModeVC1_B
#define DXVADDI_ModeVC1_IDCT  DXVADDI_ModeVC1_C
#define DXVADDI_ModeVC1_VLD  DXVADDI_ModeVC1_D

#define DXVADDI_ModeH264_MoComp_NoFGT  DXVADDI_ModeH264_A
#define DXVADDI_ModeH264_MoComp_FGT  DXVADDI_ModeH264_B
#define DXVADDI_ModeH264_IDCT_NoFGT  DXVADDI_ModeH264_C
#define DXVADDI_ModeH264_IDCT_FGT  DXVADDI_ModeH264_D
#define DXVADDI_ModeH264_VLD_NoFGT  DXVADDI_ModeH264_E
#define DXVADDI_ModeH264_VLD_FGT  DXVADDI_ModeH264_F
```

## D3DDDICAPS_GETDECODERTFORMATCOUNT and D3DDDICAPS_GETDECODERTFORMATS request types

The Direct3D runtime specifies the GUID for a particular DirectX VA decode type in a variable that the **pInfo** member of [**D3DDDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) points to. The UMD returns the number and then a list of render target formats that it supports for a particular DirectX VA decode type.

## D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFOCOUNT and D3DDDICAPS_GETDECODECOMPRESSEDBUFFERINFO request types

The Direct3D runtime specifies a [**DXVADDI_DECODEINPUT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_decodeinput) structure for a particular DirectX VA decode type in a variable that the **pInfo** member of [**D3DDDIARG_GETCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_getcaps) points to. The UMD returns the number of and information about the compressed buffer types that are required to accelerate the video decode. The UMD returns information about the compressed buffer types in an array of [**DXVADDI_DECODEBUFFERINFO**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_decodebufferinfo) structures that the **pData** member of D3DDDIARG_GETCAPS specifies.

## D3DDDICAPS_GETDECODECONFIGURATIONCOUNT and D3DDDICAPS_GETDECODECONFIGURATIONS request types

The Direct3D runtime specifies a [**DXVADDI_DECODEINPUT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_decodeinput) structure for a particular DirectX VA decode type in a variable that the **pInfo** member of D3DDDIARG_GETCAPS points to. The UMD returns the number and a list of accelerated decode configurations that it supports for a particular DirectX VA decode type. The UMD returns accelerated decode configurations in an array of [**DXVADDI_CONFIGPICTUREDECODE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_configpicturedecode) structures that the **pData** member of D3DDDIARG_GETCAPS specifies.
