---
title: Tools for Verifying Drivers
description: Tools for Verifying Drivers
ms.assetid: 1d878be6-8730-4452-a35a-0635ebed9091
keywords: ["tools WDK , verifying drivers", "driver development tools WDK , verifying drivers", "verifying drivers WDK", "driver verification WDK"]
---

# Tools for Verifying Drivers


The Windows Driver Kit (WDK) includes several very comprehensive tools that are designed to help you detect and correct errors in driver code during the development process. Many of these tools can be used very early in the development process where they are most critical and can save you the most time and effort.

These verification tools are described in the WDK documentation and recommended for your use because each tool detects different types of driver errors in different ways. These tools are much more efficient than manual checks. These tools can detect errors that are not typically found in standard driver tests, and they embody the expertise of seasoned driver developers and Windows driver interface designers.

For best results, use all of the tools that can run on your driver. If you omit any of these tools, you might miss a serious bug in your driver.

This section begins with a brief discussion of the characteristics of code verification tools and a survey of the tools included in the WDK and in Windows or available from Microsoft.

This section includes:

[Static and Dynamic Verification Tools](static-and-dynamic-verification-tools.md)

[Survey of Verification Tools](survey-of-verification-tools.md)

[DDI Compliance Rules](https://msdn.microsoft.com/library/windows/hardware/ff552840)

[Checked Build of Windows](checked-build-of-windows.md)

[Application Verifier](application-verifier.md)

[Code Analysis for Drivers](code-analysis-for-drivers.md)

[Driver Verifier](driver-verifier.md)

[Static Driver Verifier](static-driver-verifier.md)

[WDF Verifier Control Application](wdf-verifier-control-application.md)

[WdfTester: WDF Driver Testing Toolset](wdftester--wdf-driver-testing-toolset.md)

### <span id="other_tools"></span><span id="OTHER_TOOLS"></span>Other Tools

If you have access to other code or driver verification tools (from other sources), we encourage you to use them in addition to the tools in the WDK. Be sure to use [Code Analysis for Drivers](code-analysis-for-drivers.md), [Static Driver Verifier](static-driver-verifier.md), and [Driver Verifier](driver-verifier.md) because of their specific knowledge of Windows drivers, but every tool looks at the code in different ways and can therefore help you find and fix different types of problems.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Tools%20for%20Verifying%20Drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




