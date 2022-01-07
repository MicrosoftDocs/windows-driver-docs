---
title: KS Pins
description: KS Pins
keywords:
- pins WDK kernel streaming
- KS pins WDK kernel streaming , about KS pins
- KSPIN_DESCRIPTOR
- IRP source pins WDK kernel streaming
- data source pins WDK kernel streaming
- pin connections WDK kernel streaming
- kernel streaming WDK , pins
ms.date: 04/20/2017
---

# KS Pins





The minidriver supplies a [**KSPIN\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) structure for each type of pin to be instantiated. A pin descriptor structure is known as a pin factory. Each pin factory can instantiate one or more pin instances of a particular type. A pin factory contains several arrays that describe the type of pin that this descriptor instantiates.

The minidriver specifies one or more KS categories to which pins created by this descriptor belong in the **Categories** member of KSPIN\_DESCRIPTOR. KS uses categories to connect pin instances when it builds a filter graph. The [**KSPROPERTY\_TOPOLOGY\_CATEGORIES**](./ksproperty-topology-categories.md) property queries for the array of functional categories that a driver supports.

A minidriver provides an INF file that registers one or more pin device names. At installation, the operating system loads the names and corresponding categories into the system registry. Clients can then make create-file calls with these device names to instantiate pins.

User-mode clients call the Win32 function [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) with the name of the device. For example, "*\\\\.\\filters\\audio\\default renderer*" could be a link to the audio device that has been configured for default output. Kernel-mode clients call [**ZwCreateFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntcreatefile) from kernel mode. After the create-file routine returns a file handle, KS clients communicate with pin instances through [KS Properties](ks-properties.md).

In the pin descriptor structures, the minidriver lays out arrays of [**KSPIN\_INTERFACE**](./kspin-interface-structure.md) structures and [**KSPIN\_MEDIUM**](./kspin-medium-structure.md) structures that specify the [interfaces](ks-interfaces.md) and [mediums](ks-mediums.md) supported by that pin factory. [**KSPIN\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) is also where the minidriver specifies the valid data ranges for pins created by that factory. It does this by providing a pointer to an array of [**KSDATARANGE**](/previous-versions/ff561658(v=vs.85)) structures. The minidriver also specifies the directions of data and communication flow for new pins created by this pin factory.

A minidriver enables run-time discovery of pin factories by supporting the [KSPROPSETID\_Pin](./kspropsetid-pin.md) property set.

To create a pin connection, call the [**KsCreatePin**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatepin) routine. In this call, the minidriver passes a pointer to a structure of type [**KSPIN\_CONNECT**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_connect) that describes the requested connection. When a pin is created, the filter sees the new pin as a file object subordinate to the file object for that filter.

The minidriver calls [**KsValidateConnectRequest**](/windows-hardware/drivers/ddi/ks/nf-ks-ksvalidateconnectrequest) with the descriptor structures provided in the resulting IRP\_MJ\_CREATE. This routine validates these structures and returns a pointer to the connection structure and the root file object.

Minidrivers use the **DataFlow** and **Communication** members of [**KSPIN\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) structures to define the following pin specifics:

-   **IRP source pin versus IRP sink pin**

    An *IRP source* pin issues IRPs; an *IRP sink* pin receives them. A user-mode client sends I/O requests directly to an IRP sink pin through the relevant file handle. Clients use [**KSPROPERTY\_PIN\_COMMUNICATION**](./ksproperty-pin-communication.md) to check whether data flows in or out of a pin type.

-   **Data source pin versus data sink pin**

    A *data source* pin is an output pin on a filter; a *data sink* pin is an input pin. The property of being a data source or sink is independent of being an IRP source or sink. For example, the client can connect a data source, IRP sink pin to a data sink, IRP source pin. Clients use [**KSPROPERTY\_PIN\_DATAFLOW**](./ksproperty-pin-dataflow.md) to check whether data flows in or out of a pin type.

When terminating a connection, the handle of the source pin must be closed before the underlying file object is destroyed. If the source pin relies on resources provided by the sink pin, it is the responsibility of the sink pin to notify the source when the connection is terminated.

A client interacts with a kernel streaming pin by calling the **DeviceIoControl** routine (described in the Microsoft Windows SDK documentation) with [**IRP\_MJ\_DEVICE\_CONTROL**](../kernel/irp-mj-device-control.md). The caller identifies its request by the I/O control code that it places at **Parameters.DeviceIoControl.IoControlCode** in the I/O stack location structure.

To support requests, the minidriver supplies a pointer to a [**KSDISPATCH\_TABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdispatch_table) structure in a call to [**KsAllocateObjectHeader**](/windows-hardware/drivers/ddi/ks/nf-ks-ksallocateobjectheader).

Write requests contain a pointer to an array of [**KSSTREAM\_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header) structures that in turn contain pointers to stream data. Read requests contain a pointer to an array of empty header structures where the read data should be returned.

