---
title: Storage card requirements
description: This topic describes the APDU requirements for storage cards
ms.date: 11/16/2022
---

# Storage card requirements

This section describes the general APDU command set requirements for non-ISO14443-4 compliant cards (known as storage cards).

## General-Authenticate command

The General-Authenticate command is used to perform the authentication sequence on a MIFARE card. This command is only applicable for MIFARE Mini, Classic 1k and 4k cards.

### General-Authenticate command format

| Command | Class | INS | P1 | P2 | Lc | Data In |
|---|---|---|---|---|---|---|
| General-Authenticate | 0xFF | 0x86 | 0x00 | 0x00 | 0x01 | Address MSB, Address LSB, Key Type A or B, Key Number |

### General-Authenticate response format

| Response |
|---|
| SW1, SW2 |

## Get-Data command

The Get-Data command is used to retrieve information from the contactless NFC tag/card.

### Get-Data command format

| Command | Class | INS | P1 | P2 | L2 |
|---|---|---|---|---|---|
| Get-Data | 0xFF | 0xCA | 0x00: Serial number of the card (ISO14443-A: UID, ISO14443-B: PUPI, Felica: IDm, Jewel: RID)</br></br>0x01: Historical bytes of the card (Type A: Historical bytes from ATR, Type B: ATTRIB response) | 0x00 | 0x00 |

### Get-Data response format

| Response |
|---|
| Data out, SW1, SW2 |

## Load-Key command

The Load-Key command is used to store MIFARE keys in the driver. This command is only applicable for MIFARE Mini, Classic 1k and 4k cards.

### Load-Key command format

| Command | Class | INS | P1 | P2 | Lc | Data In |
|---|---|---|---|---|---|---|
| Load-Key | 0xFF | 0x82 | Key Structure | Key Number | 0x6 | Key Value |

### Load-Key response format

| Response |
|---|
| SW1, SW2 |

## Manage Session command

The implementation of this command should be per the PCSC specification.

### Manage Session command format

| Command | Class | INS | P1 | P2 | Lc | Data In |
|---|---|---|---|---|---|---|
| General Authenticate | 0xFF | 0xC2 | 0x00 | 0x00 | Variable | TLV Data Object |

The following are required TLV data objects to be supported by the driver:

| Tag | Data Object |
|---|---|
| 0x80 | Version data object |
| 0x81 | Start Transparent Session |
| 0x82 | End Transparent Session |

## Read-Binary command

The Read-Binary command is used to read data from the contactless NFC tag/card. The command is applicable only for storage cards (MIFARE Classic/UL, Felica, ISO15693 and Jewel/Topaz cards).

### Read-Binary command format

| Command | Class | INS | P1 | P2 | Lc | Data In | Li |
|---|---|---|---|---|---|---|---|
| Read-Binary | 0xFF | 0xB0 | Address MSB | Address LSB | Length of Data In | Data | Length expected |

### Read-Binary MIFARE family

| Command | CLA | INS | P1 | P2 | Le |
|---|---|---|---|---|---|
| UL READ 16 | 0xFF | 0xB0 | 0x00 | 0x00 to 0x15 | 0x10 |
| CL 1k READ 16 | 0xFF | 0xB0 | 0x00 | 0x00 to 0x3F | 0x10 |
| CL 4k READ 16 | 0xFF | 0xB0 | 0x00 | 0x00 to 0xFF | 0x10 |

### Read-Binary Jewel family

| Command | CLA | INS | P1 | P2 | Le |
|---|---|---|---|---|---|
| READ ALL | 0xFF | 0xB0 | 0x00 | 0x00 | 0x00 |
| RID | 0xFF | 0xB0 | 0x00 | 0x00 | 0x06 |
| READ | 0xFF | 0xB0 | Block No | Block Offset | 0x01 |
| READ 8 | 0xFF | 0xB0 | Block No | 0x00 | 0x08 |
| READ SEG | 0xFF | 0xB0 | 0x00 | Segment Addr | 0x80 |

### Read-Binary Felica family

| Command | CLA | INS | P1 | P2 | Lc | Data In |
|---|---|---|---|---|---|---|
| CHECK | 0xFF | 0xB0 | 0x00 | 0x00 | Length of Data In | Number of Service, Number of Blocks, Block list |

### ISO 15693 family

| Command | CLA | INS | P1 | P2 | Le |
|---|---|---|---|---|---|
| READ | 0xFF | 0xB0 | Block Number | 0x00 | 0x04 |

### ISO 15693 family Response

| Response |
|---|
| Data out, SW1, SW2 |

## Transparent exchange command

### Transparent exchange command format

| Command | Class | INS | P1 | P2 | Lc | Data In |
|---|---|---|---|---|---|---|
| General Authenticate | 0xFF | 0xC2 | 0x00 | 0x01 | Variable | TLV Data Object |  |

The following are the required TLV data objects for Transparent Exchange Command to be supported by the driver for transparent exchange of commands to storage cards:

| Tag | Data Object |
|---|---|
| 0x95 | Transceive - Transmit and receive |
| 0x5F46 | Timer |

## Update-Binary command

The Update-Binary command is used to write data to the contactless NFC tag/card. The command is applicable only for storage cards (MIFARE Classic/UL, Felica, ISO15693 and Jewel/Topaz cards). The format of the request and response for the command is as described below.

### Update-Binary command format

| Command | Class | INS | P1 | P2 | Lc | Data In |
|---|---|---|---|---|---|---|
| Update-Binary | 0xFF | 0xD6 | Address MSB | Address LSB | Length of Data In | Data |

### Update-Binary MIFARE family

| Command | CLA | INS | P1 | P2 | Le |
|---|---|---|---|---|---|
| UL WRITE 4 | 0xFF | 0xD6 | 0x00 | 0x00 to 0x15 | 0x04 |
| CL 1k WRITE 16 | 0xFF | 0xD6 | 0x00 | 0x00 to 0x3F | 0x10 |
| CL 4k WRITE 16 | 0xFF | 0xB0 | 0x00 | 0x00 to 0xFF | 0x10 |

### Update-Binary Jewel family

| Command | CLA | INS | P1 | P2 | Le |
|---|---|---|---|---|---|
| WRITE1-E | 0xFF | 0xD6 | Block Number | Block Offset | 0x01 |
| WRITE8-E | 0xFF | 0xD6 | Block Number | 0x00 | 0x08 |

### Update-Binary Felica family

| Command | CLA | INS | P1 | P2 | Le | Data In |
|---|---|---|---|---|---|---|
| UPDATE | 0xFF | 0xD6 | 0x00 | 0x00 | Length of Data In | Number of Service, Number of blocks, Block list |

### Response format

| Command | CLA | INS | P1 | P2 | Le |
|---|---|---|---|---|---|
| WRITE | 0xFF | 0xD6 | Block Number | 0x00 | 0x04 |
