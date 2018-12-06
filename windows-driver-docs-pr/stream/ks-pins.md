---
title: KS Pins
description: KS Pins
ms.assetid: 04d0d17b-c326-417d-b2e8-58b33420455a
keywords:
- pins WDK kernel streaming
- KS pins WDK kernel streaming , about KS pins
- KSPIN_DESCRIPTOR
- IRP source pins WDK kernel streaming
- data source pins WDK kernel streaming
- pin connections WDK kernel streaming
- kernel streaming WDK , pins
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KS Pins





The minidriver supplies a [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structure for each type of pin to be instantiated. A pin descriptor structure is known as a pin factory. Each pin factory can instantiate one or more pin instances of a particular type. A pin factory contains several arrays that describe the type of pin that this descriptor instantiates.

The minidriver specifies one or more KS categories to which pins created by this descriptor belong in the **Categories** member of KSPIN\_DESCRIPTOR. KS uses categories to connect pin instances when it builds a filter graph. The [**KSPROPERTY\_TOPOLOGY\_CATEGORIES**](https://msdn.microsoft.com/library/windows/hardware/ff565799) property queries for the array of functional categories that a driver supports.

A minidriver provides an INF file that registers one or more pin device names. At installation, the operating system loads the names and corresponding categories into the system registry. Clients can then make create-file calls with these device names to instantiate pins.

User-mode clients call the Win32 function [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) with the name of the device. For example, "*\\\\.\\filters\\audio\\default renderer*" could be a link to the audio device that has been configured for default output. Kernel-mode clients call [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424) from kernel mode. After the create-file routine returns a file handle, KS clients communicate with pin instances through [KS Properties](ks-properties.md).

In the pin descriptor structures, the minidriver lays out arrays of [**KSPIN\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff563537) structures and [**KSPIN\_MEDIUM**](https://msdn.microsoft.com/library/windows/hardware/ff563538) structures that specify the [interfaces](ks-interfaces.md) and [mediums](ks-mediums.md) supported by that pin factory. [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) is also where the minidriver specifies the valid data ranges for pins created by that factory. It does this by providing a pointer to an array of [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures. The minidriver also specifies the directions of data and communication flow for new pins created by this pin factory.

A minidriver enables run-time discovery of pin factories by supporting the [KSPROPSETID\_Pin](https://msdn.microsoft.com/library/windows/hardware/ff566584) property set.

To create a pin connection, call the [**KsCreatePin**](https://msdn.microsoft.com/library/windows/hardware/ff561652) routine. In this call, the minidriver passes a pointer to a structure of type [**KSPIN\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff563531) that describes the requested connection. When a pin is created, the filter sees the new pin as a file object subordinate to the file object for that filter.

The minidriver calls [**KsValidateConnectRequest**](https://msdn.microsoft.com/library/windows/hardware/ff567227) with the descriptor structures provided in the resulting IRP\_MJ\_CREATE. This routine validates these structures and returns a pointer to the connection structure and the root file object.

Minidrivers use the **DataFlow** and **Communication** members of [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structures to define the following pin specifics:

-   **IRP source pin versus IRP sink pin**

    An *IRP source* pin issues IRPs; an *IRP sink* pin receives them. A user-mode client sends I/O requests directly to an IRP sink pin through the relevant file handle. Clients use [**KSPROPERTY\_PIN\_COMMUNICATION**](https://msdn.microsoft.com/library/windows/hardware/ff565194) to check whether data flows in or out of a pin type.

-   **Data source pin versus data sink pin**

    A *data source* pin is an output pin on a filter; a *data sink* pin is an input pin. The property of being a data source or sink is independent of being an IRP source or sink. For example, the client can connect a data source, IRP sink pin to a data sink, IRP source pin. Clients use [**KSPROPERTY\_PIN\_DATAFLOW**](https://msdn.microsoft.com/library/windows/hardware/ff565197) to check whether data flows in or out of a pin type.

When terminating a connection, the handle of the source pin must be closed before the underlying file object is destroyed. If the source pin relies on resources provided by the sink pin, it is the responsibility of the sink pin to notify the source when the connection is terminated.

A client interacts with a kernel streaming pin by calling the **DeviceIoControl** routine (described in the Microsoft Windows SDK documentation) with [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744). The caller identifies its request by the I/O control code that it places at **Parameters.DeviceIoControl.IoControlCode** in the I/O stack location structure.

To support requests, the minidriver supplies a pointer to a [**KSDISPATCH\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff561723) structure in a call to [**KsAllocateObjectHeader**](https://msdn.microsoft.com/library/windows/hardware/ff560972).

Write requests contain a pointer to an array of [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structures that in turn contain pointers to stream data. Read requests contain a pointer to an array of empty header structures where the read data should be returned.

 

 




