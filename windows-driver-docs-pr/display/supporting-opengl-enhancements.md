---
title: Supporting OpenGL Enhancements
description: Supporting OpenGL Enhancements
ms.assetid: 5f8b7d96-7941-44ce-bd32-546ec0f32883
keywords: ["OpenGL enhancements WDK display"]
---

# Supporting OpenGL Enhancements


## <span id="Windows_7_Enhancements"></span><span id="windows_7_enhancements"></span><span id="WINDOWS_7_ENHANCEMENTS"></span>Windows 7 Enhancements


This section applies only to Windows 7 and later, Windows Server 2008 R2 and later.

You can implement your OpenGL installable client driver (ICD) to use the following OpenGL enhancements that ship with Windows 7:

### <span id="enhancing_synchronization"></span><span id="ENHANCING_SYNCHRONIZATION"></span>Enhancing Synchronization

You can enhance the synchronization capabilities of your OpenGL ICD by using the following second-generation OpenGL synchronization functions:

-   [**D3DKMTCreateSynchronizationObject2**](https://msdn.microsoft.com/library/windows/hardware/ff546879)

-   [**D3DKMTOpenSynchronizationObject**](https://msdn.microsoft.com/library/windows/hardware/ff547069)

-   [**D3DKMTWaitForSynchronizationObject2**](https://msdn.microsoft.com/library/windows/hardware/ff547262)

-   [**D3DKMTSignalSynchronizationObject2**](https://msdn.microsoft.com/library/windows/hardware/ff547227)

### <span id="controlling_resource_access_with_mutexes"></span><span id="CONTROLLING_RESOURCE_ACCESS_WITH_MUTEXES"></span>Controlling Resource Access with Mutexes

You can use the following OpenGL mutex functions to control access to resources:

-   [**D3DKMTCreateKeyedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff546845)

-   [**D3DKMTOpenKeyedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff547054)

-   [**D3DKMTDestroyKeyedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff546920)

-   [**D3DKMTAcquireKeyedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff546732)

-   [**D3DKMTReleaseKeyedMutex**](https://msdn.microsoft.com/library/windows/hardware/ff547129)

### <span id="managing_access_to_shared_resources"></span><span id="MANAGING_ACCESS_TO_SHARED_RESOURCES"></span>Managing Access to Shared Resources

You can use the following OpenGL functions to manage access to a shared resource:

-   [**D3DKMTConfigureSharedResource**](https://msdn.microsoft.com/library/windows/hardware/ff546798)

-   [**D3DKMTCheckSharedResourceAccess**](https://msdn.microsoft.com/library/windows/hardware/ff546769)

### <span id="monitoring_present_history"></span><span id="MONITORING_PRESENT_HISTORY"></span>Monitoring Present History

You can use the following OpenGL functions to monitor the history of present operations:

-   [**D3DKMTPresent**](https://msdn.microsoft.com/library/windows/hardware/ff547091) with [**D3DKMT\_PRESENTHISTORYTOKEN**](https://msdn.microsoft.com/library/windows/hardware/ff548188) structures populated in the **PresentHistoryToken** member of the [**D3DKMT\_PRESENT**](https://msdn.microsoft.com/library/windows/hardware/ff548168) structure

-   [**D3DKMTGetPresentHistory**](https://msdn.microsoft.com/library/windows/hardware/ff546987)

### <span id="miscellaneous_enhancements"></span><span id="MISCELLANEOUS_ENHANCEMENTS"></span>Miscellaneous Enhancements

You can use the following OpenGL miscellaneous enhancements:

-   [**D3DKMTCheckVidPnExclusiveOwnership**](https://msdn.microsoft.com/library/windows/hardware/ff546779)

-   [**D3DKMTGetOverlayState**](https://msdn.microsoft.com/library/windows/hardware/ff546977)

-   [**D3DKMTSetDisplayMode**](https://msdn.microsoft.com/library/windows/hardware/ff547169) with the [**D3DKMT\_SETDISPLAYMODE\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff548286) structure populated in the **Flags** member of the [**D3DKMT\_SETDISPLAYMODE**](https://msdn.microsoft.com/library/windows/hardware/ff548275) structure

-   [**D3DKMTPollDisplayChildren**](https://msdn.microsoft.com/library/windows/hardware/ff547077) with new flags set in the [**D3DKMT\_POLLDISPLAYCHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff548161) structure

## <span id="windows_8_enhancements"></span><span id="WINDOWS_8_ENHANCEMENTS"></span>Windows 8 Enhancements


This section applies only to Windows 8 and later, and Windows Server 2012 and later.

You can implement your OpenGL installable client driver (ICD) to use the following OpenGL enhancements that ship with Windows 8:

### <span id="Controlling_Resource_Access_with_Mutexes_"></span><span id="controlling_resource_access_with_mutexes_"></span><span id="CONTROLLING_RESOURCE_ACCESS_WITH_MUTEXES_"></span>Controlling Resource Access with Mutexes

You can use these OpenGL mutex functions and associated structures to control access to resources while specifying private data to associate with a keyed mutex:

-   [**D3DKMTAcquireKeyedMutex2**](https://msdn.microsoft.com/library/windows/hardware/hh439340)
-   [**D3DKMTCreateKeyedMutex2**](https://msdn.microsoft.com/library/windows/hardware/hh439345)
-   [**D3DKMT\_ACQUIREKEYEDMUTEX2**](https://msdn.microsoft.com/library/windows/hardware/hh439466)
-   [**D3DKMT\_CREATEKEYEDMUTEX2**](https://msdn.microsoft.com/library/windows/hardware/hh439474)

### <span id="OpenGL_Helper_Functions"></span><span id="opengl_helper_functions"></span><span id="OPENGL_HELPER_FUNCTIONS"></span>OpenGL Helper Functions

You can use these functions and their associated structures to access objects and their handles:

-   [**D3DKMTGetSharedResourceAdapterLuid**](https://msdn.microsoft.com/library/windows/hardware/jj128339)
-   [**D3DKMTOpenAdapterFromLuid**](https://msdn.microsoft.com/library/windows/hardware/hh780247)
-   [**D3DKMTOpenNtHandleFromName**](https://msdn.microsoft.com/library/windows/hardware/hh439409)
-   [**D3DKMTOpenResourceFromNtHandle**](https://msdn.microsoft.com/library/windows/hardware/hh439413)
-   [**D3DKMTOpenSyncObjectFromNtHandle**](https://msdn.microsoft.com/library/windows/hardware/hh780248)
-   [**D3DKMT\_GETSHAREDRESOURCEADAPTERLUID**](https://msdn.microsoft.com/library/windows/hardware/jj128344)
-   [**D3DKMT\_OPENADAPTERFROMLUID**](https://msdn.microsoft.com/library/windows/hardware/hh780267)
-   [**D3DKMT\_OPENNTHANDLEFROMNAME**](https://msdn.microsoft.com/library/windows/hardware/hh406493)
-   [**D3DKMT\_OPENRESOURCEFROMNTHANDLE**](https://msdn.microsoft.com/library/windows/hardware/hh406496)
-   [**D3DKMT\_OPENSYNCOBJECTFROMNTHANDLE**](https://msdn.microsoft.com/library/windows/hardware/hh780268)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20OpenGL%20Enhancements%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




