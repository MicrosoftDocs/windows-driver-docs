---
Description: Requirements for Objects
MS-HAID: 'wpddk.requirements\_for\_objects'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Requirements for Objects
---

# Requirements for Objects


Windows Portable Devices (WPD) classifies all objects by content type. An object of a specific type is expected to support a minimum list of properties and resources (and, for the device object, a set of commands). An object's type is described by its [WPD\_OBJECT\_CONTENT\_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff597893#wpd-object-content-type) property; every object must support this property.

WPD defines the following content types (as GUID values). A vendor can create their own custom-content type by providing their own GUID.

Note General purpose applications typically only handle one of the predefined types. Vendor applications can, take full advantage of the custom types that they know about.

To learn which properties and resources each object type must support, see the description page for each of object types in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Content Type GUID</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_ALL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597834)</td>
<td align="left">This content type is only valid to use in certain query methods to indicate that you are interested in all device types; you cannot create an object of this type.
<p>If you are designing a custom object, it must support these properties, at minimum.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_APPOINTMENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597835)</td>
<td align="left">Object is an appointment in a calendar.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_AUDIO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597836)</td>
<td align="left">Object is an audio file, such as a WMA or MP3 file.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_AUDIO_ALBUM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597837)</td>
<td align="left">Object is an audio album.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_CALENDAR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597838)</td>
<td align="left">Object is a calendar.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_CERTIFICATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597839)</td>
<td align="left">Object is a certificate that is used for authentication.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_CONTACT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597840)</td>
<td align="left">Object is personal contact data, such as a vCard file.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_CONTACT_GROUP</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597841)</td>
<td align="left">Object represents a group of contacts. This object’s WPD_OBJECT_REFERENCES property contains a list of object identifiers for various WPD_CONTENT_TYPE_CONTACT objects.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_DOCUMENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597842)</td>
<td align="left">Object is a container for text, with or without formatting. Examples include Microsoft Word files and plain text files.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_EMAIL</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597843)</td>
<td align="left">Object is an E-mail message.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_FOLDER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597844)</td>
<td align="left">Object is a folder.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597845)</td>
<td align="left">Object is a functional object that represents device functionality.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_GENERIC_FILE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597846)</td>
<td align="left">Object is a generic, physical file that does not fall into any of the other predefined content types for files.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_IMAGE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597848)</td>
<td align="left">Object is a still image, such as a JPEG file.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_IMAGE_ALBUM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597849)</td>
<td align="left">Object is an image album.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_MEDIA_CAST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597851)</td>
<td align="left">Object is a media cast object. A media cast object can represent a container object that groups related content that is published online. For example, an RSS channel can be represented as a media cast object, and this object’s WPD_OBJECT_REFERENCES property contains a list of object identifiers that represent each item in the channel.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_MEMO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597851)</td>
<td align="left">Object represents memo data, for example, a text note.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597852)</td>
<td align="left">Object is an album of mixed media objects—for example, audio, image, and video files.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_PLAYLIST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597854)</td>
<td align="left">Object is a playlist.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_PROGRAM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597855)</td>
<td align="left">Object represents a file that can be run, for example, a script or an executable.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_SECTION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597856)</td>
<td align="left">Object describes a section of data that is contained in another object. For example, a large audio file might best be described by a series of chapters. Each chapter could be a WPD_CONTENT_TYPE_SECTION object with its own chapter art, metadata, and so on, and whose data is a subset of the large audio file (For example, the first chapter is the first 10 minutes, the second chapter is the next 20 minutes, and so on).</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_TASK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597857)</td>
<td align="left">Object is a task, such as an item in a to-do list.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_TELEVISION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597858)</td>
<td align="left">Object is a television recording.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_UNSPECIFIED</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597859)</td>
<td align="left">Object is a generic object that does not fall into the predefined WPD content types.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_VIDEO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597860)</td>
<td align="left">Object is a video, such as a WMV or AVI file.</td>
</tr>
<tr class="even">
<td align="left">[<strong>WPD_CONTENT_TYPE_VIDEO_ALBUM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597861)</td>
<td align="left">Object is a video album.</td>
</tr>
<tr class="odd">
<td align="left">[<strong>WPD_CONTENT_TYPE_WIRELESS_PROFILE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff597862)</td>
<td align="left">Object contains wireless network access information.</td>
</tr>
<tr class="even">
<td align="left">[Device Object](https://msdn.microsoft.com/library/windows/hardware/ff597563)</td>
<td align="left">Not a <strong>PROPERTYKEY</strong>, but all objects must support the properties listed in this section.</td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wpd_dk\wpddk]:%20Requirements%20for%20Objects%20%20RELEASE:%20%281/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




