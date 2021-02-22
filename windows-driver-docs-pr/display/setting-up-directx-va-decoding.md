---
title: Setting Up DirectX VA Decoding
description: Setting Up DirectX VA Decoding
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

-   The format of the video data to be decoded. The [**DXVA\_ConnectMode**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_connectmode) structure is used to specify the format.

-   The configuration determining the format used for data exchange between the host and the accelerator, and establishing which process resides on the host and which on the accelerator. This configuration is established by the negotiation of a connection configuration for each DirectX VA function to be used (as determined by the [bDXVA\_Func](bdxva-func-variable.md) variable). The [**DXVA\_ConfigPictureDecode**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_configpicturedecode) structure specifies the configuration.

 

