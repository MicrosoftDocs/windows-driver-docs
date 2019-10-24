---
title: Supporting OpenGL Enhancements
description: Supporting OpenGL Enhancements
ms.assetid: 5f8b7d96-7941-44ce-bd32-546ec0f32883
keywords:
- OpenGL enhancements WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting OpenGL Enhancements


## <span id="Windows_7_Enhancements"></span><span id="windows_7_enhancements"></span><span id="WINDOWS_7_ENHANCEMENTS"></span>Windows 7 Enhancements


This section applies only to Windows 7 and later, Windows Server 2008 R2 and later.

You can implement your OpenGL installable client driver (ICD) to use the following OpenGL enhancements that ship with Windows 7:

### <span id="enhancing_synchronization"></span><span id="ENHANCING_SYNCHRONIZATION"></span>Enhancing Synchronization

You can enhance the synchronization capabilities of your OpenGL ICD by using the following second-generation OpenGL synchronization functions:

-   [**D3DKMTCreateSynchronizationObject2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtcreatesynchronizationobject2)

-   [**D3DKMTOpenSynchronizationObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtopensynchronizationobject)

-   [**D3DKMTWaitForSynchronizationObject2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtwaitforsynchronizationobject2)

-   [**D3DKMTSignalSynchronizationObject2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtsignalsynchronizationobject2)

### <span id="controlling_resource_access_with_mutexes"></span><span id="CONTROLLING_RESOURCE_ACCESS_WITH_MUTEXES"></span>Controlling Resource Access with Mutexes

You can use the following OpenGL mutex functions to control access to resources:

-   [**D3DKMTCreateKeyedMutex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtcreatekeyedmutex)

-   [**D3DKMTOpenKeyedMutex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtopenkeyedmutex)

-   [**D3DKMTDestroyKeyedMutex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtdestroykeyedmutex)

-   [**D3DKMTAcquireKeyedMutex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtacquirekeyedmutex)

-   [**D3DKMTReleaseKeyedMutex**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtreleasekeyedmutex)

### <span id="managing_access_to_shared_resources"></span><span id="MANAGING_ACCESS_TO_SHARED_RESOURCES"></span>Managing Access to Shared Resources

You can use the following OpenGL functions to manage access to a shared resource:

-   [**D3DKMTConfigureSharedResource**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtconfiguresharedresource)

-   [**D3DKMTCheckSharedResourceAccess**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtchecksharedresourceaccess)

### <span id="monitoring_present_history"></span><span id="MONITORING_PRESENT_HISTORY"></span>Monitoring Present History

You can use the following OpenGL functions to monitor the history of present operations:

-   [**D3DKMTPresent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtpresent) with [**D3DKMT\_PRESENTHISTORYTOKEN**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_presenthistorytoken) structures populated in the **PresentHistoryToken** member of the [**D3DKMT\_PRESENT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_present) structure

-   [**D3DKMTGetPresentHistory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtgetpresenthistory)

### <span id="miscellaneous_enhancements"></span><span id="MISCELLANEOUS_ENHANCEMENTS"></span>Miscellaneous Enhancements

You can use the following OpenGL miscellaneous enhancements:

-   [**D3DKMTCheckVidPnExclusiveOwnership**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtcheckvidpnexclusiveownership)

-   [**D3DKMTGetOverlayState**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtgetoverlaystate)

-   [**D3DKMTSetDisplayMode**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtsetdisplaymode) with the [**D3DKMT\_SETDISPLAYMODE\_FLAGS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_setdisplaymode_flags) structure populated in the **Flags** member of the [**D3DKMT\_SETDISPLAYMODE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_setdisplaymode) structure

-   [**D3DKMTPollDisplayChildren**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtpolldisplaychildren) with new flags set in the [**D3DKMT\_POLLDISPLAYCHILDREN**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_polldisplaychildren) structure

## <span id="windows_8_enhancements"></span><span id="WINDOWS_8_ENHANCEMENTS"></span>Windows 8 Enhancements


This section applies only to Windows 8 and later, and Windows Server 2012 and later.

You can implement your OpenGL installable client driver (ICD) to use the following OpenGL enhancements that ship with Windows 8:

### <span id="Controlling_Resource_Access_with_Mutexes_"></span><span id="controlling_resource_access_with_mutexes_"></span><span id="CONTROLLING_RESOURCE_ACCESS_WITH_MUTEXES_"></span>Controlling Resource Access with Mutexes

You can use these OpenGL mutex functions and associated structures to control access to resources while specifying private data to associate with a keyed mutex:

-   [**D3DKMTAcquireKeyedMutex2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtacquirekeyedmutex2)
-   [**D3DKMTCreateKeyedMutex2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtcreatekeyedmutex2)
-   [**D3DKMT\_ACQUIREKEYEDMUTEX2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_acquirekeyedmutex2)
-   [**D3DKMT\_CREATEKEYEDMUTEX2**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_createkeyedmutex2)

### <span id="OpenGL_Helper_Functions"></span><span id="opengl_helper_functions"></span><span id="OPENGL_HELPER_FUNCTIONS"></span>OpenGL Helper Functions

You can use these functions and their associated structures to access objects and their handles:

-   [**D3DKMTGetSharedResourceAdapterLuid**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtgetsharedresourceadapterluid)
-   [**D3DKMTOpenAdapterFromLuid**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtopenadapterfromluid)
-   [**D3DKMTOpenNtHandleFromName**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtopennthandlefromname)
-   [**D3DKMTOpenResourceFromNtHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtopenresourcefromnthandle)
-   [**D3DKMTOpenSyncObjectFromNtHandle**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtopensyncobjectfromnthandle)
-   [**D3DKMT\_GETSHAREDRESOURCEADAPTERLUID**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_getsharedresourceadapterluid)
-   [**D3DKMT\_OPENADAPTERFROMLUID**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_openadapterfromluid)
-   [**D3DKMT\_OPENNTHANDLEFROMNAME**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_opennthandlefromname)
-   [**D3DKMT\_OPENRESOURCEFROMNTHANDLE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_openresourcefromnthandle)
-   [**D3DKMT\_OPENSYNCOBJECTFROMNTHANDLE**](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_opensyncobjectfromnthandle)

 

 





