---
title: DoubleFetch rule (wdm)
description: Learn about the DoubleFetch rule (wdm). 
ms.date: 10/21/2020
keywords: ["DoubleFetch rule (wdm)"]
topic_type:
- apiref
api_name:
- doublefetch
api_type:
- NA
ms.localizationpriority: medium
---

# DoubleFetch rule (wdm)

The **DoubleFetch** rule is an important security rule that checks that a driver is safely accessing buffers that are passed to user-space via IRPs.  The appropriate way to safely send data between a driver and a user-mode component is described in [Using Neither Buffered Nor Direct I/O](../kernel/using-neither-buffered-nor-direct-i-o.md).

A driver should access data buffers following the guidelines and best practices described in [Methods for Accessing Data Buffers](../kernel/methods-for-accessing-data-buffers.md).

This rule checks for double fetch from user mode memory pointers. Double kernel mode accesses of user mode memory can lead to a race condition security issue.  When accessing user mode data, kernel mode code needs to make a copy of the user mode data locally and avoid accessing the user mode data multiple times.  Failing to do so results in a type of problem known as a “double fetch”, where the data may change after it was first accessed.

This rule is available beginning with Windows 10 WDK, build 20236. This rule is only available for *WDM* and *generic* driver types.

**Driver model: WDM, Generic**

## How to test

At compile time:

1. Run [Static Driver Verifier](./static-driver-verifier.md) and specify the **doublefetch** rule.
2. Use the following steps (found in [Using Static Driver Verifier to Find Defects in Windows Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md)) to run an analysis of your code:

    - [Prepare your code (use role type declarations).](./using-static-driver-verifier-to-find-defects-in-drivers.md#preparing-your-source-code)
    - [Run Static Driver Verifier.](./using-static-driver-verifier-to-find-defects-in-drivers.md#running-static-driver-verifier)
    - [View and analyze the results.](./using-static-driver-verifier-to-find-defects-in-drivers.md#viewing-and-analyzing-the-results)

For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md).
