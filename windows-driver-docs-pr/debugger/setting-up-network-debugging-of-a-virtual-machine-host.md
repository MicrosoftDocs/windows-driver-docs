---
title: Setting Up Network Debugging of a Virtual Machine Host
description: If your target computer is a virtual machine host, you can set up network debugging and still have network access for the virtual machines.
ms.assetid: E4C4D2A1-2FB0-4028-8A52-30B8F4F738D0
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up Network Debugging of a Virtual Machine Host


If your target computer is a virtual machine host, you can set up network debugging and still have network access for the virtual machines.

Suppose you want to set up network debugging in the following situation.

-   The target computer has a single network interface card.
-   You intend to install the Hyper-V role on the target computer.
-   You intend to create one or more virtual machines on the target computer.

The best approach is to set up network debugging on the target computer before you install the Hyper-V role. Then the virtual machines will have access to the network.

If you decide to set up network debugging after the Hyper-V role has been installed on the target computer, you must change the network settings for your virtual machines to bridge them to the Microsoft Kernel Network Debug Adapter. Otherwise, the virtual machines will not have access to the network.

## <span id="related_topics"></span>Related topics


[Setting Up Network Debugging in Visual Studio](setting-up-a-network-debugging-connection-in-visual-studio.md)

[Setting Up a Network Connection Manually](setting-up-a-network-debugging-connection.md)

 

 






