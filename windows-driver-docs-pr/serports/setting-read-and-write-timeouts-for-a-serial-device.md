---
title: Setting Read and Write Timeouts for a Serial Device
author: windows-driver-content
description: Setting Read and Write Timeouts for a Serial Device
ms.assetid: ed5b80a9-93cb-4e3f-9038-e715be35f206
keywords: ["Serial driver WDK , time-outs", "time-outs WDK serial devices", "serial devices WDK , time-outs", "read time-outs WDK serial devices", "write time-outs WDK serial devices"]
---

# Setting Read and Write Timeouts for a Serial Device


## <a href="" id="ddk-setting-read-and-write-timeouts-for-a-serial-device-kg"></a>


A client can use an [**IOCTL\_SERIAL\_SET\_TIMEOUTS**](https://msdn.microsoft.com/library/windows/hardware/ff546772) request to set time-out values that the system-supplied Serial.sys driver uses for read and write requests. Serial.sys continues to transfer bytes until the requested number of bytes are transferred or a time-out event occurs.

The time-out operation in Serial.sys is compliant with the user-mode operation of [COM ports](configuration-of-com-ports.md) that is supported by the communication functions that are supported by the Windows Base Services in the Microsoft Windows SDK.

Note that the time-out operation is not applied to a pending request while it is queued. The time-out operation is applied to a request after the request becomes current (that is, Serial.sys starts to process the request).

For more information about the read and write time-outs, see the following:

-   The [**SERIAL\_TIMEOUTS**](https://msdn.microsoft.com/library/windows/hardware/hh439614) structure in the Ntddser.h header file in the Windows Driver Kit (WDK).

-   The [**SetCommTimeouts**](https://msdn.microsoft.com/library/windows/desktop/aa363437) function and the [**COMMTIMEOUTS**](https://msdn.microsoft.com/library/windows/desktop/aa363190) structure that are supported by the Windows Base Services in the Windows SDK.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Setting%20Read%20and%20Write%20Timeouts%20for%20a%20Serial%20Device%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


