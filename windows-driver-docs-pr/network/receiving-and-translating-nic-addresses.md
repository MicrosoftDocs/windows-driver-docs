---
title: Receiving and Translating NIC Addresses
description: Receiving and Translating NIC Addresses
ms.assetid: c7171a4d-cc77-427e-8d23-8811f650e543
keywords:
- Windows Sockets Direct WDK , initializing SAN usage
- initializing SAN usage
- NIC address translations WDK SANs
- translating NIC address WDK SANs
- receiving NIC addresses for SANs
- addresses WDK SANs
- delete-address notifications WDK SANs
- add-address notifications WDK SANs
- notifications WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving and Translating NIC Addresses





The Windows Sockets switch always uses the [WSK address families](https://msdn.microsoft.com/library/windows/hardware/ff571151), which contain IP addresses, when it interacts with SAN service providers and SAN NICs. The switch does not use a SAN's native address family. Therefore, a SAN service provider must use its associated proxy driver to retrieve the list of IP addresses assigned to its NICs. The SAN service provider uses these IP addresses when interacting with its proxy driver. The proxy driver must translate between IP addresses and native addresses.

During initialization, a proxy driver typically registers with Transport Driver Interface (TDI) for address change notifications. All Plug and Play (PnP) aware transports, including TCP/IP, supply address change notifications through TDI to clients that have registered for such notifications.

**Note**  TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](https://msdn.microsoft.com/library/windows/hardware/ff571067) or [Winsock Kernel](https://msdn.microsoft.com/library/windows/hardware/ff571083) instead.

 

### Registering for Address Change Notification

During initialization, a proxy driver calls the [**TdiRegisterPnPHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff565062) function to register for address change notifications. In this call, the proxy driver passes pointers to callback functions for address additions and deletions in the **AddAddressHandlerV2** and **DelAddressHandlerV2** members of the TDI\_CLIENT\_INTERFACE\_INFO structure. After the proxy driver registers to receive these notifications, TDI promptly indicates all currently active network addresses using the add-address callback.

TDI passes the following parameters to a proxy driver's add-address or delete-address callback functions:

<a href="" id="address"></a>*Address*  
Pointer to a TA\_ADDRESS structure that describes the network address assigned to or removed from the NIC. In the case of TCP/IP, this pointer is actually a pointer to a TA\_ADDRESS\_IP structure.

<a href="" id="devicename"></a>*DeviceName*  
Pointer to a Unicode string that identifies the transport-to-NIC binding with which the address is associated. In case of TCP/IP, the Unicode string has the following format:

\\Device\\Tcpip\_{NIC-GUID}

where NIC-GUID is the globally unique identifier assigned by the network configuration subsystem to the NIC.

The preceding structure definitions are defined in the tdi.h header file. The preceding registration and callback functions are defined in the tdikrnl.h header file. These header files are available in the Microsoft Windows Driver Development Kit (DDK) and the Windows Driver Kit (WDK). Detailed information about TDI PnP notifications is included in [TDI Client Callbacks](https://msdn.microsoft.com/library/windows/hardware/ff565081) and [TDI Client Event and PnP Notification Handlers](https://msdn.microsoft.com/library/windows/hardware/ff565082).

**Note**  TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](https://msdn.microsoft.com/library/windows/hardware/ff571067) or [Winsock Kernel](https://msdn.microsoft.com/library/windows/hardware/ff571083) instead.

 

### Maintaining a List of IP Addresses

A SAN service provider's proxy driver uses add-address and delete-address notifications to maintain the list of IP addresses assigned to each NIC under its control. The proxy driver uses this list to translate between one or more IP addresses assigned to a SAN NIC by the TCP/IP transport and native SAN addresses. The proxy driver must also supply a device-control routine that makes the list of IP addresses assigned to a NIC available to the Windows Sockets switch whenever the switch makes an SIO\_ADDRESS\_LIST\_QUERY control-code query. The proxy driver's **DriverEntry** routine must specify an entry point for this device-control routine.

The Windows Sockets switch maintains a list of all IP addresses assigned to each SAN NIC. To retrieve IP addresses for this inclusive list, the switch calls each SAN service provider 's [**WSPIoctl**](https://msdn.microsoft.com/library/windows/hardware/ff566296) function, passing the SIO\_ADDRESS\_LIST\_QUERY control code. Each SAN service provider, in turn, queries its associated proxy driver for its individual list of IP addresses assigned to its SAN NICs. After the switch is notified of an address change, it again queries each SAN service provider for updates in each individual list.

 

 





