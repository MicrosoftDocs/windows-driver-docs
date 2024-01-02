---
UID: NF:wdtfdriverpackageaction.IWDTFDriverPackageAction2.Compare
title: IWDTFDriverPackageAction2::Compare (wdtfdriverpackageaction.h)
description: Compares two driver packages.
old-location: dtf\iwdtfdriverpackageaction2_compare.htm
tech.root: dtf
ms.date: 04/04/2018
keywords: ["IWDTFDriverPackageAction2::Compare"]
ms.keywords: Compare, Compare method [Windows Device Testing Framework], Compare method [Windows Device Testing Framework],IWDTFDriverPackageAction2 interface, IWDTFDriverPackageAction2 interface [Windows Device Testing Framework],Compare method, IWDTFDriverPackageAction2.Compare, IWDTFDriverPackageAction2::Compare, Microsoft.WDTF.IWDTFDriverPackageAction2.Compare, Microsoft::WDTF::IWDTFDriverPackageAction2::Compare, dtf.iwdtfdriverpackageaction2_compare, wdtfdriverpackageaction/IWDTFDriverPackageAction2::Compare
f1_keywords:
 - "wdtfdriverpackageaction/IWDTFDriverPackageAction2.Compare"
 - "IWDTFDriverPackageAction2.Compare"
req.header: wdtfdriverpackageaction.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTFDriverPackageAction.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTFDriverPackageAction.Interop.dll
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
- WDTFDriverPackageAction.Interop.dll
api_name:
- IWDTFDriverPackageAction2.Compare
targetos: Windows
req.typenames: 
---

# IWDTFDriverPackageAction2::Compare


## -description


Compares two driver packages.


## -parameters




### -param pDp [in]

The second driver package.


### -param pbIsIdentical [out, retval]

True if the two driver packages are the same; 
otherwise, false.


## -returns



If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.




## -see-also




<a href="/windows-hardware/drivers/ddi/wdtfdriverpackageaction/nn-wdtfdriverpackageaction-iwdtfdriverpackageaction2">IWDTFDriverPackageAction2</a>
 

 
