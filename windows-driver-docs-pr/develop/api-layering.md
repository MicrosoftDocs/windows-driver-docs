---
ms.assetid: 9f14c40b-0d6a-45d0-9c8b-6c5603fee3c6
title: API Layering
description: Windows drivers allow you to create one driver that runs on multiple device types, from embedded systems to tablets and PCs.
ms.date: 04/28/2020
ms.localizationpriority: medium
---

# API Layering

## Overview

API Layering requires that binaries in Windows Driver packages call only those APIs and DDIs that are included in UWP-based editions of Windows 10 or are from a curated set of Win32 APIs. API Layering is an extension of the previous "U" requirement that was a part of DCHU design principles.

To see which platform an API supports, visit the API's documentation page and examine the "Target Platform" section.  Windows Drivers must only use API's or DDI's that have a "Target Platform" listed as "Universal".

## Validating API Layering  

[ApiValidator](https://docs.microsoft.com/windows-hardware/test/hlk/testref/df4a9671-c2aa-4c81-b964-7247fb4799df) is the main tool used to validate API Layering compliance for Windows Drivers.  ApiValidator ships as part of the Windows Driver Kit (WDK).  

See [Validating Windows Drivers](https://review.docs.microsoft.com/en-us/windows-hardware/drivers/develop/validating-windows-drivers) for more details regarding how to use ApiValidator to verify your Windows Driver is adhering to the API Layering requirement.
