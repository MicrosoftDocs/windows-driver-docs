---
title: Emulating State Blocks
description: Emulating State Blocks
ms.assetid: 1ede9f1c-f5bb-4f41-8152-63d8663fd99e
keywords:
- emulating state blocks WDK display
- state block emulation WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Emulating State Blocks


To enable the Microsoft Direct3D runtime to emulate state blocks, the registry can be configured in the following way:

```
KeyPath   : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Direct3D
KeyValue  : EmulateStateBlocks
ValueType : REG_DWORD
ValueData : 1 for D3D runtime emulation of stateblocks, 0 for driver implementation (default).
```

**Note**   After the registry is configured to turn on emulation of state blocks by the Direct3D runtime, the runtime does not call the user-mode display driver's [**StateSet**](https://msdn.microsoft.com/library/windows/hardware/ff569730) function to set any state-block information.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Emulating%20State%20Blocks%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




