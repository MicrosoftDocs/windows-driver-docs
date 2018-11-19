---
title: MB Interface Model supplement
description: This section provides supplemental information for the MB Interface Model (MBIM)
ms.assetid: 577BCF39-868B-44F5-A5C0-75E28689C2B6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Interface Model Supplement


The Microsoft OS descriptor is broken up into the following segments:

-   One Microsoft OS string descriptor
-   One or more Microsoft OS feature descriptors

To support the OS descriptor, the device must implement the string descriptor.
**String Descriptor**

The Microsoft OS string descriptor is a string that is stored at string index 0xEE. The format of this string is well defined.

The Microsoft OS String Descriptor is used to achieve the following objectives

-   The presence of the Microsoft OS string descriptor indicates to the operating system that the device has information embedded in it, in the form of Microsoft OS feature descriptors.
-   The Microsoft OS string descriptor has an embedded signature field that is used to differentiate it from random strings that might happen to be on a device at string index 0xEE.
-   The Microsoft OS string descriptor also has an embedded version number that allows for future revisions of the Microsoft OS descriptor.

Only one Microsoft OS string descriptor is stored on a device. The following sections describe the structure of the Microsoft OS string descriptor and its retrieval procedure.
**Structure of the OS string**

Here is the structure of the string descriptor:

*String Descriptor Structure*

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Length (Bytes)</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>bLength</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x12</p></td>
<td align="left"><p>Length of the descriptor</p></td>
</tr>
<tr class="even">
<td align="left"><p>bDescriptorType</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x03</p></td>
<td align="left"><p>String descriptor</p></td>
</tr>
<tr class="odd">
<td align="left"><p>qwSignature</p></td>
<td align="left"><p>14</p></td>
<td align="left"><p>&quot;MSFT100&quot;</p></td>
<td align="left"><p>Signature field (4D00530046005400310030003000)</p></td>
</tr>
<tr class="even">
<td align="left"><p>bMS_VendorCode</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Vendor Code</p></td>
<td align="left"><p>Vendor code to fetch other OS feature descriptors</p></td>
</tr>
<tr class="odd">
<td align="left"><p>bPad</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x00</p></td>
<td align="left"><p>Pad field</p></td>
</tr>
</tbody>
</table>

 

The structure of the Microsoft OS string descriptor is fixed for version 1.00 and has an overall length of 18 bytes. The version number of the Microsoft OS string descriptor is listed in the **qwSignature** field. The information stored in the **bMS\_VendorCode** field must be a single byte value. It will be used to retrieve Microsoft OS feature descriptors, and this byte value is used in the **bmRequestType** field described as follows:

**Retrieving the OS string descriptor**

To retrieve the information stored in the string, a standard GET\_DESCRIPTOR request must be issued to the device. Here is the format of the request:

*Standard Get\_Descriptor String Request*

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">bmRequestType</th>
<th align="left">bRequest</th>
<th align="left">wValue</th>
<th align="left">wIndex</th>
<th align="left">wLength</th>
<th align="left">Data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1000 0000b</p></td>
<td align="left"><p>GET_DESCRIPTOR</p></td>
<td align="left"><p>0x03EE</p></td>
<td align="left"><p>0x0000</p></td>
<td align="left"><p>0x12</p></td>
<td align="left"><p>Returns the string</p></td>
</tr>
</tbody>
</table>

 

The **bmRequestType** field is a bitmap composed of three parts—direction of data transfer, descriptor type, and recipient. According to the USB specification, the value of **bmRequestType** is set to 1000 0000b (0x80).

For a GET\_DESCRIPTOR request, the **wValue** field is split into two parts. The high byte stores the descriptor type and the low byte stores the descriptor index. To retrieve the Microsoft OS string descriptor, the high byte should be set to retrieve a string descriptor—0x03. Because the Microsoft OS string descriptor is always stored at index 0xEE, this string index should be stored in the lower byte of the **wValue** field.

The **wIndex** is used to store the language ID, but it must be set to zero for a Microsoft OS string descriptor.

The **wLength** field is used to indicate the length of the string descriptor to be retrieved. The device should respond to any valid range from 0x02–0xFF.

If a device does not have a valid descriptor at the corresponding address (0xEE), it will respond with a request error or stall. When devices do not respond with a stall, a single-ended zero reset will be issued to the device (to recover it, if it should go into an unknown state).

**Verifying the integrity of the OS descriptor**

Because vendors are allowed to use any string ID to store information, the operating system must verify that the string stored in index 0xEE is indeed the Microsoft OS string descriptor. To verify this, the following tests will be conducted. Failure of either will inhibit retrieval of the Microsoft OS feature descriptors.

