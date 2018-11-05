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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting Up DirectX VA Decoding


## <span id="ddk_setting_up_directx_va_decoding_gg"></span><span id="DDK_SETTING_UP_DIRECTX_VA_DECODING_GG"></span>


In order for a decoder to operate correctly with an accelerator, the decoder and the accelerator must be set up for two distinct aspects of operation:

-   The format of the video data to be decoded. The [**DXVA\_ConnectMode**](https://msdn.microsoft.com/library/windows/hardware/ff563138) structure is used to specify the format.

-   The configuration determining the format used for data exchange between the host and the accelerator, and establishing which process resides on the host and which on the accelerator. This configuration is established by the negotiation of a connection configuration for each DirectX VA function to be used (as determined by the [bDXVA\_Func](bdxva-func-variable.md) variable). The [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure specifies the configuration.

 

 





