---
title: Managing Multiple Attached Provider Modules
description: Managing Multiple Attached Provider Modules
keywords:
- provider modules WDK Network Module Registrar , multiple attached
- client modules WDK Network Module Registrar , multiple attached
- multiple attached network modules WDK Network Module Registrar
ms.date: 04/20/2017
---

# Managing Multiple Attached Provider Modules


A single client module can attach to more than one provider module. In order to manage multiple attached provider modules, a client module must independently save the binding handle, the provider module's binding context, and the provider module's dispatch table for each provider module to which it is attached. Typically this data is saved in the client module's binding context for each attachment. However, a client module can manage the data for each attached provider module in whatever way it chooses.

A [Network Programming Interface (NPI)](network-programming-interface.md) typically defines the client module callback functions such that they include either a pointer to the client module's binding context or some other NPI-specific identifier as one of the function parameters. As a result, a client module can determine which provider module is the caller when one of it's NPI callback functions is called.

 

 





