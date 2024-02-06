---
title: Unidrv Keywords
description: Unidrv Keywords
ms.date: 02/02/2024
---

# Unidrv keywords

[!include[Print Support Apps](../includes/print-support-apps.md)]

Unidrv plug-ins should use strings as they appear in the GPD view (not the GDL view) of the configuration file for calls to methods on the helper interface. In addition, Unidrv-provided features are preceded by a percent sign (%). The following table lists the simulated features that are supported.

| Feature name | Options | Description |
|--|--|--|
| **%MetafileSpooling** | "True" "False" | Enable EMF spooling. Document-sticky. |
| **%PageOrder** | "FrontToBack" "BackToFront" | Specify the order in which pages are printed. This feature is available only if the print processor is able to perform EMF spooling. Document-sticky. |
| **%PagePerSheet** | "1", "2", "4", 6", "9", "16", "Booklet" | Specify the number of logical pages that are printed on a physical page. The "Booklet" option is available only if the duplex feature is defined. This feature is available only if the print processor is able to perform EMF spooling. Document-sticky. |
| **%TextAsGraphics** | "True" "False" | Print text as graphics. Document-sticky. |

Some GPD syntax is expanded at parse time to create features and options. The most common syntax that falls into this category is the **MemConfigKB** keyword. Others include the **MemConfigMB**, **MemoryConfigKB**, and **Installable** keywords.
