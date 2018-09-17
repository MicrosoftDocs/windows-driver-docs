---
title: CancelJobResponse element
description: The required CancelJobResponse operation element acknowledges a client's job cancelation request.
ms.assetid: 754b6cf0-3581-4530-9ad6-6b3a19b540f1
keywords: ["CancelJobResponse element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn CancelJobResponse /
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# CancelJobResponse element


The required **CancelJobResponse** operation element acknowledges a client's job cancelation request.

Usage
-----

``` syntax
<wscn:CancelJobResponse />
</wscn:CancelJobResponse />
```

Attributes
----------

There are no attributes.

Text value
----------

None

## Child elements


There are no child elements.

## Parent elements


There are no parent elements.

Remarks
-------

[**CancelJobRequest**](canceljobrequest.md)

The WSD Scan Service sends a **CancelJobResponse** operation to a client when it successfully processes a client's [**CancelJobRequest**](canceljobrequest.md) operation.

## <span id="see_also"></span>See also


[**CancelJobRequest**](canceljobrequest.md)

 

 






