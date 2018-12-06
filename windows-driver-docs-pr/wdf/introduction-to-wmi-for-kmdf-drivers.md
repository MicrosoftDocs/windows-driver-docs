---
title: Introduction to WMI for KMDF Drivers
description: Introduction to WMI for KMDF Drivers
ms.assetid: e919f6c9-a4c5-4972-91e7-f4fa609455fe
keywords:
- WMI WDK KMDF
- WMI WDK KMDF , about WMI for framework-based drivers
- callback functions WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
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

-   [MOF Syntax for WMI Data and Event Blocks](https://msdn.microsoft.com/library/windows/hardware/ff556400)

-   [Designing WMI Data and Event Blocks](https://msdn.microsoft.com/library/windows/hardware/ff543036)

-   [Publishing a WMI Schema](https://msdn.microsoft.com/library/windows/hardware/ff559963)

-   [WMI Property Sheets](https://msdn.microsoft.com/library/windows/hardware/ff566368)

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

 

 





