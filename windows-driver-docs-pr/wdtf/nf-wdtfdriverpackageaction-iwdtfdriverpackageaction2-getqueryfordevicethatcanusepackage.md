---
UID: NF:wdtfdriverpackageaction.IWDTFDriverPackageAction2.GetQueryForDeviceThatCanUsePackage
title: IWDTFDriverPackageAction2::GetQueryForDeviceThatCanUsePackage method (wdtfdriverpackageaction.h)
description: Returns an SDEL statement that queries for all devices that can use the driver package.
old-location: dtf\iwdtfdriverpackageaction2_getqueryfordevicethatcanusepackage.htm
tech.root: dtf
ms.date: 03/29/2018
keywords: ["IWDTFDriverPackageAction2::GetQueryForDeviceThatCanUsePackage method"]
ms.keywords: GetQueryForDeviceThatCanUsePackage,IWDTFDriverPackageAction2.GetQueryForDeviceThatCanUsePackage, GetQueryForDevicesThatCanUsePackage method [Windows Device Testing Framework], GetQueryForDevicesThatCanUsePackage method [Windows Device Testing Framework], IWDTFDriverPackageAction2 interface, IWDTFDriverPackageAction2, IWDTFDriverPackageAction2 interface [Windows Device Testing Framework], GetQueryForDevicesThatCanUsePackage method, IWDTFDriverPackageAction2::GetQueryForDeviceThatCanUsePackage, IWDTFDriverPackageAction2::GetQueryForDevicesThatCanUsePackage, Microsoft.WDTF.IWDTFDriverPackageAction2.GetQueryForDevicesThatCanUsePackage, Microsoft::WDTF::IWDTFDriverPackageAction2::GetQueryForDevicesThatCanUsePackage, dtf.iwdtfdriverpackageaction2_getqueryfordevicethatcanusepackage, wdtfdriverpackageaction/IWDTFDriverPackageAction2::GetQueryForDevicesThatCanUsePackage
f1_keywords:
 - "wdtfdriverpackageaction/IWDTFDriverPackageAction2.GetQueryForDevicesThatCanUsePackage"
 - "IWDTFDriverPackageAction2.GetQueryForDevicesThatCanUsePackage"
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
- IWDTFDriverPackageAction2.GetQueryForDevicesThatCanUsePackage
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---

# IWDTFDriverPackageAction2::GetQueryForDeviceThatCanUsePackage method


## -description


Returns an SDEL statement that queries for all devices that can use the driver package.


## -parameters




### -param pSDEL [out, retval]

The SDEL statement.


## -returns



If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.




## -see-also




<a href="/windows-hardware/drivers/ddi/wdtfdriverpackageaction/nn-wdtfdriverpackageaction-iwdtfdriverpackageaction2">IWDTFDriverPackageAction2</a>
 

 
