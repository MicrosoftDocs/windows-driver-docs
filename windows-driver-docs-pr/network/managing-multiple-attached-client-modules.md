---
title: Managing Multiple Attached Client Modules
description: Managing Multiple Attached Client Modules
ms.assetid: dcb2ebba-6df7-47d5-97b6-ed2691b5e6c8
keywords:
- provider modules WDK Network Module Registrar , multiple attached
- client modules WDK Network Module Registrar , multiple attached
- multiple attached network modules WDK Network Module Registrar
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Multiple Attached Client Modules


A single provider module can attach to more than one client module. In order to manage multiple attached client modules, a provider module must independently save the binding handle, the client module's binding context, and the client module's dispatch table for each client module to which it is attached. Typically this data is saved in the provider module's binding context for each attachment. However, a provider module can manage the data for each attached client module in whatever way it chooses.

A [Network Programming Interface (NPI)](network-programming-interface.md) typically defines the provider module functions such that they include either a pointer to the provider module's binding context or some other NPI-specific identifier as one of the function parameters. As a result, a provider module can determine which client module is the caller when one of it's NPI functions is called.

 

 





