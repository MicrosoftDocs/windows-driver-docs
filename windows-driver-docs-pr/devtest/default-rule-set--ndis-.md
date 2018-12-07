---
title: Default rule set (NDIS)
description: The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.
ms.assetid: ED809122-5938-4087-AAB8-0D3EB6DB1092
ms.date: 05/21/2018
ms.localizationpriority: medium
---

# Default rule set (NDIS)


The Default rule set (Default.sdv) specifies the recommended sets of rules to use when you analyze your driver.

[DDI usage rule set (NDIS)](ddi-usage-rule-set--ndis-.md)
[IRQL rule set (NDIS)](irql-rule-set--ndis-.md)
[Locking rule set (NDIS)](locking-rule-set--ndis-.md)
[Memory usage rule set (NDIS)](memory-usage-rule-set--ndis-.md)
[Miscellaneous rule set (NDIS)](miscellaneous-rule-set--ndis-.md)
[OidProcessing rule set (NDIS)](oidprocessing-rule-set--ndis-.md)
**To select the default rules**

1.  Select your driver project (.vcxProj) in Microsoft Visual Studio. From the **Driver** menu, click **Launch Static Driver Verifier…**.

2.  Click the **Rules** tab. Under **Rule Sets**, select **Default**.

    To select the default rule set from a Visual Studio developer command prompt window, specify **Default.sdv** with the **/check** option. For example:

    ```
    msbuild /t:sdv /p:Inputs="/check:Default.sdv" mydriver.VcxProj /p:Configuration="Win8 Release" /p:Platform=Win32
    ```

    For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281) and [Static Driver Verifier commands (MSBuild)](https://msdn.microsoft.com/library/windows/hardware/hh466459).

 

 





