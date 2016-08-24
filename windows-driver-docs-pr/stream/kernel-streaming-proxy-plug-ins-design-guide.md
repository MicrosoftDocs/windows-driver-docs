---
title: Kernel Streaming Proxy Plug-ins Design Guide
author: windows-driver-content
description: Kernel Streaming Proxy Plug-ins Design Guide
MS-HAID:
- 'ksproxy\_dg\_716b697a-a5b5-4509-9727-c83ecb1b09b6.xml'
- 'stream.kernel\_streaming\_proxy\_plug\_ins\_design\_guide'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9a2b83ab-f54c-421b-bc9b-7dad63cd8cb5
keywords: ["Kernel Streaming Proxy WDK AVStream , plug-ins"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Kernel%20Streaming%20Proxy%20Plug-ins%20Design%20Guide%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


