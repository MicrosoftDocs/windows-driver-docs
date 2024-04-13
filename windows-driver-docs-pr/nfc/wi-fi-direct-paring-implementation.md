---
title: Wi-Fi Direct Pairing Implementation
description: This section provides design guidelines and requirements for a peripheral device to participate in the Tap and Setup and Tap and Reconnect use cases.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# Wi-Fi direct pairing implementation

This section provides design guidelines and requirements for a peripheral device to participate in the Tap and Setup and Tap and Reconnect use cases.

> [!NOTE]
> The pairing implementation described in this topic is currently supported in Windows 8.1, for pairing to printer devices only.
> 
> Windows 10 and later supports NFC to Wi-Fi Direct static connection handover through the Wi-Fi alliance's Wi-Fi P2P Carrier Configuration Record. For more information, see [Wi-Fi Alliance](https://www.wi-fi.org/).

## Peripheral Wi-Fi direct device pairing

During the tap, NFP receives pairing information from the connecting device. NFP passes the pairing information to Windows. Wi-Fi Direct devices follow the Wi-Fi Alliance Out-Of-Band (OOB) pairing procedure and the NFC Forum recommendations. Windows relies on a proprietary pairing message as defined below.

Windows will prompt the user for consent, and if it is given, Windows will attempt to connect to each of the addresses, in order, until one succeeds. There is no further interaction between an NFP provider in the PC and the connecting device.

Using NFC as an example, unidirectional installation is accomplished by storing the pairing information in a static or passive NFC tag (an active NFC tag in static-emulation mode may also be used). Windows subscribes to this pairing information. An NFC-enabled NFP provider on the PC receives the connection information from the tag and passes this to Windows as a subscriber. Upon receipt of the connection information, Windows performs the actual installation of the device in-band using device class specific techniques.

## Interoperability requirements

To ensure interoperability across NFP providers, the pairing information should be encapsulated in a provider-specific message format.

As described elsewhere in this document, there are no specific requirements for proximity technologies other than for NFC-enabled NFP providers.

Windows requires NFC-enabled NFP providers to support a specific NFC Forum–defined mechanism for conveying the Wi-Fi Direct OOB pairing information for unidirectional pairing. The NDEF message contains a first record with a TNF field value of 0x01 and a TYPE field that is equal to "Hs", and an alternative carrier record that points to a Wi-Fi Direct Carrier Configuration Record. In this method, only the PAYLOAD of the NDEF record will be used.

## Unidirectional pairing using NFC for Wi-Fi Direct

This section provides more details on how NFC, Wi-Fi Direct, and Windows work together to support unidirectional wireless pairing for Wi-Fi Direct devices such as printers.

### NFP provider references

Wi-Fi Direct pairing is accomplished using an NFC Forum standardized Connection Handover Select message type. The below graphic provides an overview of how a Connection Handover Select message is applied for Wi-Fi Direct device pairing, specifically NDEF records 3 and 4. The Handover Select message describes one or more "ac" or "Alternate Carrier" records. These records follow the Handover Select record sequentially and each have a well defined type. Finally, the message will contain a Microsoft defined device pairing record which provides Windows with information about how to process the pairing operation.

![connection handover select message.](images/handover.png)

### Wi-Fi Direct device pairing message

In the sample use cases that follow, NFC type 2 tags are used as an illustrative example. If it is necessary to use a different NFC tag type, the NDEF message must be properly encapsulated according to that tag definition.

| Field | Value | Description |
|---|---|---|
| TNF | 0x02 | Format of the Type field that follows. Media-type as defined in RFC 2046. |
| Type | 'application/vnd.ms-windows.wfd.oob' | New type string we define for this scenario. |
| Size of OOB data | WORD | Up to 64 KB of OOB data supported. |
| Wi-Fi Direct OOB data | &lt;blob of size indicated by previous field&gt; | Wi-Fi Direct OOB data as defined below. |

### Wi-Fi Direct OOB format

The following table describes the format of the WiFi Direct OOB data. OOB Unidirectional Data may be transmitted by any unidirectional P2P OOB Device.

