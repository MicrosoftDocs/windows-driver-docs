---
title: Using NMR for WSK Registration and Unregistration
description: Using NMR for WSK Registration and Unregistration
keywords:
- Winsock Kernel WDK networking , registering
- registering Winsock Kernel applications
- WSK WDK networking , registering
- unregistering Winsock Kernel applications
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using NMR for WSK Registration and Unregistration


The [Registering a Winsock Kernel Application](registering-a-winsock-kernel-application.md) and [Unregistering a Winsock Kernel Application](unregistering-a-winsock-kernel-application.md) sections describe how a WSK application can attach to and detach from the WSK subsystem by using the [WSK registration functions](/windows-hardware/drivers/ddi/_netvista/). However, WSK can also attach to the WSK subsystem by using the [Network Module Registrar (NMR)](network-module-registrar2.md).

A WSK application can register itself with the NMR as a client of the WSK [Network Programming Interface (NPI)](network-programming-interface.md) by using the procedures in the following sections:

-   [Initializing NMR Data Structures](initializing-nmr-data-structures.md)
-   [Attaching the WSK Client to the WSK Subsystem](attaching-the-wsk-client-to-the-wsk-subsystem.md)
-   [Unregistering and Unloading the WSK Client](unregistering-and-unloading-the-wsk-client.md)

Using the [**WskRegister**](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskregister) and [**WskDeregister**](/windows-hardware/drivers/ddi/wsk/nf-wsk-wskderegister) functions is the preferred method for registering and unregistering WSK applications. The [Network Module Registrar](network-module-registrar2.md) remains available for compatibility.

 

