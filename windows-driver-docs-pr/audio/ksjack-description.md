---
title: KSJACK\_DESCRIPTION structure
description: The KSJACK\_DESCRIPTION structure specifies the physical attributes of an audio jack.
ms.assetid: 303bc73a-fe47-499b-97b3-7c49a40e8cfa
keywords: ["KSJACK_DESCRIPTION structure Audio Devices", "PKSJACK_DESCRIPTION structure pointer Audio Devices"]
topic_type:
- apiref
api_name:
- KSJACK_DESCRIPTION
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSJACK\_DESCRIPTION structure


The KSJACK\_DESCRIPTION structure specifies the physical attributes of an audio jack.

Syntax
------

```ManagedCPlusPlus
typedef struct {
  DWORD              ChannelMapping;
  DWORD              Color;
  EPcxConnectionType ConnectionType;
  EPcxGeoLocation    GeoLocation;
  EPcxGenLocation    GenLocation;
  EPxcPortConnection PortConnection;
  BOOL               IsConnected;
} KSJACK_DESCRIPTION, *PKSJACK_DESCRIPTION;
```

Members
-------

**ChannelMapping**  
Specifies the mapping of the audio channels to the corresponding speaker positions. **ChannelMapping** is a bitmask of the KSAUDIO\_SPEAKER\_*XXX* flags (for example, SPEAKER\_FRONT\_LEFT | SPEAKER\_FRONT\_RIGHT), which are defined in the header file Ksmedia.h. **ChannelMapping** should be nonzero only for analog rendering pins. For capture pins or for digital rendering pins, set this member to 0.

&gt; \[!Note\]
&gt;  Devicetopology.h originally defined **ChannelMapping** as an enumeration of type **EChannelMapping**. The **EChannelMapping** enumeration has since been deprecated and is no longer used in Windows Vista and later versions of the Windows operating systems.

 

**Color**  
Specifies the jack color. The color is expressed as a 32-bit RGB value that is formed by concatenating the 8-bit blue, green, and red color components. The blue component occupies the 8 least-significant bits (bits 0-7), the green component occupies bits 8-15, and the red component occupies bits 16-23. The 8 most-significant bits are zeros. If the jack color is unknown or the physical connector has no identifiable color, the value of this member is 0x00000000, which represents black.

**ConnectionType**  
Specifies the physical connection type for this jack. The value of this member is one of the **EPcxConnectionType** enumeration values shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Connector type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>eConnTypeUnknown</p></td>
<td align="left"><p>Unknown</p></td>
</tr>
<tr class="even">
<td align="left"><p>eConnType3Point5mm</p></td>
<td align="left"><p>3.5 mm minijack</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eConnTypeQuarter</p></td>
<td align="left"><p>1/4-inch jack</p></td>
</tr>
<tr class="even">
<td align="left"><p>eConnTypeAtapiInternal</p></td>
<td align="left"><p>ATAPI internal connector</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eConnTypeRCA</p></td>
<td align="left"><p>RCA jack</p></td>
</tr>
<tr class="even">
<td align="left"><p>eConnTypeOptical</p></td>
<td align="left"><p>Optical connector</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eConnTypeOtherDigital</p></td>
<td align="left"><p>Generic digital connector</p></td>
</tr>
<tr class="even">
<td align="left"><p>eConnTypeOtherAnalog</p></td>
<td align="left"><p>Generic analog connector</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eConnTypeMultichannelAnalogDIN</p></td>
<td align="left"><p>Multichannel analog DIN connector</p></td>
</tr>
<tr class="even">
<td align="left"><p>eConnTypeXlrProfessional</p></td>
<td align="left"><p>XLR connector</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eConnTypeRJ11Modem</p></td>
<td align="left"><p>RJ11 modem connector</p></td>
</tr>
<tr class="even">
<td align="left"><p>eConnTypeCombination</p></td>
<td align="left"><p>Connector combination</p></td>
</tr>
</tbody>
</table>

 

