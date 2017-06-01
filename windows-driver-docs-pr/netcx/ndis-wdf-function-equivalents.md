---
title: NDIS-WDF Function Equivalents
---

# NDIS-WDF Function Equivalents

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The following table lists NDIS functions and their WDF equivalents:

|NDIS API Family|WDF Equivalent|
|-|-|
|[**NdisAllocateIoWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff561604)|[**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201)|
|[**NdisAllocateTimerObject**](https://msdn.microsoft.com/library/windows/hardware/ff561618)|[**WdfTimerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550050)|
|[**NdisAcquireSpinLock**](https://msdn.microsoft.com/library/windows/hardware/ff560699)|[**WdfSpinLockAcquire**](https://msdn.microsoft.com/library/windows/hardware/ff550040)|
|[**NdisInterlockedIncrement**](https://msdn.microsoft.com/library/windows/hardware/ff562752)|[**InterlockedIncrement**](https://msdn.microsoft.com/library/windows/hardware/ff547910)|
|[**NdisInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff562732)|[**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137)|
|[**NdisMInitializeScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff553543)|[**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983)|
|[**NdisInitializeString**](https://msdn.microsoft.com/library/windows/hardware/ff562741)|[**WdfStringCreate**](https://msdn.microsoft.com/library/windows/hardware/ff550046)|
|[**NdisSystemActiveProcessorCount**](https://msdn.microsoft.com/library/windows/hardware/ff564577)|[**KeGetCurrentProcessorNumberEx**](https://msdn.microsoft.com/library/windows/hardware/ff552076) (kernel)|
|[**NdisWriteRegisterUchar**](https://msdn.microsoft.com/library/windows/hardware/ff564678)|[**WDF_WRITE_REGISTER_UCHAR**](https://msdn.microsoft.com/library/windows/hardware/dn265684)|
