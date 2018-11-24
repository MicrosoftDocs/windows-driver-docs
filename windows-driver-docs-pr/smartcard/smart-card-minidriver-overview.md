---
title: Smart Card Minidriver Overview
description: Smart Card Minidriver Overview
ms.assetid: B5047C79-F74E-44FA-ADE5-8716ABC9EB79
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Smart Card Minidriver Overview


The card-specific minidriver is the lowest logical interface layer in the Base CSP/KSP. This minidriver lets the Base CSP/KSP and applications interact directly with a specific type of card by using SCRM.

The card minidriver is a DLL that exports a specific set of APIs as defined in this specification. Each call to the card minidriver includes a pointer to a [**CARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn468748) structure that provides context information. This context information provides some state information in addition to a table of function pointers that is used to facilitate communication between the upper layer and the card minidriver.

For more information about this context structure, see [**CardAcquireContext**](https://msdn.microsoft.com/library/windows/hardware/dn468701).

## <span id="Related_Document"></span><span id="related_document"></span><span id="RELATED_DOCUMENT"></span>Related Document


The *Cardmod.h* C header file provides additional information that is relevant to this specification. This file contains the function prototypes and structures that Microsoft smart card minidriver API specifies. This API is available through the Microsoft Cryptographic Provider Development Kit (CPDK).

## <span id="General_Design_Guidelines"></span><span id="general_design_guidelines"></span><span id="GENERAL_DESIGN_GUIDELINES"></span>General Design Guidelines


-   The card minidriver should be distributed as a DLL.
-   Each card-specific operation should implement a single, atomic transaction except as otherwise noted.
-   A standardized set of macro-level operations should be implemented.
-   The logical card file-system objects should be mapped to their physical locations.
-   Cards that are based on this new model should be able to dynamically grow any files that are stored on the card. For cards that are read-only and cannot follow this guideline, the minidriver should follow the specific guidelines for read-only cards that were detailed in this specification.
-   The minidriver imports definitions from the CPDK. The minidriver header file (*Cardmod.h*) includes *Bcrypt.h* for this purpose. Implementations must resolve this dependency through Microsoft Visual Studio project settings for compiling minidrivers.
-   Protected process requirements for plug-ins or drivers

    -   For an LSA plug-in, or a driver to successfully load as a protected process, it must meet the following criteria:

        -   Signature verification

            o Protected mode requires that any plug-in loaded into the LSA must be digitally signed with a Microsoft signature. Therefore, any unsigned, or third party signed plug-ins will fail to load in LSA. Examples of such plug-ins are smart card drivers, crypto plug-ins, password filters, etc.

            o LSA plug-ins that are drivers (such as smart card drivers) need to be digitally signed.

            **Note**  The [Windows Hardware Compatibility Program](https://msdn.microsoft.com/library/windows/hardware/dn922588.aspx) offers the only method for digitally signing drivers for Windows. So it is important to refer to the web site for this information.

             

    -   Adherence to Microsoft Security Development Lifecycle (SDL) Process Guidance.

        -   All plug-ins also need to conform to the applicable portions of the [Microsoft Security Development Lifecycle (SDL) – Process Guidance](https://msdn.microsoft.com/library/windows/desktop/cc307891.aspx) topic. For example, see *No Shared Sections*, described in the SDL Process in Appendix G.

        -   Even if the plug-ins are properly signed with a Microsoft signature, non-compliance with the SDL Process might result in a failure to load the plug-ins.

For information about SDL, see [Microsoft Security Development Lifecycle (SDL) – Process Guidance](https://msdn.microsoft.com/library/windows/desktop/cc307891.aspx)..

And for a discussion about guidelines for developers, see [Developer Guidelines](developer-guidelines.md)

## <span id="Transaction_Management"></span><span id="transaction_management"></span><span id="TRANSACTION_MANAGEMENT"></span>Transaction Management


-   A card minidriver should assume that transactions are handled by the caller, if it uses SCRM to access the card.
-   The card minidriver can assume that all entry points except [**CardDeleteContext**](https://msdn.microsoft.com/library/windows/hardware/dn468715) are called by holding the card transaction. This cannot be assumed in **CardDeleteContext** because the card might have been removed or it is being called as part of a cleanup procedure.
-   Multiple contexts can exist in a single process. Calling [**CardDeleteContext**](https://msdn.microsoft.com/library/windows/hardware/dn468715) on one process should not prevent the other context from functioning.
-   Handling the authentication state of the card is also the responsibility of the caller, not the card minidriver.

## <span id="Conventions"></span><span id="conventions"></span><span id="CONVENTIONS"></span>Conventions


### <span id="Strings__UNICODE_and_ANSI"></span><span id="strings__unicode_and_ansi"></span><span id="STRINGS__UNICODE_AND_ANSI"></span>Strings: UNICODE and ANSI

At the application level, strings are generally encountered as elements of the user interface, either directly or indirectly. Therefore, they usually must be localized (translated into the user’s language) so that they can be understood. For this reason, the string type that most applications use is double-byte (that is, UNICODE) to accommodate different character sets.

However, smart cards operate with minimal resources and with very few options on what to name directories, files, users, and so on. The character set for strings is single-byte ANSI, which provides a more compact representation of string data.

Accordingly, string buffers to and from the card minidriver are expected to be single-byte ANSI, and conversions to and from this character type as required must be performed outside the card minidriver.

### <span id="_Error_Handling"></span><span id="_error_handling"></span><span id="_ERROR_HANDLING"></span> Error Handling

To ensure consistent error handling, response to failure, and consistent behavior for card minidrivers, the following conventions should be followed:

-   All NULL and invalid parameters, including bad flags return SCARD\_E\_INVALID\_PARAMETER.
-   All incorrect PIN or attempts with the wrong key return SCARD\_W\_WRONG\_CHV.
-   If a generic failure happens, the APIs return SCARD\_E\_UNEXPECTED.

In addition, the errors returned by the functions that are described in the following sections should be from the SCARD\_\* category (*winerror.h*). For example, we recommend that you use SCARD\_E\_INVALID\_PARAMETER (0x80100004) instead of ERROR\_INVALID\_PARAMETER (0x00000057).

**Note**  
If a file cannot be read from a card due to I/O errors, or some other unrecoverable data issue that is not related to the actual existence of that file on the card, then Microsoft recommends returning SCARD\_E\_COMM\_DATA\_LOST.

Returning SCARD\_E\_FILE\_NOT\_FOUND as an umbrella error code in such situations, provides misleading debugging information.

 

## <span id="Authentication_and_Authorization"></span><span id="authentication_and_authorization"></span><span id="AUTHENTICATION_AND_AUTHORIZATION"></span>Authentication and Authorization


Beginning with Version 6, the minidriver interface expands the concept of a PIN to beyond just a traditional alphanumeric string. For more information, see “SECRET\_TYPE (enumeration)” later in this specification.

## <span id="Handling_Memory_Allocations"></span><span id="handling_memory_allocations"></span><span id="HANDLING_MEMORY_ALLOCATIONS"></span>Handling Memory Allocations


All API elements in this specification that allocate memory buffers internally do so by calling [**PFN\_CSP\_ALLOC**](https://msdn.microsoft.com/library/windows/hardware/dn468763). Because of this, any such memory buffers must be freed by calling [**PFN\_CSP\_FREE**](https://msdn.microsoft.com/library/windows/hardware/dn468767).

Any allocation of memory that the card minidriver performs should be done by using [**PFN\_CSP\_ALLOC**](https://msdn.microsoft.com/library/windows/hardware/dn468763) or [**PFN\_CSP\_REALLOC**](https://msdn.microsoft.com/library/windows/hardware/dn468770).

## <span id="Caching"></span><span id="caching"></span><span id="CACHING"></span>Caching


The Card Interface layer in the Base CSP/KSP implements a data cache to minimize the amount of data that must be written to or read from the card. The data cache is also made available for the card minidriver to use through function pointers in the [**CARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn468748) structure, and the card minidriver should use these pointers to enhance performance by caching its internal data files that are stored on the card.

Data caching requires write access to the card to persist cache freshness counters to the card. The minidriver can control data caching if writing data to the card is not feasible.

For more information on how to control data caching, see the definition of the CP\_CARD\_CACHE\_MODE property in [**CardGetProperty**](https://msdn.microsoft.com/library/windows/hardware/dn468729) later in this specification.

## <span id="Mandatory_Version_Checking"></span><span id="mandatory_version_checking"></span><span id="MANDATORY_VERSION_CHECKING"></span>Mandatory Version Checking


All card minidrivers must implement version checks. The version of the [**CARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn468748) structure is a negotiation between the version that the caller wants to support and the version that the card minidriver can actually support.

### <span id="CARD_DATA_Version_Checks"></span><span id="card_data_version_checks"></span><span id="CARD_DATA_VERSION_CHECKS"></span>CARD\_DATA Version Checks

Define minimum version as the minimum version of the card minidriver context structure (that is, [**CARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn468748) structure) that is supported, and define the current version as the level for which this card minidriver was designed and for which all card-minidriver-set structure items are guaranteed to be valid on a successful return from [**CardAcquireContext**](https://msdn.microsoft.com/library/windows/hardware/dn468701). The current version must be greater than or equal to the minimum version and less than or equal to CARD\_DATA\_CURRENT\_VERSION, which is defined in *Cardmod.h*.

When the calling application calls [**CardAcquireContext**](https://msdn.microsoft.com/library/windows/hardware/dn468701), it specifies the desired version that it wants to load. This requested version is set in the **dwVersion** member in the [**CARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn468748) structure.

If the requested version is less than the minimum version that the card minidriver supports, [**CardAcquireContext**](https://msdn.microsoft.com/library/windows/hardware/dn468701) must return a revision mismatch error (see the following sample code).

If the requested version is at least as great as the minimum version, the card minidriver should set the **dwVersion** member to the highest version that it can support that is less than or equal to the requested version.

The following sample code shows the expected card minidriver behavior when checking the version. This is assumed to be in the body of the **CardAcquireContext** function. *pCardData* is a pointer to the [**CARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn468748) structure passed into this call.

```ManagedCPlusPlus
#define MINIMUM_VERSION_SUPPORTED (4)
#define CURRENT_VERSION_SUPPORTED (7)

    // The lowest supported version is 4.
    If (pCardData->dwVersion < MINIMUM_VERSION_SUPPORTED)
    {
        dwError = (DWORD) ERROR_REVISION_MISMATCH;
        goto Ret;
    }

    // Set the version to what we support, but don’t exceed the
    // requested version
    pCardData->dwVersion =
       min(pCardData->dwVersion, CURRENT_VERSION_SUPPORTED);
```

**Note**  If the version that the card minidriver returns is not suitable for the purposes of the calling application, it is the responsibility of the calling application to handle this appropriately.

 

After **dwVersion** is set in the call to [**CardAcquireContext**](https://msdn.microsoft.com/library/windows/hardware/dn468701), assume that it will not be changed by either the caller or the card minidriver while it is in the same context.

### <span id="Other_Structure_Version_Checks"></span><span id="other_structure_version_checks"></span><span id="OTHER_STRUCTURE_VERSION_CHECKS"></span>Other Structure Version Checks

For other versioned structures and other card minidriver API methods, version handling is the same as for the [**CARD\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn468748) structure, with one exception. If the API method is called with a structure that contains a **dwVersion** member that is set to 0, this must be treated as a **dwVersion** value of 1.

The [**CardRSADecrypt**](https://msdn.microsoft.com/library/windows/hardware/dn468737) and [**CardSignData**](https://msdn.microsoft.com/library/windows/hardware/dn468741) functions have special handling for version numbers for the data structures that are passed in.

 

 





