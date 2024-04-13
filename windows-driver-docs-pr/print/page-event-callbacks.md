---
title: Page Event Callbacks
description: Page Event Callbacks
keywords:
- callback functions WDK CPSUI
- Common Property Sheet User Interface WDK print , callbacks
- CPSUI WDK print , callbacks
- property sheet pages WDK print , callbacks
- page event callbacks WDK CPSUI
- event callbacks WDK CPSUI
ms.date: 01/30/2023
---

# Page Event Callbacks

[!include[Print Support Apps](../includes/print-support-apps.md)]

When a user interacts with a property sheet page, the operation system sends notification of such window events as a changed focus or a modified value. How a CPSUI application receives notification of a page's window events depends on how the application has defined the page:

- If the page was defined using [CPSUI-supplied pages and templates](cpsui-supplied-pages-and-templates.md), it can supply a [CPSUI message handler](cpsui-message-handler.md).

- If the application created a customized page that is not supplied by CPSUI, it must provide a dialog box procedure. For more information, see [Dialog Box Procedures and CPSUI](dialog-box-procedures-and-cpsui.md).

A CPSUI application supplies CPSUI with the address of a page event callback when it calls the [**ComPropSheet**](/windows-hardware/drivers/ddi/compstui/nc-compstui-pfncompropsheet) function.
