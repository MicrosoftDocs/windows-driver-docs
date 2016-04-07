---
title: Videos Debugging KMDF Drivers
description: This topic contains links to a three part video series by Kumar Rajeev that demonstrates how to debug Kernel-Mode Driver Framework (KMDF) drivers.
ms.assetid: 62D0F1DA-318F-4989-94C5-968C67F420C8
---

# Videos: Debugging KMDF Drivers


This topic contains links to a three part video series by Kumar Rajeev that demonstrates how to debug Kernel-Mode Driver Framework (KMDF) drivers.

After watching the videos, you'll be familiar with the KMDF debugger extensions and know how to use them in basic debugging scenarios.

## Prerequisites


This series of demonstrations is given at an advanced technical level. To get the most from this content you should have working knowledge of the Windows kernel debugger (windbg.exe) and should be familiar with creating and using code with KMDF. Because each session builds on the previous one, we recommend that you view these demonstrations in the order listed.

## Video Series: Debugging Kernel-Mode Driver Framework Drivers


-   [Session 1: Dumping the KMDF Log (10 minutes)](http://download.microsoft.com/download/B/5/E/B5ECC1FC-7408-461C-B226-CF3AE3E3873F/Debugging-KMDF-Drivers-Part-1.wmv) \[media file\]

    The KMDF log is an important feature that helps quickly identify the root cause of a problem. This session shows you how to dump the KMDF log in the kernel debugger. It also provides information on how to change the size and verbosity of the log, and gives some tips on scanning the log.

-   [Session 2: Getting Information about a KMDF Driver and Its Objects (15 minutes)](http://download.microsoft.com/download/B/5/E/B5ECC1FC-7408-461C-B226-CF3AE3E3873F/Debugging-KMDF-Drivers-Part-2.wmv) \[media file\]

    The KMDF provides several debugger commands that help you explore various types of information about a driver. This session shows how to dump all the framework objects created by a KMDF driver, including parent-child hierarchy, verifier state, and device hierarchy. These commands are usually the starting point for a deeper investigation.

-   [Session 3: Dumping Device and Queues (15 minutes)](http://download.microsoft.com/download/B/5/E/B5ECC1FC-7408-461C-B226-CF3AE3E3873F/Debugging-KMDF-Drivers-Part-3.wmv) \[media file\]

    This session shows you how to get detailed information about a KMDF device object including plug and play (PnP) and power state, power policy ownership, power configuration, PnP and power callbacks, and device properties. It also shows you how to get information on open handles, explore all the I/O queues configured for the device, and dump individual requests.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Videos:%20Debugging%20KMDF%20Drivers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




