---
title: General WIA Utility Functions
description: General WIA Utility Functions
ms.date: 04/25/2023
---

# General WIA Utility Functions

You can use the following functions to retrieve the driver item context, retrieve information from the system registry, and copy a string.

| Function | Description |
|--|--|
| [**wiauGetDrvItemContext**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaugetdrvitemcontext) | Gets the driver item context and, optionally, the driver item. |
| [**wiauGetResourceString**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaugetresourcestring) | Gets a resource string, storing it as a **BSTR**. |
| [**wiauGetValidFormats**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaugetvalidformats) | Calls the [**IWiaMiniDrv::drvGetWiaFormatInfo**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetwiaformatinfo) method and makes a list of valid formats, using a specified TYMED value. |
| [**wiauPropInPropSpec**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaupropinpropspec) | Determines whether a specified property specification identifier (ID) is contained in an array of such values. The function optionally gets the index where the property specification ID was found. |
| [**wiauPropsInPropSpec**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaupropsinpropspec) | Determines whether any of a list of property specification IDs is contained within an array of such values. |
| [**wiauRegGetDword**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaureggetdwordw) | Gets a **DWORD** value from the **DeviceData** section of the registry. |
| [**wiauRegGetStr**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaureggetstrw) | Gets a string value from the **DeviceData** section of the registry. |
| [**wiauRegOpenData**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiauregopendataw) | Opens the **DeviceData** registry key. |
| [**wiauSetImageItemSize**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiausetimageitemsize) | Calculates the size and width, in bytes, for an image, based on the current [WIA_IPA_FORMAT](wia-ipa-format.md) setting, and writes the new values to the appropriate properties. |
| [**wiauStrC2C**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrc2c) | Copies an ANSI character string to another ANSI character string. |
| [**wiauStrC2W**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrc2w) | Converts an ANSI character string to a Unicode string. |
| [**wiauStrW2C**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrw2c) | Converts a Unicode string to an ANSI character string. |
| [**wiauStrW2W**](/windows-hardware/drivers/ddi/wiautil/nf-wiautil-wiaustrw2w) | Copies a Unicode string to another Unicode string. |
