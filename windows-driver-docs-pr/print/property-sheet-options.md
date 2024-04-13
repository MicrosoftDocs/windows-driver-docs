---
title: Property Sheet Options
description: Property Sheet Options
keywords:
- Common Property Sheet User Interface WDK print , property sheet options
- CPSUI WDK print , property sheet options
- property sheet pages WDK print , property sheet options
- property sheets WDK print
- selectable property sheet page items WDK print
ms.date: 01/30/2023
---

# Property Sheet Options

[!include[Print Support Apps](../includes/print-support-apps.md)]

A property sheet option is a displayable, selectable item on a property sheet page. Typically, users can modify an option's value. CPSUI helps applications create options in a standard format, using a predefined set of [CPSUI-supported window controls](cpsui-supported-window-controls.md). Applications do not have to provide resources for these controls.

Each property sheet page typically contains several options. For each property sheet option, a CPSUI application must use the following CPSUI structures:

- One [**OPTITEM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optitem) structure, which identifies the option's display name and other characteristics.

- One [**OPTTYPE**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_opttype) structure, which identifies the option's display dialog type ([CPSUI option type](./cpsui-option-types.md)).

- One or more [**OPTPARAM**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_optparam) structures, which identify the option's user-selectable parameter values.

To use these CPSUI structures to describe property sheet options, the page containing the option must be defined using a [**COMPROPSHEETUI**](/windows-hardware/drivers/ddi/compstui/ns-compstui-_compropsheetui) structure.
