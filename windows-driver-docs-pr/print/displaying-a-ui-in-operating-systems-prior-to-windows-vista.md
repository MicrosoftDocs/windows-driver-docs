---
title: Displaying a UI in Operating Systems Prior to Windows Vista
description: Displaying a UI in Operating Systems Prior to Windows Vista
ms.assetid: de62310e-b10a-49b0-9bcc-b918318b2728
keywords:
- print spooler customizing WDK , pre-Windows Vista UI display
- spooler customizing WDK print , pre-Windows Vista UI display
- customizing print spooler components WDK , pre-Windows Vista UI display
- displaying UI for print component
- UI displaying WDK print
- user interface WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Displaying a UI in Operating Systems Prior to Windows Vista





-   Do not display UI in any component that runs in the spooler's process.

    The spooler runs at a high-privilege security level; therefore, displaying UI opens the spooler to the risk of malicious user code.

-   Check for errors in the driver.

    Asynchronous notification calls fail in operating system releases prior to Windows Vista.

-   Display simple dialog boxes by using the [**SplPromptUIInUsersSession**](https://msdn.microsoft.com/library/windows/hardware/ff562679) function.

-   Display complex user interface elements by writing a status monitor.

    A status monitor is an application that the IHV develops and that the user installs. Because the status monitor runs in the user's context under the user's credentials, it is safe for the status monitor to display UI elements at any time. The status monitor can communicate with the spooler by using bidirectional communication or by using the TCPMON Xcv interface. For information, see [Adding Bidirectional Communication](adding-bidirectional-communication.md) and [TCPMON Xcv Interface](tcpmon-xcv-interface.md).

 

 




