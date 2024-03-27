---
title: ImagesToTransfer Element
description: The optional ImagesToTransfer element specifies the number of images to scan for the current job.
keywords: ["ImagesToTransfer element Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- wscn ImagesToTransfer wscn MustHonor "" wscn Override "" wscn UsedDefault ""
api_type:
- Schema
ms.date: 04/28/2023
---

# ImagesToTransfer element

The optional **ImagesToTransfer** element specifies the number of images to scan for the current job.

## Usage

```xml
<wscn:ImagesToTransfer wscn:MustHonor="" wscn:Override="" wscn:UsedDefault=""
  MustHonor = "xs:string"
  Override = "xs:string"
  UsedDefault = "xs:string">
  text
</wscn:ImagesToTransfer wscn:MustHonor="" wscn:Override="" wscn:UsedDefault="">
```

## Attributes

| Attribute           | Type      | Required | Description                                                               |
|---------------------|-----------|----------|---------------------------------------------------------------------------|
| **MustHonor**   | xs:string | No       | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **Override**    | xs:string | No       | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |
| **UsedDefault** | xs:string | No       | Optional. A Boolean value that must be 0, false, 1, or true.**falsetrue** |

## Text value

Required. An integer in the range from 0 through 2147483648.

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**DocumentFinalParameters**](documentfinalparameters.md) |
| [**DocumentParameters**](documentparameters.md) |

## Remarks

The **ImagesToTransfer** value is useful when the scan device has a document feeder that can contain more pages of media than the current job.

When the value is 0, the device scans as many pages as are available for the selected input source which is specified in the [**InputSource**](inputsource.md) element. If the input source is **Platen** or **Film**, a value of 0 in **ImagesToTransfer** will yield a single image acquisition. If the input source is **ADF** or **ADFDuplex**, a value of 0 in **ImagesToTransfer** indicates that device should acquire images until the feeder is empty.

When the device acquires images from **ADFDuplex**, each side of the media represents a single image. When an odd value is specified for **ADFDuplex**, the device will acquire only the front side of the last sheet of media.

The client can specify the optional **MustHonor** attribute only when the **ImagesToTransfer** element is contained within a **CreateScanJobRequest** hierarchy. For more information about **MustHonor** and its usage, see [**CreateScanJobRequest**](createscanjobrequest.md).

The WSD Scan Service can specify the optional **Override** and **UsedDefault** attributes only when the **ImagesToTransfer** element is contained within a **DocumentFinalParameters** hierarchy. For more information about **Override** and **UsedDefault** and their usage, see [**DocumentFinalParameters**](documentfinalparameters.md).

## See also

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DocumentFinalParameters**](documentfinalparameters.md)

[**DocumentParameters**](documentparameters.md)

[**InputSource**](inputsource.md)
