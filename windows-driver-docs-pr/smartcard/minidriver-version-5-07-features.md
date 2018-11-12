---
title: Minidriver Version 5.07 Features
description: Minidriver Version 5.07 Features
ms.assetid: BFB38805-D2D3-40D2-B336-127B3B84141D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidriver Version 5.07 Features


The following features are introduced in this version.

## <span id="Changes_to_the_CARD_DATA_structure"></span><span id="changes_to_the_card_data_structure"></span><span id="CHANGES_TO_THE_CARD_DATA_STRUCTURE"></span>Changes to the CARD\_DATA structure


[**CARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn468748) structure changes including the following:

-   The **dwVersion** member, as input, is taken as the desired version to be returned from the [**CardAcquireContext**](https://msdn.microsoft.com/library/windows/hardware/dn468701) function. Older card minidrivers may only support version 4 entry points, however. All card minidrivers will set the version returned, which is &lt;= the version passed in. Existing Base CSP- and SC KSP-based card minidrivers will be updated to have this behavior as well.
-   The **pfnCardPrivateKeyDecrypt** member is replaced with the **pfnCardRSADecrypt** member. Associated structures and function types were modified to reflect this.
-   The **pfnCardSign** member is added. This takes only unpadded input and will perform a cryptographic sign based on the indicated key. For ECC card minidrivers, this will be an ECDSA operation.
-   The **pfnCardConstructDHAgreement** member is added. This performs Diffie-Helman key agreement. For ECC card minidrivers, this will be an ECDHE operation.
-   The **pfnCspPadData** entry point is added so that cards that do not support on-card padding can call back to the CSP/KSP to have their data padded.

## <span id="Expanded_meaning_of_the_dwKeySpec_parameter"></span><span id="expanded_meaning_of_the_dwkeyspec_parameter"></span><span id="EXPANDED_MEANING_OF_THE_DWKEYSPEC_PARAMETER"></span>Expanded meaning of the dwKeySpec parameter


The meaning of the **dwKeySpec** member or parameter (present in various structures and entry points) is expanded.

-   AT\_KEYEXCHANGE and AT\_SIGNATURE indicate RSA keys and their intended purpose. Sizes of RSA keys follow a regular progression.
-   ECC keys will come in very few sizes and do not follow a regular progression. The ECC **dwKeySpec** will indicate exact sizes, such as AT\_ECDHA\_P521 for a P-curve 521-bit key for ECDHA. See [**CardCreateContainer**](https://msdn.microsoft.com/library/windows/hardware/dn468708) for a full listing of the new **dwKeySpec** constants.

## <span id="Manifest_registration"></span><span id="manifest_registration"></span><span id="MANIFEST_REGISTRATION"></span>Manifest registration


Registration of a recognized card ATRs is now handled through the manifest, not with *DllRegisterServer* and *DllUnRegisterServer*.

## <span id="Interfaces_for_Secret_Agreement_Changes"></span><span id="interfaces_for_secret_agreement_changes"></span><span id="INTERFACES_FOR_SECRET_AGREEMENT_CHANGES"></span>Interfaces for Secret Agreement Changes


Interfaces for Secret Agreement Changes to ECDH are updated.

 

 





