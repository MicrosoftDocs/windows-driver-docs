---
title: Configuring Exceptions and Events in WinDbg
description: You can configure WinDbg to react to specified exceptions and events in a specific way. For each exception, you can set the break status and the handling status.
ms.assetid: B91DD7B6-5206-4BA6-8B49-8ECCA2FA730B
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Configuring Exceptions and Events in WinDbg


You can configure WinDbg to react to specified exceptions and events in a specific way. For each exception, you can set the break status and the handling status. For each event, you can set the break status.

You can configure the break status by doing one of the following:

-   Choose **Event Filters** from the **Debug** menu, click the event that you want from the list in the **Event Filters** dialog box, and then select **Enabled**, **Disabled**, **Output**, or **Ignore**.

-   Use the [**SXE**](sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md), **SXD**, **SXN**, or **SXI** command.

You can configure the handling status by doing one of the following:

-   Choose **Event Filters** from the **Debug** menu, click the event that you want from the list in the **Event Filters** dialog box, and then select **Handled** or **Not Handled**.

-   Use the [**SXE**](sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md), **SXD**, **SXN**, or **SXI** command.

For a detailed discussion of exceptions and events, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

 

 





