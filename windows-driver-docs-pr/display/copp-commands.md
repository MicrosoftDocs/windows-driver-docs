---
title: COPP Commands
description: COPP Commands
keywords:
- copy protection WDK COPP , commands
- video copy protection WDK COPP , commands
- COPP WDK DirectX VA , commands
- protected video WDK COPP , commands
- commands WDK COPP
ms.date: 04/20/2017
---

# COPP Commands


## <span id="ddk_copp_command_gg"></span><span id="DDK_COPP_COMMAND_GG"></span>


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

The video miniport driver can receive a request to perform an operation on the physical connector associated with the DirectX VA COPP device. The video miniport driver's [*COPPCommand*](./coppcommand.md) function is passed a pointer to a [**DXVA\_COPPCommand**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_coppcommand) structure that specifies the operation to perform. The **guidCommandID** and **CommandData** members of DXVA\_COPPCommand specify the operation. The following operations are supported:

-   [Setting the protection level](setting-the-protection-level.md)

-   [Instructing how to protect the signal](instructing-how-to-protect-the-signal.md)

 

