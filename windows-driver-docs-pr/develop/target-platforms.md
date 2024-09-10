---
title: Target Platform on Driver Reference Pages
description: In the Requirements block at the bottom of Microsoft driver reference pages, you''ll see an entry called Target Platform.
ms.date: 06/21/2024
---

# Target platforms

Set the target platform to the  type of driver that you wish to develop. For more information, see [Building a Driver with the WDK](building-a-driver.md).

Here are the values for **Target Platform**, and what they mean:

|Term|Description|
|--- |--- |
|Universal|A driver binary in a Windows Driver can call this device driver interface (DDI). For more info, see [Get started developing Windows drivers](get-started-developing-windows-drivers.md).|
|Desktop|A driver binary for Windows 10 for desktop editions or Windows Server 2016 can call this DDI.|
|Windows Driver | A *Windows Driver* runs on the following Universal Windows Platform (UWP)-based editions of Windows: <p> Windows 11 <p> Windows Server 2022 <p> Windows Server 2019 <p> Windows 10 for desktop editions (Home, Pro, and Enterprise) <p> Windows 10 in S-Mode <p> Windows 10 IoT Core <p> Windows Server 2016 <p>|

## Target platform on driver reference pages

In the Requirements block at the bottom of Microsoft driver reference documentation pages, you'll see an entry called **Target Platform**. This line lists editions of Windows to which the page applies.

Here's an example of such an entry:

![target platform set to universal in requirements block.](images/TargetPlatform.png)

Here are the values you might see for **Target Platform**, and what they mean:

|Term|Description|
|--- |--- |
|Universal|A driver binary in a Universal, Desktop, or Windows Driver can call this device driver interface (DDI). For more info, see [Get started developing Windows drivers](get-started-developing-windows-drivers.md) or [Using a Universal INF File](../install/using-a-universal-inf-file.md).|
|Desktop|A driver binary for a Desktop driver can call this DDI.|

These two values that can appear on documentation pages map to three values that you can use in Visual Studio, in the **Target Platform** property under **Configuration Properties->Driver Settings->General**.  All three classifications, Universal, Desktop, or Windows Driver can use any DDI that specifies **Universal** as the Target Platform on the documentation page.

A Universal driver runs on the following Universal Windows Platform (UWP)-based editions of Windows:

*   Windows 11
*   Windows Server 2022
*   Windows Server 2019
*   Windows 10 for desktop editions (Home, Pro, and Enterprise)
*   Windows 10 in S-Mode
*   Windows 10 IoT Core
*   Windows Server 2016


