---
title: COPP and Display Modes
description: COPP and Display Modes
keywords:
- copy protection WDK COPP , display modes
- video copy protection WDK COPP , display modes
- COPP WDK DirectX VA , display modes
- protected video WDK COPP , display modes
- display modes WDK COPP
ms.date: 04/20/2017
---

# COPP and Display Modes


This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.

The video miniport driver should report all the protection types that are supported on the physical connector associated with the DirectX VA COPP device, regardless of the display mode currently being used. The video miniport driver reports supported protection types when it receives a call to its [*COPPQueryStatus*](./coppquerystatus.md) function with the DXVA\_COPPQueryProtectionType set in the **guidStatusRequestID** member of the [**DXVA\_COPPStatusInput**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_coppstatusinput) structure. For more information, see [COPP Status](copp-status.md).

If the current resolution is too high for a particular protection type, then when the video miniport driver's [*COPPCommand*](./coppcommand.md) function is called to set the protection level for that protection type, the driver should return an error. The following scenarios give examples of when the driver's *COPPCommand* function should return success or an error:

-   If the DirectX VA COPP device is associated with an S-Video output connector, a call to the video miniport driver's [*COPPQueryStatus*](./coppquerystatus.md) function with DXVA\_COPPQueryProtectionType set should indicate support of the analog content protection (ACP) type (COPP\_ProtectionType\_ACP). Thereafter, if the driver's [*COPPCommand*](./coppcommand.md) function is called to set a level for the ACP type on this connector, the driver should return success because the output resolution of S-Video is fixed, even though desktop resolution (display mode) might be higher.

-   If the DirectX VA COPP device is associated with component output connectors, a call to the video miniport driver's [*COPPQueryStatus*](./coppquerystatus.md) function with DXVA\_COPPQueryProtectionType set should also indicate support of the ACP type. However, if the driver's [*COPPCommand*](./coppcommand.md) function is called to set a level for the ACP type on this output when the display resolution is 720p or 1080i, the driver should return the DDERR\_TOOBIGSIZE error code because the resolution is too high to set the protection level for the ACP type on component output connectors.

 

