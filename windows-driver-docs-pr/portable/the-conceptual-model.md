---
Description: The Conceptual Model
MS-HAID: 'wpddk.the\_conceptual\_model'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: The Conceptual Model
---

# The Conceptual Model


The WPD conceptual model describes a device in terms of objects, properties, and resources. The following topics describe these elements.

## <span id="Objects"></span><span id="objects"></span><span id="OBJECTS"></span>Objects


In WPD, logical entities on devices are referred to as objects. Typically, but not always, these represent data on the device. Objects have properties, and are referenced by object identifiers. Examples of objects include pictures and folders on a camera, songs and playlists on a media player, contacts on a mobile phone, and so on.

Objects can also represent functional or informational parts of the device. Examples of these include player controls (play/record/pause), camera settings, a mobile phone's short message service (SMS) capabilities, and so on. Objects can also have binary data, which is stored as a resource.

## <span id="Properties"></span><span id="properties"></span><span id="PROPERTIES"></span>Properties


Object properties provide a mechanism for exchanging object-describing metadata. For example, an image object may include properties that describe its filename, size, format, width in pixels, and so on.

Properties have a current value, as well as attributes. WPD defines a set of standard properties that make up the API and DDI definitions. Vendors are not limited to the predefined WPD properties and are free to add their own.

## <span id="Property_Attributes"></span><span id="property_attributes"></span><span id="PROPERTY_ATTRIBUTES"></span>Property Attributes


Property attributes describe the access rights, valid values, and other information related to a property. For example, the property representing bit rate could be a range from 8 kilobits per second (Kbps) to 20 Kbps with a step value of 1 Kbps.

Access rights indicate whether callers can read, write and/or delete the property. Valid values indicate restrictions for property values. Valid values are said to be of a specific form. Valid value forms include Range (that is, property can take a value from Min to Max with specified Step), Enumeration (that is, property value is one of those in the specified List), and None (that is, there are no specific valid values).

## <span id="Resources"></span><span id="resources"></span><span id="RESOURCES"></span>Resources


Resources are placeholders for binary data. An object can have more than one resource. For example, if the object represented an image file with an audio annotation, then the resources for this object might be as follows:

-   A default resource. This resource represents the entire image file. (This includes any embedded data such as audio annotations, thumbnails, and so on)
-   A thumbnail resource. This resource represents the thumbnail data for the image.
-   An audio annotation resource. This resource represents the audio data associated with the image.

## <span id="Resource_Attributes"></span><span id="resource_attributes"></span><span id="RESOURCE_ATTRIBUTES"></span>Resource Attributes


Similar to property attributes, resource attributes describe the access rights, size, format and other information related to a resource. For example, the attributes for an audio annotation resource on an image object may specify the bit rate, channel count, and data format of the audio.

## <span id="Object_Illustration"></span><span id="object_illustration"></span><span id="OBJECT_ILLUSTRATION"></span>Object Illustration


The following diagram shows the relationship between an object, its properties, and its resources, using an Image object as an example.

![wpd objects](images/wpd_overview_figure2.png)

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20The%20Conceptual%20Model%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




