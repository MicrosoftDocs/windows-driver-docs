---
title: Shutting Down a SAN Connection
description: Shutting Down a SAN Connection
ms.assetid: 1ef509e4-fc8c-4feb-ae65-3c0f19033f34
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Shutting Down a SAN Connection





The Windows Sockets switch uses its session protocol to shut down a connection to a SAN socket. That is, the switch handles **WSPRecvDisconnect**, **WSPSendDisconnect**, and **WSPShutdown** calls from applications. The switch does not forward these calls to a SAN service provider. The switch uses its session protocol to disable the reception and transmission of data on a SAN socket.

 

 