-   If a vendor stores a string in index location 0xEE, the operating system will retrieve the string and query it to see if it is the Microsoft OS string. This can be verified by comparing the signature field in the string to the signature field entry specified previously. A mismatch would prevent further parsing of the string.
-   The second test will include a verification of the length of the string based on the version number specified in the signature field. The version number specified (in the string "MSFT100") is 1.00. This corresponds to an 18-byte string descriptor.

**Microsoft OS string descriptor constraints**

The following constraints apply to Microsoft OS string descriptors and their retrieval:

-   To store information in compliance with the Microsoft OS descriptor specification, the device must have one and only Microsoft OS string descriptor that is in compliance with the information outlined in [Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?linkid=308932).
-   A device vendor is free to use any value in the **bMS\_VendorCode** field in the Microsoft OS string descriptor

**Feature Descriptor**

A feature descriptor is a fixed-format descriptor that has been defined for a specific purpose.

**Retrieving an OS feature descriptor**

To retrieve a Microsoft OS feature descriptor, a special GET\_MS\_DESCRIPTOR request needs to be issued to the device. Here is the format of the request:

*Standard device request format*

<table style="width:100%;">
<colgroup>
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">bmRequestType</th>
<th align="left">bRequest</th>
<th align="left">wValue</th>
<th align="left">wIndex</th>
<th align="left">wLength</th>
<th align="left">Data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>1100 0000b</p></td>
<td align="left"><p>GET_MS_DESCRIPTOR</p></td>
<td align="left"><p>X</p></td>
<td align="left"><p>Feature Index</p></td>
<td align="left"><p>Length</p></td>
<td align="left"><p>Returns descriptor</p></td>
</tr>
</tbody>
</table>

 

The **bmRequestType** field is a bitmap composed of three parts—direction of data transfer, descriptor type, and recipient—and is in accordance with the USB specification. The Microsoft OS feature descriptor is a vendor-specific descriptor and the direction of data transfer is from the device to the host. Therefore, the value of **bmRequestType** is set to 1100 0000b (0xC0).

The **bRequest** field is used to indicate the format of the request. To retrieve a Microsoft OS feature descriptor, the **bRequest** field should be populated with a special GET\_MS\_DESCRIPTOR byte. The value of this byte is indicated by the **bMS\_VendorCode**, which is retrieved from the Microsoft string descriptor. For more information about the retrieval of the Microsoft OS string descriptor, see **Retrieving the OS string descriptor**.

