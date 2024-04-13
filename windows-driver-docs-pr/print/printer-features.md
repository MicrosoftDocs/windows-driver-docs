---
title: Printer Features
description: Printer Features
keywords:
- Unidrv, printer features
- GPD files WDK Unidrv , printer features
- printer features WDK Unidrv
- printer features WDK Unidrv , about printer features
- Unidrv WDK print
ms.date: 01/30/2023
---

# Printer Features

[!include[Print Support Apps](../includes/print-support-apps.md)]

Printer features are capabilities that can be controlled by the Unidrv driver. By listing a feature and its characteristics in a GPD file, you inform the Unidrv driver that your printer supports the feature.

Each printer feature can be assigned to one or more states, and [printer options](printer-options.md) are used to define the possible states. For example, if your printer accepts both letter-sized and legal-sized pages, your GPD file should specify the PaperSize feature, along with the Letter and Legal options.

All features and their associated options are listed on either the printer property sheet or the document property sheet associated with the printer. For more information about these property sheets, see [Unidrv User Interface](unidrv-user-interface.md).

This section explains GPD language support for both [standard features](standard-features.md) and [customized features](customized-features.md). Additional topics in this section include [Feature Entry Format](feature-entry-format.md), [Feature Attributes](feature-attributes.md), and [Feature Conflict Priority](feature-conflict-priority.md).
