---
title: Private Display-Miniport Driver IOCTL_VIDEO_XXX Requests
description: A miniport driver can define one or more private I/O control codes for its corresponding display driver.
keywords:
- video miniport drivers WDK Windows 2000 , processing requests
- request processing WDK video miniport
- privately-defined IOCTL_VIDEO_XXX requests WDK video miniport
- IOCTL_VIDEO_XXX requests WDK video miniport
- I/O WDK video miniport
ms.date: 12/06/2018
---

# Privately Defined Display-Miniport Driver IOCTL\_VIDEO\_XXX Requests

A miniport driver can define one or more private I/O control codes for its corresponding display driver.

However, only a specific display-and-miniport driver pair can use privately defined I/O control codes. That is, a miniport driver designed to run under an existing display driver should not define private I/O control codes because the existing display driver cannot make new I/O control requests without being rewritten and, possibly, without breaking existing miniport drivers it already uses. An existing or generic display driver layered over many different models of adapters, such as SVGA adapters, also cannot rely on a privately defined I/O control code to have the same effects in every underlying miniport driver.

For more information about defining private I/O control codes, see [Using I/O Control Codes](../kernel/introduction-to-i-o-control-codes.md).

 
