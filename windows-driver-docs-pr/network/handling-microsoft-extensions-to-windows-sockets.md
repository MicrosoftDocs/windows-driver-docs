---
title: Handling Microsoft Extensions to Windows Sockets
description: Handling Microsoft Extensions to Windows Sockets
keywords:
- extensions WDK Windows Sockets
- Windows Sockets Direct WDK , extensions
ms.date: 04/20/2017
---

# Handling Microsoft Extensions to Windows Sockets





The Windows Sockets switch handles all Microsoft-specific Windows Sockets extension functions internally. The Windows Sockets documentation in the Microsoft Windows SDK defines an extension as a mechanism that exposes advanced transport functionality to application programs. These extension functions are: **TransmitFile**, **AcceptEx**, and **GetAcceptExSockAddrs**. The switch converts these calls, as necessary, and forwards them to the appropriate SAN service provider function: [**WSPSend**](/previous-versions/windows/hardware/network/ff566316(v=vs.85)), [**WSPAccept**](/previous-versions/windows/hardware/network/ff566266(v=vs.85)), [**WSPRdmaWrite**](/previous-versions/windows/hardware/network/ff566306(v=vs.85)), or [**WSPRdmaRead**](/previous-versions/windows/hardware/network/ff566304(v=vs.85)).

 

