---
title: Host Process Timeouts in UMDF
description: Host Process Timeouts in UMDF
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: b8a0a4cc-9c6d-40e2-a3f1-9807dbcf15d9
keywords: ["User Mode Driver Framework WDK time outs", "UMDF WDK time outs", "user mode drivers WDK UMDF time outs", "time outs WDK UMDF"]
---

# Host Process Timeouts in UMDF


When the reflector sends a critical request to the driver host process, the host starts an internal timer. The default timeout interval is 60 seconds. Critical requests include Plug and Play, power, and I/O cancellation.

As long as the User-Mode Driver Framework (UMDF) driver performs operations on a regular basis toward completing the request, the reflector extends the timeout period. For example, for a remove request, the driver needs to return from the remove callbacks at regular intervals.

If the timeout period expires, the reflector generates a WER error report, terminates the host process, and attempts to restart the device. For info about automatic restart, see [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md).

For info about the fields in this report, see [Accessing UMDF Metadata in WER Reports](accessing-umdf-metadata-in-wer-reports.md).

Timeout expiration is the most common reason for the reflector to terminate the host process.

You can extend the timeout period by using the [WDF Verifier Control Application](https://msdn.microsoft.com/library/windows/hardware/ff556129).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Host%20Process%20Timeouts%20in%20UMDF%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




