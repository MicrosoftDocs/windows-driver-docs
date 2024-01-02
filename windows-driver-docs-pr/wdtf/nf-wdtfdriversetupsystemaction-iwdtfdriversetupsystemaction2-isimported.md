---
UID: NF:wdtfdriversetupsystemaction.IWDTFDriverSetupSystemAction2.IsImported
title: IWDTFDriverSetupSystemAction2::IsImported (wdtfdriversetupsystemaction.h)
description: Returns a value that indicates whether a package has already been imported.
old-location: dtf\iwdtfdriversetupsystemaction2_isimported.htm
tech.root: dtf
ms.date: 04/04/2018
keywords: ["IWDTFDriverSetupSystemAction2::IsImported"]
ms.keywords: IWDTFDriverSetupSystemAction2 interface [Windows Device Testing Framework],IsImported method, IWDTFDriverSetupSystemAction2.IsImported, IWDTFDriverSetupSystemAction2::IsImported, IsImported, IsImported method [Windows Device Testing Framework], IsImported method [Windows Device Testing Framework],IWDTFDriverSetupSystemAction2 interface, Microsoft.WDTF.IWDTFDriverSetupSystemAction2.IsImported, Microsoft::WDTF::IWDTFDriverSetupSystemAction2::IsImported, dtf.iwdtfdriversetupsystemaction2_isimported, wdtfdriversetupsystemaction/IWDTFDriverSetupSystemAction2::IsImported
f1_keywords:
 - "wdtfdriversetupsystemaction/IWDTFDriverSetupSystemAction2.IsImported"
 - "IWDTFDriverSetupSystemAction2.IsImported"
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
- IWDTFDriverSetupSystemAction2.IsImported
targetos: Windows
req.typenames: 
---

# IWDTFDriverSetupSystemAction2::IsImported


## -description


Returns a value that indicates whether a package has already been imported.


## -parameters




### -param pDp [in]

The package that is to be checked.


### -param bRet






### -param pbIsImported [out, retval]

True if the package has already been imported; otherwise, false.


## -returns



If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.




## -see-also




<a href="/windows-hardware/drivers/ddi/wdtfdriversetupsystemaction/nn-wdtfdriversetupsystemaction-iwdtfdriversetupsystemaction2">IWDTFDriverSetupSystemAction2</a>
 

 
