---
title: KS Properties, Events, and Methods
author: windows-driver-content
description: KS Properties, Events, and Methods
ms.assetid: 933bbe81-92d8-4bcc-b935-9ae929464ca1
keywords: ["kernel streaming WDK , properties", "KS properties WDK kernel streaming", "kernel streaming WDK , events", "KS WDK , events", "kernel streaming WDK , methods", "KS WDK , methods", "properties WDK kernel streaming", "events WDK kernel streaming", "methods WDK kernel streaming", "alias structures WDK kernel streaming", "set operations WDK kernel streaming", "get operations WDK kernel streaming"]
---

# KS Properties, Events, and Methods


## <a href="" id="ddk-ks-properties-events-and-methods-ksg"></a>


Kernel streaming architecture supports interaction between minidrivers and user-mode clients through [properties](ks-properties.md), [events](ks-events.md), and [methods](ks-methods.md). Using these constructs, clients of a KS object can get and set object state, register notification callbacks for events, and execute object methods.

Clients request all three operation classes in a standardized manner. The client provides an alias structure of [**KSIDENTIFIER**](https://msdn.microsoft.com/library/windows/hardware/ff562676) in a call to **DeviceIoControl** (described in the Microsoft Windows SDK documentation) or [**KsSynchronousDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff567142).

The alias structures are [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262), [**KSEVENT**](https://msdn.microsoft.com/library/windows/hardware/ff561744), and [**KSMETHOD**](https://msdn.microsoft.com/library/windows/hardware/ff563398). All three include the following parameters:

-   **Set**

    Functionally similar operations are grouped together in a set. Each property, event, or method set is identified by a GUID. Microsoft defines GUIDs for standard technology-specific operations. Minidrivers can define their own GUIDs for custom operations.

-   **Identifier**

    Each operation is specified by an ID number within the set.

-   **Operation-specific identification data**

    Certain property requests require additional data. For example, pins on an audio device support the [KSPROPSETID\_Audio](https://msdn.microsoft.com/library/windows/hardware/ff537440) property set. An audio pin may support several different audio channels. Clients getting or setting certain KSPROPSETID\_Audio properties must specify the audio channel to which the request applies. Event and method requests do not require additional data.

Microsoft-defined set GUIDs and identifiers for general-purpose operations are located in the header *ks.h*. Standard GUIDs and identifiers for particular classes of multimedia technology are found in *ksmedia.h*.

AVStream minidrivers support properties, events, and methods by providing a pointer to a [**KSAUTOMATION\_TABLE**](https://msdn.microsoft.com/library/windows/hardware/ff560990) structure in the relevant [**KSFILTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff562553) or [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534). A KSAUTOMATION\_TABLE contains a pointer to an array of [**KSPROPERTY\_SET**](https://msdn.microsoft.com/library/windows/hardware/ff565617) objects. To learn more, see [Defining Automation Tables](defining-automation-tables.md).

These sections contain information about how minidrivers support the three operation classes:

[KS Properties](ks-properties.md)

[KS Events](ks-events.md)

[KS Methods](ks-methods.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KS%20Properties,%20Events,%20and%20Methods%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


