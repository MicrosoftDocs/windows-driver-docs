---
title: ScannerLocation Element
description: The optional ScannerLocation element specifies the administratively assigned location of the scanner.
keywords: ["ScannerLocation element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScannerLocation xml lang "..."
api_type:
- Schema
ms.date: 05/02/2023
---

# ScannerLocation element

The optional **ScannerLocation** element specifies the administratively assigned location of the scanner.

## Usage

```xml
<wscn:ScannerLocation xml:lang="..."
  lang = "xs:string">
  text
</wscn:ScannerLocation xml:lang="...">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **lang** | xs:string | No | (Optional) A character string that identifies the languages of the string that string specifies.*string* |

## Text value

A character string that specifies the scanner's location.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ScannerDescription**](scannerdescription.md) |

## Remarks

The configuration of the **ScannerLocation** element's value is implementation-specific; for example, you can configure this value through the scanner's local console or the device's web server. A scan device can return multiple versions of this element to enable support for multiple localized languages by using the **xml:lang** attribute.

## Examples

The following code example shows how you can use the ScannerLocation element.

```xml
<wscn:ScannerLocation xml:lang="en-AU, en-CA, en-GB, en-US">
  LA Campus - Building 1
</wscn:ScannerLocation>
```

## See also

[**ScannerDescription**](scannerdescription.md)
