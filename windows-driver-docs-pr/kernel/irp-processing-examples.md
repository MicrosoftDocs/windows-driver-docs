---
title: IRP Processing Examples
author: windows-driver-content
description: IRP Processing Examples
ms.assetid: 1bf555c7-87fd-43c2-ab74-aa6f9133f808
keywords: ["IRPs WDK kernel , processing examples"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IRP Processing Examples


## <a href="" id="ddk-irp-processing-examples-kg"></a>


The following sections describe how IRPs might be processed in two prototype drivers. One is a prototype of a lowest-level driver for a mass storage device. The other is a prototype for an intermediate-level [*mirror driver*](https://msdn.microsoft.com/library/windows/hardware/ff556308#wdkgloss-mirror-driver), which would exist above the lowest-level driver in a stack of storage drivers. (A mirror driver duplicates all write requests to multiple driver, and alternates read requests among the duplicate drives.)

[Processing IRPs in a Lowest-Level Driver](processing-irps-in-a-lowest-level-driver.md)

[Processing IRPs in an Intermediate-Level Driver](processing-irps-in-an-intermediate-level-driver.md)

To learn more about creating and sending IRPs, see [Different ways of handling IRPs – cheat sheet](https://go.microsoft.com/fwlink/?linkid=834615).

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP%20Processing%20Examples%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
