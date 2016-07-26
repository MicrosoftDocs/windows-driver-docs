---
title: Setting and Clearing the Communication Mode on a Parallel Port
author: windows-driver-content
description: Setting and Clearing the Communication Mode on a Parallel Port
MS-HAID:
- 'vspd\_015cd500-d62c-48bb-b2d6-323e79142594.xml'
- 'parports.setting\_and\_clearing\_the\_communication\_mode\_on\_a\_parallel\_port'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a22cdeef-4ae7-49f8-b0b5-a4d68feb4235
keywords: ["parallel ports WDK , communication modes", "communication modes WDK parallel ports"]
---

# Setting and Clearing the Communication Mode on a Parallel Port


## <a href="" id="ddk-setting-and-clearing-the-communication-mode-on-a-parallel-port-kg"></a>


A client sets the communication mode on a parallel port by using the following internal device control requests:

[**IOCTL\_INTERNAL\_PARALLEL\_SET\_CHIP\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff544031)

[**IOCTL\_INTERNAL\_PARALLEL\_CLEAR\_CHIP\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff544017)

A kernel-mode driver can also use the system-supplied [parallel device callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544275) obtained with an [**IOCTL\_INTERNAL\_GET\_PARALLEL\_PNP\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff543997) request. This request returns a [**PARALLEL\_PNP\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544299) structure that includes the following pointers to system-supplied callbacks:

-   The **TrySetChipMode** member is a pointer to a [*PPARALLEL\_SET\_CHIP\_MODE*](https://msdn.microsoft.com/library/windows/hardware/ff544542) callback, which sets the operating mode of a parallel port.

-   The **ClearChipMode** member is a pointer to a [*PPARALLEL\_CLEAR\_CHIP\_MODE*](https://msdn.microsoft.com/library/windows/hardware/ff544398) callback, which clears the operating mode of a parallel port by resetting the communication mode of the host chipset to IEEE 1284-compatibility mode.

A client must first allocate a parallel port before it can set or clear the communication mode.

A client must first clear the communication mode before it can set a new communication mode. Clearing the communication mode returns the host chipset to IEEE 1284-compatibility mode.

To determine the current mode, a client can use the IOCTL\_INTERNAL\_GET\_PARALLEL\_PNP\_INFO request, which returns a PARALLEL\_PNP\_INFORMATION structure that contains information about the current communication mode.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Setting%20and%20Clearing%20the%20Communication%20Mode%20on%20a%20Parallel%20Port%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


