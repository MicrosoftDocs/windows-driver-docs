---
title: MS\_SM\_FabricAndDomainManagementMethods WMI Class
description: MS\_SM\_FabricAndDomainManagementMethods WMI Class
ms.assetid: dfd6afd3-0a0c-4620-b961-2235a91d8b17
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# MS\_SM\_FabricAndDomainManagementMethods WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SM\_FabricAndDomainManagementMethods WMI class to provide Fibre Channel services to WMI clients. Fibre channel services are defined by the T11 committee's *Fibre Channel HBA API* specification. This WMI class has no data blocks. Therefore, the WMI tool suite generates structures that hold parameter data for the methods that belong to the class, but it does not generate a structure that corresponds to the class itself.

The MOF syntax for each method that belongs to this class is described in the reference page for the method. The following topics describe these methods and their accompanying structures:

SM\_SendTEST

SM\_SendECHO

SM\_SendSMPPassThru

[**SM\_SendCTPassThru**](sm-sendctpassthru.md)

[**SM\_GetRNIDMgmtInfo**](sm-getrnidmgmtinfo.md)

[**SM\_SetRNIDMgmtInfo**](sm-setrnidmgmtinfo.md)

[**SM\_SendRNID**](sm-sendrnid.md)

[**SM\_SendRPL**](sm-sendrpl.md)

[**SM\_SendRPS**](sm-sendrps.md)

[**SM\_SendSRL**](sm-sendsrl.md)

[**SM\_SendLIRR**](sm-sendlirr.md)

[**SM\_SendRLS**](sm-sendrls.md)

The MS\_SM\_FabricAndDomainManagementMethods class is defined as follows in *Hbaapi.mof*:

```cpp
class MS_SM_FabricAndDomainManagementMethods
{
    [key]
    string  InstanceName;
    boolean Active;

// new FC specific

    [Implemented, WmiMethodId(1)]
    void SM_SendTEST(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DestWWN[8],
                [in ] uint32  DestFCID,
                [in ] uint32  ReqBufferSize,
                [in, WmiSizeIs("ReqBufferSize") ] uint8  ReqBuffer[],
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
                );

// new FC specific

    [Implemented, WmiMethodId(2)]
    void SM_SendECHO(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DestWWN[8],
                [in ] uint32  DestFCID,
                [in ] uint32  InRespBufferMaxSize,
                [in ] uint32  ReqBufferSize,
                [in, WmiSizeIs("ReqBufferSize") ] uint8  ReqBuffer[],
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus,
                [out] uint32  OutRespBufferSize,
                [out, WmiSizeIs("OutRespBufferSize") ] uint8  RespBuffer[]
                );

// new SAS specific

    [Implemented, WmiMethodId(3)]
    void SM_SendSMPPassThru(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DestPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8  DomainPortWWN[8],
                [in ] uint32  InRespBufferMaxSize,
                [in ] uint32  ReqBufferSize,
                [in, WmiSizeIs("ReqBufferSize") ] uint8  ReqBuffer[],
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus,
                [out] uint32  TotalRespBufferSize,
                [out] uint32  OutRespBufferSize,
                [out, WmiSizeIs("OutRespBufferSize") ] uint8  RespBuffer[]
                );

// old FC specific

    [Implemented, WmiMethodId(10)]
    void SM_SendCTPassThru(
                [in, HBAType("HBA_WWN")] uint8  HbaPortWWN[8],
                [in ] uint32  InRespBufferMaxSize,
                [in ] uint32  ReqBufferSize,
                [in, WmiSizeIs("ReqBufferSize") ] uint8  ReqBuffer[],
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus,
                [out] uint32  TotalRespBufferSize,
                [out] uint32  OutRespBufferSize,
                [out, WmiSizeIs("OutRespBufferSize") ] uint8  RespBuffer[]
                );

// old FC specific

    [Implemented, WmiMethodId(11)]
    void SM_GetRNIDMgmtInfo(
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus,
                [out] HBAFC3MgmtInfo MgmtInfo
                );

// old FC specific

    [Implemented, WmiMethodId(12)]
    void SM_SetRNIDMgmtInfo(
                [in ] HBAFC3MgmtInfo MgmtInfo,
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus
                );

// old FC specific

    [Implemented, WmiMethodId(13)]
    void SM_SendRNID(
                [in, HBAType("HBA_WWN")] uint8 HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8 DestWWN[8],
                [in ] uint32  DestFCID,
                [in ] uint32  NodeIdDataFormat,
                [in ] uint32  InRespBufferMaxSize,
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus,
                [out] uint32  TotalRespBufferSize,
                [out] uint32  OutRespBufferSize,
                [out, WmiSizeIs("OutRespBufferSize")] uint8 RespBuffer[]
                );

// old FC specific

    [Implemented, WmiMethodId(14)]
    void SM_SendRPL(
                [in, HBAType("HBA_WWN")] uint8 HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8 AgentWWN[8],
                [in ] uint32  AgentDomain,
                [in ] uint32  PortIndex,
                [in ] uint32  InRespBufferMaxSize,
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus,
                [out] uint32  TotalRespBufferSize,
                [out] uint32  OutRespBufferSize,
                [out, WmiSizeIs("OutRespBufferSize")] uint8 RespBuffer[]
                );

// old FC specific

    [Implemented, WmiMethodId(15)]
    void SM_SendRPS(
                [in, HBAType("HBA_WWN")] uint8 HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8 AgentWWN[8],
                [in, HBAType("HBA_WWN")] uint8 ObjectWWN[8],
                [in ] uint32  AgentDomain,
                [in ] uint32  ObjectPortNumber,
                [in ] uint32  InRespBufferMaxSize,
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus,
                [out] uint32  TotalRespBufferSize,
                [out] uint32  OutRespBufferSize,
                [out, WmiSizeIs("OutRespBufferSize")] uint8 RespBuffer[]
                );

// old FC specific

    [Implemented, WmiMethodId(16)]
    void SM_SendSRL(
                [in, HBAType("HBA_WWN")] uint8 HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8 WWN[8],
                [in ] uint32  Domain,
                [in ] uint32  InRespBufferMaxSize,
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus,
                [out] uint32  TotalRespBufferSize,
                [out] uint32  OutRespBufferSize,
                [out, WmiSizeIs("OutRespBufferSize")] uint8 RespBuffer[]
                );

// old FC specific

    [Implemented, WmiMethodId(17)]
    void SM_SendLIRR(
                [in, HBAType("HBA_WWN")] uint8 SourceWWN[8],
                [in, HBAType("HBA_WWN")] uint8 DestWWN[8],
                [in ] uint8   Function,
                [in ] uint8   Type,
                [in ] uint32  InRespBufferMaxSize,
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus,
                [out] uint32  TotalRespBufferSize,
                [out] uint32  OutRespBufferSize,
                [out, WmiSizeIs("OutRespBufferSize")] uint8 RespBuffer[]
                );

// old FC specific

    [Implemented, WmiMethodId(18)]
    void SM_SendRLS(
                [in, HBAType("HBA_WWN")] uint8 HbaPortWWN[8],
                [in, HBAType("HBA_WWN")] uint8 DestWWN[8],
                [in ] uint32  InRespBufferMaxSize,
                [out, HBA_STATUS_QUALIFIERS ] HBA_STATUS HBAStatus,
                [out] uint32  TotalRespBufferSize,
                [out] uint32  OutRespBufferSize,
                [out, WmiSizeIs("OutRespBufferSize")] uint8 RespBuffer[]
                );
};
```

 

 





