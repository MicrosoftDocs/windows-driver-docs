---
title: About Kernel Mode Performance Counters
description: About Kernel Mode Performance Counters
ms.assetid: 57655e65-6db4-487d-8831-282e8d30d84e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# About Kernel Mode Performance Counters


Performance Counters for Windows (PCW) interacts with different components in the system and keeps track of the counter sets (and their instances) that are provided by kernel-mode components. Additionally, PCW tracks service requests from consumers by reviewing the counter sets and returning the requested data.

Kernel-mode PCW providers are installed in the system as Performance Counter Library (PERFLIB) (Version 2 providers), which allows their counters to be browsed, and allows for data collection and instance enumeration. Consumers can query KM PCW providers by using PDH and PERFLIB Version 1 without any modification to the consumer code. For more information, see [Developing with Performance Counters](http://go.microsoft.com/fwlink/p/?linkid=144623).

Providers running in kernel-mode register their counter sets by using the kernel-mode PCW provider API. Providers can manage the instances of the registered counter sets and use notifications to be informed when various events related to performance counters occur (for example, when consumers add, remove, or collect counters).

**Note**   The kernel-mode PCW provider API (PERFLIB version 2), introduced in Windows 7, does not currently support session-space drivers.

 

 

 





