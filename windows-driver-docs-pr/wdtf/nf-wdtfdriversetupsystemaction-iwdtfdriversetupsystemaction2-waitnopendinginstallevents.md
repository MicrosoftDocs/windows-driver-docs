---
UID: NF:wdtfdriversetupsystemaction.IWDTFDriverSetupSystemAction2.WaitNoPendingInstallEvents
title: IWDTFDriverSetupSystemAction2::WaitNoPendingInstallEvents (wdtfdriversetupsystemaction.h)
description: Waits until all device installations have completed.
old-location: dtf\iwdtfdriversetupsystemaction2_waitnopendinginstallevents.htm
tech.root: dtf
ms.date: 04/04/2018
keywords: ["IWDTFDriverSetupSystemAction2::WaitNoPendingInstallEvents"]
ms.keywords: IWDTFDriverSetupSystemAction2 interface [Windows Device Testing Framework],WaitNoPendingInstallEvents method, IWDTFDriverSetupSystemAction2.WaitNoPendingInstallEvents, IWDTFDriverSetupSystemAction2::WaitNoPendingInstallEvents, Microsoft.WDTF.IWDTFDriverSetupSystemAction2.WaitNoPendingInstallEvents, Microsoft::WDTF::IWDTFDriverSetupSystemAction2::WaitNoPendingInstallEvents, WaitNoPendingInstallEvents, WaitNoPendingInstallEvents method [Windows Device Testing Framework], WaitNoPendingInstallEvents method [Windows Device Testing Framework],IWDTFDriverSetupSystemAction2 interface, dtf.iwdtfdriversetupsystemaction2_waitnopendinginstallevents, wdtfdriversetupsystemaction/IWDTFDriverSetupSystemAction2::WaitNoPendingInstallEvents
f1_keywords:
 - "wdtfdriversetupsystemaction/IWDTFDriverSetupSystemAction2.WaitNoPendingInstallEvents"
 - "IWDTFDriverSetupSystemAction2.WaitNoPendingInstallEvents"
req.header: wdtfdriversetupsystemaction.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFDriverSetupSystemAction.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFDriverSetupSystemAction.Interop.dll
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
- APIRef
- kbSyntax
api_type:
- COM
api_location:
- WDTFDriverSetupSystemAction.Interop.dll
api_name:
- IWDTFDriverSetupSystemAction2.WaitNoPendingInstallEvents
targetos: Windows
req.typenames: 
---

# IWDTFDriverSetupSystemAction2::WaitNoPendingInstallEvents


## -description


Waits until all device installations have completed.


## -parameters




### -param dwTimeout




### -param pNoMoreEvents [out, retval]

True if all device installations completed before the time-out expired; 
otherwise, false.


## -returns



If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.




## -see-also




<a href="/windows-hardware/drivers/ddi/wdtfdriversetupsystemaction/nn-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2">IWDTFDriverSetupSystemAction2</a>
 

 
