---
title: PC/SC interface for smart cards
description: This topic describes the ATR format for different NFC card types. 
ms.date: 10/17/2018
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

## ATR format for storage cards
<table>
    <tbody>
        <tr>
            <th>Byte offset</th>
            <th>Value</th>
            <th>Designation</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>0</td>
            <td>3B</td>
            <td>Initial header</td>
        </tr>
        <tr>
            <td>1</td>
            <td>8n</td>
            <td>T0</td>
            <td>Higher nibble indicates only presence of TD1. Lower nibble indicates the size of the historical bytes.</td>
        </tr>
        <tr>
            <td>2</td>
            <td>80</td>
            <td>TD1</td>
            <td>Presence of TD2</td>
        </tr>
        <tr>
            <td>3</td>
            <td>01</td>
            <td>TD2</td>
        </tr>
        <tr>
            <td>4 to 3+N</td>
            <td>80</td>
            <td>T1</td>
            <td>Category indicator byte.</td>
        </tr>
        <tr>
            <td>4 to 3+N</td>
            <td>4F</td>
            <td>TK</td>
            <td>Application identifier presence.</td>
        </tr>
        <tr>
            <td>4 to 3+N</td>
            <td>0C</td>
            <td>TK</td>
            <td>Length</td>
        </tr>
        <tr>
            <td>4 to 3+N</td>
            <td>A0 00 00 03 06</td>
            <td>TK</td>
            <td>RID as specified in part 3 supplemental doc from PC/SC</td>
        </tr>
        <tr>
            <td>4 to 3+N</td>
            <td>SS</td>
            <td>TK</td>
            <td>Byte for standard. The values should correspond to Table 2 of the supplemental doc.</td>
        </tr>
        <tr>
            <td>4 to 3+N</td>
            <td>NN</td>
            <td>TK</td>
            <td>Bytes for card name. The values should correspond to Table 3 of the supplemental doc.</td>
        </tr>
        <tr>
            <td>4 to 3+N</td>
            <td>00 00 00 00</td>
            <td>RFU</td>
            <td></td>
        </tr>
        <tr>
            <td>4+N</td>
            <td>XX</td>
            <td>TCK<td>
            <td>Check-sum</td>
        </tr>
    </tbody>
</table>
