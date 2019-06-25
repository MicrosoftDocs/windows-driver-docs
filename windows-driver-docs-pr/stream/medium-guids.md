---
title: Medium GUIDs
description: Medium GUIDs
ms.assetid: 4209952c-0ba5-4359-b612-91529a0a46f1
keywords:
- video capture WDK AVStream , mediums
- capturing video WDK AVStream , mediums
- mediums WDK video capture
- pin connections WDK video capture
- GUIDs WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Medium GUIDs


Minidrivers must be able to support multiple devices. In addition, because the TV/radio tuner, TV audio, crossbar, and video capture components are separated into different kernel streaming filters, a method is necessary to correctly describe the topological hardware connections between these components on the device, as well as on multiple devices. For example, two built but not running filter graphs that support FM radio and TV capture must be able to coexist. Minidrivers use mediums to address these scenarios. Also, filter graph building applications, such as *Graph Edit*, use mediums during filter graph construction to ensure that filters for one device connect correctly to filters of another device. For example, the tuner filter of one device should not connect to the crossbar filter of another device.

A minidriver describes mediums with the [**KSPIN\_MEDIUM**](https://docs.microsoft.com/previous-versions/ff563538(v=vs.85)) structure that consists of a GUID data type member (**Set**) followed by two ULONG members (**Id** and **Flags**):

-   The **Set** member should be assigned the GUID representing the topological hardware connection.

-   The minidriver must set the **Id** member to a unique value for the device instance.

-   The **Flags** member is reserved for system use and should be set to zero.

To ensure proper construction of filter graphs with multiple devices present in the system, the **Set** member of the KSPIN\_MEDIUM structure remains the same for each device instance. However, the minidriver must assign a unique value to the **Id** member of the KSPIN\_MEDIUM structure per device instance. Failure to set the **Id** member to a unique value causes problems when multiple devices are present in the system. If two devices are installed in the system, then the minidriver must set the **Id** member to a different value for each device instance. Note that the **Id** member for filters of devices that reside on the same piece of hardware, such as tuners and crossbars, must be the same. One technique to ensure that the **Id** member differs between device instances is to have a global counter in the minidriver and increment that counter during device Plug and Play start time, before setting **Id** to its value.

Depending on the kernel streaming interface that the minidriver follows (AVStream or the Stream class), the minidriver must specify the value of the **Id** member differently:

-   Stream class minidrivers specify the value when processing [**SRB\_GET\_STREAM\_INFO**](https://docs.microsoft.com/windows-hardware/drivers/stream/srb-get-stream-info).

-   AVStream minidrivers specify the value in the [**KSPIN\_DESCRIPTOR\_EX**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-_kspin_descriptor_ex) structure. There are two separate ways for AVStream minidrivers to specify the value in the KSPIN\_DESCRIPTOR\_EX structure:

    1.  Provide static descriptors with a global **Id** counter and call [**\_KsEdit**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/nf-ks-_ksedit) during *Add* or *Start* dispatch handlers to change the **Id** member to a unique value.
    2.  Call [**KsCreateFilterFactory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/nf-ks-kscreatefilterfactory) to dynamically build the filter/pin descriptors during *Add* or *Start* dispatch handlers.

Minidrivers must also call a special function to register themselves with Microsoft DirectShow to allow applications to automatically construct filter graphs with TV/radio tuner, TV audio, and crossbar filters because they do not actually create kernel-streaming pins for their inputs and outputs. When the minidriver registers these filters, it should set the **Id** member of the KSPIN\_MEDIUM structure to a unique value. If the minidriver does not set the **Id** member of the KSPIN\_MEDIUM structure to a unique value, then automatic graph building applications can fail to load the necessary adjacent filters. However, manual filter-graph building, in Graph Edit for example, may still work.

To register a minidriver with DirectShow:

-   Stream class minidrivers call the [**StreamClassRegisterFilterWithNoKSPins**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/strmini/nf-strmini-streamclassregisterfilterwithnokspins) function to register the filter with DirectShow.

-   AVStream minidrivers call the [**KsRegisterFilterWithNoKSPins**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/nf-ks-ksregisterfilterwithnokspins) function to register the filter with DirectShow.

-   Alternately, if the minidriver follows the BDA model, and multiple instances of a particular [**KSFILTER\_DESCRIPTOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-_ksfilter_descriptor) structure under a specific [**KSDEVICE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-_ksdevice) structure are registered in the same kernel streaming category, call the [**KsFilterFactoryUpdateCacheData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/nf-ks-ksfilterfactoryupdatecachedata) (or [**BdaFilterFactoryUpdateCacheData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/bdasup/nf-bdasup-bdafilterfactoryupdatecachedata)) functions to register the filter with DirectShow.

The KSPIN\_MEDIUM structure returned from either SRB\_GET\_STREAM\_INFO (for a Stream class minidriver), or KSPIN\_DESCRIPTOR\_EX (for an AVStream minidriver) must match the KSPIN\_MEDIUM member returned in the following properties:

-   The **Medium** member of the [**KSPROPERTY\_CROSSBAR\_PININFO\_S**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_crossbar_pininfo_s) structure of [**KSPROPERTY\_CROSSBAR\_PININFO**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-crossbar-pininfo). If the mediums do not match, then graph building can fail between the minidriver's filter and an adjacent filter in the graph.

-   The **VideoMedium** and **AudioMedium** members of the [**KSPROPERTY\_TUNER\_CAPS\_S**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tuner_caps_s) structure of [**KSPROPERTY\_TUNER\_CAPS**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-tuner-caps).

-   The **InputMedium** and **OutputMedium** members of the [**KSPROPERTY\_TVAUDIO\_CAPS\_S**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-ksproperty_tvaudio_caps_s) structure of [**KSPROPERTY\_TVAUDIO\_CAPS**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-tvaudio-caps).

In addition to implementing mediums and medium GUIDs correctly, it is necessary to follow other guidelines to ensure processes can work with multiple filter graphs. The minidriver must not lock any hardware resources until the filter graph transitions to the **KSSTATE\_ACQUIRE** value of KSSTATE. This helps to ensure that two built, but not running filter graphs can coexist without interfering with one another.

For more information about mediums, including how to implement them, see the [AVStream Simulated Hardware Sample Driver (AVSHwS)](https://go.microsoft.com/fwlink/p/?linkid=256083).

**Note**  : When deriving a new minidriver from sample code in the Windows Driver Kit, you must generate new GUID values for the mediums to reflect the unique hardware topology of the device. Failure to do so can result in the mediums for one device colliding with the mediums that are defined for another device.

 

 

 




