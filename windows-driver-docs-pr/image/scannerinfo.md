---
title: ScannerInfo Element
description: The optional ScannerInfo element contains any administratively assigned descriptive information about the scanner.
keywords: ["ScannerInfo element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScannerInfo xml lang "..."
api_type:
- Schema
ms.date: 05/02/2023
---

# ScannerInfo element

The optional **ScannerInfo** element contains any administratively assigned descriptive information about the scanner.

## Usage

```xml
<wscn:ScannerInfo xml:lang="..."
  lang = "xs:string">
  text
</wscn:ScannerInfo xml:lang="...">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **lang** | xs:string | No | (Optional) A character string that identifies the languages of the string that string specifies.*string* |

## Text value

A character string that provides descriptive information about the scanner.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ScannerDescription**](scannerdescription.md) |

## Remarks

The configuration of the **ScannerInfo** element's value is implementation-specific; for example, you can configure this value through the scanner's local console or the device's web server. A scan device can return multiple versions of this element to enable support for multiple localized languages by using the **xml:lang** attribute.

## Examples

The following code example shows how you can use the ScannerInfo element.

```xml
<wscn:ScannerInfo xml:lang="en-AU, en-CA, en-GB, en-US">
  Out of courtesy to others, please scan only
  small (1-5 page) jobs at this scanner.
</wscn:ScannerInfo>
```

## See also

[**Description**](scannerdescription.md)
