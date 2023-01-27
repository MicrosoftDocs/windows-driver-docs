---
title: Details of the IPrintCoreHelperPS Interface
description: Details of the IPrintCoreHelperPS Interface
keywords:
- IPrintCoreHelperPS
ms.date: 01/27/2023
---

# Details of the IPrintCoreHelperPS Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

Pscript5 does not have an equivalent to the GDL parser, so for Pscript5 drivers, additional methods are provided to read data that appears in the PPD file. In addition to all of the methods of the base **IPrintCoreHelper** interface, the **IPrintCoreHelperPS** interface contains the following methods, which provide access to the data in the PPD file:

- [**IPrintCoreHelperPS::GetFeatureAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcorehelperps-getfeatureattribute)

- [**IPrintCoreHelperPS::GetGlobalAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcorehelperps-getglobalattribute)

- [**IPrintCoreHelperPS::GetOptionAttribute**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintcorehelperps-getoptionattribute)

Because the PPD information does not depend on the configuration, you do not need to supply an input [**DEVMODEW**](/windows/win32/api/wingdi/ns-wingdi-devmodew) parameter to these methods.
