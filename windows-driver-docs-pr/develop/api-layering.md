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

To see which platform an API supports, visit the documentation page for the API and examine the **Target Platform** entry of the Requirements section.  Windows Drivers must only use APIs or DDIs that have a **Target Platform** listed as `Universal`, meaning the subset of functionality that is available on all Windows offerings.

## Validating API Layering  

[ApiValidator](/windows-hardware/test/hlk/testref/df4a9671-c2aa-4c81-b964-7247fb4799df) is the main tool used to validate API Layering compliance for Windows Drivers.  ApiValidator ships as part of the Windows Driver Kit (WDK).  

See [Validating Windows Drivers](validating-windows-drivers.md) for more details on using ApiValidator to verify that a Windows Driver meets the API Layering requirement.