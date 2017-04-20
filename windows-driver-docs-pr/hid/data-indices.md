---
title: Data Indices
author: windows-driver-content
description: Data Indices
ms.assetid: 84577544-515a-4fdc-86e5-518182c6c461
keywords:
- data index WDK HID
- index WDK HID data
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Data Indices


## <a href="" id="ddk-data-indices-kg"></a>


The HID parser assigns a *data index* that uniquely identifies each usage described in a top-level collection's [button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md). Conceptually, a data index is a zero-based array index that a user-mode application or kernel-mode driver can use to access individual control data in a report. The parser assigns a unique set of data indices to each report type supported by each top-level collection.

Capability structures cross-reference usages and data indices in the following way:

-   Each capability structure that describes a usage has its **NotRange.Usage** member set to identify the usage and its **NotRange.DataIndex** member set to the usage's corresponding data index.

-   Each capability structure that describes a usage range has its **Range.UsageMin** and **Range.UsageMax** members set to identify the usage range and its **Range.DataIndexMin** and **Range.DataIndexMax** members set to identify the usage range's corresponding data index range. (*Data index range* specifies a consecutive sequence of data indices; and the number of data indices in a data index range is equal to the number of usages in a corresponding usage range.)

For more information about how to use data indices, see [Extracting and Setting Control Data by Data Indices](extracting-and-setting-control-data-by-data-indices.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Data%20Indices%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