The **wValue** field is put to special use and is broken up into a high byte and a low byte. The high byte is used to store the interface number. This is essential for storing feature descriptors on a per interface basis, especially for composite devices, or devices with [multiple interfaces](https://msdn.microsoft.com/library/windows/hardware/ff537102). In most cases, interface 0 will be used. The low byte is used to store a page number. This feature prevents descriptors from having a size boundary of 64 KB (a limit set by the size of the **wLength** field). A descriptor will be fetched with the page value initially set to zero. If a full descriptor (size is 64 KB) is received, the page value will be incremented by one and the request for the descriptor will be sent again (this time with the incremented page value). This process will repeat until a descriptor with a size less than 64 KB is received. Note that the maximum number of pages is 255, which places a limit of 16 MB on the descriptor size.

The **wIndex** field stores the feature index number for the Microsoft OS feature descriptor being retrieved. Microsoft will maintain this list of Microsoft OS feature descriptors and indexes. To learn more about Microsoft OS feature descriptors, see [Microsoft OS Descriptors](http://go.microsoft.com/fwlink/p/?linkid=308932).

The **wLength** field specifies the length of the descriptor to be fetched. If the descriptor is longer than the number of bytes stated in the **wLength** field, only the initial bytes of the descriptor are returned. If it is shorter than the value specified in the **wLength** field, a short packet is returned.

If a particular OS descriptor is not present, the device will issue a request error or stall.

**Microsoft OS feature descriptor constraints**

The following constraints apply to Microsoft OS feature descriptors and their retrieval.

-   All Microsoft OS feature descriptors are defined and standardized. Vendors are not allowed to modify, append, or create Microsoft OS feature descriptors without direct consent from Microsoft.
-   All Microsoft OS feature descriptors will have a size and version number embedded in them. These values should always report correct information to the operating system.
-   A device can have more than one Microsoft OS feature descriptor embedded in its firmware.
-   Some Microsoft OS feature descriptors are stored on a per-interface level, while others are unique to the device. Device-level Microsoft OS feature descriptors should set the high byte of the wValue field as zero.

**Structure of the feature descriptor**

To identify itself as capable of supporting MBIM, a device must also support the extended configuration descriptor, which is one of the defined feature descriptors. The structure of this descriptor is as follows.

**Header section**

The header section stores information about the rest of the extended configuration descriptor. The **dwLength** field contains the length of the entire extended configuration descriptor. The header section also contains a version number, which will be initially set to 1.00 (0100H). Future revisions of this descriptor may be released at a later stage. Note that future versions of the extended configuration descriptor might also need to increase the number of entries in the header section, so please verify that this number is accurately stored in the device and read by the operating system.

*Extended configuration descriptor header section*

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Offset</th>
<th align="left">Field</th>
<th align="left">Size</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>dwLength</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>Unsigned DWORD</p></td>
<td align="left"><p>The length field describes the length of the extended configuration descriptor, in bytes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>bcdVersion</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>BCD</p></td>
<td align="left"><p>Extended configuration descriptor release number in Binary Coded Decimal (for example, version 1.00 is 0100H).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>6</p></td>
<td align="left"><p>wIndex</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>WORD</p></td>
<td align="left"><p>Fixed = 0x0004</p></td>
</tr>
<tr class="even">
<td align="left"><p>8</p></td>
<td align="left"><p>bCount</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>BYTE</p></td>
<td align="left"><p>Total number of function sections that follow the header section = 0x01</p></td>
</tr>
<tr class="odd">
<td align="left"><p>9</p></td>
<td align="left"><p>RESERVED</p></td>
<td align="left"><p>7</p></td>
<td align="left"><p></p></td>
<td align="left"><p>RESERVED</p></td>
</tr>
</tbody>
</table>

 

**Function section**

The function section provides two important pieces of information. It groups consecutive interfaces that serve a similar purpose into function groups, and provides compatible and subcompatible IDs for each function.

Here is the format of the function section, including values that should be used by an MBIM device:

*Extended configuration descriptor function section*

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Offset¹</th>
<th align="left">Field</th>
<th align="left">Size</th>
<th align="left">Value</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>bFirstInterfaceNumber</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Byte</p></td>
<td align="left"><p>Starting interface number for this function = 0x00</p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>bInterfaceCount</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>Byte</p></td>
<td align="left"><p>Total number of Interfaces that must be included to from this function = 0x01</p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>compatibleID</p></td>
<td align="left"><p>8</p></td>
<td align="left"><p>Bytes</p></td>
<td align="left"><p>Compatible ID</p></td>
</tr>
<tr class="even">
<td align="left"><p>10</p></td>
<td align="left"><p>subCompatibleID</p></td>
<td align="left"><p>8</p></td>
<td align="left"><p>Bytes</p></td>
<td align="left"><p>Subcompatible ID</p></td>
</tr>
<tr class="odd">
<td align="left"><p>18</p></td>
<td align="left"><p>RESERVED</p></td>
<td align="left"><p>6</p></td>
<td align="left"><p></p></td>
<td align="left"><p>RESERVED = 0</p></td>
</tr>
</tbody>
</table>

 

¹Offset of the custom property section has been reset to zero. To calculate the offset of a field from the beginning of the extended configuration descriptor, add the length of the sections that precede it.

*Compatible and Subcompatible IDs based on the configuration exposing the MBIM function*

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">bConfiguration</th>
<th align="left">compatibleID</th>
<th align="left">subCompatibleID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>ALTRCFG</p>
<p>(0x41 0x4C 0x54 0x52 0x43 0x46 0x47 0x00)</p></td>
<td align="left"><p>20000000</p>
<p>(0x32 0x00 0x00 0x00 0x00 0x00 0x00 0x00)</p></td>
</tr>
<tr class="even">
<td align="left"><p>3</p></td>
<td align="left"><p>ALTRCFG</p>
<p>(0x41 0x4C 0x54 0x52 0x43 0x46 0x47 0x00)</p></td>
<td align="left"><p>30000000</p>
<p>(0x33 0x00 0x00 0x00 0x00 0x00 0x00 0x00)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>4</p></td>
<td align="left"><p>ALTRCFG</p>
<p>(0x41 0x4C 0x54 0x52 0x43 0x46 0x47 0x00)</p></td>
<td align="left"><p>40000000</p>
<p>(0x34 0x00 0x00 0x00 0x00 0x00 0x00 0x00)</p></td>
</tr>
</tbody>
</table>

 

-   **bConfiguration** refers to the **bConfiguration** value within the USB configuration descriptor of the configuration that exposes the MBIM function. **bConfiguration** cannot be 1 because that is the default configuration exposing only the CDROM function. **bConfiguration** cannot be greater than 4; that is, the MBIM function should be exposed within the first four configurations.
-   compatibleID remains the same for all configurations. The subcompatibleID changes based on the configuration

**Example**

This table shows a sample multi-configuration scenario. The table lists the functions available in each configuration and the actions that different versions of the operating system takes for each of these configurations:

*Example of a multi-configuration mobile broadband device*

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">bConfiguration</th>
<th align="left">1 (Windows-7-Configuration)</th>
<th align="left">2 (IHV-NCM-1.0-Configuration)</th>
<th align="left">3 (Windows-8-Configuration)</th>
<th align="left">3 (IHV-NCM-2.0-Configuration)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Functions exposed</p></td>
<td align="left"><p>CDROM</p>
<p>SD</p></td>
<td align="left"><p>CD-ROM</p>
<p>SD</p>
<p>NCM1.0</p>
<p>Modem</p>
<p>TV</p>
<p>GPS</p>
<p>FP</p>
<p>PC/SC smart card</p>
<p>Voice</p>
<p>Diag</p></td>
<td align="left"><p>CD-ROM</p>
<p>SD</p>
<p>MBIM</p></td>
<td align="left"><p>CD-ROM</p>
<p>SD</p>
<p>NCM2.0</p>
<p>Modem</p>
<p>TV</p>
<p>GPS</p>
<p>FP</p>
<p>PC/SC smart card</p>
<p>Voice</p>
<p>Diag</p></td>
</tr>
</tbody>
</table>

 

The following tables show the values used by the Microsoft OS string descriptor and the Microsoft OS extended configuration feature descriptor for the previous sample’s multi-configuration scenario.

*Example of a multi-configuration mobile broadband device*

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Field</th>
<th align="left">Length (Bytes)</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>bLength</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x12</p></td>
</tr>
<tr class="even">
<td align="left"><p>bDescriptorType</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x03</p></td>
</tr>
<tr class="odd">
<td align="left"><p>qwSignature</p></td>
<td align="left"><p>14</p></td>
<td align="left"><p>‘MSFT100’</p>
<p>0x4D 0x00 0x53 0x00 0x46 0x00 0x54 0x00 0x31 0x00 0x30 0x00 0x30 0x00</p></td>
</tr>
<tr class="even">
<td align="left"><p>bMS_VendorCode</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0xA5</p></td>
</tr>
<tr class="odd">
<td align="left"><p>bPad</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>0x00</p></td>
</tr>
</tbody>
</table>

 

*Example Microsoft OS extended configuration feature descriptor header*

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Offset</th>
<th align="left">Field</th>
<th align="left">Size</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>dwLength</p></td>
<td align="left"><p>4</p></td>
<td align="left"><p>16</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>bcdVersion</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>0100H</p></td>
</tr>
<tr class="odd">
<td align="left"><p>6</p></td>
<td align="left"><p>wIndex</p></td>
<td align="left"><p>2</p></td>
<td align="left"><p>0x0004</p></td>
</tr>
<tr class="even">
<td align="left"><p>8</p></td>
<td align="left"><p>bCount</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>9</p></td>
<td align="left"><p>RESERVED</p></td>
<td align="left"><p>7</p></td>
<td align="left"><p></p></td>
</tr>
</tbody>
</table>

 

*Example Microsoft OS extended configuration feature descriptor function*

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Offset²</th>
<th align="left">Field</th>
<th align="left">Size</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0</p></td>
<td align="left"><p>bFirstInterfaceNumber</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p></p></td>
</tr>
<tr class="even">
<td align="left"><p>1</p></td>
<td align="left"><p>bInterfaceCount</p></td>
<td align="left"><p>1</p></td>
<td align="left"><p></p></td>
</tr>
<tr class="odd">
<td align="left"><p>2</p></td>
<td align="left"><p>compatibleID</p></td>
<td align="left"><p>8</p></td>
<td align="left"><p></p></td>
</tr>
<tr class="even">
<td align="left"><p>10</p></td>
<td align="left"><p>subCompatibleID</p></td>
<td align="left"><p>8</p></td>
<td align="left"><p></p></td>
</tr>
<tr class="odd">
<td align="left"><p>18</p></td>
<td align="left"><p>RESERVED</p></td>
<td align="left"><p>6</p></td>
<td align="left"><p></p></td>
</tr>
</tbody>
</table>

 

²Offset of the custom property section has been reset to zero. To calculate the offset of a field from the beginning of the extended configuration descriptor, add the length of the sections that precede it.

 

 





