---
title: Mapping WIA properties with the same IDs and names
description: Mapping WIA properties with the same IDs and names
ms.date: 05/10/2023
---

# Mapping WIA properties with the same IDs and names

> [!IMPORTANT]
> This article contains information that applies to obsolete Windows operating systems.

There are Windows XP properties that have the same property IDs and property names as their Windows Vista counterparts. The following is a table of these Windows XP root properties and the FLATBED and FEEDER (ADF) properties that they are translated to in Windows Vista.

| Windows XP property | Windows XP item/context | Windows Vista property | Windows Vista item |
|--|--|--|--|
| WIA_IPA_ITEM_NAME | Root | WIA_IPA_ITEM_NAME | Root |
| Read-only access, see note: d | See note: c | Read-only access, see note: d | See note: c |
| WIA_IPA_ITEM_NAME or Generic: "FLATBED" | Child / FLATBED | WIA_IPA_ITEM_NAME | FLATBED |
| Read-only access,  see notes: d and e | See note: b | Read-only access, see notes: d and e | See note: b |
| WIA_IPA_ITEM_NAME or Generic: "FEEDER" | Child / FEEDER | WIA_IPA_ITEM_NAME | FEEDER |
| Read-only access, see notes: d and e | See note: a | Read-only access, see notes: d and e | See note: a |
| WIA_IPA_FULL_ITEM_NAME | Root | WIA_IPA_FULL_ITEM_NAME | Root |
| Read-only access, see note: d | See note: c | Read-only access, see note: d | See note: c |
| WIA_IPA_FULL_ITEM_NAME or Generic: "\Root\FLATBED" | Child / FLATBED | WIA_IPA_FULL_ITEM_NAME | FLATBED |
| Read-only access, see notes: d and e | See note: b | Read-only access | See note: b |
| WIA_IPA_FULL_ITEM_NAME or Generic: "\Root\FEEDER" | Child / FEEDER | WIA_IPA_FULL_ITEM_NAME | FEEDER |
| Read-only access | See note: a | Read-only access, see notes: d and e | See note: a |
| WIA_IPA_ITEM_TIME | Child / FLATBED | WIA_IPA_ITEM_TIME | FLATBED |
| Read-only access | See note: b | Read-only access | See note: b |
| WIA_IPA_ITEM_TIME | Child / FEEDER | WIA_IPA_ITEM_TIME | FEEDER |
| Read-only access | See note: a | Read-only access | See note: a |
| WIA_IPA_ITEM_FLAGS | Root | WIA_IPA_ITEM_FLAGS | Root |
| Read-only access, see notes: d and e | See note: c | Read-only access, see notes: d and e | See note: c |
| WIA_IPA_ITEM_FLAGS | Child / FLATBED | WIA_IPA_ITEM_FLAGS | FLATBED |
| Read-only access, see notes: d and e | See note: b | Read-only access, see notes: d and e | See note: b |
| WIA_IPA_ITEM_FLAGS | Child / FEEDER | WIA_IPA_ITEM_FLAGS | FEEDER |
| Read-only access, see notes: d and e | See note: a | Read-only access, see notes: d and e | See note: a |
| WIA_IPA_ACCESS_RIGHTS | Root | WIA_IPA_ACCESS_RIGHTS | Root |
| Read-only access | See note: c | Read-only access | See note: c |
| WIA_IPA_ACCESS_RIGHTS | Child / FLATBED | WIA_IPA_ACCESS_RIGHTS | FLATBED |
| Read-only access | See note: b | Read-only access | See note: b |
| WIA_IPA_ACCESS_RIGHTS | Child / FEEDER | WIA_IPA_ACCESS_RIGHTS | FEEDER |
| Read-only access | See note: a | Read-only access | See note: a |
| WIA_IPA_DATATYPE | Child / FLATBED | WIA_IPA_DATATYPE | FLATBED |
| See note: b | See note: b | Read/Write access | See note: b |
| WIA_IPA_DATATYPE | Child / FEEDER | WIA_IPA_DATATYPE | FEEDER |
| Read/Write access | See note: a | Read/Write access | See note: a |
| WIA_IPA_DEPTH | Child / FLATBED | WIA_IPA_DEPTH | FLATBED |
| Read/Write access | See note: b | Read/Write access | See note: b |
| WIA_IPA_DEPTH | Child / FEEDER | WIA_IPA_DEPTH | FEEDER |
| Read/Write access | See note: a | Read/Write access | See note: a |
| WIA_IPA_PREFERRED_FORMAT | Child / FLATBED | WIA_IPA_PREFERRED_FORMAT | FLATBED |
| Read-only access, see note: f | See note: b | Read-only access, see note: f | See note: b |
| WIA_IPA_PREFERRED_FORMAT | Child / FEEDER | WIA_IPA_PREFERRED_FORMAT | FEEDER |
| Read-only access, see note: f | See note: a | Read-only access, see note: f | See note: a |
| WIA_IPA_FORMAT | Child / FLATBED | WIA_IPA_FORMAT | FLATBED |
| Read/Write access, see notes: h and i | See note: b | Read/Write access, see notes: h and i | See note: b |
| WIA_IPA_FORMAT | Child / FEEDER | WIA_IPA_FORMAT | FEEDER |
| Read/Write access, see notes: h and i | See note: a | Read/Write access, see notes: h and i | See note: a |
| WIA_IPA_COMPRESSION | Child / FLATBED | WIA_IPA_COMPRESSION | FLATBED |
| Read/Write access | See note: b | Read/Write access | See note: b |
| WIA_IPA_COMPRESSION | Child / FEEDER | WIA_IPA_COMPRESSION | FEEDER |
| Read/Write access | See note: a | Read/Write access | See note: a |
| WIA_IPA_TYMED | Child / FLATBED | WIA_IPA_TYMED | FLATBED |
| Read/Write access, see notes: h, i and k | See note: b | Read/Write access, see notes: h, i and k | See note: b |
| WIA_IPA_TYMED | Child / FEEDER | WIA_IPA_TYMED | FEEDER |
| Read/Write access, see notes: h and i | See note: a | Read/Write access, see notes: h and i | See note: a |
| WIA_IPA_CHANNELS_PER_PIXEL | Child / FLATBED | WIA_IPA_CHANNELS_PER_PIXEL | FLATBED |
| Read-only access | See note: b | Read-only access | See note: b |
| WIA_IPA_CHANNELS_PER_PIXEL | Child / FEEDER | WIA_IPA_CHANNELS_PER_PIXEL | FEEDER |
| Read-only access | See note: a | Read-only access | See note: a |
| WIA_IPA_BITS_PER_CHANNEL | Child / FLATBED | WIA_IPA_BITS_PER_CHANNEL | FLATBED |
| Read-only access | See note: b | Read-only access | See note: b |
| WIA_IPA_BITS_PER_CHANNEL | Child / FEEDER | WIA_IPA_BITS_PER_CHANNEL | FEEDER |
| Read-only access | See note: a | Read-only access | See note: a |
| WIA_IPA_ITEM_SIZE | Child / FLATBED | WIA_IPA_ITEM_SIZE | FLATBED |
| Read-only access | See note: b | Read-only access | See note: b |
| WIA_IPA_ITEM_SIZE |  | WIA_IPA_ITEM_SIZE |  |
| Read-only access | See note: a | Read-only access | See note: a |
| WIA_IPA_ICM_PROFILE_NAME | Child / FLATBED | WIA_IPA_ICM_PROFILE_NAME | FLATBED |
| Read/Write access | See note: b | Read/Write access | See note: b |
| WIA_IPA_ICM_PROFILE_NAME | Child / FEEDER | WIA_IPA_ICM_PROFILE_NAME | FEEDER |
| Read/Write access | See note: c | Read/Write access | See note: a |
| WIA_IPA_FILENAME_EXTENSION | Child / FLATBED | WIA_IPA_FILENAME_EXTENSION | FLATBED |
| Read-only access | See note: b | Read-only access | See note: b |
| WIA_IPA_FILENAME_EXTENSION | Child / FEEDER | WIA_IPA_FILENAME_EXTENSION | FEEDER |
| Read-only access | See note: a | Read-only access | See note: a |
| WIA_IPA_SUPPRESS_PROPERTY_PAGE | Child / FLATBED | WIA_IPA_SUPPRESS_PROPERTY_PAGE | FLATBED |
| Read-only access | See note: b | Read-only access | See note: b |
| WIA_IPA_SUPPRESS_PROPERTY_PAGE | Child / FEEDER | WIA_IPA_SUPPRESS_PROPERTY_PAGE | FEEDER |
| Read-only access | See note: a | Read-only access | See note: a |
| Generic: WIA_CATEGORY_ROOT | Root | WIA_IPA_ITEM_CATEGORY | Root |
|  | See note: c | Read-only access, see note: f |  |
| Generic: WIA_CATEGORY_FLATBED | Child / FLATBED | WIA_IPA_ITEM_CATEGORY | FLATBED |
|  | See note: b | Read-only access, see note: f | See note: b |
| Generic: WIA_CATEGORY_FEEDER | Child / FEEDER | WIA_IPA_ITEM_CATEGORY | FEEDER |
|  | See note: a | Read-only access, see note: f | See note: a |
| WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES | Root | WIA_DPS_DOCUMENT_HANDLING_CAPABILITIES | Root |
| Read-only access, see note: l | See note: c | Read-only access, see note: l | See note: c |
| WIA_IPA_BUFFER_SIZE | Child / FLATBED | WIA_IPA_BUFFER_SIZE | FLATBED |
| Read-only access, see note: l | See note: b | Read-only access, see note: l | See note: b |
| WIA_IPA_BUFFER_SIZE | Child / FEEDER | WIA_IPA_BUFFER_SIZE | FEEDER |
| Read-only access, see note: l | See note: a | Read-only access, see note: l | See note: a |
| WIA_IPA_MIN_BUFFER_SIZE | Child / FLATBED | WIA_IPA_MIN_BUFFER_SIZE | FLATBED |
| Read-only access, see note: l | See note: b | Read-only access, see note: l | See note: b |
| WIA_IPA_MIN_BUFFER_SIZE | Child / FEEDER | WIA_IPA_MIN_BUFFER_SIZE | FEEDER |
| Read-only access, see note: l | See note: a | Read-only access, see note: l | See note: a |
| WIA_IPA_PIXELS_PER_LINE | Child / FLATBED | WIA_IPA_PIXELS_PER_LINE | FLATBED |
| Read-only access, see note: m | See note: b | Read-only access, see note: m | See note: b |
| WIA_IPA_PIXELS_PER_LINE | Child / FEEDER | WIA_IPA_PIXELS_PER_LINE | FEEDER |
| Read-only access, see note: m | See note: a | Read-only access, see note: m | See note: a |
| WIA_IPA_NUMBER_OF_LINES | Child / FLATBED | WIA_IPA_NUMBER_OF_LINES | FLATBED |
| Read-only access, see note: m | See note: b | Read-only access, see note: m | See note: b |
| WIA_IPA_NUMBER_OF_LINES | Child / FEEDER | WIA_IPA_NUMBER_OF_LINES | FEEDER |
| Read-only access, see note: m |  | Read-only access, see note: m |  |
| WIA_IPA_BYTES_PER_LINE | Child / FLATBED | WIA_IPA_BYTES_PER_LINE | FLATBED |
| Read-only access, see note: m | See note: b | Read-only access, see note: m | See note: b |
| WIA_IPA_BYTES_PER_LINE | Child / FEEDER | WIA_IPA_BYTES_PER_LINE | FEEDER |
| Read-only access, see note: m | See note: a | Read-only access, see note: m | See note: a |
| WIA_IPA_PLANAR | Child / FLATBED | WIA_IPA_PLANAR | FLATBED |
| Read-only access | See note: b | Read-only access | See note: b |
| WIA_IPA_PLANAR | Child / FEEDER | WIA_IPA_PLANAR | FEEDER |
| Read-only access | See note: a | Read-only access | See note: a |
| WIA_DPS_MAX_SCAN_TIME | Root | WIA_DPS_MAX_SCAN_TIME | Root |
| Read-only access | See note: c | Read-only access | See note: c |

