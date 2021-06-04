---
title: BCDEdit /timeout
description: The **BCDEdit /timeout** command sets the time to wait, in seconds, before the boot manager selects a default entry. 
ms.date: 09/23/2020
keywords: ["BCDEdit /timeout Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /timeout
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /timeout

The **BCDEdit /timeout** command sets the time to wait, in seconds, before the boot manager selects a default entry. For information about setting the default entry, run "bcdedit /? default".

``` syntax
bcdedit /timeout <timeout>
```

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

## Parameters

**\<timeout\>** *seconds*

Specifies the time to wait, in seconds, before the boot manager selects a default entry.

## Examples

The following command sets the boot manager <timeout> to 30 seconds:

`bcdedit /timeout 30`
