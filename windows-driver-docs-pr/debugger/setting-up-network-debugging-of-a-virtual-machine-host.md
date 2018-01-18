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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20Network%20Debugging%20of%20a%20Virtual%20Machine%20Host%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





