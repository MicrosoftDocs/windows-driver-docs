---
title: AV/C Streaming Protocol Driver Function Codes
description: The AV/C Streaming filter driver intercepts IRPs on their way down the device stack.
ms.date: 07/27/2021
ms.localizationpriority: medium
---

# AV/C Streaming Protocol Driver Function Codes

The AV/C Streaming filter driver intercepts IRPs on their way down the device stack.

To communicate with *avcstrm.sys*, subunit drivers must set their IRP's **IoControlCode** member to IOCTL_AVCSTRM_CLASS.

To make I/O requests, include the header file *avcstrm.h*, which is included with the Microsoft Windows Driver Kit (WDK).
