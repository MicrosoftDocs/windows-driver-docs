---
title: Option entry format
description: Option entry format
keywords:
- printer options WDK Unidrv , entry format
- formats WDK printer options
ms.date: 07/18/2023
---

# Option entry format

[!include[Print Support Apps](../includes/print-support-apps.md)]

To specify a printer option entry in a GPD file, use the following format:

\***Option**: *OptionName* { *OptionAttributes* }

where *OptionName* is either the name of one of the predefined [standard options](standard-options.md) or a customized option name, and *OptionAttributes* is a set of [option attributes](option-attributes.md).

For an example of a set of \***Option** entries associated with a feature, see [Feature Entry Format](feature-entry-format.md).

If you repeat an option specification, for example by specifying two or more \***Option** entries for the **PaperSize** feature's LETTER option, each duplicate option attribute within the \***Option** entry overwrites the previous one, and the GPD parser only retains the last one encountered. On the other hand, if the GPD parser encounters two or more \*Feature entries for the **PaperSize** (or any other) feature, \***Option** entries not previously specified are added to the parser's database.

You can control the order in which options are displayed to the user. See [Specifying Feature and Option Display Order](specifying-feature-and-option-display-order.md).
