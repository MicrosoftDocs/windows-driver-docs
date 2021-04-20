---
title: Decoding Video
description: Decoding Video
keywords:
- video decoding WDK DirectX VA , about decoding video
- decoding video WDK DirectX VA , about decoding video
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Decoding Video


The Microsoft Direct3D runtime calls the user-mode display driver's [**DecodeBeginFrame**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodebeginframe) and [**DecodeEndFrame**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodeendframe) functions to indicate a time period between these function calls that the user-mode display driver can decode video. Before the user-mode display driver can perform any video decode operations, the Microsoft Direct3D runtime must call the user-mode display driver's [**SetDecodeRenderTarget**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_setdecoderendertarget) function to set the render target surface for those decode operations. However, the call to **SetDecodeRenderTarget** can occur only outside the begin-frame and end-frame time period.

In protected mode and in the call to [**DecodeBeginFrame**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodebeginframe), the Direct3D runtime sets or changes a DirectX VA content key in a variable that the **pPVPSetKey** member of the [**D3DDDIARG\_DECODEBEGINFRAME**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_decodebeginframe) structure points to. The decode device uses this key for protected transfers of the compressed DirectX VA buffers for this and subsequent frames.

**Note**   The Direct3D runtime sets the **pPVPSetKey** pointer only to change or set the key. To keep the previously set key in use, the runtime sets the pointer to **NULL** to avoid potentially time consuming reloading of the same key. The driver does not eliminate the redundant settings. A decoder application must avoid redundant settings.

 

After the render target surface for decode operations is set, the user-mode display driver can receive calls to its [**DecodeExecute**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodeexecute) function to perform video decode operations between the begin-frame and end-frame time period.

In calls to [**DecodeExecute**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodeexecute), not all of the buffer types that are specified in the **CompressedBufferType** members of the [**DXVADDI\_DECODEBUFFERDESC**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_decodebufferdesc) structures of the **pCompressedBuffers** array of the [**D3DDDIARG\_DECODEEXECUTE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_decodeexecute) structure are used for each decode GUID that the **hDecode** member of D3DDDIARG\_DECODEEXECUTE specifies. For example, the slice-control (D3DDDIFMT\_SLICECONTROLDATA), inverse-quantization (D3DDDIFMT\_INVERSEQUANTIZATIONDATA), and bit-stream (D3DDDIFMT\_BITSTREAMDATA) buffers are required only for variable-length decode (VLD) processing, and the deblocking-control buffer (D3DDDIFMT\_DEBLOCKINGDATA) is not used by MPEG-2 at all.

In protected mode, the buffers that were encrypted for a protected transfer with a content key contain a pointer to initial counter values in their buffer descriptors (that is, in variables that the **pCipherCounter** members of the [**DXVADDI\_DECODEBUFFERDESC**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_decodebufferdesc) structures point to). Each call to the user-mode display driver's [**DecodeExecute**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodeexecute) function must perform a protected transfer of such buffers to local video memory before **DecodeExecute** uses the buffers' data in the decode operation. However, no plans exist to encrypt DirectX VA compressed buffers of types other than residual-difference (D3DDDIFMT\_RESIDUALDIFFERENCEDATA) and bit-stream (D3DDDIFMT\_BITSTREAMDATA) types.

 

