---
title: Network Programming Interface
description: Network Programming Interface
ms.assetid: 74d706e1-5398-4685-b3ab-7b4c4b6b5588
keywords:
- NPI WDK Network Module Registrar
- client characteristics structure WDK Network Module Registrar
- provider characteristics structure WDK Network Module Registrar
- client dispatch tables WDK Network Module Registrar
- dispatch tables WDK Network Module Registrar
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Network Programming Interface


A *Network Programming Interface*, or NPI, defines the interface between [network modules](network-module.md) that can be attached to one another. A [client module](client-module.md) that is registered as a client of a particular NPI can only be attached to [provider modules](provider-module.md) that are registered as providers of the same NPI. Likewise, a provider module that is registered as a provider of a particular NPI can only be attached to client modules that are registered as clients of the same NPI.

Each NPI defines the following items:

-   An *NPI identifier* that uniquely identifies the NPI. A network module specifies an NPI identifier to indicate the particular NPI that it supports when the network module registers itself with the Network Module Registrar (NMR). A network module can support multiple NPIs by registering itself with the NMR multiple times, once for each NPI that it supports. The NMR will initiate attaching a client module to a provider module only if they both support the same NPI.

-   An optional [*client characteristics*](https://msdn.microsoft.com/library/windows/hardware/ff568812) structure that specifies the NPI-specific characteristics of each client module. Such NPI-specific characteristics might include items such as which version (or versions) of the NPI that a client module supports, or which address family or protocol a client module requires. A provider module can use the information contained in a client module's client characteristics structure to determine if it will attach to the client module. If an NPI does not define any NPI-specific client characteristics, then this structure is not required.

-   An optional [*provider characteristics*](https://msdn.microsoft.com/library/windows/hardware/ff568814) structure that specifies the NPI-specific characteristics of each provider module. Such NPI-specific characteristics might include items such as which version (or versions) of the NPI that a provider module supports, or which address families or protocols a provider module supports. A client module can use the information contained in a provider module's client characteristics structure to determine if it will attach to the provider module. If an NPI does not define any NPI-specific provider characteristics, then this structure is not required.

-   Zero or more client module callback functions. After a provider module successfully attaches to a client module, the provider module can access the client module's functionality by calling the client module's callback functions.

-   One or more provider module functions. After a client module successfully attaches to a provider module, the client module can access the provider module's functionality by calling the provider module's functions.

-   A *client dispatch table* structure that contains function pointers to each of the client module callback functions. If an NPI does not define any client module callback functions, then this structure is not required.

-   A *provider dispatch table* structure that contains function pointers to each of the provider module functions.

A client module that supports a particular NPI uses the items defined by the NPI to implement the client side of the interface. Similarly, a provider module that supports a particular NPI uses the items defined by the NPI to implement the provider side of the interface.

All of the items defined by an NPI are opaque to the NMR except for the NPI identifier. The NMR uses the NPI identifier to determine which client modules should be attached to which provider modules.

 

 





