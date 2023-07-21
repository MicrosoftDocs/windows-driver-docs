---
title: Naming conventions in Pscript and Unidrv minidrivers
description: Naming conventions in Pscript and Unidrv minidrivers
keywords:
- in-box autoconfiguration support WDK printer , naming conventions
- names WDK printer autoconfig
ms.date: 07/18/2023
---

# Naming conventions in Pscript and Unidrv minidrivers

Hardware vendors who intend to support autoconfiguration in their Pscript5 or Unidrv minidrivers must adhere to the following naming conventions. Printer description files should be named in accordance with the printer's model name. In the file names shown in this topic, &lt;printerModelName&gt; is a placeholder for the model name of the printer.

## Pscript5 Minidrivers

| Type of file | Naming convention |
|--|--|
| Main printer description file | \<printerModelName\>.PPD |
| Auxiliary printer description file | \<printerModelName\>.GDL |

An auxiliary printer description file contains bidi or autoconfiguration information.

To enable autoconfiguration, a Pscript5 driver must include \<printerModelName\>.GDL and ps_schm.GDL in its dependent files list. For information about dependent files, see [Printer INF File Entries](printer-inf-file-entries.md).

## Unidrv minidrivers

| Type of file | Naming convention |
|--|--|
| Main printer description file | \<printerModelName\>.GPD or \<printerModelName\>.GDL<br><br>The type of file used depends on the printer description format that is used. |
| Auxiliary printer description file (optional) | \<printerModelName\>.GDL |

An auxiliary printer description file, which is optional for Unidrv minidrivers, contains bidi or autoconfiguration information. Alternatively, autoconfiguration information can be contained in the main description file.

To enable autoconfiguration, a Unidrv driver must include any \<printerModelName\>.GPD or \<printerModelName\>.GDL files in its dependent files list, as well as the following files:

Stddtype.gdl

Stdschem.gdl

Stdschmx.gdl
