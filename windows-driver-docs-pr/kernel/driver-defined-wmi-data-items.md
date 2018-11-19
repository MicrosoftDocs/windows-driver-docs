---
title: Driver-Defined WMI Data Items
description: Driver-Defined WMI Data Items
ms.assetid: 97b64571-95ff-4d61-9fa0-5690e9f29345
keywords: ["data types WDK WMI", "embedded classes WDK WMI", "data items WDK WMI", "WMI WDK kernel , driver-defined data items", "driver-defined data items WDK WMI", "classes WDK WMI", "WMI WDK kernel , classes"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Driver-Defined WMI Data Items





A data item in a class definition of WMI data or event block can be one of the following:

-   A basic data type such as a string or an unsigned integer.

-   An embedded class. An embedded class is used only as a data item in another class definition and is not exposed as a data block or event block.

-   A fixed-length or variable-length array of a basic data type or embedded class.

When sending a data block to WMI, a driver must align the start of the block on an 8-byte boundary. All subsequent data items in the block must be aligned on the corresponding alignment for the data type. A **boolean** or **uint8** should be aligned on a 1-byte boundary. A **sint16**, **uint16**, or **string** item should be aligned on a 2-byte boundary, and so on. Arrays should be aligned based upon the base type of the array. An array of bytes should be aligned on a byte boundary, an array of uint64 should be aligned on an 8-byte boundary, and so on. An embedded class should be aligned based upon the natural alignment of the embedded class which is defined to be the largest element within the embedded class. For example, if an embedded class has a **uint64**, the class should be aligned on an 8-byte boundary. WMI data item alignment follows the same conventions as the **/Zp8** switch on the Microsoft C compiler.

A driver writer does not necessarily have to define data items in a block other than the required items **InstanceName** and **Active**. For example, an empty event block can serve as notification that an event occurred, without additional data. Or a data block might simply enumerate instance names in response to an [**IRP\_MN\_QUERY\_ALL\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff551650) request.

The following table lists the MOF data types that can be used to define items in a WMI data or event block. For more information about MOF data types, see the Microsoft Windows SDK.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Data type</th>
<th>Data format</th>
<th>Alignment (in bytes)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>string</strong></p></td>
<td><p>A USHORT specifying the string length in bytes, followed by the Unicode string data. The string data may optionally include a terminating 0 followed by padding. If so, the string length must include the terminating 0 and padding. Drivers can use the <strong>MaxLen</strong> qualifier to specify the maximum length in characters of the string. Drivers that specify a maximum string length can use a fixed size buffer to hold the string. If the string is strictly smaller than the size of the buffer, then the driver can pad the rest of the string with zeros.</p></td>
<td><p>2</p></td>
</tr>
<tr class="even">
<td><p><strong>boolean</strong></p></td>
<td><p>A one-byte value where 0 is FALSE and any nonzero value is TRUE</p></td>
<td><p>1</p></td>
</tr>
<tr class="odd">
<td><p><strong>sint8</strong></p></td>
<td><p>Signed 8-bit integer</p></td>
<td><p>1</p></td>
</tr>
<tr class="even">
<td><p><strong>uint8</strong></p></td>
<td><p>Unsigned 8-bit integer</p></td>
<td><p>1</p></td>
</tr>
<tr class="odd">
<td><p><strong>sint16</strong></p></td>
<td><p>Signed 16-bit integer</p></td>
<td><p>2</p></td>
</tr>
<tr class="even">
<td><p><strong>uint16</strong></p></td>
<td><p>Unsigned 16-bit integer</p></td>
<td><p>2</p></td>
</tr>
<tr class="odd">
<td><p><strong>sint32</strong></p></td>
<td><p>Signed 32-bit integer</p></td>
<td><p>4</p></td>
</tr>
<tr class="even">
<td><p><strong>uint32</strong></p></td>
<td><p>Unsigned 32-bit integer</p></td>
<td><p>4</p></td>
</tr>
<tr class="odd">
<td><p><strong>sint64</strong></p></td>
<td><p>Signed 64-bit integer</p></td>
<td><p>8</p></td>
</tr>
<tr class="even">
<td><p><strong>uint64</strong></p></td>
<td><p>Unsigned 64-bit integer</p></td>
<td><p>8</p></td>
</tr>
<tr class="odd">
<td><p><strong>datetime</strong></p></td>
<td><p>A fixed-length 25-character Unicode string that specifies an absolute date or time interval. A <strong>datetime</strong> value has the following format:</p>
<p><em>yyyymmddhhmmss.mmmmmmsutc</em></p>
<p>where:</p>
<p><em>yyyy</em> is the 4-digit year</p>
<p><em>mm</em> is the 2-digit month</p>
<p><em>dd</em> is the 2-digit day of the month</p>
<p><em>hh</em> is the hour according to a 24-hour clock</p>
<p><em>mm</em> is the minute</p>
<p><em>ss</em> is the seconds</p>
<p><em>mmmmmm</em> is the number of microseconds</p>
<p><em>s</em> is a plus sign (+) or minus sign (-), indicating whether <em>utc</em> is a positive or negative offset from Universal Time Coordinates; or a colon (:), indicating that the <strong>datetime</strong> value is an interval.</p>
<p><em>utc</em> is the offset in minutes from Universal Time Coordinates. If <em>utc</em> is zero (000), the <strong>datetime</strong> value is an interval.</p>
<p>Values must be zero-padded. Fields that are not significant can be filled with asterisks (*).</p></td>
<td><p>2</p></td>
</tr>
</tbody>
</table>

 

 

 




