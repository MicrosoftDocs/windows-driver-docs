---
title: Installing a Network Print Provider
description: Installing a Network Print Provider
ms.assetid: 448101f8-cb26-4a6f-807d-f110978321da
keywords:
- print providers WDK , installing
- network print providers WDK , installing
- installing print providers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Network Print Provider





To install a new network print provider, you must supply an installer that copies the provider DLL into the target system's \\System32 subdirectory and then calls **AddPrintProvidor** (described in the Microsoft Windows SDK documentation). This function creates a registry entry for the provider and adds the provider to the end of the spooler's list of installed providers. The function then loads the provider DLL and calls the provider's [**InitializePrintProvidor**](https://msdn.microsoft.com/library/windows/hardware/ff551614) function.

To create a connection to a printer supported by a network print provider, a user invokes the Add Printer Wizard and chooses the "Network printer server" option. The user specifies a print queue using the \\\\*Server*\\*Printer* format, and the provider's **OpenPrinter** function must recognize that print queue name.

 

 




