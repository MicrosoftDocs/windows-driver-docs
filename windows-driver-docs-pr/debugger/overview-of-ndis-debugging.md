---
title: Overview of NDIS Debugging
description: Overview of NDIS Debugging
ms.assetid: d15e8a0c-e553-4e0d-84ed-5fdc2026a2d3
keywords: ["NDIS debugging, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Overview of NDIS Debugging


The two primary tools for debugging a network driver are debug tracing and the Network Driver Interface Specification (NDIS) extensions. For more information on debug tracing, see [Enabling NDIS Debug Tracing](enabling-ndis-debug-tracing.md). For more information on the NDIS debugging extensions, see [NDIS Extensions](ndis-extensions--ndiskd-dll-.md), which provides a complete list of the extension commands found in the extension module Ndiskd.dll. The Windows 2000 version of this extension module appears in the w2kfre and w2kchk directories. The Windows XP and later version of this extension module appear in the winxp directory.

An additional tool for debugging a network driver is the collection of regular debugging extensions, which are useful for obtaining debugging information. For example, entering [**!stacks 2 ndis!**](-stacks.md) displays all threads in the stack beginning with **ndis!**. This information can be useful for debugging hangs and stalls.

There is also an NDIS-specific bug check code, bug check 0x7C (BUGCODE\_NDIS\_DRIVER). For a complete list of its parameters, see [**Bug Check 0x7C**](bug-check-0x7c--bugcode-ndis-driver.md).

Another useful tool for testing an NDIS driver is NDIS Verifier. For more information, consult the NDIS Verifier topic in the Windows Driver Kit (WDK) documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Overview%20of%20NDIS%20Debugging%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




