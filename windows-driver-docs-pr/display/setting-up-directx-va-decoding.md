---
title: Setting Up DirectX VA Decoding
description: Setting Up DirectX VA Decoding
ms.assetid: 8841c366-df00-4e88-9f50-85345ba77e03
keywords:
- video decoding WDK DirectX VA , setting up
- decoding video WDK DirectX VA , setting up
- picture decoding WDK DirectX VA , setting up
- video decoding WDK DirectX VA , formats
- decoding video WDK DirectX VA , formats
- picture decoding WDK DirectX VA , formats
- formats WDK DirectX VA
- picture decoding WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up DirectX VA Decoding


## <span id="ddk_setting_up_directx_va_decoding_gg"></span><span id="DDK_SETTING_UP_DIRECTX_VA_DECODING_GG"></span>


In order for a decoder to operate correctly with an accelerator, the decoder and the accelerator must be set up for two distinct aspects of operation:

-   The format of the video data to be decoded. The [**DXVA\_ConnectMode**](https://msdn.microsoft.com/library/windows/hardware/ff563138) structure is used to specify the format.

-   The configuration determining the format used for data exchange between the host and the accelerator, and establishing which process resides on the host and which on the accelerator. This configuration is established by the negotiation of a connection configuration for each DirectX VA function to be used (as determined by the [bDXVA\_Func](bdxva-func-variable.md) variable). The [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure specifies the configuration.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20Up%20DirectX%20VA%20Decoding%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




