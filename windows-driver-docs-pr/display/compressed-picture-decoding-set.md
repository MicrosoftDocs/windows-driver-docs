---
title: Compressed Picture Decoding Set
description: Compressed Picture Decoding Set
ms.assetid: 7d6e2050-663e-4370-a210-1d319cfbde6d
keywords:
- compressed picture decoding set WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Compressed Picture Decoding Set


## <span id="ddk_compressed_picture_decoding_set_gg"></span><span id="DDK_COMPRESSED_PICTURE_DECODING_SET_GG"></span>


This section defines the minimal interoperability configuration set for compressed picture decoding. This entire set of configurations must be supported by a decoder, and one or more configurations in this set must be supported by an accelerator. An [additional configuration set](additional-encouraged-configuration-set.md) is provided for which support is encouraged (these configurations are not required).

The first six configurations in this set are for all [restricted profiles](restricted-profiles.md). The seventh configuration in this set is defined only for MPEG2\_C and MPEG2\_D.

The minimal interoperability configuration set of configurations for compressed picture decoding is defined by the third through the last members of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Compressed%20Picture%20Decoding%20Set%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




