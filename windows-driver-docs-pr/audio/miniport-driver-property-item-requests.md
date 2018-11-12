---
title: Miniport Driver Property Item Requests
description: Miniport Driver Property Item Requests
ms.assetid: 37baad27-539b-46ab-b300-175bc0c2b992
keywords:
- property item requests WDK DirectMusic
- miniport drivers WDK audio , property item requests
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Miniport Driver Property Item Requests


## <span id="miniport_driver_property_item_requests"></span><span id="MINIPORT_DRIVER_PROPERTY_ITEM_REQUESTS"></span>


This section is a brief introduction to DirectMusic property item requests. A complete overview of this and other kernel-streaming concepts can be found in [Kernel Streaming](https://msdn.microsoft.com/library/windows/hardware/ff560842).

DirectMusic miniport drivers must handle [audio drivers property sets](https://msdn.microsoft.com/library/windows/hardware/ff536197). A property request comes in two parts. The first part is the property set that is defined by the [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure. The second is a data buffer that contains instance data that is specific to the property item.

The KSPROPERTY structure contains the following:

-   A predefined GUID specifying the set (such as [KSPROPSETID\_Synth\_Dls](https://msdn.microsoft.com/library/windows/hardware/ff537488)).

-   An item ID specifying the property item within the set (such as [**KSPROPERTY\_SYNTH\_DLS\_DOWNLOAD**](https://msdn.microsoft.com/library/windows/hardware/ff537396)).

-   Flags specifying the requested operation.

The **Flags** member of KSPROPERTY may contain exactly one of the following flags to specify the operation requested of the miniport driver:

<span id="KSPROPERTY_TYPE_GET"></span><span id="ksproperty_type_get"></span>KSPROPERTY\_TYPE\_GET  
To retrieve the given property item's value.

<span id="KSPROPERTY_TYPE_SET"></span><span id="ksproperty_type_set"></span>KSPROPERTY\_TYPE\_SET  
To set the given property item's value.

<span id="KSPROPERTY_TYPE_BASICSUPPORT"></span><span id="ksproperty_type_basicsupport"></span>KSPROPERTY\_TYPE\_BASICSUPPORT  
To determine the type of support available for the property set. The data returned in *\*pvPropertyData* is a DWORD containing one or both of KSPROPERTY\_TYPE\_GET and KSPROPERTY\_TYPE\_SET, indicating which operations are possible.

The second part of the property item request is the instance data, which is a buffer that can be used to pass data to or from the miniport driver. How this buffer is used is dependent on whether the request is a SET or a GET:

-   If the request is a KSPROPERTY\_TYPE\_SET, the instance data is sent to the miniport driver but is not returned to the requester.

-   If the request is a KSPROPERTY\_TYPE\_GET, the instance data is filled out in the miniport driver and returned to the requester.

A property item request can be directed to a particular node in the miniport driver topology. The miniport driver topology describes the layout of the driver and the underlying hardware. Within the topology can be nodes where property items can be sent, whether there are pin instances available at the time of the request.

A pin instance must be created for DirectMusic playback. DirectMusic data is sent to the node of type [**KSNODETYPE\_DMSYNTH**](https://msdn.microsoft.com/library/windows/hardware/ff537167). The following is an example of a miniport driver connection:

-   Connect stream in to synth:

    PCFILTER\_NODE Pin 0 (out) -&gt; Node 0 Pin 1 (in)

-   Connect synth to audio out:

    Node 0 Pin 0 (out) -&gt; PCFILTER\_NODE Pin 1 (in)

The supported data formats are a data range that specifies what format a pin can receive data in.

The DirectMusic format (STATIC\_KSDATAFORMAT\_SUBTYPE\_DIRECTMUSIC) must be defined in the miniport driver's topology so that DirectMusic can send its data to the miniport driver. This format is defined by the DMUS\_EVENTHEADER structure (see the Microsoft Windows SDK documentation) in dmusbuff.h. When the miniport driver specifies that it supports this particular data range, DirectMusic can expose that data range to the user (through a pin on the port itself).

 

 




