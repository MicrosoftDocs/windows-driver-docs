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
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





