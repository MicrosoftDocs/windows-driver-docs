---
title: WIA_IPA_FILENAME_EXTENSION
description: The WIA_IPA_FILENAME_EXTENSION property contains the file name extension for a particular file format. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPA_FILENAME_EXTENSION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_FILENAME_EXTENSION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/04/2021
ms.localizationpriority: medium
---

# WIA_IPA_FILENAME_EXTENSION

The WIA_IPA_FILENAME_EXTENSION property contains the file name extension for a particular file format. The WIA minidriver creates and maintains this property.

Property Type: VT_BSTR

Valid Values: WIA_PROP_NONE

Access Rights: Read-only

## Remarks

The minidriver updates the WIA_IPA_FILENAME_EXTENSION property to reflect the current value of the [**WIA_IPA_FORMAT**](wia-ipa-format.md) property.

For example, if WIA_IPA_FORMAT is WiaImgFmt_JPEG, WIA_IPA_FILENAME_EXTENSION should be "jpg". If WIA_IPA_FORMAT is WiaImgFmt_BMP, WIA_IPA_FILENAME_EXTENSION should be "bmp". Note that the file name extension does not include the period (".").

The WIA_IPA_FILENAME_EXTENSION property is recommended for drivers that support standard formats and is required for drivers that implement custom-defined formats. WIA_IPA_FILENAME_EXTENSION informs the application of the correct file name extension to use during the transfer of privately formatted files. For example, if the A. Datum Corporation created a WIA driver that transferred a file in a new format, the company could specify an extension of "adc". This extension enables applications to transfer data in that format to a file and to create a file name such as *Myfile.adc*, which is useful to others who understand the new extension.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_FORMAT**](wia-ipa-format.md)
