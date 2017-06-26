---
title: Using Critical Sections
author: windows-driver-content
description: Using Critical Sections
ms.assetid: 439ba7ef-6473-40ca-9daa-a8c61d789d97
keywords: ["interrupt service routines WDK kernel , critical sections", "ISRs WDK kernel , critical sections", "InterruptService", "synchronization WDK kernel , interrupts"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Critical Sections


## <a href="" id="ddk-using-critical-sections-kg"></a>


Any driver that contains an [*InterruptService*](https://msdn.microsoft.com/library/windows/hardware/ff547958) routine will most likely require one or more critical sections to synchronize access to hardware resources or driver data among the ISR and other routines.

This section includes the following topics:

[Introduction to SynchCritSection Routines](introduction-to-synchcritsection-routines.md)

[Writing SynchCritSection Routines](writing-synchcritsection-routines.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Critical%20Sections%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


