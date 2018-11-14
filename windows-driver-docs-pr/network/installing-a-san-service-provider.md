---
title: Installing a SAN Service Provider
description: Installing a SAN Service Provider
ms.assetid: 3a7fcacf-ef26-4a41-a991-230daf67accf
keywords:
- Windows Sockets Direct WDK , installing components
- SAN service providers WDK , installing
- SAN service providers WDK , registering
- registering SAN service providers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a SAN Service Provider





A SAN service provider is typically installed as a base Windows Sockets service provider that interfaces with the Windows Sockets switch. Although a SAN service provider can be installed for direct use by an application instead, the Windows Sockets Direct technology does not support using a SAN service provider in this manner. A SAN service provider that is installed for direct use by an application exports its native address family and protocol characteristics rather than those of TCP/IP protocol.

A SAN service provider that is indirectly exposed to applications through the Windows Sockets switch must set the PFL\_HIDDEN flag in the **dwProviderFlags** member of the SAN service provider's [**WSAPROTOCOL\_INFOW**](https://msdn.microsoft.com/library/windows/hardware/ff565963) structure. To install the SAN service provider on the operating system, the SAN service provider's installation mechanism passes this structure in a call to the **WSCInstallProvider** function. For more information about **WSCInstallProvider**, see the Microsoft Windows SDK documentation. The SAN service provider's installation mechanism can be for example, a setup program or a function exported by the SAN service provider and called by a INF file directive.

The SAN service provider's installation mechanism must add a value of type REG\_BINARY to the following key in the registry before the SAN service provider can be detected by the Windows Sockets switch as a base Windows Sockets service provider:

```Console
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Winsock\
Parameters\TCP on SAN
```

This value contains the binary representation of the value in the **ProviderId** member from the WSAPROTOCOL\_INFOW structure. This value registers a SAN service provider with the Windows Sockets switch. This member contains the globally unique identifier (GUID) that the vendor assigned to the SAN service provider.

The vendor can also assign a unique name that represents this GUID, for example:

-   Trademarked name of the product

-   Unique numeric value

-   Textual representation of the GUID

**To register a SAN service provider**

1.  The switch calls the **WSAProviderConfigChange** function to detect Windows Sockets provider installation and removal events.

2.  After a new Windows Sockets service provider is installed, the switch calls the **WSCEnumProtocols** function to query the Windows Sockets catalog and the list of SAN service providers in the registry to determine whether the new service provider controls a SAN. For more information about **WSCEnumProtocols**, see the Windows SDK.

3.  If the switch detects a new SAN service provider, the switch initializes that service provider as described in [Initializing a SAN Service Provider](initializing-a-san-service-provider.md).

4.  The switch also calls the following functions of the newly installed SAN service provider after the SAN service provider is initialized to service any existing listening sockets bound to the wildcard IP address (0.0.0.0) (the wildcard IP address implies that the SAN service provider should accept incoming connection requests from all NICs it controls):

    <a href="" id="wspsocket"></a>**WSPSocket**  
    Creates a socket

    <a href="" id="wspbind"></a>**WSPBind**  
    Binds the socket to the wildcard IP address

    <a href="" id="wsplisten"></a>**WSPListen**  
    Sets the socket to acknowledge and queue incoming connection requests until accepted by the switch

    **Note**  Beginning with Windows Vista, the wildcard IP address 0.0.0.0 is not available.
    Also beginning with Windows Vista, if the **IPAutoconfigurationEnabled** registry key is set to a value of 0, automatic IP address assignment is disabled, and no IP address is assigned. In this case, the **ipconfig** command line tool will not display an IP address. If the key is set to a nonzero value, an IP address is automatically assigned. This key can be located at the following paths in the registry:

    **HKEY\_LOCAL\_MACHINE\\SYSTEM\\Current Control Set\\Services\\Tcpip\\Parameters\\IPAutoconfigurationEnabled**

    **HKEY\_LOCAL\_MACHINE\\SYSTEM\\Current Control Set\\Services\\Tcpip\\Parameters\\Interfaces\\*GUID*\\IPAutoconfigurationEnabled**

     

 

 





