---
title: Default rule set (KMDF)
description: The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.
ms.assetid: A86161C6-52E8-457B-9C75-100D36796183
ms.date: 05/21/2018
ms.localizationpriority: medium
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

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





