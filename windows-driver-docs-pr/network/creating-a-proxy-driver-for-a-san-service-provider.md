---
title: Creating a Proxy Driver for a SAN Service Provider
description: Creating a Proxy Driver for a SAN Service Provider
ms.assetid: 350c21a3-98e3-48a2-8403-68de97314933
keywords:
- Windows Sockets Direct WDK , proxy drivers
- proxy drivers WDK SANs
- SAN proxy drivers WDK
- proxy drivers WDK SANs , about SAN proxy drivers
- SAN proxy drivers WDK , about SAN proxy drivers
- SAN service providers WDK , proxy drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a Proxy Driver for a SAN Service Provider





A proxy driver for a SAN service provider is a kernel-mode driver that performs tasks required by the Windows Sockets switch and the SAN service provider. Such tasks include managing memory and determining the IP addresses of network interface controllers (NICs) that are under the proxy driver's control. The proxy driver is not required to be a Windows Driver Model (WDM) driver. That is, it is not required to support Plug and Play or power management. For more information about developing a kernel-mode driver, see [Kernel-Mode Driver Components](https://msdn.microsoft.com/library/windows/hardware/ff553213).

Different vendors might use different underlying technologies to implement their SAN network interface controllers (NICs), therefore Windows Sockets Direct does not specify an interface between a SAN service provider and its proxy driver or between the proxy driver and a SAN transport.

A SAN NIC vendor must implement a transport interface that is suitable for its underlying technologies. A vendor can implement this interface in the SAN NIC, in a kernel-mode driver for the SAN NIC, or both. A SAN service provider maps this interface directly into a user-mode process's address space. A vendor must ensure that all buffers passed across this interface are locked down and registered with the SAN NIC.

The following sections describe how to create a proxy driver for a SAN service provider DLL:

[Initializing and Unloading a SAN Proxy Driver](initializing-and-unloading-a-san-proxy-driver.md)

[Allocating and Releasing Memory for a SAN Proxy Driver](allocating-and-releasing-memory-for-a-san-proxy-driver.md)

[Securing and Releasing Ownership of Virtual Addresses](securing-and-releasing-ownership-of-virtual-addresses.md)

[Registering for SAN NIC Notifications](registering-for-san-nic-notifications.md)

[Translating to a SAN Native Address](translating-to-a-san-native-address.md)

[Implementing IOCTLs for a SAN Service Provider](implementing-ioctls-for-a-san-service-provider.md)

 

 





