---
Description: Requirements for Objects
title: Requirements for Objects
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597834" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_ALL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597834)"><strong>WPD_CONTENT_TYPE_ALL</strong></a></td>
<td align="left">This content type is only valid to use in certain query methods to indicate that you are interested in all device types; you cannot create an object of this type.
<p>If you are designing a custom object, it must support these properties, at minimum.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597835" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_APPOINTMENT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597835)"><strong>WPD_CONTENT_TYPE_APPOINTMENT</strong></a></td>
<td align="left">Object is an appointment in a calendar.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597836" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_AUDIO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597836)"><strong>WPD_CONTENT_TYPE_AUDIO</strong></a></td>
<td align="left">Object is an audio file, such as a WMA or MP3 file.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597837" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_AUDIO_ALBUM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597837)"><strong>WPD_CONTENT_TYPE_AUDIO_ALBUM</strong></a></td>
<td align="left">Object is an audio album.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597838" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_CALENDAR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597838)"><strong>WPD_CONTENT_TYPE_CALENDAR</strong></a></td>
<td align="left">Object is a calendar.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597839" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_CERTIFICATE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597839)"><strong>WPD_CONTENT_TYPE_CERTIFICATE</strong></a></td>
<td align="left">Object is a certificate that is used for authentication.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597840" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_CONTACT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597840)"><strong>WPD_CONTENT_TYPE_CONTACT</strong></a></td>
<td align="left">Object is personal contact data, such as a vCard file.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597841" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_CONTACT_GROUP&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597841)"><strong>WPD_CONTENT_TYPE_CONTACT_GROUP</strong></a></td>
<td align="left">Object represents a group of contacts. This object’s WPD_OBJECT_REFERENCES property contains a list of object identifiers for various WPD_CONTENT_TYPE_CONTACT objects.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597842" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_DOCUMENT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597842)"><strong>WPD_CONTENT_TYPE_DOCUMENT</strong></a></td>
<td align="left">Object is a container for text, with or without formatting. Examples include Microsoft Word files and plain text files.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597843" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_EMAIL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597843)"><strong>WPD_CONTENT_TYPE_EMAIL</strong></a></td>
<td align="left">Object is an E-mail message.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597844" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_FOLDER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597844)"><strong>WPD_CONTENT_TYPE_FOLDER</strong></a></td>
<td align="left">Object is a folder.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597845" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597845)"><strong>WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT</strong></a></td>
<td align="left">Object is a functional object that represents device functionality.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597846" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_GENERIC_FILE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597846)"><strong>WPD_CONTENT_TYPE_GENERIC_FILE</strong></a></td>
<td align="left">Object is a generic, physical file that does not fall into any of the other predefined content types for files.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597848" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_IMAGE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597848)"><strong>WPD_CONTENT_TYPE_IMAGE</strong></a></td>
<td align="left">Object is a still image, such as a JPEG file.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597849" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_IMAGE_ALBUM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597849)"><strong>WPD_CONTENT_TYPE_IMAGE_ALBUM</strong></a></td>
<td align="left">Object is an image album.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597851" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_MEDIA_CAST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597851)"><strong>WPD_CONTENT_TYPE_MEDIA_CAST</strong></a></td>
<td align="left">Object is a media cast object. A media cast object can represent a container object that groups related content that is published online. For example, an RSS channel can be represented as a media cast object, and this object’s WPD_OBJECT_REFERENCES property contains a list of object identifiers that represent each item in the channel.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597851" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_MEMO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597851)"><strong>WPD_CONTENT_TYPE_MEMO</strong></a></td>
<td align="left">Object represents memo data, for example, a text note.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597852" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597852)"><strong>WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM</strong></a></td>
<td align="left">Object is an album of mixed media objects—for example, audio, image, and video files.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597854" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_PLAYLIST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597854)"><strong>WPD_CONTENT_TYPE_PLAYLIST</strong></a></td>
<td align="left">Object is a playlist.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597855" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_PROGRAM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597855)"><strong>WPD_CONTENT_TYPE_PROGRAM</strong></a></td>
<td align="left">Object represents a file that can be run, for example, a script or an executable.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597856" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_SECTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597856)"><strong>WPD_CONTENT_TYPE_SECTION</strong></a></td>
<td align="left">Object describes a section of data that is contained in another object. For example, a large audio file might best be described by a series of chapters. Each chapter could be a WPD_CONTENT_TYPE_SECTION object with its own chapter art, metadata, and so on, and whose data is a subset of the large audio file (For example, the first chapter is the first 10 minutes, the second chapter is the next 20 minutes, and so on).</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597857" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_TASK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597857)"><strong>WPD_CONTENT_TYPE_TASK</strong></a></td>
<td align="left">Object is a task, such as an item in a to-do list.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597858" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_TELEVISION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597858)"><strong>WPD_CONTENT_TYPE_TELEVISION</strong></a></td>
<td align="left">Object is a television recording.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597859" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_UNSPECIFIED&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597859)"><strong>WPD_CONTENT_TYPE_UNSPECIFIED</strong></a></td>
<td align="left">Object is a generic object that does not fall into the predefined WPD content types.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597860" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_VIDEO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597860)"><strong>WPD_CONTENT_TYPE_VIDEO</strong></a></td>
<td align="left">Object is a video, such as a WMV or AVI file.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597861" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_VIDEO_ALBUM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597861)"><strong>WPD_CONTENT_TYPE_VIDEO_ALBUM</strong></a></td>
<td align="left">Object is a video album.</td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597862" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_WIRELESS_PROFILE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff597862)"><strong>WPD_CONTENT_TYPE_WIRELESS_PROFILE</strong></a></td>
<td align="left">Object contains wireless network access information.</td>
</tr>
<tr class="even">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff597563" data-raw-source="[Device Object](https://msdn.microsoft.com/library/windows/hardware/ff597563)">Device Object</a></td>
<td align="left">Not a <strong>PROPERTYKEY</strong>, but all objects must support the properties listed in this section.</td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

 

 





