---
title: Enabling NDIS Debug Tracing
description: Enabling NDIS Debug Tracing
ms.assetid: 4ca3c246-3e73-46fb-93a5-ea376788e330
keywords: ["NDIS debugging, debug tracing"]
---

# Enabling NDIS Debug Tracing


NDIS debug tracing is the primary method for debugging NDIS drivers. When you set up NDIS debug tracing, you are actually enabling one or more levels of DbgPrint statements with NDIS. The resulting information is sufficient for debugging most network driver problems.

You can enable debug tracing by setting appropriate registry values. For details, see [Enabling NDIS Debug Tracing By Setting Registry Values](enabling-ndis-debug-tracing-by-setting-registry-values.md).

Setting registry values to enable debug tracing works even if the host computer does not have the checked version of the Ndis.sys symbols installed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Enabling%20NDIS%20Debug%20Tracing%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