**Note a:**
FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FEEDER).

**Note b:**
FLATBED item or FLATBED context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FLATBED).

**Note c:**
Root item, no context specified for Windows XP.

**Note d:**
Managed by the WIA service.

**Note e:**
Customized for application's application item tree (A-AIT).

**Note f:**
Add to A-AIT even when not supported on driver's application item tree (D-AIT). Set to **WiaImgFmt_BMP**.

**Note g:**
For Windows Vista to Windows XP translation, add **WiaImgFmt_MEMORYBMP** to be used with [TYMED_CALLBACK](understanding-tymed.md).

**Note h:**
For Windows Vista to Windows XP translation, add TYMED_CALLBACK and **WiaImgFmt_MEMORYBMP**. For Windows XP to Windows Vista translation, only [TYMED_FILE](understanding-tymed.md) and TYMED_MULTIPAGE_FILE are translated.

**Note i:**
For Windows XP to Windows Vista translation, translate only:

TYMED_FILE

TYMED_MULTIPAGE_FILE

**Note j:**
For Windows XP to Windows Vista translation, translate only:

DUP

FEED

FLAT

DETECT_FEED

DETECT_FLAT

DETECT_SCAN

**Note k:**
Add to A-AIT even when not supported on D-AIT. Set to TYMED_FILE.

**Note l:**
Add to A-AIT even when not supported on D-AIT.

**Note m:**
Optional for Windows Vista for all transfer-enabled devices. If these properties are implemented, the legacy applications can get estimate on the number of pixels per line, number of bytes required for each scan line, and total number of scan lines in the image. These values are not accurate because the image processing filter might modify the actual values that these properties represent.

If these properties are not supplied by the Windows Vista driver, the compatibility layer in WIA service will add these properties. When these properties are added by WIA service, they will be updated using properties: WIA_IPA_DEPTH, WIA_IPS_XEXTENT, and WIA_IPS_YEXTENT.

When possible, applications should always parse the image header data to get accurate information on the image. They should not rely on this property since it is not accurate.
