---
title: Data Indices
description: Data Indices
ms.assetid: 84577544-515a-4fdc-86e5-518182c6c461
keywords:
- data index WDK HID
- index WDK HID data
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Data Indices





The HID parser assigns a *data index* that uniquely identifies each usage described in a top-level collection's [button capability arrays](button-capability-arrays.md) and [value capability arrays](value-capability-arrays.md). Conceptually, a data index is a zero-based array index that a user-mode application or kernel-mode driver can use to access individual control data in a report. The parser assigns a unique set of data indices to each report type supported by each top-level collection.

Capability structures cross-reference usages and data indices in the following way:

-   Each capability structure that describes a usage has its **NotRange.Usage** member set to identify the usage and its **NotRange.DataIndex** member set to the usage's corresponding data index.

-   Each capability structure that describes a usage range has its **Range.UsageMin** and **Range.UsageMax** members set to identify the usage range and its **Range.DataIndexMin** and **Range.DataIndexMax** members set to identify the usage range's corresponding data index range. (*Data index range* specifies a consecutive sequence of data indices; and the number of data indices in a data index range is equal to the number of usages in a corresponding usage range.)

For more information about how to use data indices, see [Extracting and Setting Control Data by Data Indices](extracting-and-setting-control-data-by-data-indices.md).

 

 




