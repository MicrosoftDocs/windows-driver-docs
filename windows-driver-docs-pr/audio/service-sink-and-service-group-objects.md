---
title: Service Sink and Service Group Objects
description: Service Sink and Service Group Objects
keywords:
- helper objects WDK audio , service sink objects
- helper objects WDK audio , service group objects
- service sink objects WDK audio
- service group objects WDK audio
- IServiceSink interface
- IServiceGroup interface
- distributing interrupt notifications WDK audio
- notifications WDK audio
- interrupt notifications WDK audio
- interrupt service routines WDK audio
- ISRs WDK audio
ms.date: 04/20/2017
---

# Service Sink and Service Group Objects


## <span id="service_sink_and_service_group_objects"></span><span id="SERVICE_SINK_AND_SERVICE_GROUP_OBJECTS"></span>


The PortCls system driver implements the [IServiceSink](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicesink) and [IServiceGroup](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicegroup) interfaces for the benefit of port and miniport drivers. The port driver uses these interfaces to distribute interrupt notifications to its own service routines, and a miniport driver has the option of using these interfaces for similar purposes. An IServiceSink object encapsulates a service routine, and an IServiceGroup object represents a group of IServiceSink objects. When a service group receives a service request, it distributes the request to each of its service sinks.

[IServiceGroup](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicegroup) inherits from [IServiceSink](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicesink). Because a service group is also a service sink, a service group is capable of containing other service groups, although audio drivers typically make no use of this capability. Port drivers currently use service groups to demultiplex requests for interrupt service, although the functionality of a service group is general enough to make it potentially useful for other purposes as well.

The miniport driver's interrupt service routine (ISR) calls one of the following notification methods in the port driver:

[**IPortDMus::Notify**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iportdmus-notify)

[**IPortMidi::Notify**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportmidi-notify)

[**IPortWaveCyclic::Notify**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportwavecyclic-notify)

[**IPortWavePci::Notify**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportwavepci-notify)

The notification method takes a pointer to the service group as a call parameter. During this call, the port driver calls the service group's [**IServiceSink::RequestService**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iservicesink-requestservice) method, which queues a deferred procedure call (DPC). When the DPC executes, it forwards the service request to all member objects in the service group.

The miniport-driver code typically does not need to call any [IServiceGroup](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicegroup) interface methods. However, the port driver calls these methods to add its own [IServiceSink](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicesink) objects to the service groups that it obtains from the miniport driver. Miniport drivers create service group objects as required and associate those service groups with miniport and stream objects that require periodic servicing. For example, a WaveCyclic miniport driver associates a stream object with the service group that it specifies as an output parameter to the [**IMiniportWaveCyclic::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavecyclic-newstream) method.

In the context of WaveCyclic miniport drivers, associating all streams with one service group causes the port driver to service all streams based on a single notification. Associating each stream with its own service group allows the interrupt service routine to select the stream that will be serviced by the port driver during the execution of the DPC.

A miniport driver outputs a reference to its service group when the port driver calls one of the following initialization methods:

[**IMiniportDMus::Init**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iminiportdmus-init)

[**IMiniportMidi::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidi-init)

[**IMiniportWavePci::Init**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-init)

The port driver adds its own [IServiceSink](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicesink) object to the service group that it obtains from the **Init** call. When the miniport driver's ISR later calls **Notify** to send notification to that service group, the service group queues a DPC that forwards notification to the port driver's IServiceSink object, which in turn forwards notification to the miniport driver by calling one of the following service methods:

[**IMiniportDMus::Service**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iminiportdmus-service) (not used)

[**IMiniportMidi::Service**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidi-service)

[**IMiniportWavePci::Service**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-service)

A miniport driver also outputs a reference to its service group when the port driver calls one of the following stream-creation methods:

[**IMiniportDMus::NewStream**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iminiportdmus-newstream)

[**IMiniportMidi::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidi-newstream)

[**IMiniportWaveCyclic::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavecyclic-newstream)

[**IMiniportWavePci::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-newstream)

As discussed previously, the miniport driver has the option of creating a different service group for each stream or sharing a single service group across all streams.

The following methods help MIDI and DMus port drivers avoid dropping hardware interrupts:

[**IPortMidi::RegisterServiceGroup**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportmidi-registerservicegroup)

[**IPortDMus::RegisterServiceGroup**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iportdmus-registerservicegroup)

During execution of its **Init** method, a MIDI or DMus miniport driver typically calls the port driver's **RegisterServiceGroup** method before starting up the synthesizer. The purpose for this call is to allow the port driver to insert its service sink object (containing its interrupt handler) into the service group before the hardware begins generating interrupts. Although the **Init** method outputs a service group pointer to the port driver, the port driver can make use of this pointer only after the return from **Init**.

In the case of a WavePci port driver, the port object adds its own [IServiceSink](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicesink) object to the service group that it obtains from the [**IMiniportWavePci::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-newstream) call. When the miniport driver's ISR later calls **Notify** to send notification to that service group, the service group queues a DPC that forwards the notification to the port driver's IServiceSink object, which in turn does the following:

-   Forwards notification to the miniport stream by calling the service method [**IMiniportWavePciStream::Service**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepcistream-service).

-   Triggers any position and/or clock events on the pin that are ready to fire.

The [IServiceSink](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicesink) interface supports a single method:

[**IServiceSink::RequestService**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iservicesink-requestservice)

The [IServiceGroup](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicegroup) interface supports the following methods:

[**IServiceGroup::AddMember**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iservicegroup-addmember)

[**IServiceGroup::CancelDelayedService**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iservicegroup-canceldelayedservice)

[**IServiceGroup::RequestDelayedService**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iservicegroup-requestdelayedservice)

[**IServiceGroup::RemoveMember**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iservicegroup-removemember)

[**IServiceGroup::SupportDelayedService**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iservicegroup-supportdelayedservice)

In addition, the PortCls system driver provides a [**PcNewServiceGroup**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewservicegroup) function for creating a new service group object. However, no similar function exists for creating a service sink object. The port driver simply adds an [IServiceSink](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicesink) interface to the implementation of its main port object--when the object is created, so is the service sink. The port driver can add the port object's IServiceSink interface to the service group that it receives from the miniport driver's **Init** or **NewStream** method. For convenience, header file Portcls.h defines **IMP\_IServiceSink** and **IMP\_IServiceGroup** constants for adding IServiceSink and [IServiceGroup](/windows-hardware/drivers/ddi/portcls/nn-portcls-iservicegroup) interfaces to driver objects.

 

