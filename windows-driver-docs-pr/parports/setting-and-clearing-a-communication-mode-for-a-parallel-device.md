---
title: Setting and Clearing a Communication Mode for a Parallel Device
author: windows-driver-content
description: Setting and Clearing a Communication Mode for a Parallel Device
MS-HAID:
- 'vspd\_076e8fc6-dda5-434a-808e-efb4785af6e0.xml'
- 'parports.setting\_and\_clearing\_a\_communication\_mode\_for\_a\_parallel\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2ff53ed0-dbb7-4c8f-b6e4-5f7d20124a7c
keywords: ["parallel devices WDK , communication modes", "communication modes WDK parallel devices", "clearing communication modes"]
---

# Setting and Clearing a Communication Mode for a Parallel Device


## <a href="" id="ddk-setting-and-clearing-a-communication-mode-for-a-parallel-device-kg"></a>


A client can set the communication mode of a parallel device using the following device control requests:

-   [**IOCTL\_IEEE1284\_GET\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff543975) returns the current communication protocols set on the device. The port does not have to be locked to use this request.

-   [**IOCTL\_IEEE1284\_NEGOTIATE**](https://msdn.microsoft.com/library/windows/hardware/ff543978) negotiates a new communication mode. The parallel port must be allocated and the IEEE 1284.3 device selected.

-   [**IOCTL\_INTERNAL\_DISCONNECT\_IDLE**](https://msdn.microsoft.com/library/windows/hardware/ff543993) sets the communication mode to IEEE\_COMPATIBLE. The parallel port must be allocated and the IEEE 1284.3 device selected.

A kernel-mode driver can also use the system-supplied [parallel device callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544275). An [**IOCTL\_INTERNAL\_PARCLASS\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff544040) request returns a [**PARCLASS\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544334) structure that includes the following pointers to system-supplied callback routines:

-   The **DetermineIeeeMode** member is a pointer to the [**PDETERMINE\_IEEE\_MODES**](https://msdn.microsoft.com/library/windows/hardware/ff544365) callback, which determines the IEEE communication modes that the parallel port supports.

-   The **NegotiateIeeeMode** member is a pointer to the [**PNEGOTIATE\_IEEE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff544386) callback, which sets the fastest IEEE communication mode that the parallel port bus driver supports from among the modes specified by the caller.

-   The **TerminateIeeeMode** member is a pointer to the [**PTERMINATE\_IEEE\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff544773) callback, which sets the communication mode to IEEE 1284-compatibility mode.

-   The **IeeeFwdToRev** member is a pointer to the [**PPARALLEL\_IEEE\_FWD\_TO\_REV**](https://msdn.microsoft.com/library/windows/hardware/ff544524) callback, which changes the data transfer direction from forward to reverse (from write to read).

-   The **IeeeRevToFwd** member is a pointer to the [**PPARALLEL\_IEEE\_REV\_TO\_FWD**](https://msdn.microsoft.com/library/windows/hardware/ff544528) callback, changes the transfer direction from reverse to forward (from read to write).

For more information about the communication modes that the parallel port bus driver supports, see the modes NONE through ECP\_ANY that are defined in the header file *ntddpar.h* in the Windows Driver Kit (WDK).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Setting%20and%20Clearing%20a%20Communication%20Mode%20for%20a%20Parallel%20Device%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


