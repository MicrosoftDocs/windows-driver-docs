---
title: Using Crypto Session with DXVA 2.0 Decoder
description: Using Crypto Session with DirectX Video Accelerator 2.0 Decoder
keywords:
- DXVA 2.0 decoder WDK Windows 7 display
- DXVA 2.0 decoder WDK Windows Server 2008 R2 display
- DXVA 2.0 decoder WDK Windows 7 display , associating with a crypto session
- DXVA 2.0 decoder WDK Windows Server 2008 R2 display , associating with a crypto session
- DirectX Video Accelerator 2.0 decoder WDK Windows 7 display
- DirectX Video Accelerator 2.0 decoder WDK Windows Server 2008 R2 display
- DirectX Video Accelerator 2.0 decoder WDK Windows 7 display , associating with a crypto session
- DirectX Video Accelerator 2.0 decoder WDK Windows Server 2008 R2 display , associating with a crypto session
- crypto session WDK Windows 7 display
- crypto session WDK Windows Server 2008 R2 display
- crypto session WDK Windows 7 display , associating with a DXVA 2.0 decoder
- crypto session WDK Windows Server 2008 R2 display , associating with a DXVA 2.0 decoder
ms.date: 12/06/2018
---

# Using Crypto Session with DirectX Video Accelerator 2.0 Decoder


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The user-mode display driver can associate a crypto session with a DirectX Video Accelerator (VA) 2.0 decode device to make the DirectX VA 2.0 decode device use the session key of the crypto session. If the Direct3D runtime specifies a valid decode GUID in the **DecodeProfile** member of the [**D3DDDIARG\_CREATECRYPTOSESSION**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_createcryptosession) structure when the runtime calls the driver's [**CreateCryptoSession**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createcryptosession) function to create the crypto session, the runtime can subsequently call the driver's [**ConfigureAuthenticatedChannel**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_configureauthenicatedchannel) function with D3DAUTHETICATEDCONFIGURE\_CRYPTOSESSION set to configure the crypto session with the DirectX VA 2.0 decode device. Before configuring the crypto session with the DirectX VA 2.0 decode device, the runtime must call the driver's [**DecodeExtensionExecute**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodeextensionexecute) function to retrieve a driver handle for the DirectX VA 2.0 decode device. The runtime sets the members of the [**D3DDDIARG\_DECODEEXTENSIONEXECUTE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_decodeextensionexecute) structure to the following values to retrieve the driver handle for the DirectX VA 2.0 decode device:

```cpp
#define DXVA2_DECODE_GET_DRIVER_HANDLE    0x725
D3DDDIARG_DECODEEXTENSIONEXECUTE.Function = DXVA2_DECODE_GET_DRIVER_HANDLE;
D3DDDIARG_DECODEEXTENSIONEXECUTE.pPrivateInput->pData = NULL;
D3DDDIARG_DECODEEXTENSIONEXECUTE.pPrivateInput->DataSize = 0;
D3DDDIARG_DECODEEXTENSIONEXECUTE.pPrivateOutput->pData = HANDLE*;
D3DDDIARG_DECODEEXTENSIONEXECUTE.pPrivateOutput->DataSize = sizeof(HANDLE);
```

When the runtime calls the driver's [**CreateDecodeDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createdecodedevice) function to create the DirectX VA 2.0 decode device, the runtime specifies zeros for the decode-encryption GUIDs within the [**DXVADDI\_CONFIGPICTUREDECODE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_configpicturedecode) structure.

After the runtime calls the driver's [**CreateCryptoSession**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createcryptosession) function with the **CryptoType** member of the [**D3DDDIARG\_CREATECRYPTOSESSION**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_createcryptosession) structure set to D3DCRYPTOTYPE\_AES128\_CTR to create the crypto session, the setting of the **pPVPSetKey** member of the [**D3DDDIARG\_DECODEBEGINFRAME**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_decodebeginframe) structure in a call to the driver's [**DecodeBeginFrame**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodebeginframe) function to decode a frame indicates the following meanings:

-   If **pPVPSetKey** is set to **NULL**, none of the buffers for the frame contain encrypted data and hence do not require decryption.

-   If **pPVPSetKey** points to the NULL\_GUID (all zeros), the buffers for the frame are encrypted with the session key.

-   If **pPVPSetKey** points to a content key, it indicates that an application used the session key to encrypt the content key. The driver should use this content key to decrypt all encrypted buffers that are associated with this frame.

The initialization vector for each encrypted buffer appears in the **pCipherCounter** member of the [**DXVADDI\_DECODEBUFFERDESC**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_decodebufferdesc) structure in a call to the driver's [**DecodeExecute**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodeexecute) function. The driver should fail the call to its *DecodeExecute* function if it determines that the initialization vector was previously used for the same content key (or session key if the content key is not used). The application should increment the **IV** member of the [**DXVADDI\_PVP\_HW\_IV**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvaddi_pvp_hw_iv) for each buffer that the application encrypts. Therefore, the driver's *DecodeExecute* function can fail if the **IV** member is less than or equal to the previous **IV** value that was passed to *DecodeExecute*.

If the runtime must partially encrypt the buffers, it calls the driver's [**DecodeExtensionExecute**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_decodeextensionexecute) function and sets the members of the [**D3DDDIARG\_DECODEEXTENSIONEXECUTE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddiarg_decodeextensionexecute) structure to the following values to specify which blocks the driver should encrypt:

```cpp
#define DXVA2_DECODE_SPECIFY_ENCRYPTED_BLOCKS    0x724
D3DDDIARG_DECODEEXTENSIONEXECUTE.Function = DXVA2_DECODE_SPECIFY_ENCRYPTED_BLOCKS;
D3DDDIARG_DECODEEXTENSIONEXECUTE.pPrivateInput->pData = D3DENCRYPTED_BLOCK_INFO*;
D3DDDIARG_DECODEEXTENSIONEXECUTE.pPrivateInput->DataSize = sizeof(D3DENCRYPTED_BLOCK_INFO);
D3DDDIARG_DECODEEXTENSIONEXECUTE.pPrivateOutput->pData = NULL;
D3DDDIARG_DECODEEXTENSIONEXECUTE.pPrivateOutput->DataSize = 0;
```

 
