---
Description: Wall Clock and Link Position Registers
MS-HAID: 'audio.wall\_clock\_and\_link\_position\_registers'
MSHAttr: 'PreferredLib:/library/windows/hardware'
title: Wall Clock and Link Position Registers
---

# Wall Clock and Link Position Registers


The HD Audio controller contains a 32-bit wall clock counter register that increments at the bit-clock rate of the HD Audio Link and rolls over approximately every 89 seconds. Software uses this counter to synchronize between two or more controller devices by measuring the relative drift between the devices' hardware clocks.

In addition, the HD Audio controller contains a set of link position registers. Each DMA engine has a link position register that indicates the current read or write position of the data that the engine is transmitting over the HD Audio Link. The position register expresses the current position as a byte offset from the beginning of the cyclic buffer:

-   In a render stream, the link position register indicates the cyclic buffer offset of the next byte that the DMA engine will send over the link to the codec.

-   In a capture stream, the link position register indicates the cyclic buffer offset of the next byte that the DMA engine will receive from the codec over the link.

The cyclic buffer offset is simply the offset in bytes of the current read or write position from the start of the cyclic buffer. Upon reaching the end of the buffer, the position wraps around to the start of the buffer and the cyclic buffer offset resets to zero. The cyclic buffer resides in system memory. For more information, see the *Intel High Definition Audio Specification* at the [Intel HD Audio](http://go.microsoft.com/fwlink/p/?linkid=42508) website.

A kernel-mode function driver can read the wall clock and link position registers directly. To enable direct access, the HD Audio bus driver maps the physical memory that contains the registers into system virtual memory. The function driver calls the [**GetWallClockRegister**](audio.getwallclockregister) or [**GetLinkPositionRegister**](audio.getlinkpositionregister) routine to obtain a system virtual address pointer to the wall clock register or a link position register. These two routines are available in both versions of the HD Audio DDI.

The HD Audio controller hardware mirrors the wall clock and link position registers into memory pages that do not contain any of the other registers in the controller. Thus, if the function driver maps the mirrored wall clock or position registers to user mode, no user-mode programs can access any of the controller's other registers. The driver never allows a user-mode program to touch these other registers and program the hardware.

Register mirroring must accommodate the host processor's page size. Depending on the host processor architecture, a typical page size might be 4,096 or 8,192 bytes.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Wall%20Clock%20and%20Link%20Position%20Registers%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


