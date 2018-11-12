---
title: DMA Verification
description: DMA Verification
ms.assetid: ffcb718a-63f5-49ff-9d36-67b2aa59761f
keywords:
- DMA Verification feature WDK Driver Verifier
- HAL Verification WDK Driver Verifier
- common-buffer DMA WDK Driver Verifier
- packet DMA WDK Driver Verifier
- scatter-gather DMA WDK Driver Verifier
- system DMA WDK Driver Verifier
- Direct Memory Access WDK Driver Verifier
- DMA errors WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DMA Verification


## <span id="ddk_dma_verification_tools"></span><span id="DDK_DMA_VERIFICATION_TOOLS"></span>


DMA Verification monitors the use of Direct Memory Access (DMA). Since the DMA routines have changed as Windows has developed, many drivers make incorrect use of DMA calls. Moreover, some driver writers attempt to bypass the HAL DMA subsystem altogether. This practice can introduce insidious bugs into the driver.

The DMA Verification option of Driver Verifier attempts to catch common DMA errors. Along with the **!dma** kernel debugger extension, it can be used to verify that a driver is using DMA in a proper manner.

This Driver Verifier option is also called *HAL Verification*. Some error messages produced by Driver Verifier may use this term.

This Driver Verifier option is only available in Windows XP and later.

### <span id="different_types_of_dma"></span><span id="DIFFERENT_TYPES_OF_DMA"></span>Different Types of DMA

DMA is a mechanism through which a hardware device can transfer data to or from memory without using the processor. The processor is required to set up the transfer, and the device will signal the processor when it has completed the transfer. The advantage of this system is that the processor can perform other tasks while the DMA transfer is being performed.

There are several types of DMA used in Windows 2000 and later:

<span id="Common-buffer_DMA"></span><span id="common-buffer_dma"></span><span id="COMMON-BUFFER_DMA"></span>*Common-buffer DMA*  
Common-buffer DMA is performed when the system can allocate a single buffer that is accessible by both the hardware and the software. The driver is responsible for synchronizing accesses to the buffer. The memory is not cached, making this synchronization easier for the driver. After setting up a common buffer, both the driver and the hardware can write directly to the addresses in the buffer without any intervention from the HAL.

<span id="Packet_DMA"></span><span id="packet_dma"></span><span id="PACKET_DMA"></span>*Packet DMA*  
Packet DMA is performed when there is a single existing buffer that must be mapped for use by the hardware. An example of using packet DMA is the transfer of a file from memory to a disk. Using common-buffer DMA in this situation would be wasteful, because the file would have to be transferred to the common buffer before the hardware could transfer it to the disk. Instead, the HAL is consulted; it gives the driver the information it needs to help the hardware find the actual buffer in memory. This operation is complicated by the need for the routines involved to work across different architectures.

<span id="Scatter_gather_DMA"></span><span id="scatter_gather_dma"></span><span id="SCATTER_GATHER_DMA"></span>*Scatter/gather DMA*  
Scatter/gather DMA is a shortcut method that sets up several packet DMA transfers at once. If you are transferring a packet over the network, for example, each part of the network stack adds its own header (TCP, IP, Ethernet, and so forth). These headers are all allocated from different places in memory. In this case, the scatter/gather DMA saves time by issuing a batch request to the HAL to map each header plus the data segment for access by the hardware. Instead of having to call the packet DMA routines on each part of the packet, this method calls each routine once, and lets the HAL be responsible for mapping each one individually.

**Note**  *Scatter/gather capability* does not mean that the device can use the scatter/gather routines. Scatter/gather capability refers to a flag in the device description that indicates that the device is able to read or write from any area in memory, instead of just a certain range.

 

<span id="System_DMA"></span><span id="system_dma"></span><span id="SYSTEM_DMA"></span>*System DMA*  
System DMA is performed by programming the system DMA controller on the motherboard to do the transfer directly. Only ISA cards can use system DMA.

### <span id="effects_of_dma_verification"></span><span id="EFFECTS_OF_DMA_VERIFICATION"></span>Effects of DMA Verification

When DMA Verification is active, Driver Verifier detects misuses of DMA routines, including:

-   Overrunning or underrunning the DMA memory buffer (these errors can be made by the hardware or the driver).

-   Double-freeing a common buffer, adapter channel, map register, or scatter/gather list.

-   Leaking memory by not freeing common buffers, adapter channels, map registers, scatter/gather lists, or adapters.

-   Having more than one adapter channel present for an adapter at one time.

-   Attempting to use an adapter that has already been freed and no longer exists.

-   Not flushing an adapter buffer.

-   Having too many outstanding reference counts for an adapter.

-   Performing DMA on a pageable buffer (all buffers should be locked before DMA transfer begins).

-   Performing DMA on an MDL with mangled flags.

-   Referencing an invalid system address, either before the first MDL, or after the end of the first MDL, or using a transfer length that is longer than the MDL buffer and crosses a page boundary within the MDL.

-   Allocating too many map registers at one time, or allocating more map registers than the maximum number that is allowed.

-   Double-mapping of map registers.

-   Attempting to free map registers while some are still mapped.

-   Attempting to flush a map register that hasn't been mapped.

-   Attempting to flush too many bytes at the end of the map register file.

-   Calling DMA routines at an improper IRQL.

-   Passing a null-value DMA\_ADAPTER to a HAL routine.

-   Passing an address and an MDL to a HAL routine when the address is not contained in the MDL.

-   Attempting to map an address range that has already been mapped.

-   Attempting to flush a buffer that isn't mapped.

-   Attempting to map a zero-length buffer for transfer.

-   Calling the obsolete function [**HalGetAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff546596) (all drivers must use [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220) instead).

Driver Verifier monitors the driver's behavior and issues bug check 0xE6 if any of these violations occur. See [**Bug Check 0xE6**](https://msdn.microsoft.com/library/windows/hardware/ff560341) (DRIVER\_VERIFIER\_DMA\_VIOLATION) for a list of the bug check parameters.

### <span id="when_is_dma_verification_useful_"></span><span id="WHEN_IS_DMA_VERIFICATION_USEFUL_"></span>When is DMA Verification Useful?

All drivers that use DMA directly (by calling the HAL DMA routines) should be tested with DMA Verification.

In addition, miniport drivers should also be tested, since they often use DMA indirectly (by calling port drivers that use DMA).

DMA Verification can also be an effective way to detect memory corruption, since it can spot when either a driver or a hardware device overruns a DMA buffer.

### <span id="monitoring_dma_verification"></span><span id="MONITORING_DMA_VERIFICATION"></span>Monitoring DMA Verification

The kernel debugger extension **!dma** can be used to display a wealth of DMA information. It can display various details about the behavior of each DMA adapter. There is a detailed example of the **!dma** extension, as well as general information about debugger extensions, in the documentation in the Debugging Tools for Windows package. See [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) for details.

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

You can activate the DMA Verification feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

-   **At the command line**

    At the command line, the DMA Verification option is represented by **Bit 7 (0x80)**. To activate DMA Verification, use a flag value of 0x80 or add 0x80 to the flag value. For example:

    ```
    verifier /flags 0x80 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

    On Windows Vista and later versions of Windows, you can also activate and deactivate DMA Verification without rebooting the computer by adding the **/volatile** parameter to the command. For example:

    ```
    verifier /volatile /flags 0x80 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or reboot the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

    The DMA Verification feature is also included in the standard settings. For example:

    ```
    verifier /standard /driver MyDriver.sys
    ```

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **DMA verification**.

    The DMA Verification feature is also included in the standard settings. To use this feature, in Driver Verifier Manager, click **Create Standard Settings**.

 

 





