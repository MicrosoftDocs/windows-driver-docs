---
title: Preparing for NDIS Debugging
description: Preparing for NDIS Debugging
ms.assetid: 9a23cc3a-5940-46c3-928f-7fac46dfaba2
keywords: ["NDIS debugging, setup"]
---

# Preparing for NDIS Debugging


To debug NDIS components, a checked version of Ndis.sys is required on the target computer. However, instead of installing an entire checked-build operating system, you can copy the checked version of Ndis.sys onto an otherwise free-build operating system. Before you copy the checked version of Ndis.sys to the target computer, you must disable Windows File Protection (WFP). To ensure that WFP is disabled, start the operating system in safe mode.

The NDIS symbols are publicly available on the Microsoft symbol store. For details on how to access this, see [Microsoft Public Symbols](microsoft-public-symbols.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Preparing%20for%20NDIS%20Debugging%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




