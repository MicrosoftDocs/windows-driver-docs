---
title: Overview of NDIS Debugging
description: Overview of NDIS Debugging
ms.assetid: d15e8a0c-e553-4e0d-84ed-5fdc2026a2d3
keywords: ["NDIS debugging, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Overview of NDIS Debugging


The two primary tools for debugging a network driver are debug tracing and the Network Driver Interface Specification (NDIS) extensions. For more information on debug tracing, see [Enabling NDIS Debug Tracing](enabling-ndis-debug-tracing.md). For more information on the NDIS debugging extensions, see [NDIS Extensions](ndis-extensions--ndiskd-dll-.md), which provides a complete list of the extension commands found in the extension module Ndiskd.dll. The Windows 2000 version of this extension module appears in the w2kfre and w2kchk directories. The Windows XP and later version of this extension module appear in the winxp directory.

An additional tool for debugging a network driver is the collection of regular debugging extensions, which are useful for obtaining debugging information. For example, entering [**!stacks 2 ndis!**](-stacks.md) displays all threads in the stack beginning with **ndis!**. This information can be useful for debugging hangs and stalls.

There is also an NDIS-specific bug check code, bug check 0x7C (BUGCODE\_NDIS\_DRIVER). For a complete list of its parameters, see [**Bug Check 0x7C**](bug-check-0x7c--bugcode-ndis-driver.md).

Another useful tool for testing an NDIS driver is NDIS Verifier. For more information, consult the NDIS Verifier topic in the Windows Driver Kit (WDK) documentation.

 

 





