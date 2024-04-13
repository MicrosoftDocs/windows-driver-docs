---
title: MediaSides Element
description: The optional MediaSides element contains the parameters that are unique to each physical side of the scanned media.
keywords: ["MediaSides element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn MediaSides wscn MustHonor ""
api_type:
- Schema
ms.date: 05/01/2023
---

# MediaSides element

The optional **MediaSides** element contains the parameters that are unique to each physical side of the scanned media.

## Usage

```xml
<wscn:MediaSides wscn:MustHonor=""
  MustHonor = "xs:string">
  child elements
</wscn:MediaSides wscn:MustHonor="">
```

## Attributes

| Attribute | Type | Required | Description |
|--|--|--|--|
| **MustHonor** | xs:string | No | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Child elements

| Element |
|--|
| [**MediaBack**](mediaback.md) |
| [**MediaFront**](mediafront.md) |

## Parent elements

| Element |
|--|
| [**DocumentFinalParameters**](documentfinalparameters.md) |
| [**DocumentParameters**](documentparameters.md) |

## Remarks

Many duplex-capable scanners allow for setting different scan regions, color processing, and resolutions for each physical side of the scanned media. The **MediaSides** element contains separate data for the front and back sides of the media. Every scan job can have parameters for the media front.

The [**MediaBack**](mediaback.md) element is valid only when the scanner supports duplex scanning, and the current [**InputSource**](inputsource.md) is **ADFDuplex**.

If **InputSource** is **ADFDuplex** and the **MediaBack** element is missing, all parameters that are specified in **MediaFront** will apply to the back side scanning as well.

The client can specify the optional **MustHonor** attribute only when the **MediaSides** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **MediaSides** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

[**InputSource**](inputsource.md)

[**MediaBack**](mediaback.md)

[**MediaFront**](mediafront.md)
