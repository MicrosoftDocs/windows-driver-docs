---
title: IRP Processing Examples
description: IRP Processing Examples
ms.assetid: 1bf555c7-87fd-43c2-ab74-aa6f9133f808
keywords: ["IRPs WDK kernel , processing examples"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# IRP Processing Examples





The following sections describe how IRPs might be processed in two prototype drivers. One is a prototype of a lowest-level driver for a mass storage device. The other is a prototype for an intermediate-level [*mirror driver*](https://msdn.microsoft.com/library/windows/hardware/ff556308#wdkgloss-mirror-driver), which would exist above the lowest-level driver in a stack of storage drivers. (A mirror driver duplicates all write requests to multiple driver, and alternates read requests among the duplicate drives.)

[Processing IRPs in a Lowest-Level Driver](processing-irps-in-a-lowest-level-driver.md)

[Processing IRPs in an Intermediate-Level Driver](processing-irps-in-an-intermediate-level-driver.md)

To learn more about creating and sending IRPs, see [Different ways of handling IRPs – cheat sheet](https://go.microsoft.com/fwlink/?linkid=834615).

