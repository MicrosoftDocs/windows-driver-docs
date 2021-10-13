---
title: AV/C Protocol Driver Function Codes
description: An AV/C subunit driver communicates with its device by submitting IRPs down the device stack to the AV/C protocol driver,
ms.date: 07/26/2021
ms.localizationpriority: medium
---

# AV/C Protocol Driver Function Codes

An AV/C subunit driver communicates with its device by submitting IRPs down the device stack to the AV/C protocol driver, *avc.sys*.

To make I/O requests, include the header file *avc.h*, which is included with the Microsoft Windows Driver Kit (WDK).
