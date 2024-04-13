---
title: Emulating State Blocks
description: Emulating State Blocks
keywords:
- emulating state blocks WDK display
- state block emulation WDK display
ms.date: 04/20/2017
---

# Emulating State Blocks


To enable the Microsoft Direct3D runtime to emulate state blocks, the registry can be configured in the following way:

```registry
KeyPath   : HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Direct3D
KeyValue  : EmulateStateBlocks
ValueType : REG_DWORD
ValueData : 1 for D3D runtime emulation of stateblocks, 0 for driver implementation (default).
```

**Note**   After the registry is configured to turn on emulation of state blocks by the Direct3D runtime, the runtime does not call the user-mode display driver's [**StateSet**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_stateset) function to set any state-block information.

 

 

