---
Description: Service Sink and Service Group Objects
MS-HAID: 'audio.service\_sink\_and\_service\_group\_objects'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Service Sink and Service Group Objects
---

# Service Sink and Service Group Objects


## <span id="service_sink_and_service_group_objects"></span><span id="SERVICE_SINK_AND_SERVICE_GROUP_OBJECTS"></span>


The PortCls system driver implements the [IServiceSink](audio.iservicesink) and [IServiceGroup](audio.iservicegroup) interfaces for the benefit of port and miniport drivers. The port driver uses these interfaces to distribute interrupt notifications to its own service routines, and a miniport driver has the option of using these interfaces for similar purposes. An IServiceSink object encapsulates a service routine, and an IServiceGroup object represents a group of IServiceSink objects. When a service group receives a service request, it distributes the request to each of its service sinks.

[IServiceGroup](audio.iservicegroup) inherits from [IServiceSink](audio.iservicesink). Because a service group is also a service sink, a service group is capable of containing other service groups, although audio drivers typically make no use of this capability. Port drivers currently use service groups to demultiplex requests for interrupt service, although the functionality of a service group is general enough to make it potentially useful for other purposes as well.

The miniport driver's interrupt service routine (ISR) calls one of the following notification methods in the port driver:

[**IPortDMus::Notify**](audio.iportdmus_notify)

[**IPortMidi::Notify**](audio.iportmidi_notify)

[**IPortWaveCyclic::Notify**](audio.iportwavecyclic_notify)

[**IPortWavePci::Notify**](audio.iportwavepci_notify)

The notification method takes a pointer to the service group as a call parameter. During this call, the port driver calls the service group's [**IServiceSink::RequestService**](audio.iservicesink_requestservice) method, which queues a deferred procedure call (DPC). When the DPC executes, it forwards the service request to all member objects in the service group.

The miniport-driver code typically does not need to call any [IServiceGroup](audio.iservicegroup) interface methods. However, the port driver calls these methods to add its own [IServiceSink](audio.iservicesink) objects to the service groups that it obtains from the miniport driver. Miniport drivers create service group objects as required and associate those service groups with miniport and stream objects that require periodic servicing. For example, a WaveCyclic miniport driver associates a stream object with the service group that it specifies as an output parameter to the [**IMiniportWaveCyclic::NewStream**](audio.iminiportwavecyclic_newstream) method.

In the context of WaveCyclic miniport drivers, associating all streams with one service group causes the port driver to service all streams based on a single notification. Associating each stream with its own service group allows the interrupt service routine to select the stream that will be serviced by the port driver during the execution of the DPC.

A miniport driver outputs a reference to its service group when the port driver calls one of the following initialization methods:

[**IMiniportDMus::Init**](audio.iminiportdmus_init)

[**IMiniportMidi::Init**](audio.iminiportmidi_init)

[**IMiniportWavePci::Init**](audio.iminiportwavepci_init)

The port driver adds its own [IServiceSink](audio.iservicesink) object to the service group that it obtains from the **Init** call. When the miniport driver's ISR later calls **Notify** to send notification to that service group, the service group queues a DPC that forwards notification to the port driver's IServiceSink object, which in turn forwards notification to the miniport driver by calling one of the following service methods:

[**IMiniportDMus::Service**](audio.iminiportdmus_service) (not used)

[**IMiniportMidi::Service**](audio.iminiportmidi_service)

[**IMiniportWavePci::Service**](audio.iminiportwavepci_service)

A miniport driver also outputs a reference to its service group when the port driver calls one of the following stream-creation methods:

[**IMiniportDMus::NewStream**](audio.iminiportdmus_newstream)

[**IMiniportMidi::NewStream**](audio.iminiportmidi_newstream)

[**IMiniportWaveCyclic::NewStream**](audio.iminiportwavecyclic_newstream)

[**IMiniportWavePci::NewStream**](audio.iminiportwavepci_newstream)

As discussed previously, the miniport driver has the option of creating a different service group for each stream or sharing a single service group across all streams.

The following methods help MIDI and DMus port drivers avoid dropping hardware interrupts:

[**IPortMidi::RegisterServiceGroup**](audio.iportmidi_registerservicegroup)

[**IPortDMus::RegisterServiceGroup**](audio.iportdmus_registerservicegroup)

During execution of its **Init** method, a MIDI or DMus miniport driver typically calls the port driver's **RegisterServiceGroup** method before starting up the synthesizer. The purpose for this call is to allow the port driver to insert its service sink object (containing its interrupt handler) into the service group before the hardware begins generating interrupts. Although the **Init** method outputs a service group pointer to the port driver, the port driver can make use of this pointer only after the return from **Init**.

In the case of a WavePci port driver, the port object adds its own [IServiceSink](audio.iservicesink) object to the service group that it obtains from the [**IMiniportWavePci::NewStream**](audio.iminiportwavepci_newstream) call. When the miniport driver's ISR later calls **Notify** to send notification to that service group, the service group queues a DPC that forwards the notification to the port driver's IServiceSink object, which in turn does the following:

-   Forwards notification to the miniport stream by calling the service method [**IMiniportWavePciStream::Service**](audio.iminiportwavepcistream_service).

-   Triggers any position and/or clock events on the pin that are ready to fire.

The [IServiceSink](audio.iservicesink) interface supports a single method:

[**IServiceSink::RequestService**](audio.iservicesink_requestservice)

The [IServiceGroup](audio.iservicegroup) interface supports the following methods:

[**IServiceGroup::AddMember**](audio.iservicegroup_addmember)

[**IServiceGroup::CancelDelayedService**](audio.iservicegroup_canceldelayedservice)

[**IServiceGroup::RequestDelayedService**](audio.iservicegroup_requestdelayedservice)

[**IServiceGroup::RemoveMember**](audio.iservicegroup_removemember)

[**IServiceGroup::SupportDelayedService**](audio.iservicegroup_supportdelayedservice)

In addition, the PortCls system driver provides a [**PcNewServiceGroup**](audio.pcnewservicegroup) function for creating a new service group object. However, no similar function exists for creating a service sink object. The port driver simply adds an [IServiceSink](audio.iservicesink) interface to the implementation of its main port object--when the object is created, so is the service sink. The port driver can add the port object's IServiceSink interface to the service group that it receives from the miniport driver's **Init** or **NewStream** method. For convenience, header file Portcls.h defines **IMP\_IServiceSink** and **IMP\_IServiceGroup** constants for adding IServiceSink and [IServiceGroup](audio.iservicegroup) interfaces to driver objects.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Service%20Sink%20and%20Service%20Group%20Objects%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



