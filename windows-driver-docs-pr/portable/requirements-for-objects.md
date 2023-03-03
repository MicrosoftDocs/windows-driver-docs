---
description: Requirements for Objects
title: Requirements for Objects
ms.date: 03/03/2023
---

# Requirements for Objects


Windows Portable Devices (WPD) classifies all objects by content type. An object of a specific type is expected to support a minimum list of properties and resources (and, for the device object, a set of commands). An object's type is described by its [WPD\_OBJECT\_CONTENT\_TYPE](/previous-versions/windows/hardware/drivers/ff597893(v=vs.85)#wpd-object-content-type) property; every object must support this property.

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
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597834(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_ALL&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597834(v=vs.85))"><strong>WPD_CONTENT_TYPE_ALL</strong></a></td>
<td align="left">This content type is only valid to use in certain query methods to indicate that you are interested in all device types; you cannot create an object of this type.
<p>If you are designing a custom object, it must support these properties, at minimum.</p></td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597835(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_APPOINTMENT&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597835(v=vs.85))"><strong>WPD_CONTENT_TYPE_APPOINTMENT</strong></a></td>
<td align="left">Object is an appointment in a calendar.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597836(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_AUDIO&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597836(v=vs.85))"><strong>WPD_CONTENT_TYPE_AUDIO</strong></a></td>
<td align="left">Object is an audio file, such as a WMA or MP3 file.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597837(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_AUDIO_ALBUM&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597837(v=vs.85))"><strong>WPD_CONTENT_TYPE_AUDIO_ALBUM</strong></a></td>
<td align="left">Object is an audio album.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597838(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_CALENDAR&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597838(v=vs.85))"><strong>WPD_CONTENT_TYPE_CALENDAR</strong></a></td>
<td align="left">Object is a calendar.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597839(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_CERTIFICATE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597839(v=vs.85))"><strong>WPD_CONTENT_TYPE_CERTIFICATE</strong></a></td>
<td align="left">Object is a certificate that is used for authentication.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597840(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_CONTACT&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597840(v=vs.85))"><strong>WPD_CONTENT_TYPE_CONTACT</strong></a></td>
<td align="left">Object is personal contact data, such as a vCard file.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597841(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_CONTACT_GROUP&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597841(v=vs.85))"><strong>WPD_CONTENT_TYPE_CONTACT_GROUP</strong></a></td>
<td align="left">Object represents a group of contacts. This object’s WPD_OBJECT_REFERENCES property contains a list of object identifiers for various WPD_CONTENT_TYPE_CONTACT objects.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597842(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_DOCUMENT&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597842(v=vs.85))"><strong>WPD_CONTENT_TYPE_DOCUMENT</strong></a></td>
<td align="left">Object is a container for text, with or without formatting. Examples include Microsoft Word files and plain text files.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597843(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_EMAIL&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597843(v=vs.85))"><strong>WPD_CONTENT_TYPE_EMAIL</strong></a></td>
<td align="left">Object is an E-mail message.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597844(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_FOLDER&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597844(v=vs.85))"><strong>WPD_CONTENT_TYPE_FOLDER</strong></a></td>
<td align="left">Object is a folder.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597845(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597845(v=vs.85))"><strong>WPD_CONTENT_TYPE_FUNCTIONAL_OBJECT</strong></a></td>
<td align="left">Object is a functional object that represents device functionality.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597846(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_GENERIC_FILE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597846(v=vs.85))"><strong>WPD_CONTENT_TYPE_GENERIC_FILE</strong></a></td>
<td align="left">Object is a generic, physical file that does not fall into any of the other predefined content types for files.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597848(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_IMAGE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597848(v=vs.85))"><strong>WPD_CONTENT_TYPE_IMAGE</strong></a></td>
<td align="left">Object is a still image, such as a JPEG file.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597849(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_IMAGE_ALBUM&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597849(v=vs.85))"><strong>WPD_CONTENT_TYPE_IMAGE_ALBUM</strong></a></td>
<td align="left">Object is an image album.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597851(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_MEDIA_CAST&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597851(v=vs.85))"><strong>WPD_CONTENT_TYPE_MEDIA_CAST</strong></a></td>
<td align="left">Object is a media cast object. A media cast object can represent a container object that groups related content that is published online. For example, an RSS channel can be represented as a media cast object, and this object’s WPD_OBJECT_REFERENCES property contains a list of object identifiers that represent each item in the channel.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597851(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_MEMO&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597851(v=vs.85))"><strong>WPD_CONTENT_TYPE_MEMO</strong></a></td>
<td align="left">Object represents memo data, for example, a text note.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597852(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597852(v=vs.85))"><strong>WPD_CONTENT_TYPE_MIXED_CONTENT_ALBUM</strong></a></td>
<td align="left">Object is an album of mixed media objects—for example, audio, image, and video files.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597854(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_PLAYLIST&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597854(v=vs.85))"><strong>WPD_CONTENT_TYPE_PLAYLIST</strong></a></td>
<td align="left">Object is a playlist.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597855(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_PROGRAM&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597855(v=vs.85))"><strong>WPD_CONTENT_TYPE_PROGRAM</strong></a></td>
<td align="left">Object represents a file that can be run, for example, a script or an executable.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597856(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_SECTION&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597856(v=vs.85))"><strong>WPD_CONTENT_TYPE_SECTION</strong></a></td>
<td align="left">Object describes a section of data that is contained in another object. For example, a large audio file might best be described by a series of chapters. Each chapter could be a WPD_CONTENT_TYPE_SECTION object with its own chapter art, metadata, and so on, and whose data is a subset of the large audio file (For example, the first chapter is the first 10 minutes, the second chapter is the next 20 minutes, and so on).</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597857(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_TASK&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597857(v=vs.85))"><strong>WPD_CONTENT_TYPE_TASK</strong></a></td>
<td align="left">Object is a task, such as an item in a to-do list.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597858(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_TELEVISION&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597858(v=vs.85))"><strong>WPD_CONTENT_TYPE_TELEVISION</strong></a></td>
<td align="left">Object is a television recording.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597859(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_UNSPECIFIED&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597859(v=vs.85))"><strong>WPD_CONTENT_TYPE_UNSPECIFIED</strong></a></td>
<td align="left">Object is a generic object that does not fall into the predefined WPD content types.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597860(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_VIDEO&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597860(v=vs.85))"><strong>WPD_CONTENT_TYPE_VIDEO</strong></a></td>
<td align="left">Object is a video, such as a WMV or AVI file.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597861(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_VIDEO_ALBUM&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597861(v=vs.85))"><strong>WPD_CONTENT_TYPE_VIDEO_ALBUM</strong></a></td>
<td align="left">Object is a video album.</td>
</tr>
<tr class="odd">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597862(v=vs.85)" data-raw-source="[&lt;strong&gt;WPD_CONTENT_TYPE_WIRELESS_PROFILE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff597862(v=vs.85))"><strong>WPD_CONTENT_TYPE_WIRELESS_PROFILE</strong></a></td>
<td align="left">Object contains wireless network access information.</td>
</tr>
<tr class="even">
<td align="left"><a href="/previous-versions/windows/hardware/drivers/ff597563(v=vs.85)" data-raw-source="[Device Object](/previous-versions/windows/hardware/drivers/ff597563(v=vs.85))">Device Object</a></td>
<td align="left">Not a <strong>PROPERTYKEY</strong>, but all objects must support the properties listed in this section.</td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[**WPD Drivers Overview**](wpd-drivers-overview.md)

