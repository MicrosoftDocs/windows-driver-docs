---
title: Details of the IPrintCoreHelperPS Interface
description: Details of the IPrintCoreHelperPS Interface
ms.assetid: 0e00012c-6ced-4369-b367-675465e29d93
keywords:
- IPrintCoreHelperPS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Details of the IPrintCoreHelperPS Interface


Pscript5 does not have an equivalent to the GDL parser, so for Pscript5 drivers, additional methods are provided to read data that appears in the PPD file. In addition to all of the methods of the base **IPrintCoreHelper** interface, the **IPrintCoreHelperPS** interface contains the following methods, which provide access to the data in the PPD file:

-   [**IPrintCoreHelperPS::GetFeatureAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff551998)

-   [**IPrintCoreHelperPS::GetGlobalAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff552899)

-   [**IPrintCoreHelperPS::GetOptionAttribute**](https://msdn.microsoft.com/library/windows/hardware/ff552903)

Because the PPD information does not depend on the configuration, you do not need to supply an input [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) parameter to these methods.

 

 




