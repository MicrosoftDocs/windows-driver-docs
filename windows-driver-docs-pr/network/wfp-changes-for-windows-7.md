---
title: WFP Changes for Windows 7
description: WFP Changes for Windows 7
ms.assetid: c7b15182-592a-4cdb-98aa-5283ed2f51a0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WFP Changes for Windows 7


Several changes have been made in the available functions and behavior of the Windows Filtering Platform that begin with Windows 7. Frequently, to take advantage of the new features, you must compile or recompile a callout driver that has the NTDDI\_VERSION macro set to NTDDI\_WIN7.

-   New functions:
    - [**FwpsAcquireClassifyHandle0**](https://msdn.microsoft.com/library/windows/hardware/ff550085)
    - [**FwpsAcquireWritableLayerDataPointer0**](https://msdn.microsoft.com/library/windows/hardware/ff550087)
    - [**FwpsApplyModifiedLayerData0**](https://msdn.microsoft.com/library/windows/hardware/ff551137)
    - [**FwpsCalloutRegister1**](https://msdn.microsoft.com/library/windows/hardware/ff551143)
    - [**FwpsCompleteClassify0**](https://msdn.microsoft.com/library/windows/hardware/ff551150)
    - [**FwpsPendClassify0**](https://msdn.microsoft.com/library/windows/hardware/ff551197)
    - [**FwpsReleaseClassifyHandle0**](https://msdn.microsoft.com/library/windows/hardware/ff551208)
    - [*classifyFn1*](https://msdn.microsoft.com/library/windows/hardware/ff544893)
    - [*notifyFn1*](https://msdn.microsoft.com/library/windows/hardware/ff568804)
    - [**FWPS\_NET\_BUFFER\_LIST\_NOTIFY\_FN0**](https://msdn.microsoft.com/library/windows/hardware/ff552406)
    - [**FwpsInjectTransportSendAsync1**](https://msdn.microsoft.com/library/windows/hardware/ff551189)
    - [**FwpsNetBufferListAssociateContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551191)
    - [**FwpsNetBufferListGetTagForContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551192)
    - [**FwpsNetBufferListRemoveContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551194)
    - [**FwpsNetBufferListRetrieveContext0**](https://msdn.microsoft.com/library/windows/hardware/ff551196)
    - [**FwpsAleEndpointCreateEnumHandle0**](https://msdn.microsoft.com/library/windows/hardware/ff550089)
    - [**FwpsAleEndpointDestroyEnumHandle0**](https://msdn.microsoft.com/library/windows/hardware/ff550091)
    - [**FwpsAleEndpointEnum0**](https://msdn.microsoft.com/library/windows/hardware/ff551126)
    - [**FwpsAleEndpointGetById0**](https://msdn.microsoft.com/library/windows/hardware/ff551128)
    - [**FwpsAleEndpointGetSecurityInfo0**](https://msdn.microsoft.com/library/windows/hardware/ff551131)
    - [**FwpsAleEndpointSetSecurityInfo0**](https://msdn.microsoft.com/library/windows/hardware/ff551133)
-   New structures and enumerations:
    - [**FWPS\_ALE\_ENDPOINT\_ENUM\_TEMPLATE0**](https://msdn.microsoft.com/library/windows/hardware/ff551216)
    - [**FWPS\_ALE\_ENDPOINT\_PROPERTIES0**](https://msdn.microsoft.com/library/windows/hardware/ff551218)
    - [**FWPS\_BIND\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551221)
    - [**FWPS\_CALLOUT1**](https://msdn.microsoft.com/library/windows/hardware/ff551226)
    - [**FWPS\_CONNECT\_REQUEST0**](https://msdn.microsoft.com/library/windows/hardware/ff551231)
    - [**FWPS\_FIELDS\_ALE\_BIND\_REDIRECT\_V4**](https://msdn.microsoft.com/library/windows/hardware/ff551247)
    - [**FWPS\_FIELDS\_ALE\_BIND\_REDIRECT\_V6**](https://msdn.microsoft.com/library/windows/hardware/ff551249)
    - [**FWPS\_FIELDS\_ALE\_CONNECT\_REDIRECT\_V4**](https://msdn.microsoft.com/library/windows/hardware/ff551251)
    - [**FWPS\_FIELDS\_ALE\_CONNECT\_REDIRECT\_V6**](https://msdn.microsoft.com/library/windows/hardware/ff551254)
    - [**FWPS\_FIELDS\_ALE\_ENDPOINT\_CLOSURE\_V4**](https://msdn.microsoft.com/library/windows/hardware/ff551256)
    - [**FWPS\_FIELDS\_ALE\_ENDPOINT\_CLOSURE\_V6**](https://msdn.microsoft.com/library/windows/hardware/ff551258)
    - [**FWPS\_FIELDS\_ALE\_RESOURCE\_RELEASE\_V4**](https://msdn.microsoft.com/library/windows/hardware/ff551269)
    - [**FWPS\_FIELDS\_ALE\_RESOURCE\_RELEASE\_V6**](https://msdn.microsoft.com/library/windows/hardware/ff551272)
    - [**FWPS\_FIELDS\_INBOUND\_MAC\_FRAME\_802\_3**](https://msdn.microsoft.com/library/windows/hardware/ff551291)
    - [**FWPS\_FIELDS\_KM\_AUTHORIZATION**](https://msdn.microsoft.com/library/windows/hardware/ff551312)
    - [**FWPS\_FIELDS\_NAME\_RESOLUTION\_CACHE\_V4**](https://msdn.microsoft.com/library/windows/hardware/ff551316)
    - [**FWPS\_FIELDS\_NAME\_RESOLUTION\_CACHE\_V6**](https://msdn.microsoft.com/library/windows/hardware/ff551320)
    - [**FWPS\_FIELDS\_OUTBOUND\_MAC\_FRAME\_802\_3**](https://msdn.microsoft.com/library/windows/hardware/ff551334)
    - [**FWPS\_FIELDS\_STREAM\_PACKET\_V4**](https://msdn.microsoft.com/library/windows/hardware/ff552379)
    - [**FWPS\_FIELDS\_STREAM\_PACKET\_V6**](https://msdn.microsoft.com/library/windows/hardware/ff552383)
    - [**FWPS\_FILTER1**](https://msdn.microsoft.com/library/windows/hardware/ff552389)
    - [**FWPS\_NET\_BUFFER\_LIST\_EVENT\_TYPE0**](https://msdn.microsoft.com/library/windows/hardware/ff552403)
    - [**FWPS\_TRANSPORT\_SEND\_PARAMS1**](https://msdn.microsoft.com/library/windows/hardware/ff552423)
-   New documentation topics:
    - [Using Bind or Connect Redirection](using-bind-or-connect-redirection.md)
    - [Using Packet Tagging](using-packet-tagging.md)
    - [ALE Endpoint Lifetime Management](ale-endpoint-lifetime-management.md)

 

 





