---
title: Interlocked Operations in Storport Miniport Drivers
author: windows-driver-content
description: Many of the interlocked functions available to Windows applications are appropriate for use in Storport miniport drivers.
ms.assetid: F3868AF4-545F-4B8E-8655-5AAD888C4B40
---

# Interlocked Operations in Storport Miniport Drivers


Many of the interlocked functions available to Windows applications are appropriate for use in Storport miniport drivers. Most of these functions are implemented as compiler intrinsic functions and are suitable for synchronizing changes to protected values.

The following interlocked functions are available for use in miniport drivers.

**Note**  The functions are declared in *miniport.h* or, for 32-bit (x86) drivers, in *storport.h*. The function topics listed from the Platform Software Development Kit (SDK) documentation are for usage reference only.

 

## <span id="interlocked_logical"></span><span id="INTERLOCKED_LOGICAL"></span>Logical


[**InterlockedAnd**](https://msdn.microsoft.com/library/windows/desktop/ms683516)
[**InterlockedAnd16**](https://msdn.microsoft.com/library/windows/desktop/ms683518)
[**InterlockedAnd64**](https://msdn.microsoft.com/library/windows/desktop/ms683527)
[**InterlockedOr**](https://msdn.microsoft.com/library/windows/desktop/ms683626)
[**InterlockedOr16**](https://msdn.microsoft.com/library/windows/desktop/ms683627)
[**InterlockedOr64**](https://msdn.microsoft.com/library/windows/desktop/ms683633)
[**InterlockedXor**](https://msdn.microsoft.com/library/windows/desktop/ms684021)
[**InterlockedXor16**](https://msdn.microsoft.com/library/windows/desktop/ms684024)
[**InterlockedXor64**](https://msdn.microsoft.com/library/windows/desktop/ms684104)
## <span id="interlocked_assignment"></span><span id="INTERLOCKED_ASSIGNMENT"></span>Assignment


[**InterlockedExchange**](https://msdn.microsoft.com/library/windows/desktop/ms683590)
[**InterlockedExchange64**](https://msdn.microsoft.com/library/windows/desktop/ms683593)
[**InterlockedExchangePointer**](https://msdn.microsoft.com/library/windows/desktop/ms683609)
## <span id="interlocked_comparison"></span><span id="INTERLOCKED_COMPARISON"></span>Comparison


[**InterlockedCompareExchange**](https://msdn.microsoft.com/library/windows/desktop/ms683560)
**InterlockedCompareExchange16**
[**InterlockedCompareExchange64**](https://msdn.microsoft.com/library/windows/desktop/ms683562)
[**InterlockedCompareExchangePointer**](https://msdn.microsoft.com/library/windows/desktop/ms683568)
## <span id="interlocked_arithmetic"></span><span id="INTERLOCKED_ARITHMETIC"></span>Arithmetic


[**InterlockedDecrement**](https://msdn.microsoft.com/library/windows/desktop/ms683580)
[**InterlockedDecrement64**](https://msdn.microsoft.com/library/windows/desktop/ms683581)
[**InterlockedExchangeAdd**](https://msdn.microsoft.com/library/windows/desktop/ms683597)
[**InterlockedExchangeAdd64**](https://msdn.microsoft.com/library/windows/desktop/ms683599)
[**InterlockedIncrement**](https://msdn.microsoft.com/library/windows/desktop/ms683614)
[**InterlockedIncrement64**](https://msdn.microsoft.com/library/windows/desktop/ms683615)
 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Interlocked%20Operations%20in%20Storport%20Miniport%20Drivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


