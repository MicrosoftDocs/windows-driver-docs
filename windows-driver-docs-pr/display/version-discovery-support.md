---
title: Version Discovery Support
description: Version Discovery Support
keywords:
- Direct3D version 10.1 WDK Windows 7 display , version discovery support
- version discovery support WDK Windows 7 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Version Discovery Support


This section applies only to Windows 7 and later operating systems.

A user-mode display driver that runs on Windows Vista and later versions and Windows Server 2008 and later versions must fail adapter creation (that is, fail a call to the driver's [**OpenAdapter10**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function) for DDI versions that the driver does not explicitly support.

Windows 7 provides a way for Direct3D applications to discover the DDI versions and hardware capabilities that the driver explicitly supports. This improves version verification. Windows 7 introduces new adapter-specific functions to improve versioning and to provide the opportunity to optimize API and driver initialization. You must implement and export the [**OpenAdapter10\_2**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function in your Direct3D version 10.1 driver so the Direct3D runtime can call the driver's new adapter-specific functions. If you instead implement [**OpenAdapter10**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) in your Direct3D version 10.1 driver, the driver can only indicate whether it supports a DDI version by passing or failing the call to **OpenAdapter10**.

[**OpenAdapter10\_2**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) returns a table of the driver's adapter-specific functions in the **pAdapterFuncs\_2** member of the [**D3D10DDIARG\_OPENADAPTER**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_openadapter) structure. **pAdapterFuncs\_2** points to a [**D3D10\_2DDI\_ADAPTERFUNCS**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10_2ddi_adapterfuncs) structure. The Direct3D runtime calls the driver's adapter-specific [**GetSupportedVersions**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10_2ddi_getsupportedversions) function to query for the DDI versions and hardware capabilities that the driver supports. **GetSupportedVersions** returns the DDI versions and hardware capabilities in an array of 64-bit values. The following code example shows a **GetSupportedVersions** implementation:

```cpp
// Array of 64-bit values that are defined in D3d10umddi.h
const UINT64 c_aSupportedVersions[] = {
    D3D10_0_7_DDI_SUPPORTED, // 10.0 on Windows 7
    D3D10_0_DDI_SUPPORTED, // 10.0 on Windows Vista
 D3D10_1_x_DDI_SUPPORTED, // 10.1 with all extended 
                           // format support (but not
                           // Windows 7 scheduling)
};

HRESULT APIENTRY GetSupportedVersions(
                 D3D10DDI_HADAPTER hAdapter, 
                 __inout UINT32* puEntries,
 __out_ecount_opt( *puEntries ) 
 UINT64* pSupportedDDIInterfaceVersions)
)
{
    const UINT32 uEntries = ARRAYSIZE( c_aSupportedVersions );
    if (pSupportedDDIInterfaceVersions &&
        *puEntries < uEntries)
    {
        return HRESULT_FROM_WIN32( ERROR_INSUFFICIENT_BUFFER );
    }

    // Determine concise hardware support from kernel, cache with hAdapter.
    // pfnQueryAdapterInfoCb( hAdapter, ... )

    *puEntries = uEntries;
    if (pSupportedDDIInterfaceVersions)
    {
        UINT64* pCurEntry = pSupportedDDIInterfaceVersions;
        memcpy( pCurEntry, c_aSupportedVersions, sizeof( c_aSupportedVersions ) );
        pCurEntry += ARRAYSIZE( c_aSupportedVersions );
        assert( pCurEntry - pSupportedDDIInterfaceVersions == uEntries );
    }
    return S_OK;
}
```

A Direct3D version 10.1 driver is not required to verify the values that are passed to the **Interface** and **Version** members of [**D3D10DDIARG\_OPENADAPTER**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_openadapter) in a call to its [**OpenAdapter10\_2**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) function even though these values contain DDI version information with which to initialize the driver. The driver can return DDI version and hardware capabilities through a call to its [**GetSupportedVersions**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10_2ddi_getsupportedversions) function.

The Direct3D runtime can pass values to the **Interface** and **Version** members of [**D3D10DDIARG\_CREATEDEVICE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d10ddiarg_createdevice) in a call to the driver's [**CreateDevice(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) function that are different than the values that the runtime passed to [**OpenAdapter10\_2**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter); the runtime passes values to the **Interface** and **Version** members of D3D10DDIARG\_CREATEDEVICE that are based on the DDI version and hardware capabilities information that the driver's [**GetSupportedVersions**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10_2ddi_getsupportedversions) returned to the runtime. The driver is not required to validate the values that are passed to the **Interface** and **Version** members of D3D10DDIARG\_CREATEDEVICE because the driver already indicated support of these values through its **GetSupportedVersions** function.

If you are porting your driver from Direct3D version 10.0 to Direct3D version 10.1, you should convert the driver to only monitor the **Interface** and **Version** members that are passed to [**CreateDevice(D3D10)**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_createdevice) instead of [**OpenAdapter10\_2**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter). You should analyze both [**CalcPrivateDeviceSize**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_calcprivatedevicesize) and **CreateDevice(D3D10)** function implementations in your ported driver to ensure that there are no assumptions about the values in the **Interface** and **Version** members for *CreateDevice(D3D10)* matching the values in the **Interface** and **Version** members for **OpenAdapter10\_2**.

**Note**  [**OpenAdapter10\_2**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) has the same function signature as [**OpenAdapter10**](/windows-hardware/drivers/ddi/d3d10umddi/nc-d3d10umddi-pfnd3d10ddi_openadapter) (that is, PFND3D10DDI\_OPENADAPTER as defined in the *D3d10umddi.h* header). You can implement both functions in the same user-mode display driver DLL.

 

 

