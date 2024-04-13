---
UID: NF:wdtfdriversetupdeviceaction.IWDTFDriverSetupAction2.UpdateDriver
title: IWDTFDriverSetupAction2::UpdateDriver (wdtfdriversetupdeviceaction.h)
description: Updates the target device with a driver from the driver package.
old-location: dtf\iwdtfdriversetupaction2_updatedriver.htm
tech.root: dtf
ms.date: 04/04/2018
keywords: ["IWDTFDriverSetupAction2::UpdateDriver"]
ms.keywords: IWDTFDriverSetupAction2 interface [Windows Device Testing Framework],UpdateDriver method, IWDTFDriverSetupAction2.UpdateDriver, IWDTFDriverSetupAction2::UpdateDriver, Microsoft.WDTF.IWDTFDriverSetupAction2.UpdateDriver, Microsoft::WDTF::IWDTFDriverSetupAction2::UpdateDriver, UpdateDriver, UpdateDriver method [Windows Device Testing Framework], UpdateDriver method [Windows Device Testing Framework],IWDTFDriverSetupAction2 interface, dtf.iwdtfdriversetupaction2_updatedriver, wdtfdriversetupdeviceaction/IWDTFDriverSetupAction2::UpdateDriver
f1_keywords:
 - "wdtfdriversetupdeviceaction/IWDTFDriverSetupAction2.UpdateDriver"
 - "IWDTFDriverSetupAction2.UpdateDriver"
req.header: wdtfdriversetupdeviceaction.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFDriverSetupDeviceAction.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFDriverSetupDeviceAction.Interop.dll
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
- WDTFDriverSetupDeviceAction.Interop.dll
api_name:
- IWDTFDriverSetupAction2.UpdateDriver
targetos: Windows
req.typenames: 
---

# IWDTFDriverSetupAction2::UpdateDriver


## -description




Updates the target device with a driver from the driver package.


## -parameters




### -param pDp [in]

The driver package.


### -param pbReboot






### -param pbRebootRequired [out, retval]

True if the device must reboot after the update; otherwise, false.


## -returns



If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.




## -see-also




<a href="/windows-hardware/drivers/ddi/wdtfdriversetupdeviceaction/nn-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2">IWDTFDriverSetupAction2</a>
 

 
