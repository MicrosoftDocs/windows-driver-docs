---
title: Encryption Support
description: Encryption Support
ms.assetid: d5ce9c02-7126-4775-bb87-dae45b93b652
keywords:
- video decoding WDK DirectX VA , encryption
- decoding video WDK DirectX VA , encryption
- picture decoding WDK DirectX VA , encryption
- encryption WDK DirectX VA
- cryptography WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Encryption Support


## <span id="ddk_encryption_support_gg"></span><span id="DDK_ENCRYPTION_SUPPORT_GG"></span>


Data used in video decoding can be encrypted for the following structures and types of data:

-   Macroblock control command structures

-   Residual difference block structures

-   Bitstream buffers

In order for the host decoder to use encryption, it must determine what types of encryption the accelerator supports. The information about the types of encryption that are supported by an accelerator is contained in a list of encryption-type GUIDs that are supplied to the host as video accelerator format GUIDs. For more information about video accelerator format GUIDs, see the Microsoft Windows SDK documentation.

**Note**   All DirectX VA accelerators must be able to operate without using encryption. Support for operating without encryption, therefore, does not need to be declared, and the DXVA\_NoEncrypt "no encryption" GUID must never be sent in the video accelerator format GUID list.

 

The host selects the type of encryption protocol to apply and indicates this choice by sending a GUID to the accelerator. In a typical encryption scenario, two more steps take place before encrypted data can be successfully transferred:

1.  The host decoder may require verification that the accelerator is authorized to receive the data. This verification can be provided by having the accelerator pass a signed structure to the host to prove that it holds an authorized public/private key pair.

2.  The host decoder then sends an encrypted content key to the accelerator.

The precise number of steps for initializing the encryption protocol depends on the type of encryption being used and how it is implemented.

Each data set that is exchanged between the host and accelerator to pass the necessary encryption initialization parameters must be prefixed by the encryption protocol type GUID. This GUID distinguishes the data of one type of encryption from the data of another. This is necessary because one type of encryption could be used for one DirectX VA buffer, and another type of encryption could be used for another DirectX VA buffer.

The [**DXVA\_EncryptProtocolHeader**](https://msdn.microsoft.com/library/windows/hardware/ff563965) structure is used to indicate that an encryption protocol is being used as well as the type of encryption being used.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Encryption%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




