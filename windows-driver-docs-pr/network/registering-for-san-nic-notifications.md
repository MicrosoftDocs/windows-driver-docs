---
title: Registering for SAN NIC Notifications
description: Registering for SAN NIC Notifications
ms.assetid: 6a630e7c-3b1a-4f4a-b808-f6b4e2315a42
keywords:
- NIC notifications WDK SANs
- proxy drivers WDK SANs , NIC notifications
- SAN proxy drivers WDK , NIC notifications
- registering NIC notifications
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering for SAN NIC Notifications





When a proxy driver receives a request from its associated SAN service provider to supply the list of IP addresses assigned to NICs under the driver's control, the driver determines and passes this list to the provider.

In order to obtain these IP addresses, the proxy driver must register with the Transport Driver Interface (TDI) to receive address change notifications. The proxy driver calls the [**TdiRegisterPnPHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff565062) function. In this call, this proxy driver passes pointers to callback functions in the **AddAddressHandlerV2** and **DelAddressHandlerV2** members of the TDI\_CLIENT\_INTERFACE\_INFO structure to specify callback functions for address additions and deletions. After the **TdiRegisterPnPHandlers** function has returned successfully, TDI immediately indicates all currently active network addresses to the proxy driver, using the address-addition callback. The indication contains both network addresses and identifiers for the devices to which those addresses are bound.

Whenever TDI calls either of these callback functions to indicate address additions or deletions, the proxy driver requires the following parameters:

<a href="" id="address"></a>*Address*  
Pointer to a TA\_ADDRESS structure that describes the network address either assigned to or removed from the NIC. In the case of TCP/IP, this pointer is actually be a pointer to a TA\_ADDRESS\_IP structure.

<a href="" id="devicename"></a>*DeviceName*  
Pointer to a Unicode string that identifies the transport-to-NIC binding with which the address is associated. In case of TCP/IP, the Unicode string has the following format: \\Device\\Tcpip\_{NIC-GUID}, where NIC-GUID is the globally unique identifier assigned by the network configuration subsystem to the NIC.

The preceding structure definitions are defined in the tdi.h header file. The preceding registration and callback functions are defined in the tdikrnl.h header file. These header files are available in the Microsoft Windows Driver Development Kit (DDK) and the Windows Driver Kit (WDK). For detailed information about TDI Plug and Play (PnP) notifications, see [TDI Client Callbacks](https://msdn.microsoft.com/library/windows/hardware/ff565081) and [TDI Client Event and PnP Notification Handlers](https://msdn.microsoft.com/library/windows/hardware/ff565082).

At system startup, TDI calls the proxy driver's address-addition callback to indicate all currently active IP addresses. TDI also calls this callback whenever the TCP/IP transport protocol registers a new IP address with TDI. The proxy driver includes in its list of IP addresses only those addresses assigned to the proxy driver's NICs. The driver's address-addition callback should return control promptly if the driver does not recognize the NIC at *DeviceName*.

TDI calls the proxy driver's address-removal callback whenever the TCP/IP transport protocol indicates to TDI that a NIC has been removed. If the IP address of the NIC belongs to one of the proxy driver's NICs, the proxy driver removes the IP address from the list.

**Note**  TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](https://msdn.microsoft.com/library/windows/hardware/ff571067) or [Winsock Kernel](https://msdn.microsoft.com/library/windows/hardware/ff571083) instead.

 

 

 





