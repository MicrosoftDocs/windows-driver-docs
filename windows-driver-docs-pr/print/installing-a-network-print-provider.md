---
title: Install a network print provider
description: Provides information about how to install a network print provider.
keywords:
- print providers WDK , installing
- network print providers WDK , installing
- installing print providers WDK
ms.date: 09/14/2022
---

# Install a network print provider

To install a new network print provider, you must supply an installer that copies the provider DLL into the target system's \\System32 subdirectory and then calls [**AddPrintProvidor**](/windows/win32/printdocs/addprintprovidor). This function creates a registry entry for the provider and adds the provider to the end of the spooler's list of installed providers. The function then loads the provider DLL and calls the provider's [**InitializePrintProvidor**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintprovidor) function.

To create a connection to a printer supported by a network print provider, a user invokes the Add Printer Wizard and chooses the "Network printer server" option. The user specifies a print queue using the \\\\*Server*\\*Printer* format, and the provider's [**OpenPrinter**](/windows/win32/printdocs/openprinter) function must recognize that print queue name.
