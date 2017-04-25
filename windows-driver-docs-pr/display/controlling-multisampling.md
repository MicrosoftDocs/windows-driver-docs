---
title: Controlling Multisampling
description: Controlling Multisampling
ms.assetid: 73cdfda8-f67a-470b-a17e-0bf78a5d1df1
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , multisample rendering, controlling
- multisample rendering WDK DirectX 8.0 , controlling
- rendering multisamples WDK DirectX 8.0 , controlling
- D3DRS_MULTISAMPLEANTIALIAS
- D3DRS_MULTISAMPLEMASK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Controlling Multisampling


## <span id="ddk_controlling_multisampling_gg"></span><span id="DDK_CONTROLLING_MULTISAMPLING_GG"></span>


Two render states of the D3DRENDERSTATETYPE enumeration control multisample rendering. For more information about D3DRENDERSTATETYPE, see the DirectX 8.0 SDK documentation.

### <span id="d3drs_multisampleantialias"></span><span id="D3DRS_MULTISAMPLEANTIALIAS"></span>D3DRS\_MULTISAMPLEANTIALIAS

A BOOL value that determines how individual samples are computed when using a multisample render target buffer. When set to **TRUE**, the multiple samples are computed so that full-scene anti-aliasing is performed by sampling at different sample positions for each multiple sample. When set to **FALSE**, the multiple samples are all written with the same sample value (sampled at the pixel center), which allows nonantialiased rendering to a multisample buffer. This render state has no effect when rendering to a single sample buffer. The default value is **TRUE**.

### <span id="d3drs_multisamplemask"></span><span id="D3DRS_MULTISAMPLEMASK"></span>D3DRS\_MULTISAMPLEMASK

Each bit in this mask, starting at the LSB, controls modification of one of the samples in a multisample render target. Thus, for an 8-sample render target, the low byte contains the 8 write enables for each of the 8 samples. This render state has no effect when rendering to a single sample buffer. The default value is 0xFFFFFFFF.

This render state enables use of a multisample buffer as an accumulation buffer, doing multipass rendering of geometry where each pass updates a subset of samples.

Each sample in a multisample render target contributes uniform intensity to the final presented image. Consider, for example, that the multisample mode is 3 and the number of samples that are enabled using multisample masking is 2. Therefore, the resulting intensity of the rendered image is 2/3. That is, the intensity of each red, green, and blue component of every pixel is factored by 2/3.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Controlling%20Multisampling%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




