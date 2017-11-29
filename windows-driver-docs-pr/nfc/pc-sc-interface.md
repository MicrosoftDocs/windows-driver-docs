---
title: PC/SC interface for smart cards
description: This topic describes the ATR format for different NFC card types. 
ms.assetid:
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PC/SC interface for smart cards

The ATR formats for different NFC card types are listed below. Please refer to PC/SC spec [3.a] for more details regarding the ATR format.

## ATR format for ISO14443-4 cards

| Byte offset | Value | Designation      | Description                                                                                                                 |
|-------------|-------|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| 0           | 3B    | Initial header   |                                                                                                                             |
| 1           | 8n    | T0               | Higher nibble indicates only presence of TD1. Lower nibble indicates the size of the historical bytes                       |
| 2           | 80    | TD1              | Presence of TD2                                                                                                             |
| 3           | 01    | TD2              |                                                                                                                             |
| 4 to 3+N    | XX    | Historical bytes | For ISO14443A: The historical bytes is from the ATS response <br> For ISO14443B: The historical bytes is from ATTRIB (ATQB) |
| 4+N         | XX    | TCK              | Checksum                                                                                                                    |

## ATR format for storage carks

| Byte offset | Value                                                       | Designation      | Description                                                                                                                                                                                                                                                                                                           |
|-------------|-------------------------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0           | 3B                                                          | Initial header   |                                                                                                                                                                                                                                                                                                                       |
| 1           | 8n                                                          | T0               | Higher nibble indicates only presence of TD1. Lower nibble indicates the size of the historical bytes                                                                                                                                                                                                                 |
| 2           | 80                                                          | TD1              | Presence of TD2                                                                                                                                                                                                                                                                                                       |
| 3           | 01                                                          | TD2              |                                                                                                                                                                                                                                                                                                                       |
| 4 to 3+N    | XX                                                          | Historical bytes | For ISO14443A: The historical bytes is from the ATS response <br> For ISO14443B: The historical bytes is from ATTRIB (ATQB)                                                                                                                                                                                           |
| 4+N         | 80<br>4F<br>0C<br>A0 00 00 03 06<br>SS<br>NN<br>00 00 00 00 | TK               | Category indicator byte<br>Application identifier presence<br>Length<br>RID as specified in part 3 supplemental doc from PC/SC<br>Byte for standard. The values should correspond to Table 2 of the supplemental doc<br>Bytes for card name. The values should correspond to Table 3 of the supplemental doc<br> <br> |
