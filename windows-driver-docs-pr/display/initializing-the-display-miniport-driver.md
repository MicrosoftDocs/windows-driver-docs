---
title: Initializing the Display Miniport Driver
description: Initializing the Display Miniport Driver
ms.assetid: 505dab48-7c00-4bf4-8433-487360f67b26
keywords:
- miniport drivers WDK display , initializing
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Initializing the Display Miniport Driver


After the operating system has loaded the display miniport driver, the following steps occur to initialize the display miniport driver:

1.  The operating system calls the display miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff556157) function.

2.  **DriverEntry** allocates a [**DRIVER\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff556169) structure and populates the **Version** member of DRIVER\_INITIALIZATION\_DATA with DXGKDDI\_INTERFACE\_VERSION and the remaining members of DRIVER\_INITIALIZATION\_DATA with pointers to the display miniport driver's other entry point functions (that is, the functions that the display miniport driver implements).

3.  **DriverEntry** calls the [**DxgkInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff560824) function to load the Microsoft DirectX graphics kernel subsystem (*Dxgkrnl.sys*) and to supply the DirectX graphics kernel subsystem with pointers to the display miniport driver's other entry point functions.

4.  After **DxgkInitialize** returns, **DriverEntry** propagates the return value of **DxgkInitialize** back to the operating system. Display miniport driver writers should make no assumptions about the value that **DxgkInitialize** returns.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Initializing%20the%20Display%20Miniport%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




