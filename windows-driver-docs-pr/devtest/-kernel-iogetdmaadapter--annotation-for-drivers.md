---
title: \_Kernel\_IoGetDmaAdapter\_ Annotation for drivers
description: Use the \_Kernel\_IoGetDmaAdapter\_ annotation to direct the code analysis tools to look for misuse of DMA pointers.
ms.assetid: 51F71815-D899-48F5-8F81-92B139FC6B8E
---

# \_Kernel\_IoGetDmaAdapter\_ Annotation for drivers


Use the \_Kernel\_IoGetDmaAdapter\_ annotation to direct the code analysis tools to look for misuse of DMA pointers.

If a function calls an interface annotated with the \_Kernel\_IoGetDmaAdapter\_ annotation, it shall have retry logic such that retries occur until the function succeeds.

The IoGetDmaAdapter routine could return fewer than the requested number of registers, and the caller is required to proceed using the actual number, not the requested number.

```ManagedCPlusPlus
_Must_inspect_result_
_IRQL_requires_max_(PASSIVE_LEVEL)
NTKERNELAPI
struct _DMA_ADAPTER *
IoGetDmaAdapter(
    _In_opt_ PDEVICE_OBJECT PhysicalDeviceObject,           // required for PnP drivers
    _In_ struct _DEVICE_DESCRIPTION *DeviceDescription,
    _Out_ _When_(return!=0, _Kernel_IoGetDmaAdapter_ _At_(*NumberOfMapRegisters, _Must_inspect_result_))
    PULONG NumberOfMapRegisters
```

## <span id="related_topics"></span>Related topics


[SAL 2.0 Annotations for Windows Drivers](sal-2-annotations-for-windows-drivers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20_Kernel_IoGetDmaAdapter_%20Annotation%20for%20drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





