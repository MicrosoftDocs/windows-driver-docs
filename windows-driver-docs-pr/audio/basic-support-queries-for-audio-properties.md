---
title: Basic Support Queries for Audio Properties
description: Basic Support Queries for Audio Properties
ms.assetid: d08b6f86-e4fd-4b2c-bfaa-191bcbac3ff8
keywords:
- audio properties WDK , basic-support queries
- WDM audio properties WDK , basic-support queries
- basic-support queries WDK audio
- set-property WDK audio
- valid ranges WDK audio
- range values WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Basic Support Queries for Audio Properties


## <span id="basic_support_queries_for_audio_properties"></span><span id="BASIC_SUPPORT_QUERIES_FOR_AUDIO_PROPERTIES"></span>


When specifying the data for a set-property request to a filter, pin, or node, the client frequently needs to know the valid data ranges for the value or values that it specifies for the property. Ranges can vary from device to device, and possibly even from node to node within the same device.

Some properties are defined to allow set-property requests to specify values that are out-of-range, but miniport drivers silently clamp those values to the supported range (for example, see [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff537309)). A subsequent get request for the same property retrieves the driver's actual settings for the value or values, which might be clamped versions of the values that the client specified in the set request.

However, a client might need to know the range for a property value instead of simply relying on the miniport driver to automatically clamp an out-of-range value. For example, a windowed application that presents a volume-control slider for an audio device might need to know the device's volume range in order to map that range to the full length of the slider.

The driver's handler routine for a particular property should be able to provide range information in response to a basic-support property request (KSPROPERTY\_TYPE\_BASICSUPPORT). When sending a basic-support property request to a driver, a client provides a value buffer into which the property handler writes the basic-support information, which consists of a [**KSPROPERTY\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff565132) structure that might be followed by property-specific data. This data typically consists of specifications for one or more parameter ranges, depending on the property.

In general, the client does not know in advance how large this value buffer should be and must send one or two preliminary requests to the property handler to determine the value size. The format for these preliminary requests is well defined. Clients expect drivers to follow these conventions when handling a basic-support request:

-   If the request specifies the value size as **sizeof**(ULONG) then the property handler should write the value of the **AccessFlags** member of the KSPROPERTY\_DESCRIPTION structure into the ULONG-sized value buffer. The handler sets the KSPROPERTY\_TYPE\_BASICSUPPORT flag bit if it provides further support for basic-support property requests.

-   If the request specifies the value size as **sizeof**(KSPROPERTY\_DESCRIPTION), the handler should write a KSPROPERTY\_DESCRIPTION structure into the data buffer. The handler sets the **DescriptionSize** field of the structure equal to that structure's size plus the size of all of the additional, property-specific information that the handler has available to load into the data buffer following the structure. This is the size of the value buffer that the client needs to allocate to contain the property's basic-support information.

-   If the request specifies a value size that is large enough to contain both the KSPROPERTY\_DESCRIPTION structure and the property-specific information, the handler should write the KSPROPERTY\_DESCRIPTION structure into the start of the buffer, and it should write the property-specific information into the portion of the data buffer that follows the end of the KSPROPERTY\_DESCRIPTION structure. When writing the KSPROPERTY\_DESCRIPTION structure, the handler should set the **DescriptionSize** field to that structure's size plus the size of the property-specific information that follows the structure.

If the request specifies a value size that does not match one of these three cases, the property handler rejects the request and returns status code STATUS\_BUFFER\_TOO\_SMALL.

The property-specific information that the handler writes into the value buffer might include data ranges for property values. The **MembersSize** member of KSPROPERTY\_MEMBERSHEADER indicates whether data ranges are included:

-   **MembersSize** is zero if no ranges are needed. This is the case, for example, if property values are of type BOOL.

-   **MembersSize** is nonzero if the KSPROPERTY\_MEMBERSHEADER structure is followed by range descriptors for one or more property values.

For a property value of type BOOL, no range descriptor is needed because the range is implicitly limited to the values **TRUE** and **FALSE**. However, range descriptors are needed to specify the ranges of property values with integer types.

For example, the basic-support request for a [**KSPROPERTY\_AUDIO\_VOLUMELEVEL**](https://msdn.microsoft.com/library/windows/hardware/ff537309) property on a volume node ([**KSNODETYPE\_VOLUME**](https://msdn.microsoft.com/library/windows/hardware/ff537208)) retrieves the minimum and maximum volume settings for that node. In this case, the client needs to allocate a value buffer that is large enough to contain the following structures:

[**KSPROPERTY\_DESCRIPTION**](https://msdn.microsoft.com/library/windows/hardware/ff565132)

[**KSPROPERTY\_MEMBERSLIST**](https://msdn.microsoft.com/library/windows/hardware/ff565190)

[**KSPROPERTY\_STEPPING\_LONG**](https://msdn.microsoft.com/library/windows/hardware/ff565631)

The three structures are packed into adjacent locations in the buffer in the order shown in the preceding list. When handling the request, the miniport driver writes the minimum and maximum volume levels into the **Bounds** member of the KSPROPERTY\_STEPPING\_LONG structure.

For an example of a basic-support request with an array of range descriptors, see the figure in [Exposing Multichannel Nodes](exposing-multichannel-nodes.md). For more information about basic-support property requests, see [KS Properties](https://msdn.microsoft.com/library/windows/hardware/ff567671). For code examples, refer to the property-handler implementations in the [sample audio drivers](sample-audio-drivers.md) in the Microsoft Windows Driver Kit (WDK).

 

 




