---
title: Default rule set (WDM)
description: The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.
ms.assetid: F03BEEDE-ED6E-4202-9FF5-74A098702E12
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Default rule set (WDM)


The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.

[DDI usage rule set (WDM)](ddi-usage-rule-set--wdm-.md)
[IrpProcessing rule set (WDM)](irpprocessing-rule-set--wdm-.md)
[IrpTracking rule set (WDM)](irptracking-rule-set--wdm-.md)
[Irql rule set (WDM)](irql-rule-set--wdm-.md)
[LocalIrpProcessing rule set (WDM)](localirpprocessing-rule-set--wdm-.md)
[Locking rule set (WDM)](locking-rule-set--wdm-.md)
[Miscellaneous rule set (WDM)](miscellaneous-rule-set--wdm-.md)
[IrpPending rule set (WDM)](irppending-rule-set--wdm-.md)
**To select the default rules**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Default**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Default.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Default.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