| Attributes | Attribute ID | Required/Optional | Note |
|---|---|---|---|
|OOB Header</br></br>See OOB Header attribute format table. | N/A | Required | The OOB Header attribute shall be present in P2P OOB Data blob, and have its OOB Type value set to "OOB Unidirectional Provisioning Data". |
| OOB Device Info</br></br>See OOB Device info attribute format table. | 1 | Required | This attribute must be present. It provides information about this P2P Device. |
| OOB Provisioning Info | 2 | Required | This attribute must be present. It provides provisioning information that this P2P Device is expecting to use. |
| OOB Configuration Timeout | 5 | Required | This attribute must be present. It provides information about how long this P2P Device will wait for a response over Wi-Fi Direct. |

### OOB Header attribute format

| Field Name | Size (octets) | Value | Description |
|---|---|---|---|
| Total Data Length | 2 | Variable | Length of entire OOB Data Blob (including header). |
| Length | 2 | Variable | Length of the following fields in OOB header. |
| Version | 1 | 0x10 | Value identifying the version of this P2P OOB record. |
| OOB Type | 1 | Variable | Value identifying the type of OOB transaction. The specific value is defined in *OOB Transaction Types* table. |
| OUI | 0 or 3 | Variable | Vendor-specific OUI. This is an optional value. Must only be present when OOB Type is Vendor Specific. |
| OUI Type | 0 or 1 | Variable | Vendor-specific Type. This is an optional value. Must only be present when OOB Type is Vendor Specific. |

### OOB transaction types

| OOB Type (Hex) | Description |
|---|---|
| 0x00 | OOB Unidirectional Provisioning Data |
| 0x01 | OOB Provisioning Listener Data |
| 0x02 | OOB Provisioning Connector Data |
| 0x03 | OOB Reinvoke Data |
| 0x04-0xDC | Reserved |
| 0xDD | Vendor-Specific |
| 0xDE-0xFF | Reserved |

### OOB device info attribute format

| Field Name | Size (octets) | Value | Description |
|---|---|---|--- |
| Attribute ID | 1 | 1 | Identifying the type of P2P OOB attribute. The specific value is defined in the P2P OOB Attributes table. |
| Length | 2 | Variable | Length of the following fields in the attribute. |
| P2P Device Address | 6 | As defined in P2P Spec. | An identifier used to uniquely reference a P2P Device. |
| Config Methods | 2 | As defined in P2P Spec. | The WSC Methods that are supported by this device.</br></br>**Note:** Byte ordering within the Config Methods field shall be big-endian. |
| Primary Device Type | 8 | As defined in P2P Spec. | Primary Device Type of the P2P Device. Contains only the Data part of the WSC Primary Device Type attribute (excludes Attribute ID and Length fields).</br></br>**Note:** Byte ordering within the Primary Device Type field shall be big-endian. |
| Device Capability Bitmap | 1 | As defined in P2P Spec. | A set of parameters indicating P2P Device's capabilities. |
| Device Name | Variable | As defined in P2P Spec. | Friendly name of the P2P Device. Contains the entire WSC Device Name attribute TLV format.</br></br>**Note:** Byte ordering within the Device Name field shall be big-endian. |

### P2P OOB attributes

| OOB Type (Hex) | Description |
|---|---|
| 0x00 | OOB Status |
| 0x01 | OOB Device Info |
| 0x02 | OOB Provisioning Info |
| 0x03 | OOB Group ID |
| 0x04 | OOB Listen Channel |
| 0x05 | OOB Configuration Timeout |
| 0x06-0xDC | Reserved |
| 0xDD | Vendor specific attribute |
| 0xDE-0xFF | Reserved |

### OOB provisioning info attribute format

| Field Name | Size (octets) | Value | Description |
|---|---|---|---|
| Attribute ID | 1 | 1 | Identifying the type of P2P OOB attribute. The specific value is defined in *P2P OOB Attributes* table. |
| Length | 2 | Variable | Length of the following fields in the attribute. |
| Provisioning Settings Bitmap | 1 | Variable | A set of provisioning settings options, as defined the *Provisioning settings* table. |
| Selected Config Method | 2 | As defined in P2P Spec. | The WSC Method that was selected by this P2P device for provisioning. |
| Pin Length | 1 | 0 - 8 | Number of bytes in the following PIN Data field. This field set to 0 indicates no additional PIN data. |
| Pin Data | Variable | n | This field is optional. This field is present only if the PIN Length field is not 0, and contains an array of octets which represent a PIN to be used for provisioning. |

