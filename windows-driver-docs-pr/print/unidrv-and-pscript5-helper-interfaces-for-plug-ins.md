---
title: Unidrv and Pscript5 Helper Interfaces for Plug-ins
description: Unidrv and Pscript5 Helper Interfaces for Plug-ins
keywords:
- IPrintCoreHelperPS
- IPrintCoreHelperUni
- IPrintCoreHelper
- helper interfaces WDK printer interface DLL
ms.date: 02/02/2024
ms.topic: reference
---

# Unidrv and Pscript5 helper interfaces for plug-ins

[!include[Print Support Apps](../includes/print-support-apps.md)]

Because the [**IPrintCoreHelperPS**](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperps) and [**IPrintCoreHelperUni**](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelperuni) interfaces inherit from the [**IPrintCoreHelper**](/windows-hardware/drivers/ddi/prcomoem/nn-prcomoem-iprintcorehelper) interface, all three interfaces share a common set of methods. The following table lists the methods in the helper interfaces and notes which methods are available in all three interfaces and which methods are available in only one of the interfaces.

| Method | Contained in |
|--|--|
| **ConvertStringToPTFormat** | All |
| **ConvertDefaultGDLSnapshot** | **IPrintCoreHelperUni** interface only |
| **ConvertGDLSnapshot** | **IPrintCoreHelperUni** interface only |
| **CreateInstanceOfMSXMLObject** | All |
| **EnumConstrainedOptions** | All |
| **EnumFeatures** | All |
| **EnumOptions** | All |
| **GetFeatureAttribute** | **IPrintCoreHelperPS** interface only |
| **GetGlobalAttribute** | **IPrintCoreHelperPS** interface only |
| **GetOptionAttribute** | **IPrintCoreHelperPS** interface only |
| **GetOption** | All |
| **SetOptions** | All |
| **WhyConstrained** | All |
