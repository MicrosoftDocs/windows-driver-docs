---
title: In-Box Support for Autoconfiguration
description: In-Box Support for Autoconfiguration
ms.assetid: cd2faef4-96ba-4d11-99f6-90e41ae2e283
keywords:
- autoconfiguration WDK printer , in-box support
- printer autoconfiguration WDK printer , in-box support
- in-box autoconfiguration support WDK printer
- in-box autoconfiguration support WDK printer , about in-box autoconfiguration support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# In-Box Support for Autoconfiguration


In Windows Vista, Unidrv-based and Pscript5-based drivers using the standard TCP/IP port monitor or the Web Services for Devices (WSD) port monitor provide support for autoconfiguration. Note that autoconfiguration support in Windows Vista is provided only for queries about installable features, such as those concerned with the duplex unit or the font cartridge. For a given feature, the response to the query can concern only one option of the feature. A query about whether the duplex unit is installed would elicit one of two responses: that the duplex unit was installed or that it was not. A query about which font cartridge is installed would generate a response indicating either that font cartridge *A* was installed or that font cartridge *B* was installed.

The current (version 1) implementation of autoconfiguration does not allow for multiple responses. A query is limited to a single option of a feature. This means, for example, that a response to a query cannot provide information about both the media size and media color in an input tray.

The following topics describe how to take advantage of the in-box support for autoconfiguration in Windows Vista:

[Printer Minidriver Changes](printer-minidriver-changes.md)

[Customizing the Printer Port Monitors](customizing-the-printer-port-monitors.md)

 

 




