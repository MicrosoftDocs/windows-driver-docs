---
title: Easier Initialization
description: Easier Initialization
ms.assetid: 34f939fd-2bcc-482b-b877-42cc57bdf59b
keywords:
- NDIS WDK , initializing drivers
- initializing drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Easier Initialization





All NDIS 6.0 and later drivers have updated driver registration interfaces. These NDIS interfaces provide simplified driver registration and the ability to register optional services separately from required services.

Miniport drivers require fewer function calls to register. In general, NDIS 6.0 and later function interfaces are more consistent when compared to the NDIS 5.*x* and earlier interfaces. Resources that are allocated also have a reciprocal function to free them.

An NDIS 6.0 or later intermediate driver can register as a miniport-intermediate driver. Such a driver has both a virtual miniport for a virtual device and a miniport adapter for a physical device. Registering as a miniport-intermediate driver simplifies the creation of an intermediate driver that binds only to a vendor's own NIC. The driver can pass network data, OID requests, and status indications between its virtual miniport and physical miniport adapter with internal calls.

Protocol drivers receive most of the information about an underlying adapter in a binding request. Therefore, protocol drivers do not send OID requests for the parameters that NDIS already provided in the bind request.

To initialize a miniport adapter, miniport drivers can receive OID requests that combine the information from many separate OID requests into fewer requests containing the combined information.

Intermediate drivers have fewer specialized functions and make better use of miniport driver and protocol driver interfaces.

A miniport driver can read or write the registry at any time -- not just during initialization. For example, when an application requests through Windows Management Instrumentation (WMI) that a driver change one of its operating parameters, the driver can record this change in the registry so that the change persists across reboots.

NDIS provides a bus-independent function call for reading and writing bus-specific configuration parameters. A driver can call this function regardless of the bus type in the system. This ensures that NDIS will be able to support future buses without the addition of new bus-specific functions.

For more information about driver initialization, see the initialization topics in the following sections:

[Writing NDIS Miniport Drivers](writing-ndis-miniport-drivers.md)

[Writing NDIS Protocol Drivers](writing-ndis-protocol-drivers.md)

[NDIS Filter Drivers](ndis-filter-drivers.md)

[Writing NDIS Intermediate Drivers](writing-ndis-intermediate-drivers.md)

 

 





