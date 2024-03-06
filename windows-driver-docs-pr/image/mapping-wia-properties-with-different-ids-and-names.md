---
title: Mapping WIA Properties with Different IDs and Names
description: Mapping WIA properties with different IDs and names
ms.date: 05/09/2023
---

# Mapping WIA properties with different IDs and names

> [!IMPORTANT]
> This article contains information that applies to obsolete Windows operating systems.

There are Windows XP properties that have different property IDs and different property names from their Windows Vista counterparts. The following is a table of these Windows XP root properties and the FLATBED and FEEDER (ADF) properties that they are translated to in Windows Vista.

| Windows XP property | Windows XP item/context | Windows Vista property | Windows Vista item |
|--|--|--|--|
| WIA_DPS_HORIZONTAL_BED_SIZE | Root | WIA_IPS_MAX_HORIZONTAL_SIZE | FLATBED |
| Read-only access | Root item, no context specified for Windows XP | Read-only access | FLATBED item or FLATBED context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FLATBED)|
| WIA_DPS_VERTICAL_BED_SIZE | Root | WIA_IPS_MAX_VERTICAL_SIZE | FLATBED |
| Read-only access | Root item, no context specified for Windows XP | Read-only access |FLATBED item or FLATBED context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FLATBED)|
| WIA_DPS_HORIZONTAL_SHEET_FEED_SIZE | Root | WIA_IPS_MAX_HORIZONTAL_SIZE | FEEDER |
| Read-only access | Root item, no context specified for Windows XP | Read-only access | FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FEEDER) |
| WIA_DPS_VERTICAL_SHEET_FEED_SIZE | Root | WIA_IPS_MAX_HORIZONTAL_SIZE | FEEDER |
| Read-only access | Root item, no context specified for Windows XP | Read-only access | FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FEEDER) |
| WIA_DPS_MIN_HORIZONTAL_SHEET_FEED_SIZE | Root | WIA_IPS_MIN_HORIZONTAL_SIZE | FEEDER |
| Read-only access | Root item, no context specified for Windows XP | Read-only access | FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FEEDER) |
| WIA_DPS_MIN_VERTICAL_SHEET_FEED_SIZE | Root | WIA_IPS_MIN_VERTICAL_SIZE | FEEDER |
| Read-only access | Root item, no context specified for Windows XP | Read-only access | FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FEEDER) |
| Generic value: 1 | NA | WIA_IPS_MIN_HORIZONTAL_SIZE | FLATBED |
| | | Read-only access |FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FEEDER)
| Generic value: 1 | NA | WIA_IPS_MIN_VERTICAL_SIZE | FLATBED |
| | | Read-only access |FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FEEDER)
