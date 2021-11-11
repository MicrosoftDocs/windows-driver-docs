---
title: EFI_RNG_SERVICE_BINDING_PROTOCOL
description: Used to locate RNG services provided by a driver, and to create and destroy instances so that multiple drivers can use the underlying RNG services.
ms.date: 08/20/2021
ms.localizationpriority: medium
---

# EFI_RNG_SERVICE_BINDING_PROTOCOL

The EFI_RNG_SERVICE_BINDING_PROTOCOL is used to locate Random Number Generation (RNG) services provided by a driver, and to create and destroy instances of the EFI_RNG_PROTOCOL so that multiple drivers can use the underlying RNG services.

The generic EFI_SERVICE_BINDING_PROTOCOL is described in sections 2.5.8 and 10.6 of the UEFI Specification. This section provides information specific to EFI_RNG_SERVICE_BINDING_PROTOCOL.

## GUID

```cpp
// {E417A4A2-0843-4619-BF11-5CE82AFCFC59}
#define EFI_RNG_SERVICE_BINDING_PROTOCOL_GUID \
  {0xe417a4a2, 0x0843, 0x4619, 0xbf, 0x11, 0x5c, 0xe8, 0x2a, 0xfc, 0xfc, 0x59};
```

## Remarks

An application or driver that requires RNG services can use one of the protocol handler services, such as EFI_BOOT_SERVICES->LocateHandleBuffer(), to search for devices that publish an EFI_RNG_SERVICE_BINDING_PROTOCOL. Each device with a published EFI_RNG_SERVICE_BINDING_PROTOCOL shall support the EFI_RNG_PROTOCOL and make it available for use.

After a successful call to the EFI_RNG_SERVICE_BINDING_PROTOCOL.CreateChild() function, the child EFI_RNG_PROTOCOL driver instance is ready for use.

Before an application terminates execution, every successful call to the EFI_RNG_SERVICE_BINDING_PROTOCOL.CreateChild() function must be matched with a call to the EFI_RNG_SERVICE_BINDING_PROTOCOL.DestroyChild() function.

## Requirements

**Header:** User generated
