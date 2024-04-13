---
title: ADFSupportsDuplex Element
description: The required ADFSupportsDuplex element specifies whether the attached automatic document feeder (ADF) supports scanning both sides of the media.
keywords: ["ADFSupportsDuplex element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ADFSupportsDuplex
api_type:
- Schema
ms.date: 03/27/2023
---

# ADFSupportsDuplex element

The required **ADFSupportsDuplex** element specifies whether the attached automatic document feeder (ADF) supports scanning both sides of the media.

## Usage

```xml
<wscn:ADFSupportsDuplex>
  text
</wscn:ADFSupportsDuplex>
```

## Attributes

There are no attributes.

## Text value

Required. A Boolean value that must be 0, 1, false, or true.**false** or **true**

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ADF**](adf.md) |

## Remarks

If the scan device has an ADF that supports duplex scanning, the WSD Scan Service should return 1 (**true**); otherwise, it should return 0 (**false**).

You cannot extend the allowed values for this element.

## See also

[**ADF**](adf.md)
