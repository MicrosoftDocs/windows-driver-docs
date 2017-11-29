---
title: Storage card requirements
description: This topic describes the APDU requirements for storage cards
ms.assetid:
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Storage card requirements

This section describes the general APDU command set requirements for storage cards.

## General-Authenticate command

The General-Authenticate command is used to perform the authentication sequence on a MIFARE card. This command is only applicable for MIFARE Mini, Classic 1k and 4k cards. 

### Command format

| Command              | Class | INS  | P1   | P2   | Lc   | Data In                                               |
|----------------------|-------|------|------|------|------|-------------------------------------------------------|
| General-Authenticate | 0xFF  | 0x86 | 0x00 | 0x00 | 0x01 | Address MSB, Address LSB, Key Type A or B, Key Number |

### Response format

| Response |
|----------|
| SW1, SW2  |

## Get-Data command

The Get-Data command is used to retrieve information from the contactless NFC tag/card. 

### Command format

<table>
    <tbody>
        <tr>
            <th>Command</th>
            <th>Class</th>
            <th>INS</th>
            <th>P1</th>
            <th>P2</th>
            <th>L2</th>
        </tr>
        <tr>
            <td>Get-Data</td>
            <td>0xFF</td>
            <td>0xCA</td>
            <td>
                <ul>
                    <li>0x00: Serial number of the card (ISO14443-A: UID, ISO14443-B: PUPI, Felica: IDm, Jewel: RID)</li>
                    <li>0x01: Historical bytes of the card (Type A: Historical bytes from ATR, Type B: ATTRIB response)</li>
                </ul>
            </td>
            <td>0x00</td>
            <td>0x00</td>
        </tr>
    <tbody>
</table>

### Response format

| Response           |
|--------------------|
| Data out, SW1, SW2 |

## Load-Key command

The Load-Key command is used to store MIFARE keys in the driver. This command is only applicable for MIFARE Mini, Classic 1k and 4k cards. 

### Command format

| Command  | Class | INS  | P1            | P2         | Lc  | Data In   |
|----------|-------|------|---------------|------------|-----|-----------|
| Load-Key | 0xFF  | 0x82 | Key Structure | Key Number | 0x6 | Key Value |

### Response format

| Response |
|----------|
| SW1, SW2 |

## Manage Session command

The implementation of this command should be per the PCSC specification.

### Command format

| Command              | Class | INS  | P1   | P2   | Lc       | Data In         |
|----------------------|-------|------|------|------|----------|-----------------|
| General Authenticate | 0xFF  | 0xC2 | 0x00 | 0x00 | Variable | TLV Data Object |

The following are required TLV data objects to be supported by the driver:

| Tag  | Data Object               |
|------|---------------------------|
| 0x80 | Version data object       |
| 0x81 | Start Transparent Session |
| 0x82 | End Transparent Session   |

## Read-Binary command

The Read-Binary command is used to read data from the contactless NFC tag/card. The command is applicable only for storage cards (MIFARE Classic/UL, Felica, ISO15693 and Jewel/Topaz cards).

### Command format
| Command     | Class | INS  | P1          | P2          | Lc                | Data In | Li              |
|-------------|-------|------|-------------|-------------|-------------------|---------|-----------------|
| Read-Binary | 0xFF  | 0xB0 | Address MSB | Address LSB | Length of Data In | Data    | Length expected |

### MIFARE Family

| Command       | CLA  | INS  | P1   | P2           | Le   |
|---------------|------|------|------|--------------|------|
| UL READ 16    | 0xFF | 0xB0 | 0x00 | 0x00 to 0x15 | 0x10 |
| CL 1k READ 16 | 0xFF | 0xB0 | 0x00 | 0x00 to 0x3F | 0x10 |
| CL 4k READ 16 | 0xFF | 0xB0 | 0x00 | 0x00 to 0xFF | 0x10 |

### Jewel Family