### Provisioning settings

| Bits(s) | Information | Notes |
|---|---|---|
| 0 | Create New Group | The Create New Group bit is set to 1 if this provisioning info is for forming a new group with the target P2P device. Otherwise, this provisioning info is for joining an existing group. |
| 1 | Enforce Group Type Setting | The Enforce Group Type Setting bit is set to 1 if Desired Group Type bit must be enforced, Otherwise, Desired Group Type bit is simply a preference. |
| 2 | Desired Group Type | Desired Group Type bit shall be set to 0 if Desired Group Type is transient, and shall be set to 1 if Desired Group Type is persistent. |
| 3 - 7 | Reserved | &nbsp; |

### OOB configuration timeout attribute format

| Field Name | Size (octets) | Value | Description |
|---|---|---|---|
| Attribute ID | 1 | 5 | Identifying the type of P2P OOB attribute. The specific value is defined in *P2P OOB Attributes* table. |
| Length | 2 | 1 | Length of the following fields in the attribute. |
| Listener Configuration Timeout | 1 | 0 - 255 | Amount of time this P2P device will spend waiting for Wi-Fi Direct communication after OOB data transfer, in units of 100 milliseconds. (Maximum of 25.5 seconds). |

### Windows device pairing record

The Windows Device Pairing Record follows the NDEF specification. It provides additional information to Windows about how to process the Connection Handover Select message. The TNF and Type fields must be specified according to the NDEF specification. The other fields below will be sequentially listed in the Payload field of the NDEF record.

| Field Name | Value | Length Value | Description |
|---|---|---|---|
| TNF | 0x02 | 3 bits | Format of the Type field that follows. Media-type as defined in RFC 2046. |
| Type | 'application/vnd.ms-windows.devicepairing' | 0x28 bytes | New type string we define for this scenario. |
| MajorVersion | 0x1 | 2 bytes | Major version is required to be 0x1. |
| MinorVersion | 0x0 | 2 bytes | Minor version is required to be 0x0. |
| Flags | 0x0 or 0x01 | 4 bytes | Set to 0x0 to try all transports.</br></br>Set to 0x1 to attempt installation sequentially and stop after first success. Preference for transports is indicated by sequence of alternate carrier records.</br></br>**Note** Values 0x0002 through 0x0064 are reserved. |
| Length of device friendly name | Length of device friendly name field. | 1 byte | Length of Device friendly name. |
| Device friendly name | UTF-8 encoded string up to 255 bytes. | Length of device friendly name | Friendly name for the device which will be shown in consent UI on the client. |

### Wi-Fi Direct just works ceremony, static connection handover tag format

As an example, the following is a typical implementation for an NFC passive tag. This corresponds to a static connection handover case with a Wi-Fi Direct carrier record, a network share printer, and the ms-device pairing record.

This first table illustrates the format of the Wi-Fi Direct pairing portion of the tag.

