---
title: Mapping WIA Properties with the Same IDs but Different Names
description: Mapping WIA properties with the same IDs but different names
ms.date: 05/10/2023
---

# Mapping WIA properties with the same IDs but different names

> [!IMPORTANT]
> This article contains information that applies to obsolete Windows operating systems.

There are Windows XP properties that have the same property IDs but different property names than their Windows Vista counterparts. The following is a table of these Windows XP root properties and the FLATBED and FEEDER (ADF) properties that they are translated to in Windows Vista.

| Windows XP property | Windows XP item/context | Windows Vista property | Windows Vista item |
|--|--|--|--|
| WIA_DPS_DOCUMENT_HANDLING_SELECT | Root | WIA_IPS_DOCUMENT_HANDLING_SELECT | FEEDER |
| Read/write access See note: d | See note: c | Read/write access See note: d | See note: a |
| WIA_DPS_SHEET_FEEDER_REGISTRATION | Root / FEEDER | WIA_IPS_SHEET_FEEDER_REGISTRATION | FEEDER |
| Read-only access | See note: a | Read-only access | See note: a |
| WIA_DPS_OPTICAL_XRES | Root / FLATBED | WIA_IPS_OPTICAL_XRES | FLATBED |
| Read-only access | See note: b | Read-only access | See note: b |
| WIA_DPS_OPTICAL_XRES | Root / FEEDER | WIA_IPS_OPTICAL_XRES | FEEDER |
| Read-only access | See note: a | Read-only access | See note: a |
| WIA_DPS_OPTICAL_YRES | Root / FLATBED | WIA_IPS_OPTICAL_YRES | FLATBED |
| Read-only access | See note: b | Read-only access | See note: b |
| WIA_DPS_OPTICAL_YRES | Root / FEEDER | WIA_IPS_OPTICAL_YRES | FEEDER |
| Read-only access | See note: a | Read-only access | See note: a |
| WIA_DPS_PAGES | Root / FEEDER | WIA_IPS_PAGES | FEEDER |
| Read/write access | See note: a | Read/write access | See note: a |
| WIA_DPS_PAGE_SIZE | Root / FEEDER | WIA_IPS_PAGE_SIZE | FEEDER |
| Read/write access, see note:e | See note: a | Read/write access, see note:e | See note: a |
| WIA_DPS_PAGE_WIDTH | Root / FEEDER | WIA_IPS_PAGE_WIDTH | FEEDER |
| Read/write access | See note: a | Read/write access | See note: a |
| WIA_DPS_PAGE_HEIGHT | Root / FEEDER | WIA_IPS_PAGE_HEIGHT | FEEDER |
| Read/write access | See note: a | Read/write access | See note: a |
| WIA_DPS_PREVIEW | Root / FLATBED | WIA_IPS_PREVIEW | FLATBED |
| Read/write access | See note: b | Read/write access | See note: b |
| WIA_DPS_PREVIEW | Root / FEEDER | WIA_IPS_PREVIEW | FEEDER |
| Read/write access | See note: a | Read/write access | See note: a |
| WIA_DPS_SHOW_PREVIEW_CONTROL | Root / FLATBED | WIA_IPS_SHOW_PREVIEW_CONTROL | FLATBED |
| Read/write access | See note: c | Read/write access | See note: c |
| WIA_DPS_SHOW_PREVIEW_CONTROL | Root / FEEDER | WIA_IPS_SHOW_PREVIEW_CONTROL | FEEDER |
| Read/write access | See note: a | Read/write access | See note: a |

**Note a:**
FEEDER item (ADF) or FEEDER context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FEEDER)

**Note b:**
FLATBED item or FLATBED context on the Windows XP root or child item (WIA_DPS_DOCUMENT_HANDLING_SELECT is set to FLATBED)

**Note c:**
Root item, no context specified for Windows XP

**Note d:**
For Windows XP to Windows Vista translation only:

BACK_FIRST

BACK_ONLY

DUPLEX

FRONT_FIRST

FRONT_ONLY

FRONT_ONLY is the default if this property is not implemented.

**Note e:**
Translate all values, not just the legacy ones (WIA_PAGE_CUSTOM, WIA_PAGE_A4, WIA_PAGE_LETTER)

The Windows XP root item must be configured into the appropriate FLATBED/FEEDER context set (through WIA_DPS_DOCUMENT_HANDLING_SELECT) before accessing context-dependent property (both for read and write access).
