---
title: Creating Compressed Buffers and Decode Render Targets
description: Creating Compressed Buffers and Decode Render Targets
ms.assetid: 4d386b72-24d9-424b-8d48-7eaf75aab76c
keywords:
- video decoding WDK DirectX VA , render targets
- decoding video WDK DirectX VA , render targets
- video decoding WDK DirectX VA , compressed buffers
- decoding video WDK DirectX VA , compressed buffers
- compressed buffers WDK DirectX VA
- buffers WDK DirectX VA
- render targets WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating Compressed Buffers and Decode Render Targets


The Microsoft Direct3D runtime calls the user-mode display driver's [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function to create compressed buffers and render targets for decoding.

Each compressed buffer type has its own surface format as well as a special flag that indicates that the surface that the runtime creates contains compressed buffer information for accelerated video decode. The user-mode display driver determines to create a compressed buffer if the **DecodeCompressedBuffer** bit-field flag in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure that the *pResource* parameter of [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) points to is set. The user-mode display driver determines the type of compressed buffer to create by the format value in the **Format** member of D3DDDIARG\_CREATERESOURCE. The following formats are defined:

```
D3DDDIFMT_PICTUREPARAMSDATA       = 150
D3DDDIFMT_MACROBLOCKDATA          = 151
D3DDDIFMT_RESIDUALDIFFERENCEDATA  = 152
D3DDDIFMT_DEBLOCKINGDATA          = 153
D3DDDIFMT_INVERSEQUANTIZATIONDATA = 154
D3DDDIFMT_SLICECONTROLDATA        = 155
D3DDDIFMT_BITSTREAMDATA           = 156
```

The Direct3D runtime creates each decode render target independently in a call to the user-mode display driver's [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function. Each of the targets is referenced as a subresource index of a single resource. The user-mode display driver determines to create a decode render target if the **DecodeRenderTarget** bit-field flag in the **Flags** member of D3DDDIARG\_CREATERESOURCE is set.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Creating%20Compressed%20Buffers%20and%20Decode%20Render%20Targets%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




