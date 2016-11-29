---
title: About Kernel Mode Performance Counters
description: About Kernel Mode Performance Counters
ms.assetid: 57655e65-6db4-487d-8831-282e8d30d84e
---

# About Kernel Mode Performance Counters


Performance Counters for Windows (PCW) interacts with different components in the system and keeps track of the counter sets (and their instances) that are provided by kernel-mode components. Additionally, PCW tracks service requests from consumers by reviewing the counter sets and returning the requested data.

Kernel-mode PCW providers are installed in the system as Performance Counter Library (PERFLIB) (Version 2 providers), which allows their counters to be browsed, and allows for data collection and instance enumeration. Consumers can query KM PCW providers by using PDH and PERFLIB Version 1 without any modification to the consumer code. For more information, see [Developing with Performance Counters](http://go.microsoft.com/fwlink/p/?linkid=144623).

Providers running in kernel-mode register their counter sets by using the kernel-mode PCW provider API. Providers can manage the instances of the registered counter sets and use notifications to be informed when various events related to performance counters occur (for example, when consumers add, remove, or collect counters).

**Note**   The kernel-mode PCW provider API (PERFLIB version 2), introduced in Windows 7, does not currently support session-space drivers.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20About%20Kernel%20Mode%20Performance%20Counters%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




