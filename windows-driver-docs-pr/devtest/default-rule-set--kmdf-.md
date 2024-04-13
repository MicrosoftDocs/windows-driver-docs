---
title: Default Rule Set (KMDF)
description: Learn about the default rule set (KMDF) that specifies the recommended sets of rules to use when you analyze your driver.
ms.date: 05/21/2018
---

# Default rule set (KMDF)


The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.

[DDI usage rule set (KMDF)](ddi-usage-rule-set--kmdf-.md)
[IrpProcessing rule set (KMDF)](irpprocessing-rule-set--kmdf-.md)
[Irql rule set (KMDF)](irql-rule-set--kmdf-.md)
[Locking rule set (KMDF)](locking-rule-set--kmdf-.md)
[Miscellaneous rule set (KMDF)](miscellaneous-rule-set--kmdf-.md)
[RequestProcessing rule set (KMDF)](requestprocessing-rule-set--kmdf-.md)
[Usb rule set (KMDF)](usb-rule-set--kmdf-.md)
**To select the default rules**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Default**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Default.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Default.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](./using-static-driver-verifier-to-find-defects-in-drivers.md) and [Static Driver Verifier commands (MSBuild)](./-static-driver-verifier-commands--msbuild-.md).

 