| Command  | CLA  | INS  | P1       | P2           | Le   |
|----------|------|------|----------|--------------|------|
| READ ALL | 0xFF | 0xB0 | 0x00     | 0x00         | 0x00 |
| RID      | 0xFF | 0xB0 | 0x00     | 0x00         | 0x06 |
| READ     | 0xFF | 0xB0 | Block No | Block Offset | 0x01 |
| READ 8   | 0xFF | 0xB0 | Block No | 0x00         | 0x08 |
| READ SEG | 0xFF | 0xB0 | 0x00     | Segment Addr | 0x80 |

### Felica Family

| Command | CLA  | INS  | P1   | P2   | Lc                | Data In                                         |
|---------|------|------|------|------|-------------------|-------------------------------------------------|
| CHECK   | 0xFF | 0xB0 | 0x00 | 0x00 | Length of Data In | Number of Service, Number of Blocks, Block list |

### ISO 15693 Family

| Command | CLA  | INS  | P1           | P2   | Le   |
|---------|------|------|--------------|------|------|
| READ    | 0xFF | 0xB0 | Block Number | 0x00 | 0x04 |

### Response

| Response           |
|--------------------|
| Data out, SW1, SW2 |

## Transparent exchange command

### Command format
| Command              | Class | INS  | P1   | P2   | Lc       | Data In         |
|----------------------|-------|------|------|------|----------|-----------------|
| General Authenticate | 0xFF  | 0xC2 | 0x00 | 0x01 | Variable | TLV Data Object | 

The following are the required TLV data objects for Transparent Exchange Command to be supported by the driver for transparent exchange of commands to storage cards:

| Tag    | Data Object                       |
|--------|-----------------------------------|
| 0x95   | Transceive - Transmit and receive |
| 0x5F46 | Timer                             |

## Update-Binary command

The Update-Binary command is used to write data to the contactless NFC tag/card. The command is applicable only for storage cards (MIFARE Classic/UL, Felica, ISO15693 and Jewel/Topaz cards). The format of the request and response for the command is as described below.

### Command format
| Command       | Class | INS  | P1          | P2          | Lc                | Data In |
|---------------|-------|------|-------------|-------------|-------------------|---------|
| Update-Binary | 0xFF  | 0xD6 | Address MSB | Address LSB | Length of Data In | Data    |

### MIFARE family
| Command        | CLA  | INS  | P1   | P2           | Le   |
|----------------|------|------|------|--------------|------|
| UL WRITE 4     | 0xFF | 0xD6 | 0x00 | 0x00 to 0x15 | 0x04 |
| CL 1k WRITE 16 | 0xFF | 0xD6 | 0x00 | 0x00 to 0x3F | 0x10 |
| CL 4k WRITE 16 | 0xFF | 0xB0 | 0x00 | 0x00 to 0xFF | 0x10 |

### Jewel family
| Command  | CLA  | INS  | P1           | P2           | Le   |
|----------|------|------|--------------|--------------|------|
| WRITE1-E | 0xFF | 0xD6 | Block Number | Block Offset | 0x01 |
| WRITE8-E | 0xFF | 0xD6 | Block Number | 0x00         | 0x08 |

### Felica family
| Command | CLA  | INS  | P1   | P2   | Le                | Data In                                         |
|---------|------|------|------|------|-------------------|-------------------------------------------------|
| UPDATE  | 0xFF | 0xD6 | 0x00 | 0x00 | Length of Data In | Number of Service, Number of blocks, Block list |

### Response Format
| Command | CLA  | INS  | P1           | P2   | Le  |
|---------|------|------|--------------|------|-----|
| WRITE   | 0xFF | 0xD6 | Block Number | 0x00 | 0x4 |

## Supported smart card attributes

The only supported attributes are listed below; all other attributes defined in the Winsmcrd.h are returned as STATUS_NOT_SUPPORTED. The attributes are described in *Interoperability Specification for ICCs and Personal Computer Systems*.

### Reader attributes

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
                        </tr>                      
                    </tbody>
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