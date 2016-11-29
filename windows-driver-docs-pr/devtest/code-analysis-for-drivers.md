---
title: Code Analysis for Drivers
description: Code Analysis for Drivers is a compile-time static verification tool that detects basic coding errors in C and C++ programs and includes a specialized module that is designed to detect errors in (primarily) kernel-mode driver code.
ms.assetid: 2F3549EF-B50F-455A-BDC7-1F67782B8DCA
---

# Code Analysis for Drivers


Code Analysis for Drivers is a compile-time static verification tool that detects basic coding errors in C and C++ programs and includes a specialized module that is designed to detect errors in (primarily) kernel-mode driver code.

**Note**  In previous versions of the WDK, the driver-specific module for code analysis was part of a stand-alone tool called PREfast for Drivers (PFD). PREfast for Drivers was also integrated into the WDK Build environment, as part of Microsoft Automated Code Review (OACR). Starting with Windows Driver Kit (WDK) 8, the driver-specific features have been integrated with the [Code Analysis tool in Visual Studio](http://go.microsoft.com/fwlink/p/?linkid=226836).

 

## <span id="in_this_section"></span>In this section


-   [Code Analysis for drivers overview](code-analysis-for-drivers-overview.md)
-   [How to run Code Analysis for drivers](how-to-run-code-analysis-for-drivers.md)
-   [SAL 2 Annotations for Windows Drivers](sal-2-annotations-for-windows-drivers.md)
-   [Code Analysis for Drivers Warnings](prefast-for-drivers-warnings.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Code%20Analysis%20for%20Drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




