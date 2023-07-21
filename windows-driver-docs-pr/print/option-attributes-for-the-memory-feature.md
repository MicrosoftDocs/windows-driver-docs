---
title: Option attributes for the Memory feature
description: Option attributes for the Memory feature
keywords:
- Memory Feature WDK print
ms.date: 07/19/2023
---

# Option attributes for the Memory feature

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the attributes associated with the Memory feature. For more information about the Memory feature, see [Standard Features](standard-features.md).

| Attribute name | Attribute parameter | Comments |
|--|--|--|
| \***MemConfigKB** | PAIR of numeric values indicating the total and available printer-resident memory, in kilobytes. For example, PAIR (1024, 450) indicates 1024 kilobytes total, 450 kilobytes available, with a GPD-generated option name of "1024KB". | Optional. For more information, see [Describing Printer Memory Configurations](describing-printer-memory-configurations.md). |
| \***MemConfigMB** | PAIR of numeric values indicating the total and available printer-resident memory, in megabytes. For example, PAIR (2, 1) indicates 2 megabytes total, 1 megabyte available, with a GPD-generated option name of "2MB". | Optional. For more information, see [Describing Printer Memory Configurations](describing-printer-memory-configurations.md). |
| \***MemoryConfigKB** | PAIR of numeric values indicating the total and available printer-resident memory, in kilobytes. For example, PAIR (1024, 450) indicates 1024 kilobytes total, 450 kilobytes available. | Optional. For more information, see [Describing Printer Memory Configurations](describing-printer-memory-configurations.md). |

For examples, see the [sample GPD files](sample-gpd-files.md).

For more information about using these attributes, along with examples, see [Describing Printer Memory Configurations](describing-printer-memory-configurations.md).

For information about additional option attributes, see [Option Attributes for All Features](option-attributes-for-all-features.md).
