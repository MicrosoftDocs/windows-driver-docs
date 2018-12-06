---
title: Introduction to the Network Module Registrar
description: Introduction to the Network Module Registrar
ms.assetid: affa7979-bc43-4e34-a528-5484982d940d
keywords:
- Network Module Registrar WDK , about Network Module Registrar
- NMR WDK , about Network Module Registrar
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to the Network Module Registrar


The Network Module Registrar (NMR) is an operating system module that facilitates the attachment of [network modules](network-module.md) to each other. Each network module registers itself with the NMR, specifying the characteristics that describe the network module. The NMR initiates attachment between pairs of registered network modules that can be attached to each other. After they are attached, the network modules can interact with each other independent of the NMR. The NMR also facilitates detachment of attached pairs of network modules when one of the network modules deregisters with the NMR. The deregistration of a network module is not complete until the network module is completely detached from all network modules to which it was previously attached.

Although the NMR was developed for use by network modules, the design of the NMR architecture is sufficiently generic so that it can also be used by software modules in other technology areas.

 

 





