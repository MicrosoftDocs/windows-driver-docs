---
title: Call to action and resources (Windows security model)
description: This article contains call to action recommendations and resources for the Windows security model.
ms.assetid: FCD98CE0-7E6E-4D6D-AF36-EA6A55160147
ms.author: windowsdriverdev
ms.date: 06/06/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Call to action and resources (Windows security model)


**Last updated:**

-   July 7, 2004

This article contains call to action recommendations and resources for the Windows security model.

-   Set strong default ACLs in calls to the **IoCreateDeviceSecure** routine.
-   Specify ACLs in the INF file for each device. These ACLs can loosen tight default ACLs if necessary.
-   Set the FILE\_DEVICE\_SECURE\_OPEN characteristic to apply device object security settings to the device namespace.
-   Do not define IOCTLs that permit FILE\_ANY\_ACCESS unless such access cannot be exploited maliciously.
-   Use the **IoValidateDeviceIoControlAccess** routine to tighten security on existing IOCTLS that allow FILE\_ANY\_ACCESS.

For more information, see:

-   *Writing Secure Code*, Second Edition. LeBlanc, David and Michael Howard. Redmond, WA: Microsoft Press, 2003.
-   *Windows Internals, Part 1* / *Windows Internals, Part 2*, Sixth Edition. Mark Russinovich, David Solomon and Alex Ionescu. Redmond, WA: Microsoft Press, 2012.
-   [Windows Driver Kit (WDK)](http://msdn.microsoft.com/en-US/library/windows/hardware/gg487463)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20Call%20to%20action%20and%20resources%20%28Windows%20security%20model%29%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




