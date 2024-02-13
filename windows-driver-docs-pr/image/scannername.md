---
title: ScannerName Element
description: The required ScannerName element specifies the administratively assigned user-friendly name of the scanner.
keywords: ["ScannerName element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ScannerName xml lang "..."
api_type:
- Schema
ms.date: 05/02/2023
---

# ScannerName element

The required **ScannerName** element specifies the administratively assigned user-friendly name of the scanner.

## Usage

```xml
<wscn:ScannerName xml:lang="..."
  lang = "xs:string">
  text
</wscn:ScannerName xml:lang="...">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **lang** | xs:string | No | (Optional) A character string that identifies the languages of the string that string specifies.*string* |

## Text value

A character string that specifies the scanner's user-friendly name.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ScannerDescription**](scannerdescription.md) |

## Remarks

The configuration of the **ScannerName** element's value is implementation-specific; for example, you can configure this value through the scanner's local console or the device's web server. If a device has only one hosted service, its friendly name and **ScannerName** element should have the same value. If the device contains several hosted services, **ScannerName** should identify the scanner.

A scan device can return multiple versions of this element to enable support for multiple localized languages by using the **xml:lang** attribute.

## Examples

The following code example shows how you can use the ScannerName element.

```xml
<wscn:ScannerName xml:lang="en-AU, en-CA, en-GB, en-US">
  Accounting Scanner in Copy Room 2
</wscn:ScannerName>
```

## See also

[**ScannerDescription**](scannerdescription.md)
