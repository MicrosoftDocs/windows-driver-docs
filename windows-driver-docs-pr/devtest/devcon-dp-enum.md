---
title: DevCon Dp_enum
description: Lists the third-party (OEM) driver packages in the driver store on the local computer.
ms.assetid: 974b34db-ac83-4d92-87d2-067c15492046
keywords:
- DevCon Dp_enum Driver Development Tools
topic_type:
- apiref
api_name:
- DevCon Dp_enum
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DevCon Dp\_enum


Lists the third-party (OEM) driver packages in the driver store on the local computer.

```
    devcon dp_enum
```

### <span id="comments"></span><span id="COMMENTS"></span>Comments

A DevCon Dp\_enum command lists the OEM\*.inf files in the %windir%/Inf on the local computer. For each file, this command displays the provider, class, date, and version number from the INF file.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
devcon dp_enum
```

### <span id="examples"></span><span id="EXAMPLES"></span>Examples

[Example 45: Add and Remove Driver Packages](example-45--add-and-remove-driver-packages.md)









