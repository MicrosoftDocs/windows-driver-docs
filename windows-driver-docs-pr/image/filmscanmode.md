---
title: FilmScanMode element
description: The optional FilmScanMode element specifies the exposure type of the film to be scanned.
keywords: ["FilmScanMode element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn FilmScanMode wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 04/25/2023
---

# FilmScanMode element

The optional **FilmScanMode** element specifies the exposure type of the film to be scanned.

## Usage

```xml
<wscn:FilmScanMode wscn:MustHonor="" wscn:Override="" wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:FilmScanMode wscn:MustHonor="" wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute           | Type      | Required | Description                                                               |
|---------------------|-----------|----------|---------------------------------------------------------------------------|
| **MustHonor**   | xs:string | No       | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **Override**    | xs:string | No       | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **UsedDefault** | xs:string | No       | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Text value

You can both extend and subset the allowed values for this element.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**DocumentFinalParameters**](documentfinalparameters.md) |
| [**DocumentParameters**](documentparameters.md) |

## Remarks

The **FilmScanMode** element is valid only if the [**InputSource**](inputsource.md) element is set to a value of **Film**.

The client can specify the optional **MustHonor** attribute only when the **FilmScanMode** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **FilmScanMode** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**InputSource**](inputsource.md)

[**DocumentParameters**](documentparameters.md)
