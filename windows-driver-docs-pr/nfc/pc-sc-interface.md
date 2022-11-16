---
title: PC/SC interface for smart cards
description: This topic describes the ATR format for different NFC card types. 
ms.date: 11/16/2022
---

# PC/SC interface for smart cards

The ATR formats for different NFC card types are listed below. Please refer to PC/SC spec \[3.a\] for more details regarding the ATR format.

## ATR format for ISO14443-4 cards

| Byte offset | Value | Designation | Description |
|---|---|---|---|
| 0 | 3B | Initial header |  |
| 1 | 8n | T0 | Higher nibble indicates only presence of TD1. Lower nibble indicates the size of the historical bytes |
| 2 | 80 | TD1 | Presence of TD2 |
| 3 | 01 | TD2 | &nbsp; |
| 4 to 3+N | XX | Historical bytes | For ISO14443A: The historical bytes is from the ATS response</br>For ISO14443B: The historical bytes is from ATTRIB (ATQB) |
| 4+N | XX | TCK | Checksum |

## ATR format for storage cards

| Byte offset | Value | Designation | Description |
|---|---|---|---|
| 0 | 3B | Initial header | &nbsp; |
| 1 | 8n | T0 | Higher nibble indicates only presence of TD1. Lower nibble indicates the size of the historical bytes. |
| 2 | 80 | TD1 | Presence of TD2 |
| 3 | 01 | TD2 | &nbsp; |
| 4 to 3+N | 80 | T1 | Category indicator byte. |
| 4 to 3+N | 4F | TK | Application identifier presence. |
| 4 to 3+N | 0C | TK | Length |
| 4 to 3+N | A0 00 00 03 06 | TK | RID as specified in part 3 supplemental doc from PC/SC |
| 4 to 3+N | SS | TK | Byte for standard. The values should correspond to Table 2 of the supplemental doc. |
| 4 to 3+N | NN | TK | Bytes for card name. The values should correspond to Table 3 of the supplemental doc. |
| 4 to 3+N | 00 00 00 00 | RFU | &nbsp; |
| 4+N | XX | TCK | Check-sum |