| Offset | Content | Length | Explanation |
|---|---|---|---|
| 0 | 0x91 | 1 | NDEF Record Header:</br></br>MB=1b, ME=0b, CF=0b, SR=1b, IL=0b, TNF=001b |
| 1 | 0x02 | 1 | Record Type Length: 2 octets |
| 2 | 0x0A | 1 | Record Type Length: 10 octets |
| 3 | 0x48 0x73 | 2 | Record Type: "Hs" |
| 5 | 0x12 | 1 | Version Number: Major = 1, Minor = 2 |
| 6 | 0xD1 | 1 | NDEF Record Header:</br></br>MB=1b, ME=1b, CF=0b, SR=1b, IL=0b, TNF=001b |
| 7 | 0x02 | 1 | Record Type Length: 2 octets |
| 8 | 0x04 | 1 | Payload Length: 4 octets |
| 9 | 0x61 0x63 | 2 | Record Type: "ac" |
| 11 | 0x01 | 1 | Carrier Flags: CPS=1, "active" |
| 12 | 0x01 | 1 | Carrier Data Reference Length: 1 octet |
| 13 | 0x30 | 1 | Carrier Data Reference: "0" |
| 14 | 0x00 | 1 | Auxiliary Data Reference Count: 0 |
| 15 | 0x1A | 1 | NDEF Record Header:</br></br>MB=0b, ME=0b, CF=0b, SR=1b, IL=1b, TNF=010b |
| 16 | 0x22 | 1 | Record Type Name Length: 34 octets |
| 17 | 0x3E | 1 | Payload Length: 62 octets |
| 18 | 0x01 | 1 | Id Length: 1 octet |
| 19 | 0x61&nbsp;0x70&nbsp;0x70&nbsp;0x6C</br></br>0x69&nbsp;0x63&nbsp;0x61&nbsp;0x74</br></br>0x69&nbsp;0x6F&nbsp;0x6E&nbsp;0x2F</br></br>0x76&nbsp;0x6E&nbsp;0x64&nbsp;0x2E</br></br>0x6D&nbsp;0x73&nbsp;0x2D&nbsp;0x77</br></br>0x69&nbsp;0x6E&nbsp;0x64&nbsp;0x6F</br></br>0x77&nbsp;0x73&nbsp;0x2E&nbsp;0x77</br></br>0x66&nbsp;0x64&nbsp;0x2E&nbsp;0x6F</br></br>0x6F&nbsp;0x62 | 34 | Record Type Name: 'application/vnd.ms-windows.wfd.oob' |
| 53 | 0x30 | 1 | Id: "0" |
| 54 | 0x3E 0x00 | 2 | Wi-Fi Direct OOB data length: 62 octets. The length is read as an unsigned short and is inclusive of the entire blob. Includes 2 length octets. This value must be stored in little-endian format. |
| 56 | 0x02, 0x00 | 2 | Header length: 2 octets |
| 58 | 0x10 | 1 | Version: 0x10 |
| 59 | 0x00 | 1 | OOB type: 0x00 (unidirectional) |
| 60 | 0x01 | 1 | Attribute: 0x01 (Device information attribute) |
| 61 | 0x22 0x00 | 2 | Device information length: 34 octets |
| 63 | 0x01&nbsp;0x23&nbsp;0x34&nbsp;0xab</br></br>0xcd&nbsp;0xef | 6 | Wi-Fi Direct P2P device MAC address: "01:23:34:ab:cd:ef" |
| 69 | 0x01 0x00 | 2 | Config type |
| 71 | 0x00&nbsp;0x01&nbsp;0x00&nbsp;0x50</br></br>0xF2&nbsp;0x00&nbsp;0x00&nbsp;0x00 | 8 | Primary device type |
| 79 | 0x12 | 1 | Capability |
| 80 | 0x10 0x11 | 2 | Attribute: Device name |
| 82 | 0x00 0x0d | 2 | Device name length: 13 octets |
| 84 | 0x43&nbsp;0x6f&nbsp;0x6e&nbsp;0x74</br></br>0x6f&nbsp;0x73&nbsp;0x6f&nbsp;0x20</br></br>0x4d&nbsp;0x6f&nbsp;0x75&nbsp;0x73</br></br>0x65 | 13 | Device friendly name in UTF-8. Note that there is no NULL terminating character and that UTF-8 may be one or two bytes per character. This example reads "Contoso Mouse" |
| 97 | 0x02 | 1 | Attribute: provisioning info |
| 98 | 0x0c 0x00 | 2 | Provisioning info length: 12 octets |
| 100 | 0x07 | 1 | Setting bitmap: new group, enforce persistent |
| 101 | 0x01 0x00 | 2 | Config method: pin entry |
| 103 | 0x08 | 1 | Pin length: 8 octets |
| 104 | 0x01&nbsp;0x02&nbsp;0x03&nbsp;0x04</br></br>0x05&nbsp;0x06&nbsp;0x07&nbsp;0x08 | 8 | Pin: "12345678" |
| 112 | 0x05 | 1 | Attribute: Configuration timeout information |
| 113 | 0x01 0x00 | 2 | Configuration timeout length |
| 115 | 0x64 | 1 | 10 seconds, in 100 millisecond units |

