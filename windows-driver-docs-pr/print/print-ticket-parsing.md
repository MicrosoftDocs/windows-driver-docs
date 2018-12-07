---
title: Print Ticket Parsing
description: Print Ticket Parsing
ms.assetid: 8328110a-abb4-47aa-ab1d-730e4a2ce7bd
keywords:
- XPSDrv printer drivers WDK , render modules
- render modules WDK XPSDrv , Print Tickets
- Print Tickets WDK , XPSDrv printer drivers
- parsing Print Ticket objects
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Print Ticket Parsing


After the Print Ticket has been merged for the current document part, the print driver filter must parse the contents to find the settings that apply to the filter. The methods of the [IPrintCoreHelper interface](https://msdn.microsoft.com/library/windows/hardware/ff552960) can be used in the print driver filter modules to help parse the Print Ticket elements. After the Print Ticket elements have been extracted from the Print Ticket, they can be integrated into the filter module function. The filter modules are described in the [XPS Filter Pipeline](xpsdrv-printer-driver.md) section.

 

 




