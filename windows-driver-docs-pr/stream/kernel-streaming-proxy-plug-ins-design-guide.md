---
title: Kernel Streaming Proxy Plug-ins Design Guide
description: Kernel Streaming Proxy Plug-ins Design Guide
ms.assetid: 9a2b83ab-f54c-421b-bc9b-7dad63cd8cb5
keywords:
- Kernel Streaming Proxy WDK AVStream , plug-ins
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Kernel Streaming Proxy Plug-ins Design Guide


The kernel-streaming (KS) proxy module (*Ksproxy.ax*) is a DirectShow filter that brokers communication between KS objects in kernel-mode and user-mode applications. User-mode components can use KS proxy to communicate with any minidriver that is based on *Ks.sys*.

Specifically, an application can use the KS proxy module to control and retrieve information from KS objects that a KS minidriver implements. KS objects include, for example, KS filters, KS pins, and KS clocks.

You can extend KS proxy by writing a plug-in, which is a COM interface that provides methods to access property values. An advantage of the plug-in model is that it provides application writers with a mechanism that is more familiar than working directly with KS pin and KS filter property sets.

The following sections provide a high-level description of how to write an interface handler plug-in or a property page that uses KS proxy to communicate with a KS-based minidriver.

The interface plug-in provides programmatic control to get and set property values from within an application. Alternatively, if your goal is to enable users to manipulate properties through a user interface, a property page makes more sense. Both mechanisms require that you update the registry.

[Registering KS Proxy Plug-ins](registering-ks-proxy-plug-ins.md)

[Interface Handler Plug-in](interface-handler-plug-in.md)

[Property Page Plug-in](property-page-plug-in.md)

For more information about the KS proxy COM interfaces, exported helper functions, and structures that are used by applications and plug-ins, see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877).

 

 




