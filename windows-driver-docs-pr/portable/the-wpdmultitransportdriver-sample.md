---
Description: The WpdMultiTransportDriver Sample
title: The WpdMultiTransportDriver Sample
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The WpdMultiTransportDriver Sample


This section of the WPD driver documentation describes a sample multitransport driver, WpdMultiTransportDriver, that is included in the Windows Driver Kit.

A transport is a protocol over which a portable device communicates with a computer. Example transports include Internet Protocol (IP), Bluetooth, and USB.

A number of portable devices now support multiple transports. For example, some cell phones support both Bluetooth and USB.

Before Windows 7, if a user connected a portable device that supported multiple transports to their computer, the Windows Device Manager would display a unique node for each transport–. This could potentially imply that multiple devices had been installed. To resolve this, Windows 7 supports a multitransport driver model. This model ensures that only one node appears for each multitransport capable device.

The multitransport driver stack is shown in the following image:

![the driver stack](images/multi_trans_driver_stack.png)

In the previous image, a hypothetical WPD application (*App.exe*) can move data back and forth between a cell phone that is enabled with multitransport and either a USB or a Bluetooth connection. The WPD Composite driver (*Wpdcomp.dll*) is supplied by Microsoft and is included with Windows 7. The multitransport driver (*WpdMultiTranscell.dll*) is a hypothetical vendor-supplied driver.

The previous image depicts simultaneous connections over Bluetooth and USB. Some drivers mightimplement this functionality. The WpdMultiTransportDriver supports a single (rather than a simultaneous) connection at any given point in time.

This sample driver is based on the WpdHelloWorldDriver that is included in the WDK. Before you review the topics in this section, be familiar with the [WpdHelloWorldDriver](the-sample-driver-architecture.md).

The primary differences between the WpdHelloWorldDriver and the WpdMultiTransportDriver are identified in the following table.

| Revision or change     | Description                                                                                                                                                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device Arrival         | The new multitransport driver creates a Functional Unique Identifier (FUID) for the given device, enables the multitransport option, sets the necessary Plug and Play (PnP) values, and sets the current transport bandwidth. |
| Multiple queue support | The new multitransport driver supports two I/O queues. (The WpdHelloWorldDriver supports a single queue.)                                                                                                                     |

 

To explore the capabilities of a multitransport driver and to test actual transport switching, you can install the [Media Transfer Protocol Porting Kit](https://www.microsoft.com/download/details.aspx?id=19153) and use the MTP simulator (*MtpSimUi.exe)* application. By using this application, you can install Microsoft's MTP driver, connect or disconnect from the emulated device, and switch transports.

## <span id="related_topics"></span>Related topics


[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





