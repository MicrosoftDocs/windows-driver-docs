---
title: Audio Property Requests
description: Audio Property Requests
ms.assetid: dcfd139c-fca3-4068-8324-aa2c952dbc1f
keywords:
- audio properties WDK , requests
- WDM audio properties WDK , requests
- filters WDK audio , property requests
- nodes WDK audio , property requests
- pins WDK audio , property requests
- KS filters WDK audio , property requests
- overspecified requests WDK audio
- underspecified requests WDK audio
- filters WDK audio , descriptors
- property requests WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Audio Property Requests


## <span id="audio_property_requests"></span><span id="AUDIO_PROPERTY_REQUESTS"></span>


Clients of a Microsoft Windows Driver Model (WDM) audio driver can send requests for [KS properties](https://msdn.microsoft.com/library/windows/hardware/ff567671) to the KS filters and pins that the driver has instantiated. For example, a user-mode client can send a KS property request by calling the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function (see the Microsoft Windows SDK documentation) with an I/O-control code of IOCTL\_KS\_PROPERTY. This function sends an IRP containing the property request to the specified filter or pin object.

Audio drivers support get, set, and basic-support requests on properties (KSPROPERTY\_TYPE\_GET, KSPROPERTY\_TYPE\_SET, and KSPROPERTY\_TYPE\_BASICSUPPORT). For more information, see [Audio Drivers Property Sets](https://msdn.microsoft.com/library/windows/hardware/ff536197).

A client can send requests for three kinds of properties: filter properties, pin properties, and node properties. For more information, see [Filter, Pin, and Node Properties](filter--pin--and-node-properties.md).

When sending a filter-property request to a filter object, the client specifies the target filter by its instance handle (see [Filter Factories](filter-factories.md)). Similarly, when sending a pin-property request to a pin object, the target pin is specified by its instance handle (see [Pin Factories](pin-factories.md)). Either type of request contains a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure that specifies the following:

-   A GUID that identifies the property set

-   An index that identifies a property item within the specified property set

-   Flags that indicate the type of property request (get, set, or basic-support)

Related properties are gathered together to form a property set. A particular property is identified by its property set and by an index that specifies its position within that set.

A node-property request contains a [**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143) structure, which combines a KSPROPERTY structure and a node ID. Depending on the node property, the target for the property request is either a filter instance or a pin instance.

If a filter can create more than one instance of a particular node type, the target for the request is specified by a pin handle. The handle identifies the pin instance at the beginning or end of the data path on which the node instance resides. In the case of a filter containing a SUM or MUX node (see [**KSNODETYPE\_SUM**](https://msdn.microsoft.com/library/windows/hardware/ff537196) and [**KSNODETYPE\_MUX**](https://msdn.microsoft.com/library/windows/hardware/ff537180)), the following rules apply:

-   If the property belongs to a node that lies downstream from a sink (input) pin and upstream from the SUM or MUX node, the property request is sent to the sink pin.

-   If the property belongs to a node that lies downstream from a SUM or MUX node and upstream from a source (output) pin, the property request is sent to the source pin. (Also, a property request for a SUM or MUX node is sent to the source pin.)

With these conventions, a particular node on a particular data path can be identified uniquely.

For information about using the mixer API to traverse the nodes in a data path, see [Kernel Streaming Topology to Audio Mixer API Translation](kernel-streaming-topology-to-audio-mixer-api-translation.md).

 

 




