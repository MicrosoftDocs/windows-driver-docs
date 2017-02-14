---
title: Video Port DDI Support
description: Starting with Windows 8, display drivers based on the Windows 2000 Display Driver Model (XDDM) will not install or run, but GDI accessibility drivers and remote display drivers will install and run.
ms.assetid: 87A98A49-B01B-419D-B570-6ECA60E2C7AF
---

# Video Port DDI Support


Starting with Windows 8, display drivers based on the [Windows 2000 Display Driver Model (XDDM)](windows-2000-display-driver-model-design-guide.md) will not install or run, but [GDI accessibility drivers](mirror-drivers.md) and [remote display drivers](remote-display-drivers.md) will install and run. For these scenarios only some of the functions that are exported by the Video Port Driver are supported.

## <span id="Supported_Video_Port_DDIs"></span><span id="supported_video_port_ddis"></span><span id="SUPPORTED_VIDEO_PORT_DDIS"></span>Supported Video Port DDIs


For GDI accessibility drivers and remote display driver scenarios, starting with Windows 8 the following system-implemented Video Port Driver device driver interfaces (DDIs) are still supported.

-   VideoDebugPrint
-   VideoPortAcquireDeviceLock
-   VideoPortAcquireSpinLock
-   VideoPortAcquireSpinLockAtDpcLevel
-   VideoPortAllocatePool
-   VideoPortClearEvent
-   VideoPortCompareMemory
-   VideoPortCreateEvent
-   VideoPortCreateSpinLock
-   VideoPortDeleteEvent
-   VideoPortDeleteSpinLock
-   VideoPortFlushRegistry
-   VideoPortFreePool
-   VideoPortGetAssociatedDeviceExtension
-   VideoPortGetCurrentIrql
-   VideoPortGetProcAddress
-   VideoPortGetRegistryParameters
-   VideoPortGetVersion
-   VideoPortInterlockedDecrement
-   VideoPortInterlockedExchange
-   VideoPortInterlockedIncrement
-   VideoPortInitialize
-   VideoPortLockBuffer
-   VideoPortLogError
-   VideoPortMoveMemory
-   VideoPortQueryPerformanceCounter
-   VideoPortQueryServices
-   VideoPortQuerySystemTime
-   VideoPortQueueDpc
-   VideoPortReadStateEvent
-   VideoPortReleaseDeviceLock
-   VideoPortReleaseSpinLock
-   VideoPortReleaseSpinLockFromDpcLevel
-   VideoPortSetEvent
-   VideoPortSetRegistryParameters
-   VideoPortSynchronizeExecution
-   VideoPortUnlockBuffer
-   VideoPortWaitForSingleObject
-   VideoPortZeroMemory

## <span id="Unsupported_Video_Port_DDIs"></span><span id="unsupported_video_port_ddis"></span><span id="UNSUPPORTED_VIDEO_PORT_DDIS"></span>Unsupported Video Port DDIs


For GDI accessibility drivers and remote display driver scenarios, starting with Windows 8 the following system-implemented Video Port Driver DDIs are not supported.

Items marked with an asterisk (\*) are for hardware scenarios that are no longer supported starting with Windows 8.

-   VideoPortAllocateBuffer
-   VideoPortAllocateCommonBuffer
-   VideoPortAllocateContiguousMemory
-   VideoPortAssociateEventsWithDmaHandle
-   VideoPortCheckForDeviceExistence\*
-   VideoPortCompleteDma\*
-   VideoPortCreateSecondaryDisplay\*
-   VideoPortDDCMonitorHelper\*
-   VideoPortDebugPrint
-   VideoPortDisableInterrupt
-   VideoPortDoDma
-   VideoPortEnableInterrupt
-   VideoPortEnumerateChildren\*
-   VideoPortFreeCommonBuffer
-   VideoPortFreeDeviceBase\*
-   VideoPortGetAccessRanges\*
-   VideoPortGetAgpServices
-   VideoPortGetAssociatedDeviceID\*
-   VideoPortGetBusData\*
-   VideoPortGetBytesUsed
-   VideoPortGetCommonBuffer
-   VideoPortGetDeviceBase\*
-   VideoPortGetDeviceData\*
-   VideoPortGetDmaAdapter\*
-   VideoPortGetDmaContext
-   VideoPortGetMdl
-   VideoPortGetRomImage\*
-   VideoPortGetVgaStatus\*
-   VideoPortInt10\*
-   VideoPortIsNoVesa\*
-   VideoPortLockPages
-   VideoPortMapBankedMemory
-   VideoPortMapDmaMemory
-   VideoPortMapMemory\*
-   VideoPortProtectWCMemory\*
-   VideoPortPutDmaAdapter\*
-   VideoPortReadPortBufferUchar\*
-   VideoPortReadPortBufferUlong\*
-   VideoPortReadPortBufferUshort\*
-   VideoPortReadPortUchar\*
-   VideoPortReadPortUlong\*
-   VideoPortReadPortUshort\*
-   VideoPortReadRegisterBufferUchar
-   VideoPortReadRegisterBufferUlong
-   VideoPortReadRegisterBufferUshort
-   VideoPortReadRegisterUchar
-   VideoPortReadRegisterUlong
-   VideoPortReadRegisterUshort
-   VideoPortRegisterBugcheckCallback
-   VideoPortReleaseBuffer
-   VideoPortReleaseCommonBuffer\*
-   VideoPortRestoreWCMemory\*
-   VideoPortScanRom\*
-   VideoPortSetBusData\*
-   VideoPortSetBytesUsed
-   VideoPortSetDmaContext
-   VideoPortSetTrappedEmulatorPorts\*
-   VideoPortSignalDmaComplete
-   VideoPortStallExecution
-   VideoPortStartDma\*
-   VideoPortStartTimer
-   VideoPortStopTimer
-   VideoPortUnlockPages
-   VideoPortUnmapDmaMemory
-   VideoPortUnmapMemory\*
-   VideoPortVerifyAccessRanges\*
-   VideoPortWritePortBufferUchar\*
-   VideoPortWritePortBufferUlong\*
-   VideoPortWritePortBufferUshort\*
-   VideoPortWritePortUchar\*
-   VideoPortWritePortUlong\*
-   VideoPortWritePortUshort\*
-   VideoPortWriteRegisterBufferUchar
-   VideoPortWriteRegisterBufferUlong
-   VideoPortWriteRegisterBufferUshort
-   VideoPortWriteRegisterUchar
-   VideoPortWriteRegisterUlong
-   VideoPortWriteRegisterUshort
-   VideoPortZeroDeviceMemory\*

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Video%20Port%20DDI%20Support%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