**GeoLocation**  
The geometric location of the jack. The value of this member is one of the **EPcxGeoLocation** enumeration values shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Geometric location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>eGeoLocRear</p></td>
<td align="left"><p>Rear</p></td>
</tr>
<tr class="even">
<td align="left"><p>eGeoLocFront</p></td>
<td align="left"><p>Front</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eGeoLocLeft</p></td>
<td align="left"><p>Left</p></td>
</tr>
<tr class="even">
<td align="left"><p>eGeoLocRight</p></td>
<td align="left"><p>Right</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eGeoLocTop</p></td>
<td align="left"><p>Top</p></td>
</tr>
<tr class="even">
<td align="left"><p>eGeoLocBottom</p></td>
<td align="left"><p>Bottom</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eGeoLocRearPanel</p></td>
<td align="left"><p>Rear slide-open or pull-open panel</p></td>
</tr>
<tr class="even">
<td align="left"><p>eGeoLocRiser</p></td>
<td align="left"><p>Riser card</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eGeoLocInsideMobileLid</p></td>
<td align="left"><p>Inside lid of mobile computer</p></td>
</tr>
<tr class="even">
<td align="left"><p>eGeoLocDrivebay</p></td>
<td align="left"><p>Drive bay</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eGeoLocHDMI</p></td>
<td align="left"><p>HDMI connector</p></td>
</tr>
<tr class="even">
<td align="left"><p>eGeoLocOutsideMobileLid</p></td>
<td align="left"><p>Outside lid of mobile computer</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eGeoLocATAPI</p></td>
<td align="left"><p>ATAPI connector</p></td>
</tr>
<tr class="even">
<td align="left"><p>eGeoLocNotApplicable</p></td>
<td align="left"><p>Not applicable. See <strong>Remarks</strong> section.</p></td>
</tr>
</tbody>
</table>

 

**GenLocation**  
Specifies the general location of the jack. The value of this member is one of the **EPcxGenLocation** enumeration values shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">General location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>eGenLocPrimaryBox</p></td>
<td align="left"><p>On primary chassis</p></td>
</tr>
<tr class="even">
<td align="left"><p>eGenLocInternal</p></td>
<td align="left"><p>Inside primary chassis</p></td>
</tr>
<tr class="odd">
<td align="left"><p>eGenLocSeparate</p></td>
<td align="left"><p>On separate chassis</p></td>
</tr>
<tr class="even">
<td align="left"><p>eGenLocOther</p></td>
<td align="left"><p>Other location</p></td>
</tr>
</tbody>
</table>

 

**PortConnection**  
Specifies the type of port represented by the jack. The value of this member is one of the **EPxcPortConnection** enumeration values shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Port connection type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ePortConnJack</p></td>
<td align="left"><p>Jack</p></td>
</tr>
<tr class="even">
<td align="left"><p>ePortConnIntegratedDevice</p></td>
<td align="left"><p>Slot for an integrated device</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ePortConnBothIntegratedAndJack</p></td>
<td align="left"><p>Both a jack and a slot for an integrated device</p></td>
</tr>
<tr class="even">
<td align="left"><p>ePortConnUnknown</p></td>
<td align="left"><p>Unknown</p></td>
</tr>
</tbody>
</table>

 

**IsConnected**  
Indicates whether there is an external device connected to the jack. If the audio controller supports jack detection on this pin, the value of **IsConnected** should accurately indicate whether the jack is occupied by a plug at any given time. This value should always be set to **TRUE** for devices that do not support jack detection.

Remarks
-------

This structure is used by the [**KSPROPERTY\_JACK\_DESCRIPTION**](ksproperty-jack-description.md) property in Windows Vista and later. It describes an audio jack that is part of a connection between an endpoint device and a hardware device in an audio adapter. When a user needs to plug an endpoint device into a jack or unplug it from a jack, an audio application can use the descriptive information in the structure to help the user to find the jack.

When an audio device does not expose a physically accessible jack, the audio device uses the **eGeoLocNotApplicable** value to indicate to Windows and Windows-based apps that there is no physical jack. As such, there is no geometric location either. For example, the audio device can be integrated into the motherboard, without any accessible jacks.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY\_JACK\_DESCRIPTION**](ksproperty-jack-description.md)

 

 






