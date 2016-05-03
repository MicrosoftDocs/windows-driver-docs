---
title: EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL
author: windows-driver-content
description: The EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL is used to locate Random Number Generation (RNG) services provided by a driver, and to create and destroy instances of the EFI\_RNG\_PROTOCOL so that multiple drivers can use the underlying RNG services.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3CAD0FD8-DD26-4D26-A9E9-4B2750985E00
---

# EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL


The EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL is used to locate Random Number Generation (RNG) services provided by a driver, and to create and destroy instances of the EFI\_RNG\_PROTOCOL so that multiple drivers can use the underlying RNG services.

The generic EFI\_SERVICE\_BINDING\_PROTOCOL is described in sections 2.5.8 and 10.6 of the UEFI Specification. This section provides information specific to EFI\_RNG\_SERVICE\_BINDING\_PROTOCOL.

## GUID


``` syntax
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_RNG_SERVICE_BINDING_PROTOCOL%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