This second table illustrates the format of the network printer pairing portion of the tag.

| Offset | Content | Length | Explanation |
|---|---|---|---|
| 116 | 0x12 | 1 | NDEF record header:</br>MB=0b,ME=0b, CF=0b, SR=1b, IL=0b,TNF=010b |
| 117 | 0x29 | 1 | Type length field |
| 118 | 0x19 | 1 | Payload length field |
| 119 | 0x61 0x70 0x70 0x6c</br></br>0x69 0x63 0x61 0x74</br></br>0x69 0x6f 0x6e 0x2f</br></br>0x76 0x6e 0x64 0x2e</br></br>0x6d 0x73 0x2d 0x77</br></br>0x69 0x6e 0x64 0x6f</br></br>0x77 0x73 0x2e 0x6e</br></br>0x77 0x70 0x72 0x69</br></br>0x6e 0x74 0x69 0x6e</br></br>0x67 0x2e 0x6f 0x6f</br></br>0x62 | 41 | Record type name: "application/vnd.ms-windows.nwprinting.oob" |
| 160 | 0x5c 0x5c 0x70 0x72</br></br>0x69 0x6e 0x74 0x53</br></br>0x65 0x72 0x76 0x65</br></br>0x72 0x5c 0x70 0x72</br></br>0x69 0x6e 0x74 0x65</br></br>0x72 0x4e 0x61 0x6d</br></br>0x65 | 25 | Printer name: "\printServer\printerName" |

This third table illustrates the format of the MS-Device pairing portion of the tag.

| Offset | Content | Length | Explanation |
|---|---|---|---|
| 185 | 0x52 | 1 | NDEF record header:</br></br>MB=0b, ME=1b, CF=0b, SR=1b, IL=0b,TNF=010b |
| 186 | 0x28 | 1 | Type length field |
| 187 | 0x15 | 1 | Payload length field |
| 188 | 0x61 0x70 0x70 0x6c</br></br>0x69 0x63 0x61 0x74</br></br>0x69 0x6f 0x6e 0x2f</br></br>0x76 0x6e 0x64 0x2e</br></br>0x6d 0x73 0x2d 0x77</br></br>0x69 0x6e 0x64 0x6f</br></br>0x77 0x73 0x2e 0x64</br></br>0x65 0x76 0x69 0x63</br></br>0x65 0x70 0x61 0x69</br></br>0x72 0x69 0x6E 0x67 | 40 | Record type name: "application/vnd.ms-windows.devicepairing" |
| 228 | 0x00 0x01 0x00</br></br>0x00 | 4 | Version: Major = 1, Minor = 0 |
| 232 | 0x00 | 1 | Flags: Set to 0, try all transports |
| 233 | 0x0F | 1 | Length of device friendly name |
| 234 | 0x43 0x6f 0x6e 0x74</br></br>0x6f 0x73 0x6f 0x20</br></br>0x50 0x72 0x69 0x6e</br></br>0x74 0x65 0x72 | 15 | The device friendly name displayed to the user: "Contoso Printer" |

## Wi-Fi Direct connectivity requirements

Devices and clients must have the Wi-Fi radio turned on. If not, pairing will fail.

## Handling edge cases

If a user has previously paired a device, but then manually removes the device from the device list, tapping again will result in an attempt to install or pair.

If a user enters into the range of actuation but then suddenly leaves before the out-of-band (OOB) information is transferred, the device may become connectable but the PC will not look for the device. In this case, there will be no consent UI from the PC and the user will need to tap again. If the device is already discoverable when it is tapped again, it should remain discoverable and should reset the timeout period.

For Wi-Fi Direct devices, if the Wi-Fi radio turns off then the installation will not be successful.

If a user taps two devices at approximately the same time, only the pairing for the first received OOB information will be attempted.

Any attempt to tap the device on a system running an operating system that doesn't support Tap to Setup or Tap to Reconnect may result in the device going into connectable mode but pairing will not take place. Users will need to use a pairing UI provided for Bluetooth and use the pairing button to initiate pairing.

## Related topics

- [NFC device driver interface (DDI) reference](/windows-hardware/drivers/ddi/index)
