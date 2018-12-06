---
title: Supported smart card attributes
description: This topic describes supported smart card attributes.
ms.assetid:
ms.localizationpriority: medium
ms.date: 10/17/2018
---
# Supported smart card attributes
This topic describes the smart card attributes currently supported. The only supported attributes are listed below; all other attributes defined in the Winsmcrd.h are returned as STATUS_NOT_SUPPORTED. The attributes are described in *Interoperability Specification for ICCs and Personal Computer Systems*.

<table>
    <tbody>
        <tr>
            <th>Attribute Tag</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>CARD_ATTR_CURRENT_PROTOCOL_TYPE</td>
            <td>SCARD_PROTOCOL_T1</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_CURRENT_CLK</td>
            <td>13560 (little endian integer of 13.56MHz)</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_CURRENT_D</td>
            <td>1</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_CURRENT_IFSC</td>
            <td>32</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_CURRENT_IFSD</td>
            <td>254</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_CURRENT_BWT</td>
            <td>4</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_DEFAULT_CLK</td>
            <td>13560</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_MAX_CLK</td>
            <td>13560</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_DEFAULT_DATA_RATE</td>
            <td>1</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_MAX_DATA_RATE</td>
            <td>1</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_CHARACTERISTICS</td>
            <td>SCARD_READER_CONTACTLESS</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_MAX_IFSD</td>
            <td>254</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_VENDOR_NAME</td>
            <td>ASCII string</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_VENDOR_IFD_TYPE</td>
            <td>ASCII string</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_VENDOR_IFD_VERSION</td>
            <td>0x01000010, version 1.0.0.1</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_PROTOCOL_TYPES</td>
            <td>SCARD_PROTOCOL_T1</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_DEVICE_UNIT</td>
            <td>0</td>
        </tr>
        <tr>
            <td>SCARD_ATTR_CHANNEL_ID</td>
            <td>
                DWORD encoded as 0xDDDDCCCC, where DDDD is the data channel type, and CCCC is the channel number. The following encodings are defined for DDDD:
                <table>
                    <tbody>
                        <tr>
                            <th>Data channel (DDDD)</th>
                            <th>Type</th>
                            <th>Channel number (CCCC)</th>
                        </tr>
                        <tr>
                            <td>0x0100</td>
                            <td>NFC</td>
                            <td>0</td>
                        </tr>
                        <tr>
                            <td>0x0200</td>
                            <td>UICC</td>
                            <td>0</td>
                        </tr>
                        <tr>
                            <td>0x0800</td>
                            <td>Embedded SE</td>
                            <td>0</td>
                        </tr>
                        <tr>
                            <td>0xFXXX</td>
                            <td>Vendor-defined channel type</td>
                            <td>vendor-defined</td>
                        </tr><br/>                    </tbody>
                </table>
            </td>
        </tr>
    <tbody>
</table>

## ICC Attributes

<table>
    <tbody>
        <tr>
            <th>Attribute Tag</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>SCARD_ATTR_ICC_PRESENCE</td>
            <td>(1 byte)
                <ul>
                    <li> 0 = not present </li>
                    <li> 1 = card present</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>SCARD_ATTR_ATR_STRING</td>
            <td>(32 bytes)
                <ul>
                    <li> ATR string </li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>SCARD_ATTR_ICC_TYPE_PER_ATR</td>
            <td>(1 byte)
                <ul>
                    <li> 0 = unknown type </li>
                    <li> 5 = 14443A </li>
                    <li> 6 = 14443B </li>
                    <li> 7 = ISO-15693 </li>
                </ul>
            </td>
        </tr>
