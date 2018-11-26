---
title: EFI_RNG_SERVICE_BINDING_PROTOCOL
description: Used to locate RNG services provided by a driver, and to create and destroy instances so that multiple drivers can use the underlying RNG services.
ms.assetid: 3CAD0FD8-DD26-4D26-A9E9-4B2750985E00
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL


The EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL is used to locate Random Number Generation (RNG) services provided by a driver, and to create and destroy instances of the EFI\_RNG\_PROTOCOL so that multiple drivers can use the underlying RNG services.

The generic EFI\_SERVICE\_BINDING\_PROTOCOL is described in sections 2.5.8 and 10.6 of the UEFI Specification. This section provides information specific to EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL.

## GUID


```cpp
// {E417A4A2-0843-4619-BF11-5CE82AFCFC59}
#define EFI_RNG_SERVICE_BINDING_PROTOCOL_GUID \
  {0xe417a4a2, 0x0843, 0x4619, 0xbf, 0x11, 0x5c, 0xe8, 0x2a, 0xfc, 0xfc, 0x59};
```

## Remarks


An application or driver that requires RNG services can use one of the protocol handler services, such as EFI\_BOOT\_SERVICES-&gt;LocateHandleBuffer(), to search for devices that publish an EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL. Each device with a published EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL shall support the EFI\_RNG\_PROTOCOL and make it available for use.

After a successful call to the EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL.CreateChild() function, the child EFI\_RNG\_PROTOCOL driver instance is ready for use.

Before an application terminates execution, every successful call to the EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL.CreateChild() function must be matched with a call to the EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL.DestroyChild() function.

## Requirements


**Header:** User generated

 

 




