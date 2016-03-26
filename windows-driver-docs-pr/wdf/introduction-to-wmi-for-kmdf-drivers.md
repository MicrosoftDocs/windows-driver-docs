---
title: Introduction to WMI for KMDF Drivers
description: Introduction to WMI for KMDF Drivers
ms.assetid: e919f6c9-a4c5-4972-91e7-f4fa609455fe
keywords: ["WMI WDK KMDF", "WMI WDK KMDF , about WMI for framework-based drivers", "callback functions WDK KMDF"]
---

# Introduction to WMI for KMDF Drivers


\[Applies to KMDF only\]

Kernel-Mode Driver Framework supports drivers that provide information to [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff548187) (WMI). Such drivers are called *WMI data providers* because they provide data to *WMI clients*, which are applications that have registered to receive information from WMI.

WMI data providers support *WMI data blocks*, which can represent one or more of the following:

-   *Data items*, which contain device-specific data that a driver sends to, or receives from, a WMI client.

-   *Methods* (functions) that the driver executes on behalf of a WMI client.

-   *Events* that the driver sends to WMI clients that have registered to receive notification of device-specific events.

WMI data blocks are specified as *WMI classes* in .mof files. Each WMI data block is identified by a GUID.

All drivers must support any standard WMI data blocks that WMI defines for their device class. These WMI data blocks are defined in *Wmicore.mof*.

Your driver can also support WMI data blocks that you define in a .mof file. To learn how to define and publish customized WMI data blocks, see the following sections:

[MOF Syntax for WMI Data and Event Blocks](https://msdn.microsoft.com/library/windows/hardware/ff556400)

[Designing WMI Data and Event Blocks](https://msdn.microsoft.com/library/windows/hardware/ff543036)

[Publishing a WMI Schema](https://msdn.microsoft.com/library/windows/hardware/ff559963)

[WMI Property Sheets](https://msdn.microsoft.com/library/windows/hardware/ff566368)

### Framework WMI Objects and Callback Functions

The framework defines two objects that drivers can use to implement WMI data providers. The *WMI provider object* represents the schema for WMI data blocks that the driver provides. The *WMI instance object* represents an instance of a data block that is associated with a particular provider. Drivers communicate with WMI clients by implementing the following event callback functions that these two objects define:

<a href="" id="evtwmiproviderfunctioncontrol"></a>[*EvtWmiProviderFunctionControl*](https://msdn.microsoft.com/library/windows/hardware/ff541855)  
Enables and disables the driver's support for collecting WMI data and sending WMI events.

<a href="" id="evtwmiinstancequeryinstance"></a>[*EvtWmiInstanceQueryInstance*](https://msdn.microsoft.com/library/windows/hardware/ff541843)  
Delivers a WMI provider's instance data to a WMI client.

<a href="" id="evtwmiinstancesetinstance-and-evtwmiinstancesetitem"></a>[*EvtWmiInstanceSetInstance*](https://msdn.microsoft.com/library/windows/hardware/ff541847) and [*EvtWmiInstanceSetItem*](https://msdn.microsoft.com/library/windows/hardware/ff541852)  
Set information in a driver's data block to client-supplied values.

<a href="" id="evtwmiinstanceexecutemethod"></a>[*EvtWmiInstanceExecuteMethod*](https://msdn.microsoft.com/library/windows/hardware/ff541836)  
Executes a driver-supplied method, at the request of a client.

### Sample Drivers that Implement WMI

The FIREFLY, PCIDRV, and Toaster [sample drivers](sample-kmdf-drivers.md) are WMI data providers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Introduction%20to%20WMI%20for%20KMDF%20Drivers%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




