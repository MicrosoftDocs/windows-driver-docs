---
title: How UMDF Handles Application Failures
description: This topic describes actions that User Mode Driver Framework (UMDF) and the operating system take when an application fails. It applies to both UMDF versions 1 and 2.
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: ac59a5fe-5975-455f-9da3-318c0692bf9c
keywords: ["User Mode Driver Framework WDK application failures", "UMDF WDK application failures", "failed applications WDK UMDF", "application failures WDK UMDF"]
---

# How UMDF Handles Application Failures


This topic describes actions that User-Mode Driver Framework (UMDF) and the operating system take when an application fails. It applies to both UMDF versions 1 and 2.

When an application fails, the following events occur:

-   The reflector receives [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff550718).

-   The cleanup request is sent to the host process on the "cancel" IPC channel.

-   The host process and UMDF driver complete pending I/O requests.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20How%20UMDF%20Handles%20Application%20Failures%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




