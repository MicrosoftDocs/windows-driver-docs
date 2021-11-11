---
title: AddEuro feature
description: The AddEuro feature adds this symbol to the printer's device font.
keywords:
- minidrivers WDK Pscript , AddEuro feature
- AddEuro feature WDK print
- Euro symbol WDK print
- European Union symbol WDK print
- ADHasEuro
ms.date: 09/02/2021
ms.localizationpriority: medium
---

# AddEuro feature

The Euro symbol, as shown in the following figure, is the currency symbol for the basic monetary unit used in countries/regions of the European Union.

![figure of the euro symbol.](images/euro.png)

The AddEuro feature adds this symbol to the printer's device font. When AddEuro is enabled, a Euro symbol that appears on a display device will also be printed on paper when the document is sent to a printer. If this feature is unavailable or disabled, a user who selects an unaliased device font will be able to see a Euro symbol on the screen, but will see a large circular dot on paper. With this feature enabled, a user can print the Euro symbol, whether or not it is available in the printer's device font.

AddEuro uses a private *PPD* keyword, \***ADHasEuro**, to allow printer manufacturers to set the best defaults.

| Keyword and Value | Meaning |
|--|--|
| **ADHasEuro**: True | The printer already has a built-in Euro symbol that does not need to be downloaded. With this value, AddEuro is disabled by default. |
| **ADHasEuro**: False | The printer does not have a built-in Euro symbol; if called for by an application, this symbol should be downloaded. With this value, AddEuro is enabled by default, regardless of PostScript version. |

If the \***ADHasEuro** keyword does not appear, the AddEuro feature is enabled by default for printers with PostScript versions before 3011, and disabled by default for versions 3011 or after.
