---
title: Securing and Releasing Ownership of Virtual Addresses
description: Securing and Releasing Ownership of Virtual Addresses
ms.assetid: e7b31c8d-fed4-43e2-bcd2-295e3e17719e
keywords:
- proxy drivers WDK SANs , virtual addresses
- SAN proxy drivers WDK , virtual addresses
- virtual addresses WDK SANs
- ownership WDK virtual addresses
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Securing and Releasing Ownership of Virtual Addresses





The proxy driver must secure ownership of the virtual addresses of user-mode buffers whenever the SAN service provider for the proxy driver caches those buffers. For more information about caching buffers, see [Caching Registered Memory](caching-registered-memory.md). The proxy driver secures ownership of a user-mode buffer, so that the operating system notifies the Windows Sockets switch if the buffer is released back to the operating system by an application. To secure ownership of a buffer, the proxy driver must call the [**MmSecureVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff556374) function. In this call, the proxy driver passes a pointer to the starting address of the buffer and the size, in bytes, of the buffer.

If the virtual-to-physical mappings for the cached buffer are scheduled to change, the switch is notified and calls the SAN service provider's [**WSPMemoryRegistrationCacheCallback**](https://msdn.microsoft.com/library/windows/hardware/ff566299) function to remove the buffer registration from the SAN NIC and the buffer from the SAN service provider's cache. The SAN service provider's proxy driver, in turn, must call the [**MmUnsecureVirtualMemory**](https://msdn.microsoft.com/library/windows/hardware/ff556395) function to release ownership of the buffer. In this call, the proxy driver passes the handle to the buffer that was previously returned from the **MmSecureVirtualMemory** call.

**Note**  A driver that tries to access a user-mode buffer that was secured through a call to **MmSecureVirtualMemory** can potentially bring down the operating system. Therefore, when the proxy driver accesses such a user-mode buffer, it must also use the **try/except** mechanism around the code that accesses the buffer. For more information about **try/except**, see the Visual C++ documentation.

 

A SAN service provider can send I/O control (IOCTL) requests to the proxy driver to secure and release ownership of a buffer. For more information, see [Implementing IOCTLs for a SAN Service Provider](implementing-ioctls-for-a-san-service-provider.md).

 

 





