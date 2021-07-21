---
title: KS Properties, Events, and Methods
description: KS Properties, Events, and Methods
keywords:
- kernel streaming WDK , properties
- KS properties WDK kernel streaming
- kernel streaming WDK , events
- KS WDK , events
- kernel streaming WDK , methods
- KS WDK , methods
- properties WDK kernel streaming
- events WDK kernel streaming
- methods WDK kernel streaming
- alias structures WDK kernel streaming
- set operations WDK kernel streaming
- get operations WDK kernel streaming
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KS Properties, Events, and Methods





Kernel streaming architecture supports interaction between minidrivers and user-mode clients through [properties](ks-properties.md), [events](ks-events.md), and [methods](ks-methods.md). Using these constructs, clients of a KS object can get and set object state, register notification callbacks for events, and execute object methods.

Clients request all three operation classes in a standardized manner. The client provides an alias structure of [**KSIDENTIFIER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier) in a call to **DeviceIoControl** (described in the Microsoft Windows SDK documentation) or [**KsSynchronousDeviceControl**](/windows-hardware/drivers/ddi/ksproxy/nf-ksproxy-kssynchronousdevicecontrol).

The alias structures are [**KSPROPERTY**](ksproperty-structure.md), [**KSEVENT**](/windows-hardware/drivers/stream/ksevent-structure), and [**KSMETHOD**](/windows-hardware/drivers/stream/ksmethod-structure). All three include the following parameters:

-   **Set**

    Functionally similar operations are grouped together in a set. Each property, event, or method set is identified by a GUID. Microsoft defines GUIDs for standard technology-specific operations. Minidrivers can define their own GUIDs for custom operations.

-   **Identifier**

    Each operation is specified by an ID number within the set.

-   **Operation-specific identification data**

    Certain property requests require additional data. For example, pins on an audio device support the [KSPROPSETID\_Audio](../audio/kspropsetid-audio.md) property set. An audio pin may support several different audio channels. Clients getting or setting certain KSPROPSETID\_Audio properties must specify the audio channel to which the request applies. Event and method requests do not require additional data.

Microsoft-defined set GUIDs and identifiers for general-purpose operations are located in the header *ks.h*. Standard GUIDs and identifiers for particular classes of multimedia technology are found in *ksmedia.h*.

AVStream minidrivers support properties, events, and methods by providing a pointer to a [**KSAUTOMATION\_TABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksautomation_table_) structure in the relevant [**KSFILTER\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter_descriptor) or [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex). A KSAUTOMATION\_TABLE contains a pointer to an array of [**KSPROPERTY\_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_set) objects. To learn more, see [Defining Automation Tables](defining-automation-tables.md).

These sections contain information about how minidrivers support the three operation classes:

[KS Properties](ks-properties.md)

[KS Events](ks-events.md)

[KS Methods](ks-methods.md)

 

