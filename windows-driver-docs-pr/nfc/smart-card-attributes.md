---
title: Supported smart card attributes
description: This topic describes supported smart card attributes.
ms.date: 12/01/2022
---

# Supported smart card attributes

This topic describes the smart card attributes currently supported. The only supported attributes are listed below; all other attributes defined in the Winsmcrd.h are returned as STATUS_NOT_SUPPORTED. The attributes are described in *Interoperability Specification for ICCs and Personal Computer Systems*.

| Attribute Tag | Description |
|---|---|
| CARD_ATTR_CURRENT_PROTOCOL_TYPE | SCARD_PROTOCOL_T1 |
| SCARD_ATTR_CURRENT_CLK | 13560 (little endian integer of 13.56MHz) |
| SCARD_ATTR_CURRENT_D | 1 |
| SCARD_ATTR_CURRENT_IFSC | 32 |
| SCARD_ATTR_CURRENT_IFSD | 254 |
| SCARD_ATTR_CURRENT_BWT | 4 |
| SCARD_ATTR_DEFAULT_CLK | 13560 |
| SCARD_ATTR_MAX_CLK | 13560 |
| SCARD_ATTR_DEFAULT_DATA_RATE | 1 |
| SCARD_ATTR_MAX_DATA_RATE | 1 |
| SCARD_ATTR_CHARACTERISTICS | SCARD_READER_CONTACTLESS |
| SCARD_ATTR_MAX_IFSD | 254 |
| SCARD_ATTR_VENDOR_NAME | ASCII string |
| SCARD_ATTR_VENDOR_IFD_TYPE | ASCII string |
| SCARD_ATTR_VENDOR_IFD_VERSION | 0x01000010, version 1.0.0.1 |
| SCARD_ATTR_PROTOCOL_TYPES | SCARD_PROTOCOL_T1 |
| SCARD_ATTR_DEVICE_UNIT | 0 |
| SCARD_ATTR_CHANNEL_ID | DWORD encoded as 0xDDDDCCCC, where DDDD is the data channel type, and CCCC is the channel number. See the following table for encodings defined for DDDD. |

The following encodings are defined for SCARD_ATTR_CHANNEL_ID value 0xDDDDCCCC:

| Data channel (DDDD) | Type | Channel number (CCCC) |
|---|---|---|
| 0x0100 | NFC | 0 |
| 0x0200 | UICC | 0 |
| 0x0800 | Embedded SE | 0 |
| 0xFXXX | Vendor-defined channel type | vendor-defined |

## ICC Attributes

| Attribute Tag | Description |
|---|---|
| SCARD_ATTR_ICC_PRESENCE | (1 byte)<ul><li>0 = not present</li><li>1 = card present</li></ul> |
| SCARD_ATTR_ATR_STRING | (32 bytes)<ul><li>ATR stringM</li></ul> |
| SCARD_ATTR_ICC_TYPE_PER_ATR | (1 byte)<ul><li>0 = unknown type</li><li>5 = 14443A</li><li>6 = 14443B</li><li>7 = ISO-15693</li></ul> |
