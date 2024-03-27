---
title: Mapping PTP Format Codes to WIA Format GUIDs
description: Mapping PTP format codes to WIA format GUIDs
ms.date: 05/03/2023
---

# Mapping PTP format codes to WIA format GUIDs

The format of an object is exposed through the [**WIA_IPA_FORMAT**](./wia-ipa-format.md) property as a GUID. The mapping between PTP format codes and WIA GUIDs is shown in the following table:

| PTP Format Code | Object Type | WIA GUID |
|--|--|--|
| 0x3000 | Undefined | Not applicable. |
| 0x3001 | Association | See [Mapping PTP associations to WIA folders](mapping-ptp-associations-to-wia-folders.md) |
| 0x3002 | Script | DATAFMT_SCRIPT |
| 0x3003 | Executable | DATAFMT_EXEC |
| 0x3004 | Text | DATAFMT_UNICODE16 |
| 0x3005 | HTML | DATAFMT_HTML |
| 0x3006 | DPOF | DATAFMT_DPOF |
| 0x3007 | AIFF | AUDFMT_AIFF |
| 0x3008 | WAV | AUDFMT_WAV |
| 0x3009 | MP3 | AUDFMT_MP3 |
| 0x300A | AVI | VIDFMT_AVI |
| 0x300B | MPEG | VIDFMT_MPEG |
| 0x300C | ASF | VIDFMT_ASF |
| 0x3800 | Undefined image | Not applicable. |
| 0x3801 | EXIF/JPEG | WiaImgFmt_JPEG |
| 0x3802 | TIFF/EP | WiaImgFmt_TIFF |
| 0x3803 | FlashPix | WiaImgFmt_FLASHPIX |
| 0x3804 | BMP | WiaImgFmt_BMP |
| 0x3805 | CIFF | WiaImgFmt_CIFF |
| 0x3806 | Undefined (Reserved) | Not applicable. |
| 0x3807 | GIF | WiaImgFmt_GIF |
| 0x3808 | JFIF | WiaImgFmt_JPEG |
| 0x3809 | PCD (PhotoCD Image Pac) | WiaImgFmt_PHOTOCD |
| 0x380A | PICT | WiaImgFmt_PICT |
| 0x380B | PNG | WiaImgFmt_PNG |
| 0x380C | Undefined (Reserved) | Not applicable. |
| 0x380D | TIFF | WiaImgFmt_TIFF |
| 0x380E | TIFF/IT | WiaImgFmt_TIFF |
| 0x380F | JPEG2000 Baseline | WiaImgFmt_JPEG2K |
| 0x3810 | JPEG2000 Extended | WiaImgFmt_JPEG2KX |

The WiaImgFmt_XXX GUIDs are defined in *wiadef.h* header file.
