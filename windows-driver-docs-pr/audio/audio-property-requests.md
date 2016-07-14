---
Description: Audio Property Requests
MS-HAID: 'audio.audio\_property\_requests'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Audio Property Requests
---

# Audio Property Requests


## <span id="audio_property_requests"></span><span id="AUDIO_PROPERTY_REQUESTS"></span>


Clients of a Microsoft Windows Driver Model (WDM) audio driver can send requests for [KS properties](stream.ks_properties) to the KS filters and pins that the driver has instantiated. For example, a user-mode client can send a KS property request by calling the [**DeviceIoControl**](base.deviceiocontrol) function (see the Microsoft Windows SDK documentation) with an I/O-control code of IOCTL\_KS\_PROPERTY. This function sends an IRP containing the property request to the specified filter or pin object.

Audio drivers support get, set, and basic-support requests on properties (KSPROPERTY\_TYPE\_GET, KSPROPERTY\_TYPE\_SET, and KSPROPERTY\_TYPE\_BASICSUPPORT). For more information, see [Audio Drivers Property Sets](audio.audio_drivers_property_sets).

A client can send requests for three kinds of properties: filter properties, pin properties, and node properties. For more information, see [Filter, Pin, and Node Properties](filter--pin--and-node-properties.md).

When sending a filter-property request to a filter object, the client specifies the target filter by its instance handle (see [Filter Factories](filter-factories.md)). Similarly, when sending a pin-property request to a pin object, the target pin is specified by its instance handle (see [Pin Factories](pin-factories.md)). Either type of request contains a [**KSPROPERTY**](stream.ksproperty) structure that specifies the following:

-   A GUID that identifies the property set

-   An index that identifies a property item within the specified property set

-   Flags that indicate the type of property request (get, set, or basic-support)

Related properties are gathered together to form a property set. A particular property is identified by its property set and by an index that specifies its position within that set.

A node-property request contains a [**KSNODEPROPERTY**](audio.ksnodeproperty) structure, which combines a KSPROPERTY structure and a node ID. Depending on the node property, the target for the property request is either a filter instance or a pin instance.

If a filter can create more than one instance of a particular node type, the target for the request is specified by a pin handle. The handle identifies the pin instance at the beginning or end of the data path on which the node instance resides. In the case of a filter containing a SUM or MUX node (see [**KSNODETYPE\_SUM**](audio.ksnodetype_sum) and [**KSNODETYPE\_MUX**](audio.ksnodetype_mux)), the following rules apply:

-   If the property belongs to a node that lies downstream from a sink (input) pin and upstream from the SUM or MUX node, the property request is sent to the sink pin.

-   If the property belongs to a node that lies downstream from a SUM or MUX node and upstream from a source (output) pin, the property request is sent to the source pin. (Also, a property request for a SUM or MUX node is sent to the source pin.)

With these conventions, a particular node on a particular data path can be identified uniquely.

For information about using the mixer API to traverse the nodes in a data path, see [Kernel Streaming Topology to Audio Mixer API Translation](kernel-streaming-topology-to-audio-mixer-api-translation.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Property%20Requests%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



